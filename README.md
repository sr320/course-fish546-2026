# course-fish546-2026

FISH 546 — **Bioinformatics for Environmental Sciences** (University of Washington, SAFS), Autumn 2026. This repository builds the course website with [Quarto](https://quarto.org), published to GitHub Pages from `docs/` at <https://sr320.github.io/course-fish546-2026/>. It also hosts the two issue forms students use all quarter.

## How the course works

One loop, described in full on the site's [How We Work](https://sr320.github.io/course-fish546-2026/how-we-work.html) page:

- Each student has **one repository** in the [course organization](https://github.com/course-fish546-2026), created from [`project-template`](https://github.com/course-fish546-2026/project-template).
- Each week has **one deliverable**: a notebook entry (`notebooks/weekNN.qmd`) containing the week's analysis, reflection questions, project progress, blockers, and next-week goals. Due Friday 5:00 PM.
- Students post the commit link as a comment on their **Project Proposal issue** here. The instructor replies in the thread.
- Weeks 1–4 are shared exercises; Weeks 5–8 apply each method to the student's own project (canned fallbacks provided). Week 5 is the mid-quarter update; Week 10 is the compendium and final talk.
- Platforms come online in stages: own computer before Week 1, Raven in Week 1, Hyak in Week 3.

Design rationale and the implementation plan: [SIMPLIFY-PLAN.md](SIMPLIFY-PLAN.md). Earlier plans are in `planning/` for history.

## Local preview

```bash
quarto preview      # live-reload while editing
quarto render       # build the site into docs/
```

The three setup tutorials are standalone HTML; open `tutorials/*.html` directly in a browser.

## Course-site audit

Run the offline audit before committing student-facing changes:

```bash
python3 scripts/audit_course_site.py
```

The audit checks source links, generated-site links and anchors, published tutorial
copies, and the render-source manifest. After a successful `quarto render`, record the
new accepted source state with:

```bash
python3 scripts/audit_course_site.py --write-manifest
```

Before publishing a course offering, review external destinations from a networked
environment:

```bash
python3 scripts/audit_course_site.py --external
```

See [`maintenance/RESOURCE_INVENTORY.md`](maintenance/RESOURCE_INVENTORY.md) for the
canonical destination map and [`maintenance/EXTERNAL_LINK_REVIEW.md`](maintenance/EXTERNAL_LINK_REVIEW.md)
for the review procedure.

## Structure

| Path | What |
|------|------|
| `index.qmd` | Syllabus: format, meeting times, grading |
| `schedule.qmd` | Dated weekly cards; the current week is outlined automatically |
| `setup.qmd` | The three platform tutorials and when each is needed |
| `how-we-work.qmd` | Weekly loop, where things live, notebook template, all rubrics, skills reference |
| `lectures/` | Weekly topic pages (with reflection questions) |
| `assignments/` | Weekly analysis pages |
| `tutorials/` | Three self-paced HTML tutorials + shared CSS/JS |
| `roster.md` | Week 1 pull-request exercise |
| `.github/ISSUE_TEMPLATE/` | Project Proposal and Help Request forms |
| `.github/workflows/` | First-issue greeting, label sync |
| `SIMPLIFY-PLAN.md` | Course design and implementation plan |
