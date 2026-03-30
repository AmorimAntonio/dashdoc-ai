import os
import base64
import re
from openai import OpenAI
from dotenv import load_dotenv
from docx import Document
from pdf2image import convert_from_path
from md_to_pdf import render


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

INPUT_FOLDER  = "dashboards"
OUTPUT_FOLDER = "cases"
MD_FOLDER     = "cases/md"
IMAGE_FOLDER  = "images"

POPPLER_PATH = r"C:\Users\antonioneto\Release-25.12.0-0\poppler-25.12.0\Library\bin"  # update to your poppler path

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(MD_FOLDER,     exist_ok=True)
os.makedirs(IMAGE_FOLDER,  exist_ok=True)


def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def extract_docx_text(docx_path):
    doc = Document(docx_path)
    return "\n".join([p.text for p in doc.paragraphs])[:15000]


def already_processed(safe_name):
    return os.path.exists(f"{OUTPUT_FOLDER}/{safe_name}.pdf")


def pdf_to_images(pdf_path, name):
    # converts each PDF page to PNG
    safe_name = name.replace(" ", "_")
    folder = f"{IMAGE_FOLDER}/{safe_name}"
    os.makedirs(folder, exist_ok=True)

    pages = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    paths = []
    for i, page in enumerate(pages):
        path = f"{folder}/page_{i+1}.png"
        page.save(path)
        paths.append(path)

    print(f"  → {len(paths)} page(s) converted")
    return paths


def describe_pages(pages):
    # sends all pages to GPT-4o and returns a list of identified visual elements
    content = [
        {
            "type": "text",
            "text": (
                "Analise as imagens abaixo de um dashboard Power BI e liste "
                "TODOS os elementos visuais presentes.\n\n"
                "REGRAS IMPORTANTES sobre nomes:\n"
                "- Cada visual tem um título principal em destaque e geralmente "
                "um subtítulo menor abaixo (ex: 'por vagas', 'por período', 'por inadimplência').\n"
                "- Sempre combine os dois em um único nome corrido: 'Título por subtítulo'. "
                "Exemplos corretos: 'Resumo por vagas', 'Média de Dias por período', "
                "'Vagas e Demais por vagas'.\n"
                "- NÃO confunda valores numéricos dentro do visual (ex: '2493', 'Total') "
                "com o título. O título fica no topo do card/gráfico.\n"
                "- Se não houver subtítulo, use apenas o título principal.\n\n"
                "Formato de resposta (uma linha por elemento):\n"
                "- [tipo] Nome completo do visual\n\n"
                "Tipos: gráfico de barras, gráfico de linhas, gráfico de pizza, "
                "gráfico de donut, gráfico de área, tabela, cartão KPI, filtro/slicer.\n\n"
                "Seja objetivo. Não invente elementos que não estão visíveis."
            )
        }
    ]

    for i, page_path in enumerate(pages):
        content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/png;base64,{encode_image(page_path)}"}
        })
        content.append({"type": "text", "text": f"(Página {i+1})"})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": content}],
        temperature=0.1,
        max_tokens=1000,
    )
    return response.choices[0].message.content.strip()


def generate_documentation(doc_text, visual_elements):
    # builds the full markdown documentation using DOCX context + visual elements
    prompt = f"""
Você está escrevendo a documentação funcional de um dashboard Power BI para usuários de negócio.

Documentação técnica disponível:
{doc_text}

Elementos visuais identificados no dashboard:
{visual_elements}

ESTRUTURA OBRIGATÓRIA (siga EXATAMENTE nesta ordem):

# Visão Geral do Dashboard
Descreva em 2-3 parágrafos: qual é o dashboard, para que serve, e quem deve usá-lo.

# Objetivo de Negócio
Liste 3-5 objetivos principais que o dashboard atende (bullets).

# Principais KPIs e Indicadores
Liste os KPIs/cartões numéricos visíveis com breve explicação. Se não houver, omita esta seção.

# Descrição das Visualizações
Para CADA gráfico ou tabela listado acima, crie uma subseção:

## [Nome completo do visual]

O nome deve combinar título e subtítulo em frase corrida, sem barra nem dois-pontos.
Exemplos: "Vagas e Demais por vagas", "Média de Dias por período", "Resumo por vagas".

**Tipo:** [tipo]

[2-3 frases descrevendo o que o visual mostra]

### Funcionamento:
- [ponto 1]
- [ponto 2]
- [ponto 3 — opcional]

---

# Filtros e Interações
Descreva os filtros/slicers disponíveis e como afetam as visualizações.

# Fluxo de Uso Recomendado
Passo a passo numerado de como navegar pelo dashboard.

# Perguntas de Negócio que o Dashboard Responde
Liste 5-8 perguntas no formato:
- **[Pergunta]** → [Como encontrar a resposta no dashboard]

REGRAS:
- NÃO crie seções além das listadas
- NÃO use verbos no imperativo nas dicas de interpretação
- O nome de cada ## deve ser título + subtítulo em frase corrida
- Use markdown limpo, sem emojis excessivos
- Foque em linguagem de negócio, não técnica

Retorne APENAS o markdown formatado, sem blocos de código.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    md = response.choices[0].message.content
    md = re.sub(r"^```(?:markdown)?\s*\n?", "", md.strip())
    md = re.sub(r"\n?```\s*$", "", md.strip())
    return md.strip()


def insert_page_images(md, pages, safe_name):
    # inserts full-page screenshots in the file for visualization
    if not pages:
        return md

    images_md = "\n"
    for i, page_path in enumerate(pages):
        img_name = os.path.basename(page_path)
        images_md += f"![Página {i+1} do Dashboard](../../images/{safe_name}/{img_name})\n\n"

    lines = md.split("\n")
    result = []
    inserted = False
    for line in lines:
        if not inserted and line.startswith("# Objetivo"):
            result.append(images_md)
            inserted = True
        result.append(line)

    if not inserted:
        result.append(images_md)

    return "\n".join(result)


def save_markdown(safe_name, md):
    output_path = f"{MD_FOLDER}/{safe_name}.md"
    if os.path.exists(output_path):
        print(f"  ⏭ Markdown already exists: {output_path}")
        return output_path
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"  ✔ Markdown saved: {output_path}")
    return output_path


def process():
    pdfs = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".pdf")]

    if not pdfs:
        print("No PDFs found in", INPUT_FOLDER)
        return

    for pdf in pdfs:
        print("\n" + "=" * 60)

        name      = pdf.replace(".pdf", "")
        safe_name = name.replace(" ", "_")

        if already_processed(safe_name):
            print(f"⏭ Already done, skipping: {name}")
            continue

        pdf_path  = os.path.join(INPUT_FOLDER, pdf)
        docx_path = os.path.join(INPUT_FOLDER, safe_name + ".docx")

        if not os.path.exists(docx_path):
            print(f"⚠ No DOCX found for '{name}', skipping...")
            continue

        print(f"📄 Processing: {name}")

        doc_text        = extract_docx_text(docx_path)
        pages           = pdf_to_images(pdf_path, name)

        print("  → Analyzing visuals...")
        visual_elements = describe_pages(pages)
        print(f"  → Found:\n{visual_elements}\n")

        print("  → Generating documentation...")
        md      = generate_documentation(doc_text, visual_elements)
        md      = insert_page_images(md, pages, safe_name)
        md_path = save_markdown(safe_name, md)

        render(md_path, output_path=f"{OUTPUT_FOLDER}/{safe_name}.pdf")

        print(f"✅ Done: '{name}'")
        print("=" * 60)


if __name__ == "__main__":
    process()