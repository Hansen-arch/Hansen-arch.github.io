# Portfolio Content Sources & Update Guide

**Purpose:** Every public page on this website must be traceable to a real document.
When you update one of the source files below, re-sync the matching page here before publishing.

Last synced: 2026-11-07

---

## Source of truth map

| Website page | Source file (single source of truth) | Last synced |
|---|---|---|
| `docs/index.md` (masthead, about, capabilities) | `~/Documents/Personal/CV and Cover Letters/Reihan_Apriandi_CV updated Nov 2026.pdf`, Profile, Skills sections | 2026-11-07 |
| `docs/index.md` (readout: location, study, status) | same PDF header and objective line; Pekanbaru coordinates are public geography (0.5071 N, 101.4478 E) | 2026-11-07 |
| `docs/experience.md` (all work + org experience) | same PDF, Professional Experience, Leadership & Organizational Experience | 2026-11-07 |
| `docs/experience.md` (education) | same PDF, Education (8th semester, GPA 3.68/4.00) | 2026-11-07 |
| `docs/experience.md` (certifications) | same PDF, Certifications (4 categories) | 2026-11-07 |
| `docs/contact.md` (location, phone, email) | same PDF, header line | 2026-11-07 |
| `docs/assets/reihan-CV.pdf` (Download CV button) | same PDF, copied verbatim | 2026-11-07 |
| `docs/projects/biosift.md` | GBIF Ebbe Nielsen Challenge submission + biosift repo | 2026 (unchanged) |
| `docs/projects/flood-coverage.md` | flood-coverage repo: README and `docs/03-method.md` | 2026-11-07 |
| `docs/projects/palm-tree-counting.md` | palm-tree-counting-yolo repo: README, `docs/README.md`, `docs/REPORT.md`, `docs/ringkasan_*.json` | 2026-11-07 |
| `docs/projects/urban-heat-island.md` | `pekanbaru-uhi` repo: README, `outputs/zonal_stats.csv`, `outputs/intervention_zones.csv` | 2026-11-08 |
| `docs/projects/urban-green-space.md` | `urban-green-space-change` repo: README, `outputs/data/stats.json`, `outputs/data/area_summary.csv` | 2026-11-08 |
| `docs/projects/species-distribution-models.md` | `species-distribution-models` repo: README, `results/comparison_table.csv`, `results/fold_metrics.csv`, `results/learning_curve.csv` | 2026-11-11 |

**Excluded by decision (2026-11-07):** the `student-stress-analysis` repo. It is a student
course project, not portfolio work. Do not add a page for it.

**Excluded by decision (2026-09-22):** the GSK Deforestation thesis project. The thesis is
not complete, do not add a project page for it until the thesis itself is finished. The
working repo lives at `~/Thesis_GSK_Deforestation` (GEE land-cover pipeline). When it is
ready, copy the checklist from the top of `docs/projects/biosift.md`.

---

## Update workflow (every time the CV changes)

1. Edit `build_cv.py` in `~/Documents/Personal/CV and Cover Letters/` (the DATA block at the
top holds every line of the CV), run `python3 build_cv.py`, then
`libreoffice --headless --convert-to pdf "Reihan_Apriandi_CV updated Nov 2026.docx"`
The Sep 2026 original has no editable source and is kept only for reference.
2. Update the three content pages (`index.md`, `experience.md`, `contact.md`) from it
3. Copy the PDF over `docs/assets/reihan-CV.pdf`
4. Update the "Last synced" dates in the table above and in the checklist comment
   at the top of `docs/experience.md`
5. Preview locally: `conda activate portfolio && mkdocs serve --livereload` → http://127.0.0.1:8000
   (or `.venv/bin/mkdocs serve`)
6. Review, then commit. Publishing is `mkdocs gh-deploy`, which rebuilds and pushes the
   `gh-pages` branch. This repo has no GitHub Actions workflow, so pushing to `main` alone
   does not publish the site.

Reference tutorial: <https://courses.spatialthoughts.com/geospatial-portfolio-workshop.html>
(§6.1 "Updating Content Pages", §6.4 "Adding a Project Page")

---

## Design direction (quiet instrument panel, 2026-11-07)

Supersedes the 2026-09-22 forest-tone restyle. The full direction, palette values and the
reason for each choice live in `DESIGN.md` at the repo root.

- Palette: two neutrals (graphite ground, near-neutral ink) plus one sodium amber accent.
  No gradient, no glow, no shadow, no radius. Amber appears only as the plate index, the
  active tab underline, the primary button and the focus ring.
- Typography: IBM Plex Sans with IBM Plex Mono for data (readouts, plate captions, table
  figures, mono labels). Weights 400/500/600 are loaded explicitly in `overrides/main.html`.
- Structure: hairline rules instead of cards. Home opens with an asymmetric masthead and a
  four-line readout of checkable facts, then numbered panels (01 About, 02 Capabilities,
  03 Connect). Capabilities are a datasheet, not four cards.
- Projects: rows with a mono index, summary, stack line and one linked plate. Plates keep
  their real colour and lose it only on hover, so the accent stays the only warm colour.
- Project pages: the opening image is a plate with a mono caption naming the block and
  ground resolution, because that caption is provenance rather than decoration.
- Experience: a log, one entry per hairline, with the date line in mono.
- Capability bullets still name the certification or project that proves each line (NASA
  ARSET, Spatial Thoughts, Esri, Copernicus Marine, RECOFTC, UNITAR, Harimau Kita, Google,
  Oracle, DataCamp, openHPI). Self-assessed skill levels stay excluded from the site.
- `mkdocs.yml`: `site_description` matches the CV tagline; fonts and social card colours set
  to match the palette

## SEO setup (2026-09-23)

- Per-page `description` and `keywords` front matter on all five pages (meta plugin)
- Social cards plugin: auto-generated og:image per page (requires Pillow + cairosvg)
- JSON-LD Person schema in `overrides/main.html`
- `docs/robots.txt` with sitemap pointer; `not_in_nav` entry in mkdocs.yml
- Canonical URLs and sitemap.xml are generated by mkdocs automatically

## Verify before publishing

- [ ] All dates/claims on experience.md appear verbatim in the source CV
- [ ] Download CV button serves the updated PDF (check file size ≈ 120 KB)
- [ ] Dark mode renders correctly (toggle in header)
- [ ] No thesis project page present
