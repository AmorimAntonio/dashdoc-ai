import os
import base64
import json
from openai import OpenAI
from dotenv import load_dotenv
from docx import Document
from pdf2image import convert_from_path
from PIL import Image

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

INPUT_FOLDER = "dashboards"
OUTPUT_FOLDER = "cases"
IMAGE_FOLDER = "images"
EXAMPLES_FOLDER = "examples"  # Pasta com exemplos de cortes bons

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(IMAGE_FOLDER, exist_ok=True)

POPPLER_PATH = r"C:\Users\antonioneto\Release-25.12.0-0\poppler-25.12.0\Library\bin"

graph_counter = 0


def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def extract_docx_sections(docx_path):
    doc = Document(docx_path)
    text = "\n".join([p.text for p in doc.paragraphs])
    return text[:15000]


def pdf_to_images(pdf_path, name):
    pages = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    paths = []

    for i, page in enumerate(pages):
        safe_name = name.replace(" ", "_")
        path = f"{IMAGE_FOLDER}/{safe_name}_page_{i+1}.png"
        page.save(path)
        paths.append(path)

    return paths


def load_example_images():
    """Carrega exemplos de cortes bons da pasta 'examples/'"""
    examples = []
    
    if not os.path.exists(EXAMPLES_FOLDER):
        print(f"⚠ Pasta '{EXAMPLES_FOLDER}' não encontrada.")
        print(f"  → Crie a pasta e adicione exemplos 'good_*.png' para melhor detecção")
        os.makedirs(EXAMPLES_FOLDER, exist_ok=True)
        return examples
    
    files = os.listdir(EXAMPLES_FOLDER)
    
    for f in files:
        if f.startswith("good_") and f.endswith(".png"):
            path = os.path.join(EXAMPLES_FOLDER, f)
            examples.append(encode_image(path))
    
    if examples:
        print(f"  → Carregados {len(examples)} exemplos de referência")
    
    return examples


def detect_graphs_with_examples(image_path):
    """
    Detecção inicial usando exemplos visuais como referência
    """
    base64_image = encode_image(image_path)
    examples = load_example_images()
    
    content = []
    
    # Texto inicial
    initial_text = """
Você está analisando um dashboard Power BI para detectar gráficos.

OBJETIVO: Identificar coordenadas que capturem cada gráfico COMPLETO.
"""
    content.append({"type": "text", "text": initial_text})
    
    # Adicionar exemplos de referência (se existirem)
    if examples:
        content.append({
            "type": "text",
            "text": "\n✅ EXEMPLOS DE CORTES CORRETOS:\n\nUse estes como referência do que é um gráfico BEM cortado:"
        })
        
        for idx, img_b64 in enumerate(examples):
            content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{img_b64}"}
            })
            content.append({
                "type": "text",
                "text": f"Referência {idx+1}: Note que inclui título completo, eixos, dados e margem"
            })
    
    # Instruções detalhadas
    instructions = """

AGORA ANALISE ESTE DASHBOARD:

IGNORE:
- KPIs numéricos isolados (um número grande sozinho)
- Tabelas de dados brutas
- Filtros/slicers/dropdowns
- Botões

IDENTIFIQUE cada GRÁFICO VISUAL e retorne:

[
  {
    "title": "Nome exato visível no gráfico",
    "type": "linha|barra|pizza|área|dispersão|donut",
    "box": [x1, y1, x2, y2]
  }
]

COORDENADAS (0.0 a 1.0 normalizado):
- x1, y1 = canto SUPERIOR ESQUERDO
- x2, y2 = canto INFERIOR DIREITO

REGRAS CRÍTICAS:
1. Comece ACIMA do título (inclua margem ~3-5%)
2. Termine ABAIXO dos dados/legendas (inclua margem ~3-5%)
3. Inclua eixos COMPLETOS (Y à esquerda, X embaixo)
4. NÃO inclua elementos de OUTROS gráficos
5. NÃO inclua tabelas de dados separadas

Seja GENEROSO mas PRECISO: área maior é melhor que menor, mas não inclua lixo.

Retorne APENAS o array JSON.
"""
    content.append({"type": "text", "text": instructions})
    
    # Imagem a analisar
    content.append({
        "type": "image_url",
        "image_url": {"url": f"data:image/png;base64,{base64_image}"}
    })

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": content}],
        temperature=0.1,
        max_tokens=2000,
    )

    content_text = response.choices[0].message.content
    content_text = content_text.replace("```json", "").replace("```", "").strip()

    start = content_text.find("[")
    end = content_text.rfind("]") + 1
    json_text = content_text[start:end]

    try:
        return json.loads(json_text)
    except:
        print(f"      Erro ao parsear JSON inicial")
        return []


