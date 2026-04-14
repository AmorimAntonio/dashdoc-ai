"""
md_to_pdf.py — converts a markdown file into a styled PDF.

Usage:
    python md_to_pdf.py cases/md/my_dashboard.md
    python md_to_pdf.py cases/md/my_dashboard.md --output cases/my_dashboard.pdf

Dependencies:
    conda install -c conda-forge weasyprint
    pip install markdown
"""

import argparse
import base64
import re
import sys
from pathlib import Path
from datetime import datetime
import markdown
from weasyprint import HTML, CSS


def encode_image(path):
    """Encodes an image to base64 string."""
    if not path.exists():
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def embed_images(html: str, md_path: Path) -> str:
    """Replaces local image src with base64 so the PDF is self-contained."""
    def replacer(match):
        src = match.group(1)
        if src.startswith(("http://", "https://", "data:")):
            return match.group(0)
        img_path = (md_path.parent / src).resolve()
        if not img_path.exists():
            return match.group(0)
        suffix = img_path.suffix.lower().lstrip(".")
        mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "gif": "gif", "webp": "webp"}.get(suffix, "png")
        data = base64.b64encode(img_path.read_bytes()).decode()
        return f'src="data:image/{mime};base64,{data}"'

    return re.sub(r'src="([^"]+)"', replacer, html)


def md_to_html(md_text: str) -> str:
    """Converts markdown and returns (body_html, toc_html)."""
    md = markdown.Markdown(extensions=["extra", "toc", "sane_lists", "nl2br"])
    
    body_html = md.convert(md_text)
    toc_html = md.toc 
    
    return body_html, toc_html

def extract_summary(md_text: str) -> str:
    """
    Removes first h1 title and exctract the first text paragraph to 
    use it in the front page.
    """
    md_clean = re.sub(r"^# .+\n?", "", md_text, count=1).strip()
    paragraphs = [p.strip() for p in md_clean.split("\n\n") if p.strip() and not p.startswith('![')]
    
    if paragraphs:
        summary = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', paragraphs[0])
        summary = summary.replace('**', '').replace('__', '')
        return summary
    return ""


