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

import markdown
from weasyprint import HTML, CSS


def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def embed_images(html: str, md_path: Path) -> str:
    # replaces local image src with base64 so the PDF is self-contained
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
    return markdown.markdown(md_text, extensions=["extra", "toc", "sane_lists", "nl2br"])


CSS_STYLES = """
@page {
    size: A4;
    margin: 16mm 16mm 20mm 16mm;

    @bottom-right {
        content: element(page-footer);
        padding-right: 2mm;
    }
}

@page :first {
    margin-top: 0;
}

#page-footer {
    position: running(page-footer);
    text-align: right;
}

#page-footer img {
    height: 18px;
    width: auto;
    border: none;
    margin: 0;
    display: inline-block;
}

#page-footer span {
    color: #2d4a6b;
    font-weight: 600;
    font-size: 9pt;
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
    margin: -16mm -16mm 0 -16mm;
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
"""


def build_html(dashboard_name: str, body_html: str, logo_b64: str = "") -> str:
    from datetime import date
    date_str = date.today().strftime("%d/%m/%Y")

    footer = (
        f'<img src="data:image/png;base64,{logo_b64}" alt="logo" />'
        if logo_b64 else
        '<span>employerDados</span>'
    )

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>{dashboard_name}</title>
</head>
<body>

<div id="page-footer">{footer}</div>

<div class="doc-header">
    <div class="header-badge">Documentação · Power BI</div>
    <div class="header-title">{dashboard_name}</div>
    <div class="header-line"></div>
    <div class="header-subtitle">{date_str}</div>
</div>

<div class="page-wrapper">
{body_html}
</div>

</body>
</html>"""


def render(md_path: str | Path, output_path: str | Path | None = None) -> Path:
    md_path = Path(md_path)
    if not md_path.exists():
        raise FileNotFoundError(f"File not found: {md_path}")

    output_path = Path(output_path) if output_path else md_path.with_suffix(".pdf")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    md_text        = md_path.read_text(encoding="utf-8")
    dashboard_name = md_path.stem.replace("_", " ")

    # strip first H1 — it becomes the header title
    md_body = re.sub(r"^# .+\n?", "", md_text, count=1)

    # md is at cases/md/file.md → parent = cases/md → parent.parent = cases → parent.parent.parent = project root
    logo_b64  = ""
    logo_path = (md_path.parent.parent.parent / "images" / "logo.png").resolve()
    if logo_path.exists():
        logo_b64 = base64.b64encode(logo_path.read_bytes()).decode()

    body_html = md_to_html(md_body)
    full_html = build_html(dashboard_name, body_html, logo_b64)
    full_html = embed_images(full_html, md_path)

    HTML(string=full_html, base_url=str(md_path.parent)).write_pdf(
        str(output_path), stylesheets=[CSS(string=CSS_STYLES)]
    )
    print(f"DEBUG logo_path: {logo_path}")

    print(f"✅ PDF saved: {output_path}")
    return output_path


def main():
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
        print(f"Failed: {e}", file=sys.stderr)
        raise


if __name__ == "__main__":
    main()