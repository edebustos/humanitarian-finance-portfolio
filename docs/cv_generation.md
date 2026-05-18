# CV Generation

This repository includes a generated recruiter-friendly PDF CV at:

`assets/docs/Ernesto_de_Bustos_CV.pdf`

## Source Files Used

The PDF CV is curated from the public portfolio content in:

- `index.html`
- `pages/profile.html`
- `pages/projects.html`
- `README.md`
- `docs/portfolio_context.md`

The CV content reflects the portfolio positioning around humanitarian finance, operations management, donor compliance, CVA programming, field coordination, donor exposure, country footprint, and humanitarian analytics.

## Regenerating the PDF

From the repository root, run:

```powershell
& "C:\Users\edebu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" scripts/generate_cv_pdf.py
```

The script writes:

`assets/docs/Ernesto_de_Bustos_CV.pdf`

After regenerating, verify that the PDF remains exactly two pages and that the homepage button still points to:

`assets/docs/Ernesto_de_Bustos_CV.pdf`

## Notes

- The PDF is intentionally ATS-friendly: clean text, limited graphics, standard typography, and concise section headings.
- The generated version is designed for NGO, Red Cross Movement, and UN-style application processes.
- Update the source portfolio pages first, then regenerate the PDF so public web content and downloadable CV stay aligned.
