# course-fish546-2026

FISH 546 — **Bioinformatics for Environmental Sciences** (University of Washington, SAFS). This repository builds the 2026 course website with [Quarto](https://quarto.org), published to GitHub Pages from `docs/`.

See **[PLAN.md](PLAN.md)** for the full build plan. In short, this iteration:

- Stays **Quarto**-based (publishes to `docs/`).
- Splits student work across two repos: **pull-request submissions** for question sets and assignments in the [assignments repo](https://github.com/sr320/fish546-2026-assignments), and **GitHub Issue forms** + labels (`.github/`) for project proposals, weekly progress, and help requests.
- Adds an **eDNA / metabarcoding** module (`lectures/edna.qmd`, `edna.qmd`; the assignment lives in the [assignments repo](https://github.com/sr320/fish546-2026-assignments)).
- Ships **three self-directed, pre-course HTML tutorials** — one per platform students use — in `tutorials/`, with Hyak/Klone getting the deepest treatment.
- Structures weekly lectures, assignments, and question sets around a bioinformatics-first arc: sequence search, raw reads/QC, mapping/quantification, RNA-seq, annotation/ranges, variants, methylation, eDNA, and project synthesis.
- Moves RStudio, Quarto, Hyak mechanics, GitHub Issues, and archiving guidance into `support.qmd` as self-directed skills.
- Uses GitHub-native automatic assessment: pull-request pre-checks with `submission.yml` manifests in the assignments repo, and a weekly-progress assessment workflow on the issue forms here (GitHub Actions).

Core competencies are anchored to the [Roberts Lab Handbook](https://robertslab.github.io/resources/).

## Local preview

```bash
quarto preview      # live-reload while editing
quarto render       # build the site into docs/
```

The three setup tutorials are standalone HTML — just open `tutorials/*.html` in a browser.

## Structure

| Path | What |
|------|------|
| `index.qmd` | Syllabus |
| `schedule.qmd` | 10-week bioinformatics-first schedule |
| `setup.qmd` | Before-class landing page → the 3 tutorials |
| `support.qmd` | Self-directed skills: RStudio, Quarto, GitHub Issues, Hyak, archiving |
| `turn-in.qmd` | How to submit: pull requests to the [assignments repo](https://github.com/sr320/fish546-2026-assignments) |
| `edna.qmd` | eDNA topic hub |
| `tutorials/` | 3 pre-course HTML tutorials (+ shared CSS/JS) |
| `lectures/` | weekly lecture material (assignments & question sets live in the [assignments repo](https://github.com/sr320/fish546-2026-assignments)) |
| `.github/` | issue forms, labels, weekly-progress assessment workflow |
| `scripts/` | weekly-progress parsing/assessment helpers |
| `PLAN.md` | full build plan & open decisions |