def validate_crop_with_feedback(crop_path, graph_info, iteration_num):
    """
    Valida o corte e dá feedback ESPECÍFICO e DIRECIONADO
    
    Exigência: 90%+ de qualidade
    """
    
    base64_crop = encode_image(crop_path)
    
    validation_prompt = f"""
Você é um INSPETOR DE QUALIDADE de cortes de gráficos.

GRÁFICO: {graph_info['title']}
TIPO: {graph_info['type']}
ITERAÇÃO: {iteration_num}/5

Analise a imagem cortada e seja rigoroso. Precisamos de 85%+ de qualidade.

CHECKLIST OBRIGATÓRIO:
1. ✓ Título COMPLETO e LEGÍVEL (100% visível, nada cortado)
2. ✓ Eixo Y (se aplicável) com TODOS os números/labels visíveis
3. ✓ Eixo X (se aplicável) com TODOS os labels visíveis
4. ✓ Dados COMPLETOS (barras/linhas/pontos inteiros, nada pela metade)
5. ✓ Legenda COMPLETA (se existir)
6. ✓ Margem pequena ao redor (não colado nas bordas)
7. ✓ SEM elementos extras (CRÍTICO):
   - SEM tabelas de dados laterais
   - SEM outros gráficos adjacentes (barras, linhas, pizzas de OUTROS visuais)
   - SEM filtros ou slicers
   - APENAS o gráfico "{graph_info['title']}" do tipo {graph_info['type']}

Responda em JSON:

{{
  "quality_score": 0-100,
  "is_acceptable": true/false,
  "specific_issues": [
    {{
      "problem": "descrição específica",
      "location": "top|bottom|left|right",
      "severity": "critical|moderate|minor"
    }}
  ],
  "adjustment": {{
    "expand_left": -0.05 a 0.05,
    "expand_right": -0.05 a 0.05,
    "expand_top": -0.05 a 0.05,
    "expand_bottom": -0.05 a 0.05,
    "reasoning": "explicação clara do ajuste"
  }}
}}

REGRAS:
- quality_score >= 85 → is_acceptable: true
- quality_score < 85 → is_acceptable: false
- Ajustes PEQUENOS e PRECISOS (-5% a +5% por direção)
- reasoning DEVE explicar EXATAMENTE o que o ajuste resolve

EXEMPLOS DE BOM FEEDBACK:

Título cortado na lateral:
{{
  "quality_score": 75,
  "is_acceptable": false,
  "specific_issues": [
    {{"problem": "Título mostra apenas '...lução' ao invés de 'Evolução'", "location": "top", "severity": "critical"}}
  ],
  "adjustment": {{
    "expand_top": 0,
    "expand_left": 0.05,
    "expand_right": 0,
    "expand_bottom": 0,
    "reasoning": "Expandir 5% para a esquerda vai capturar o início do título 'Ev...'. Mantenho resto inalterado pois está OK."
  }}
}}

Título cortado no topo:
{{
  "quality_score": 75,
  "is_acceptable": false,
  "specific_issues": [
    {{"problem": "Título está cortado, aparece apenas a parte de baixo das letras", "location": "top", "severity": "critical"}}
  ],
  "adjustment": {{
    "expand_top": 0.05,
    "expand_left": 0,
    "expand_right": 0,
    "expand_bottom": 0,
    "reasoning": "Expandir 5% para o tpo vai capturar as letras do titulo por inteiras. Mantenho resto inalterado pois está OK."
  }}
}}


Eixo X cortado:
{{
  "quality_score": 80,
  "is_acceptable": false,
  "specific_issues": [
    {{"problem": "Eixo X cortado - faltam últimas datas (só vejo até 'Mar' mas deve ter 'Abr')", "location": "bottom", "severity": "critical"}}
  ],
  "adjustment": {{
    "expand_top": 0,
    "expand_left": 0,
    "expand_right": 0.05,
    "expand_bottom": 0,
    "reasoning": "Expandir 5% para a direita vai mostrar o eixo X completo. Não mexo no resto pois título e dados estão bons."
  }}
}}

Incluindo tabela extra:
{{
  "quality_score": 70,
  "is_acceptable": false,
  "specific_issues": [
    {{"problem": "Tabela de dados à esquerda não faz parte do gráfico de linha", "location": "left", "severity": "critical"}}
  ],
  "adjustment": {{
    "expand_left": -0.12,
    "expand_right": 0,
    "expand_top": 0,
    "expand_bottom": 0,
    "reasoning": "Contrair 12% da esquerda vai remover a tabela e manter só o gráfico de linha. Resto mantém."
  }}
}}

Incluindo outro gráfico adjacente:
{{
  "quality_score": 65,
  "is_acceptable": false,
  "specific_issues": [
    {{"problem": "Gráfico de barras à direita não faz parte do gráfico de pizza '{graph_info['title']}'", "location": "right", "severity": "critical"}}
  ],
  "adjustment": {{
    "expand_right": -0.15,
    "expand_left": 0,
    "expand_top": 0,
    "expand_bottom": 0,
    "reasoning": "Contrair 15% da direita vai remover o gráfico de barras adjacente e manter apenas o gráfico de pizza. Título e legenda ficam intactos."
  }}
}}

Perfeito (>85%):
{{
  "quality_score": 95,
  "is_acceptable": true,
  "specific_issues": [],
  "adjustment": {{
    "expand_top": 0,
    "expand_left": 0,
    "expand_right": 0,
    "expand_bottom": 0,
    "reasoning": "Gráfico completo: título legível, eixos visíveis, dados inteiros, legenda presente. Nenhum ajuste necessário."
  }}
}}

Seja ESPECÍFICO e CONSTRUTIVO no feedback. Retorne APENAS o JSON.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": validation_prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{base64_crop}"}
                    },
                ],
            }
        ],
        temperature=0.1,
        max_tokens=1500,
    )

    content = response.choices[0].message.content
    content = content.replace("```json", "").replace("```", "").strip()
    
    start = content.find("{")
    end = content.rfind("}") + 1
    json_text = content[start:end]

    try:
        validation = json.loads(json_text)
        return validation
    except Exception as e:
        print(f"        Erro ao parsear validação: {e}")
        # Fallback conservador
        return {
            "quality_score": 85,
            "is_acceptable": False,
            "specific_issues": [{"problem": "Erro na análise", "location": "unknown", "severity": "moderate"}],
            "adjustment": {
                "expand_top": 0,
                "expand_left": 0,
                "expand_right": 0,
                "expand_bottom": 0,
                "reasoning": "Erro ao analisar, mantendo coordenadas"
            }
        }


def iterative_crop_with_feedback(image_path, graph, dashboard_name, max_iterations=5):
    """
    Sistema iterativo com feedback específico
    """
    
    img = Image.open(image_path)
    width, height = img.size
    
    global graph_counter
    
    current_box = graph["box"].copy()
    original_box = graph["box"].copy()
    
    print(f"      🎯 {graph['title']}")
    
    for iteration in range(max_iterations):
        iter_num = iteration + 1
        print(f"        Iteração {iter_num}/{max_iterations}")
        
        # Converter para pixels
        x1 = max(0, int(current_box[0] * width))
        y1 = max(0, int(current_box[1] * height))
        x2 = min(width, int(current_box[2] * width))
        y2 = min(height, int(current_box[3] * height))
        
        if x2 <= x1 or y2 <= y1:
            print(f"          ⚠ Coordenadas inválidas, pulando")
            return None
        
        # Cortar
        crop = img.crop((x1, y1, x2, y2))
        
        safe_name = dashboard_name.replace(" ", "_")
        temp_path = f"{IMAGE_FOLDER}/temp_{safe_name}_graph_{graph_counter}.png"
        crop.save(temp_path, quality=95)
        
        # Validar com feedback específico
        validation = validate_crop_with_feedback(temp_path, graph, iter_num)
        
        quality = validation.get("quality_score", 0)
        acceptable = validation.get("is_acceptable", False)
        
        print(f"          Qualidade: {quality}%")
        
        if acceptable:
            print(f"          ✅ Aprovado! (>= 90%)")
            final_path = f"{IMAGE_FOLDER}/{safe_name}_graph_{graph_counter}.png"
            os.rename(temp_path, final_path)
            graph_counter += 1
            
            return {
                "title": graph["title"],
                "type": graph["type"],
                "path": final_path
            }
        
        # Mostrar problemas específicos
        issues = validation.get("specific_issues", [])
        if issues:
            for issue in issues:
                severity_icon = "🔴" if issue["severity"] == "critical" else "🟡"
                print(f"          {severity_icon} {issue['problem']} ({issue['location']})")
        
        # Aplicar ajuste
        adjustment = validation.get("adjustment", {})
        reasoning = adjustment.get("reasoning", "Ajustando...")
        print(f"          💡 {reasoning}")
        
        # Limitar ajustes
        MAX_ADJUST = 0.06  # 6% max por iteração
        
        # VALORES DO MODELO:
        # expand_left POSITIVO = expandir pra esquerda (diminuir x1)
        # expand_left NEGATIVO = contrair da esquerda (aumentar x1)
        # expand_top POSITIVO = expandir pra cima (diminuir y1)
        # expand_top NEGATIVO = contrair do topo (aumentar y1)
        
        expand_left = max(-MAX_ADJUST, min(MAX_ADJUST, adjustment.get("expand_left", 0)))
        expand_top = max(-MAX_ADJUST, min(MAX_ADJUST, adjustment.get("expand_top", 0)))
        expand_right = max(-MAX_ADJUST, min(MAX_ADJUST, adjustment.get("expand_right", 0)))
        expand_bottom = max(-MAX_ADJUST, min(MAX_ADJUST, adjustment.get("expand_bottom", 0)))
        
        # Aplicar
        # LÓGICA CORRETA:
        # - expand_top POSITIVO = expandir pra cima = DIMINUIR y1
        # - expand_left POSITIVO = expandir pra esquerda = DIMINUIR x1
        # - expand_bottom POSITIVO = expandir pra baixo = AUMENTAR y2
        # - expand_right POSITIVO = expandir pra direita = AUMENTAR x2
        
        new_box = [
            max(0.0, current_box[0] - expand_left),    # x1: expandir esquerda = diminuir
            max(0.0, current_box[1] - expand_top),     # y1: expandir topo = diminuir
            min(1.0, current_box[2] + expand_right),   # x2: expandir direita = aumentar
            min(1.0, current_box[3] + expand_bottom)   # y2: expandir baixo = aumentar
        ]
        
        # DEBUG: Mostrar o que mudou
        print(f"          📐 Box: [{current_box[0]:.3f}, {current_box[1]:.3f}, {current_box[2]:.3f}, {current_box[3]:.3f}]")
        print(f"          📐 Novo: [{new_box[0]:.3f}, {new_box[1]:.3f}, {new_box[2]:.3f}, {new_box[3]:.3f}]")
        if expand_top != 0:
            direction = "↑" if expand_top > 0 else "↓"
            print(f"             Topo {direction} {abs(expand_top)*100:.1f}%")
        if expand_bottom != 0:
            direction = "↓" if expand_bottom > 0 else "↑"
            print(f"             Baixo {direction} {abs(expand_bottom)*100:.1f}%")
        if expand_left != 0:
            direction = "←" if expand_left > 0 else "→"
            print(f"             Esq {direction} {abs(expand_left)*100:.1f}%")
        if expand_right != 0:
            direction = "→" if expand_right > 0 else "←"
            print(f"             Dir {direction} {abs(expand_right)*100:.1f}%")
        
        # Verificar deriva
        MAX_DRIFT = 0.25  # 25% max
        
        if (abs(new_box[0] - original_box[0]) > MAX_DRIFT or
            abs(new_box[1] - original_box[1]) > MAX_DRIFT or
            abs(new_box[2] - original_box[2]) > MAX_DRIFT or
            abs(new_box[3] - original_box[3]) > MAX_DRIFT):
            
            print(f"          ⚠ Desviou muito do original, resetando com padding")
            current_box = [
                max(0.0, original_box[0] - 0.04),
                max(0.0, original_box[1] - 0.04),
                min(1.0, original_box[2] + 0.04),
                min(1.0, original_box[3] + 0.04)
            ]
        else:
            current_box = new_box
        
        # Deletar temp
        if os.path.exists(temp_path):
            os.remove(temp_path)
    
    # Última tentativa
    print(f"          ⚠ Não atingiu 90% após {max_iterations} iterações")
    print(f"          💾 Salvando melhor tentativa (qualidade: {quality}%)")
    
    final_path = f"{IMAGE_FOLDER}/{safe_name}_graph_{graph_counter}.png"
    crop = img.crop((
        int(current_box[0] * width),
        int(current_box[1] * height),
        int(current_box[2] * width),
        int(current_box[3] * height)
    ))
    crop.save(final_path, quality=95)
    graph_counter += 1
    
    return {
        "title": graph["title"],
        "type": graph["type"],
        "path": final_path
    }


def remove_duplicate_graphs(graphs):
    """Remove duplicados"""
    seen = set()
    unique = []

    for g in graphs:
        if g is None:
            continue
        key = g["title"].lower().strip()
        if key not in seen:
            seen.add(key)
            unique.append(g)

    return unique


def generate_documentation(doc_text, graphs):
    """Gera documentação"""
    graph_list = "\n".join(
        [f"- {g['title']} (tipo: {g['type']})" for g in graphs]
    )

    prompt = f"""
