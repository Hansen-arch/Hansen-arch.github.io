# Portfolio Content Sources & Update Guide

**Purpose:** Every public page on this website must be traceable to a real document.
When you update one of the source files below, re-sync the matching page here before publishing.

Last synced: 2026-09-22

---

## Source of truth map

| Website page | Source file (single source of truth) | Last synced |
|---|---|---|
| `docs/index.md` (hero, about, skills) | `~/Documents/Personal/CV and Cover Letters/Reihan_Apriandi_CV updated.pdf` — Profile, Skills sections | 2026-09-22 |
| `docs/experience.md` (all work + org experience) | same PDF — Professional Experience, Leadership & Organizational Experience | 2026-09-22 |
| `docs/experience.md` (education) | same PDF — Education (8th semester, GPA 3.68/4.00) | 2026-09-22 |
| `docs/experience.md` (certifications) | same PDF — Certifications (4 categories) | 2026-09-22 |
| `docs/contact.md` (location, phone, email) | same PDF — header line | 2026-09-22 |
| `docs/assets/reihan-CV.pdf` (Download CV button) | same PDF — copied verbatim | 2026-09-22 |
| `docs/projects/biosift.md` | GBIF Ebbe Nielsen Challenge submission + biosift repo | 2026 (unchanged) |

**Excluded by decision (2026-09-22):** the GSK Deforestation thesis project. The thesis is
not complete — do not add a project page for it until the thesis itself is finished. The
working repo lives at `~/Thesis_GSK_Deforestation` (GEE land-cover pipeline). When it is
ready, copy the checklist from the top of `docs/projects/biosift.md`.

---

## Update workflow (every time the CV changes)

1. Save the new CV as `Reihan_Apriandi_CV updated.pdf` in
   `~/Documents/Personal/CV and Cover Letters/`
2. Update the three content pages (`index.md`, `experience.md`, `contact.md`) from it
3. Copy the PDF over `docs/assets/reihan-CV.pdf`
4. Update the "Last synced" dates in the table above and in the checklist comment
   at the top of `docs/experience.md`
5. Preview locally: `conda activate portfolio && mkdocs serve --livereload` → http://127.0.0.1:8000
6. Review, then commit and push (GitHub Actions publishes the site)

Reference tutorial: <https://courses.spatialthoughts.com/geospatial-portfolio-workshop.html>
(§6.1 "Updating Content Pages", §6.4 "Adding a Project Page")

---

## Style decisions (professional restyle, 2026-09-22)

- Palette: muted forest/earth tones (`#22332b` dark, `#43695a` accent) — same variable
  names as before, both light/slate schemes supported
- Typography: Inter only (dropped Merriweather); uppercase letter-spaced tagline in hero
- Cards: flat white/dark surfaces with 2px top border, hover = border highlight
  instead of heavy lift/shadow
- Timeline: smaller dots, thinner rail, compact entries with muted date line
- Skills grid (2026-09-23): four cards, each bullet a capability with the certification or
  project that proves it in parentheses (NASA ARSET, Spatial Thoughts, Esri, Copernicus Marine,
  RECOFTC, UNITAR, Harimau Kita, Google, Oracle, DataCamp, openHPI). Self-assessed skill levels
  (e.g. ML "Basic") are deliberately excluded from the site; if the CV keeps them, the site
  still does not repeat them. Full list on experience.md#certifications
- `mkdocs.yml`: `site_description` matches the CV tagline; theme/font config unchanged

## Verify before publishing

- [ ] All dates/claims on experience.md appear verbatim in the source CV
- [ ] Download CV button serves the updated PDF (check file size ≈ 120 KB)
- [ ] Dark mode renders correctly (toggle in header)
- [ ] No thesis project page present
