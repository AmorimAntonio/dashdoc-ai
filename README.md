# DashDoc AI

Automatically generates business-facing PDF documentation from Power BI dashboards.

Given a dashboard PDF and a technical DOCX, DashDoc AI uses GPT-4o vision to identify all visual elements, writes structured markdown documentation, and exports a styled PDF ready to share with stakeholders.

---

## How it works

1. Drop your `Dashboard.pdf` and `Dashboard.docx` into the `dashboards/` folder
2. Run `python script.py`
3. Pick up the generated PDF from `cases/`

The pipeline converts each PDF page to PNG, sends them to GPT-4o for visual analysis, generates the documentation in Portuguese using both the images and the technical DOCX context, and renders the final PDF with a branded layout.

---

## Output structure

```
project/
├── dashboards/          # input: PDF + DOCX pairs
├── cases/
│   ├── md/              # intermediate markdown files
│   └── Dashboard.pdf    # final output
└── images/              # page screenshots used in the PDF
```

---

## Setup

**Requirements:** Python 3.10+, [Poppler](https://github.com/oschwartz10612/poppler-windows/releases) (Windows), an OpenAI API key.

```bash
# create and activate the conda environment
conda create -n dashdoc python=3.10
conda activate dashdoc

# install WeasyPrint with its native dependencies (no GTK installer needed)
conda install -c conda-forge weasyprint

# install remaining packages
pip install openai python-dotenv python-docx pdf2image markdown Pillow
```

Create a `.env` file at the project root:

```
OPENAI_API_KEY=sk-...
```

Update `POPPLER_PATH` in `script.py` to point to your local Poppler `bin/` folder.

---

## Input requirements

Each dashboard requires two files in `dashboards/`, both with the same base name:

| File | Description |
|------|-------------|
| `Dashboard_Name.pdf` | Screenshot/export of the Power BI dashboard |
| `Dashboard_Name.docx` | Technical documentation with context about the dashboard |

The DOCX is used to enrich the documentation with business context that may not be visible in the screenshots.

---

## Reprocessing

The pipeline skips dashboards whose PDF already exists in `cases/`. To reprocess, delete the corresponding `.pdf` from `cases/` and the `.md` from `cases/md/`.

---

## Tech stack

- **GPT-4o** — visual analysis and documentation generation
- **WeasyPrint** — HTML/CSS to PDF rendering
- **pdf2image + Poppler** — PDF to PNG conversion
- **python-docx** — DOCX text extraction
- **markdown** — MD to HTML conversion