Você está escrevendo a documentação funcional de um dashboard Power BI para usuários de negócio.

Documentação técnica disponível:
{doc_text}

Gráficos identificados no dashboard:
{graph_list}

ESTRUTURA OBRIGATÓRIA (siga EXATAMENTE nesta ordem):

# Visão Geral do Dashboard
Descreva em 2-3 parágrafos: qual é o dashboard, para que serve, e quem deve usá-lo.

# Objetivo de Negócio
Liste 3-5 objetivos principais que o dashboard atende (bullets).

# Principais KPIs e Indicadores
Liste os KPIs numéricos visíveis (se houver), com breve explicação.

# Descrição das Visualizações
Para CADA gráfico da lista acima, crie uma subseção assim:

## [Nome do Gráfico]

**Tipo:** [tipo do gráfico]

[2-3 frases descrevendo o que o gráfico mostra]

### Como interpretar [a ideia é ser uma sugestão, então nao utilize verbos no imperativo]:

- [Ponto 1 de interpretação]
- [Ponto 2 de interpretação]
- [Ponto 3 de interpretação - opcional]

---

# Filtros e Interações
Descreva filtros disponíveis e como eles afetam as visualizações.

# Fluxo de Uso Recomendado
Passo a passo de como um usuário deve navegar pelo dashboard (numbered list).