#CSS configs, responssible for the pdf's appearance
CSS_STYLES = """
@page {
    size: A4;
    margin: 25mm 16mm 25mm 16mm;

    @bottom-left { content: element(footer-left); }
    @bottom-center { content: element(footer-center); }
    @bottom-right { content: element(footer-right); }
    
}

@page :first {
    margin-top: 0;
    @bottom-left { content: none; }
    @bottom-center { content: none; }
    @bottom-right { content: none; }
    counter-reset: page 0;
    #header-mockup { display: none; }
}

#footer-left {
    position: running(footer-left);
    font-size: 8.5pt;
    color: #2d4a6b;
    padding-bottom: 10mm;
}

#footer-center {
    position: running(footer-center);
    font-size: 9pt;
    font-weight: 600;
    color: #2d4a6b;
    padding-bottom: 10mm;
}

#footer-right {
    position: running(footer-right);
    text-align: right;
    padding-bottom: 10mm;
}

#footer-right img {
    height: 20px;
    width: auto;
}

#header-mockup {
    position: fixed; 
    top: -28mm;   
    right: -20mm; 
    width: 40mm;  
    height: 25mm; 
    z-index: 1000;
    overflow: hidden;
}

#header-mockup img {
    width: 100%;
    height: 100%;
    object-fit: cover; 
    object-position: center;
    border: none;
    margin: 0;
}

/* --- COVER STYLES --- */
.cover-page {
    page-break-after: always;
    height: 100%;
}

.cover-body {
    text-align: right;
    margin-top: 60mm;
    padding-right: 5mm;
}

.cover-title {
    font-size: 28pt;
    font-weight: 700;
    color: #1a2d42;
    line-height: 1.1;
    margin-bottom: 10mm;
    text-transform: uppercase;
}

.cover-summary {
    font-size: 11pt;
    color: #4a5568;
    max-width: 110mm;
    margin-left: auto;
    line-height: 1.6;
}

html, body {
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 10.5pt;
    color: #1e2d3d;
    background: #ffffff;
    line-height: 1.65;
    margin: 0;
    padding: 0;
}

.doc-header {
    background: linear-gradient(135deg, #1a2d42 0%, #2d4a6b 60%, #3b6ea5 100%);
    color: #ffffff;
    padding: 18mm 18mm 16mm 18mm;
    margin: 0 -16mm 0 -16mm;
    page-break-after: avoid;
    position: relative;
    overflow: hidden;
}

.doc-header::before {
    content: '';
    position: absolute;
    top: -30px;
    right: -30px;
    width: 180px;
    height: 180px;
    border-radius: 50%;
    background: rgba(78, 205, 196, 0.10);
}


.doc-header::after {
    content: '';
    position: absolute;
    bottom: -20px;
    right: 80px;
    width: 110px;
    height: 110px;
    border-radius: 50%;
    background: rgba(91, 142, 196, 0.12);
}

.header-badge {
    display: inline-block;
    color: #4ecdc4;
    font-size: 7pt;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 3px 10px;
    border: 1px solid #4ecdc4;
    border-radius: 20px;
    margin-bottom: 12px;
    background: rgba(78, 205, 196, 0.15);
}

.header-title {
    font-size: 24pt;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 8px;
}

.header-line {
    width: 48px;
    height: 3px;
    background-color: #4ecdc4;
    border-radius: 2px;
    margin: 10px 0;
}

.header-subtitle {
    font-size: 9pt;
    color: rgba(255, 255, 255, 0.6);
}

.page-wrapper {
    padding: 10mm 0 0 0;
}

h1 {
    font-size: 15pt;
    font-weight: 700;
    color: #1a2d42;
    margin-top: 22px;
    margin-bottom: 10px;
    padding-bottom: 7px;
    border-bottom: 2px solid #d0d9e8;
    page-break-after: avoid;
}

h2 {
    font-size: 12pt;
    font-weight: 600;
    color: #2d4a6b;
    margin-top: 18px;
    margin-bottom: 8px;
    padding-left: 10px;
    border-left: 4px solid #4ecdc4;
    page-break-after: avoid;
}

h3 {
    font-size: 10.5pt;
    font-weight: 600;
    color: #3b6ea5;
    margin-top: 12px;
    margin-bottom: 5px;
    page-break-after: avoid;
}

h4 {
    font-size: 10pt;
    font-weight: 600;
    color: #4a5568;
    margin-top: 10px;
    margin-bottom: 4px;
}

p {
    margin-bottom: 8px;
    color: #1e2d3d;
}

ul, ol {
    margin: 6px 0 10px 18px;
    padding: 0;
}

li {
    margin-bottom: 4px;
    color: #1e2d3d;
}

strong {
    font-weight: 600;
    color: #1a2d42;
}

em {
    color: #4a5568;
    font-style: italic;
}

code {
    background: #eef1f6;
    border: 1px solid #d0d9e8;
    border-radius: 3px;
    padding: 1px 5px;
    font-size: 9pt;
    color: #2d4a6b;
    font-family: 'Courier New', monospace;
}

pre {
    background: #1a2d42;
    border-left: 3px solid #4ecdc4;
    border-radius: 6px;
    padding: 12px 14px;
    margin: 10px 0;
    page-break-inside: avoid;
}

pre code {
    background: none;
    border: none;
    color: #e2e8f0;
    font-size: 8.5pt;
    padding: 0;
}

.toc-page { 
    page-break-after: always; 
}

.toc-title { 
    font-size: 20pt; 
    font-weight: bold; 
    color: #1a2d42; 
    margin-bottom: 15mm; 
    border-bottom: 2px solid #1a2d42; 
    padding-bottom: 10px; 
    text-transform: uppercase;
}


.toc-container div.toc ul { 
    list-style: none; 
    padding: 0; 
    margin: 0;
}

.toc-container div.toc li {
    margin-bottom: 8px;
}


.toc-container div.toc a { 
    text-decoration: none; 
    color: #1e2d3d; 
    display: flex; 
    align-items: baseline; 
    font-size: 11pt;
    font-family: 'Segoe UI', Arial, sans-serif;
}


.toc-container div.toc a::before {
    content: "";
    flex-grow: 1;
    order: 2;
    border-bottom: 1px dotted #aaa; 
    margin: 0 10px;
    position: relative;
    top: -4px;
}


.toc-container div.toc a::after { 
    content: target-counter(attr(href), page); 
    order: 3;
    font-weight: bold;
    color: #2d4a6b;
    min-width: 20px;
    text-align: right;
}


.toc-container div.toc ul ul {
    padding-left: 20px;
    margin-top: 5px;
}

body {
    font-family: 'Segoe UI', sans-serif;
    color: #333;
    line-height: 1.6;
}

blockquote {
    background: rgba(78, 205, 196, 0.07);
    border-left: 3px solid #4ecdc4;
    border-radius: 0 6px 6px 0;
    padding: 10px 14px;
    margin: 10px 0;
    color: #2d4a6b;
    font-style: italic;
    page-break-inside: avoid;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}

thead tr {
    background: linear-gradient(90deg, #2d4a6b, #3b6ea5);
    color: #ffffff;
}

thead th {
    padding: 8px 11px;
    text-align: left;
    font-weight: 600;
    font-size: 9pt;
    border: none;
}

tbody tr { background: #ffffff; }
tbody tr:nth-child(even) { background: #eef1f6; }

tbody td {
    padding: 7px 11px;
    border-bottom: 1px solid #d0d9e8;
    color: #1e2d3d;
    vertical-align: top;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 12px auto;
    border-radius: 6px;
    border: 1px solid #d0d9e8;
    page-break-inside: avoid;
}

hr {
    border: none;
    border-top: 1px solid #d0d9e8;
    margin: 20px 0;
}

.approval-section {
    margin-top: 40mm;
    page-break-inside: avoid; 
    width: 100%;
    text-align: center; 
    font-size: 0; 
}

.info-box {
    display: inline-block;
    width: 30%; 
    margin: 0 1.5%;
    border: 1px solid #2d4a6b;
    border-radius: 4px;
    padding: 8px 12px;
    box-sizing: border-box;
    text-align: left;
    vertical-align: top;
    min-height: 50px; 
    background-color: #f8fafc;
}

.box-title {
    font-size: 8pt;
    font-weight: 700;
    color: #4a5568;
    text-transform: uppercase;
    margin-bottom: 10px;
    border-bottom: 1px solid #d0d9e8;
    padding-bottom: 4px;
}

.box-content {
    font-size: 10pt;
    color: #1a2d42;
    text-align: center;
    font-weight: 600;
}
"""