# Perguntas de Negócio que o Dashboard Responde
Liste 5-8 perguntas no formato:
- **[Pergunta]** → [Como encontrar a resposta no dashboard]

REGRAS CRÍTICAS:
- NÃO crie seções adicionais além das listadas acima
- NÃO separe "Descrição" e "Como Interpretar" em seções diferentes
- CADA gráfico deve ter exatamente uma subseção em "Descrição das Visualizações"
- Use markdown limpo, sem emojis excessivos
- Foque em linguagem de negócio, não técnica

Retorne APENAS o markdown formatado.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content


def insert_images(md, graphs):
    """Insere imagens"""
    lines = md.split("\n")
    new_md = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        new_md.append(line)
        
        if line.startswith("## ") and not line.startswith("### "):
            for g in graphs:
                title_in_line = g["title"].lower().replace(" ", "").replace("-", "")
                line_clean = line.lower().replace(" ", "").replace("-", "").replace("#", "")
                
                if title_in_line in line_clean or line_clean in title_in_line:
                    img = os.path.basename(g["path"])
                    img_md = f"\n![{g['title']}](../images/{img})\n"
                    new_md.append(img_md)
                    break
        
        i += 1
    
    return "\n".join(new_md)


def create_markdown(name, md):
    """Salva markdown"""
    output_path = f"{OUTPUT_FOLDER}/{name}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✔ Markdown salvo em: {output_path}")


def process():
    """Processamento principal"""
    files = os.listdir(INPUT_FOLDER)
    pdfs = [f for f in files if f.endswith(".pdf")]

    if not pdfs:
        print("❌ Nenhum PDF encontrado na pasta 'dashboards'")
        return

    for pdf in pdfs:
        print("\n" + "="*60)
        name = pdf.replace(".pdf", "")
        safe_name = name.replace(" ", "_")
        
        pdf_path = os.path.join(INPUT_FOLDER, pdf)
        
        docx_name = name.replace(" ", "_") + ".docx"
        docx_path = os.path.join(INPUT_FOLDER, docx_name)
        
        if not os.path.exists(docx_path):
            print(f"⚠ Docx não encontrado para '{name}', pulando...")
            continue
        
        print(f"📄 Processando: {name}")
        
        # 1. Extrair contexto
        print("  → Extraindo contexto do DOCX...")
        doc_text = extract_docx_sections(docx_path)
        
        # 2. Converter PDF
        print("  → Convertendo PDF em imagens...")
        pages = pdf_to_images(pdf_path, name)
        print(f"  → {len(pages)} página(s) convertida(s)")
        
        # 3. Detectar com exemplos + refinar com feedback
        print("  → Detectando gráficos (com exemplos de referência)...")
        all_graphs = []
        
        for idx, page in enumerate(pages):
            print(f"    📄 Página {idx + 1}")
            
            graphs = detect_graphs_with_examples(page)
            print(f"      {len(graphs)} gráfico(s) detectado(s)")
            
            for graph in graphs:
                refined = iterative_crop_with_feedback(page, graph, safe_name)
                if refined:
                    all_graphs.append(refined)
        
        # 4. Remover duplicatas
        all_graphs = remove_duplicate_graphs(all_graphs)
        print(f"  → Total: {len(all_graphs)} gráfico(s) validados")
        
        if not all_graphs:
            print("  ⚠ Nenhum gráfico detectado")
            continue
        
        # 5. Documentação
        print("  → Gerando documentação...")
        md = generate_documentation(doc_text, all_graphs)
        md = insert_images(md, all_graphs)
        create_markdown(safe_name, md)
        
        print(f"✅ Concluído: '{name}'")
        print("="*60)


if __name__ == "__main__":
    process()