def build_html(dashboard_name: str, body_html: str, toc_html: str, logo_b64: str, mockup_b64: str, summary: str) -> str:
    data_atual = datetime.now().strftime("%d/%m/%Y")
    
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>{dashboard_name}</title>
</head>
<body>

<div id="footer-left">{dashboard_name}</div>
<div id="footer-center">Página <span style="content: counter(page)"></span></div>
<div id="footer-right">
    <img src="data:image/png;base64,{logo_b64}" alt="logo">
</div>

<div id="header-mockup">
    <img src="data:image/png;base64,{mockup_b64}">
</div>

<section class="cover-page">
    <div class="doc-header">
        <div class="header-badge">Documentação · Power BI</div>
        <div class="header-title">{dashboard_name}</div>
        <div class="header-line"></div>
    </div>
    <div class="cover-body">
        <div class="cover-title">{dashboard_name}</div>
        <div class="cover-summary">{summary}</div>
    </div>
</section>

<section class="toc-page">
    <h1 class="toc-title">ÍNDICE</h1>
    <div class="toc-container">
        {toc_html}  
    </div>
</section>

<div class="page-wrapper">
    {body_html}
</div>

<section class="approval-section">
    <div class="info-box">
        <div class="box-title">Versão</div>
        <div class="box-content">1 - ({data_atual})</div>
    </div>
    
    <div class="info-box">
        <div class="box-title">Desenvolvido por:</div>
        <div class="box-content">Victor Marques</div> </div>
    
    <div class="info-box">
        <div class="box-title">Aprovado por:</div>
        <div class="box-content">&nbsp;</div> </div>
</section>

</body>
</html>"""


def render(md_path: str | Path, output_path: str | Path | None = None) -> Path:
    """
    Render the MD to PDF, assuring that the title and the first paragraph 
    will be used only in the cover and removing them from de doc body
    """
    md_path = Path(md_path)
    if not md_path.exists():
        print(f"Erro: Arquivo {md_path} não encontrado.")
        sys.exit(1)

    output_path = Path(output_path) if output_path else md_path.with_suffix(".pdf")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"  → Processando: {md_path.name}")
    
    md_text = md_path.read_text(encoding="utf-8")
    dashboard_name = md_path.stem.replace("_", " ").title()

    summary_text = extract_summary(md_text)

    lines = md_text.splitlines()


    if lines and lines[0].strip().startswith('#'):
        lines.pop(0)
        

    while lines and not lines[0].strip():
        lines.pop(0)


    while lines and lines[0].strip():
        lines.pop(0)


    md_body = "\n".join(lines).strip()

    root_path = md_path.parent.parent.parent
    logo_path = (root_path / "images" / "logo.png").resolve()
    mockup_path = (root_path / "images" / "mockup.png").resolve()

    logo_b64 = encode_image(logo_path)
    mockup_b64 = encode_image(mockup_path)

    content_html, toc_html = md_to_html(md_body) 
    full_html = build_html(
        dashboard_name, 
        content_html, 
        toc_html, 
        logo_b64, 
        mockup_b64, 
        summary_text
    )
    

    full_html = embed_images(full_html, md_path)

    # generating the final pdf
    try:
        HTML(string=full_html, base_url=str(md_path.parent)).write_pdf(
            str(output_path), 
            stylesheets=[CSS(string=CSS_STYLES)]
        )
        print(f"  ✔ PDF gerado com sucesso: {output_path}")
    except Exception as e:
        print(f"  ✘ Erro na geração: {e}")
        raise

    return output_path


def main():
    """CLI Entry point."""
    parser = argparse.ArgumentParser(description="Convert a markdown file to a styled PDF.")
    parser.add_argument("md_file", help="Path to the .md file")
    parser.add_argument("--output", "-o", default=None, help="Output PDF path")
    args = parser.parse_args()

    try:
        render(args.md_file, args.output)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Failed to process PDF: {e}", file=sys.stderr)
        raise


if __name__ == "__main__":
    main()