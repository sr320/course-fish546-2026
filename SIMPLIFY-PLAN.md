# Plan: Simplify FISH 546 (2026) to One Track, One Repo, One Home Platform

**Status:** phases 1–4 implemented in this repo (uncommitted as of Sep 7, 2026). Phase 5 complete: org created, `project-template` pushed and marked as a template (Sep 7, 2026).
Supersedes the workflow sections of `PLAN.md` and all of `ASSIGNMENTS-REPO-PLAN.md`.

**Goal.** Keep every weekly learning objective and the final compendium, but cut
the number of things a student must juggle:

| Dimension | Now | Target |
|---|---|---|
| Weekly deliverables | 3 (question set Tue, assignment Fri, progress issue) | 1 weekly notebook entry, Friday 5pm |
| Repositories a student touches | 3 (assignments repo, course repo, own repo) | 1 (own repo, created from a template) |
| Automation to maintain | PR pre-check bot, manifest schema, progress-issue parser, labeler | none required (optional link checker only) |
| Issue forms | 5 | 2 (Project Proposal, Help Request) |
| Platforms required before Week 1 | 3 | 1 (own computer). Raven in Week 1, Hyak in Week 3 |
| Shared canned assignments | 8 to 10, everyone does all | 4 core weeks shared; Weeks 5 to 8 apply the method to your own project, canned fallback provided |
| Grade components | 5 | 3 |
| Site navbar items | 7 | 4 |

**Principle.** The weekly assignment *is* the project step. The student's repo *is* the
submission. The instructor's weekly comment *is* the feedback loop.

---

## 1. Target student experience

The whole course, as a student sees it:

1. Before Week 1: do Tutorial 1, create your repo from the template, open a
   Project Proposal issue (can be a rough draft).
2. Every week: read the lecture page, do the week's work in your repo, write
   `notebooks/weekNN.qmd` from the template, render it, push by Friday 5pm, and
   paste the commit link as a comment on your Project Proposal issue.
3. The instructor replies to that comment within a few days with feedback.
4. Week 5: mid-quarter update in class. Week 10: compendium and final talk.
5. Stuck? Open a Help Request issue.

That is the entire submission contract. It should fit on one page of the site, and it will
(`how-we-work.qmd`, section 3.1).

---

## 2. Course design changes

### 2.1 Grading (edit `index.qmd`)

| Component | Weight | Evidence |
|---|---:|---|
| Weekly notebook entries (Weeks 1 to 9, best 8 of 9) | 60% | `notebooks/weekNN.qmd` + rendered HTML, linked from the project issue |
| Presentations (mid-quarter update + final) | 15% | In class; slides or rendered notebook in repo |
| Final compendium | 25% | Repo state at Week 10 tag `v1.0` |

Late policy unchanged (40% deduction, not accepted after 5 days). "Best 8 of 9"
replaces the need for an excused-absence process.

### 2.2 The weekly notebook entry

One Quarto document per week, always the same five sections. This maps directly to the
existing weekly-progress rubric criteria plus one analysis criterion.

```
notebooks/week03.qmd
---
title: "Week 03 — Mapping, assembly, and quantification"
---
## 1. This week's analysis            <- the assignment (project step or canned fallback)
## 2. Reflection questions             <- 2 to 3 questions from the lecture page
## 3. Project progress                 <- what moved, with links to commits/outputs
## 4. Blockers                         <- or "none"
## 5. Next week                        <- one to three concrete goals
```

A checklist lives in the template header comment (rendered report committed, outputs in
`output/`, no raw data committed, paths relative to repo root). This replaces
`submission.yml` and the PR bot.

**Weekly entry rubric** (goes in `how-we-work.qmd`, 100 points, reuse existing wording):

| Criterion | Points | Source |
|---|---:|---|
| Analysis: appropriate method, intermediate checks, correct interpretation | 30 | new; adapt "Technical execution" from compendium rubric |
| Evidence of work: links to commits, outputs, figures | 20 | existing weekly-progress rubric |
| Reproducible practice: layout, paths, rendered from clean session | 15 | existing |
| Reflection questions answered with reasoning | 15 | replaces question-set grade |
| Blockers and help-seeking | 10 | existing |
| Next-week plan | 10 | existing |

### 2.3 Schedule (edit `schedule.qmd`)

| Week | Topic (unchanged) | Weekly analysis |
|---|---|---|
| 00 | Habits and provenance | Repo from template; first commit; Project Proposal issue (draft) |
| 01 | Sequence databases and BLAST | **Core.** Canned BLAST exercise + one BLAST on a sequence from your project. **Roster PR** (see below) |
| 02 | Raw reads, FASTQ, QC | **Core.** QC on provided FASTQ; QC on one of your own files if available |
| 03 | Mapping, assembly, quantification | **Core.** Smallest slice of your workflow to one intermediate product. Hyak tutorial assigned this week |
| 04 | RNA-seq and DGE | **Core.** Canned count matrix to DGE table; non-RNA-seq projects map their own workflow onto the same stages |
| 05 | Annotation and ranges | **Track.** Annotate/overlap something from your project; fallback: provided BED/GFF exercise. Mid-quarter update |
| 06 | Variants | **Track.** Same pattern; fallback: provided VCF |
| 07 | Methylation | **Track.** Same pattern; fallback: provided methylation table + IGV |
| 08 | eDNA and metabarcoding | **Track.** Same pattern; fallback: provided amplicon run on Klone |
| 09 | Synthesis | Final figure draft + limitations paragraph |
| 10 | Compendium | Tag `v1.0`; final talk |

"Track" weeks: the lecture page states the objective, then "In your project: ..." with two
or three concrete prompts, then "If your project has no natural fit: ..." linking the
canned exercise. Students choose; both are graded with the same rubric.

**Week 1 roster PR.** The only required pull request in the course. Students add one line
(name, repo link, project track) to `roster.md` in the course repo via a fork-and-PR.
Reviewed and merged during Thursday's working session. Teaches the mechanic once.

**Dates.** Put real Tuesday/Thursday dates on every card. Add a `current` class to the
current week's card (manually bumped, or a 10-line JS snippet comparing today to the card's
`data-start` attribute).

### 2.4 Platforms, staged (edit `setup.qmd`, tutorials, `index.qmd`)

| When | Required | Why then |
|---|---|---|
| Before Week 1 | Tutorial 1 (own computer, Git, GitHub) | Needed to create the repo and first commit |
| Week 1, Thursday session | Tutorial 2 (Raven) | First real analysis (BLAST) runs here; do it together in class |
| Week 3 | Tutorial 3 (Hyak) | First workflow that may exceed Raven; eDNA track needs it in Week 8 |

Message on the site: "Raven is home. Your laptop is for editing and Git. Hyak is for when
Raven is not enough." The completion blocks from each tutorial are pasted as a comment on
the Project Proposal issue instead of a separate Setup Check issue.

### 2.5 Issues (edit `.github/ISSUE_TEMPLATE/`)

Keep two forms:

- **Project Proposal** (`10-project-proposal.yml`): unchanged fields, plus a note that
  this issue is the weekly comment thread and where tutorial completion blocks go.
- **Help Request** (`30-help-request.yml`): merge in the "steps to reproduce" field from
  the Blocker/Bug form, then delete `40-blocker-bug.yml`.

Delete `00-setup-check.yml` and `20-weekly-progress.yml`. In `config.yml` drop the
Discussions link unless the org enables Discussions (decision D4); keep Slack and the
Handbook.

---

## 3. Repository and site changes, file by file

### 3.1 Site pages

| File | Action |
|---|---|
| `index.qmd` | Rewrite Grading and Submitting work sections per 2.1. Replace the three-tier table's "three tutorials before Week 1" callout with the staged version. Point to `how-we-work.qmd`. |
| `schedule.qmd` | Rebuild cards per 2.3: one "Analysis" link per week pointing to `assignments/NN-*.qmd` on this site, no Questions row, dates on every card, `current` marker. Add "Roster PR" chip to Week 01. |
| `setup.qmd` | Retitle "Setup". Show the staged table. Tutorial 1 is the only "before class" item. Remove Setup Check issue instructions; say where completion blocks go. |
| `how-we-work.qmd` (new) | Merge `support.qmd` + `turn-in.qmd` + `rubric.qmd`. Sections: The weekly loop (1 page), Where things live (one table: your repo / course repo / Slack), Notebook template and checklist, Weekly entry rubric, Compendium rubric, Presentation rubric, Skills reference (RStudio/Raven, Quarto, Hyak, archiving, troubleshooting checklist, trimmed). |
| `support.qmd`, `turn-in.qmd`, `rubric.qmd` | Delete after merge. Add redirects if Quarto `aliases` are wanted for old links (`aliases: [support.html, turn-in.html, rubric.html]` in `how-we-work.qmd` front matter). |
| `edna.qmd` (hub) | Delete. Its content is duplicated by `lectures/08-edna.qmd`. |
| `about.qmd` | Keep; link from page footer instead of navbar. |
| `_quarto.yml` | Navbar: Syllabus, Schedule, Setup, How We Work (+ GitHub icon right). Add `page-navigation: true`. Add a `lectures` sidebar listing Weeks 00 to 10 so lecture pages have a left nav. Add `page-footer` with About and Handbook links. Add `assignments/*.qmd` to render list. |

### 3.2 Lectures (`lectures/*.qmd`)

- Rename `lectures/edna.qmd` to `lectures/08-edna.qmd`; update the two inbound links.
- In every lecture, rename "Project checkpoint" to "This week in your project" and add
  a "Reflection questions" section holding the 2 or 3 questions kept from the old
  question set (source: `git show 4d4f8f0:questions/weekNN.qmd`). Add a link to the
  week's analysis page.
- Convert plain-text References to links (Handbook pages, IGV, BEDtools, Quarto docs).
- Add a one-line callout at the top: "Week NN. Analysis: [link]. Due Friday 5pm."

### 3.3 Restore and prune assignment prompts

The prompts still exist in git at commit `4d4f8f0`. Restore, then keep one per week:

```bash
git checkout 4d4f8f0 -- assignments/ _student-checklist.qmd
```

| Keep (rename to match week) | Drop (previous-year tooling weeks) |
|---|---|
| `00-bash`, `01-blast`, `02-fastq-qc`, `03-mapping-quantification`, `04-DGE`, `05-annotation-ranges`, `06-variants`, `07-CG` → `07-methylation`, `edna-metabarcoding` → `08-edna`, `09-synthesis`, `10-compendium` | `02-DGE`, `03-knit`, `04-hyak`, `05-slidedeck`, `08-bedtools`, `09-backup` |

For each kept prompt: change "What to submit" to point at `notebooks/weekNN.qmd` section 1;
for Weeks 5 to 8 add the "In your project" prompts above the canned tasks; replace the
`_student-checklist.qmd` include with a link to the checklist in `how-we-work.qmd`.
Delete `questions/` after the questions are moved into lectures (3.2).

### 3.4 Tutorials (`tutorials/*.html`, `tutorial.css`)

- Add a header link in each sidebar: "← Course site" to `../setup.html`.
- Add "Next up: Tutorial 3" note to the end of `02-raven.html` (currently missing).
- Change the "Pre-course · Tutorial N of 3" kicker to the staged timing ("Before Week 1",
  "Week 1", "Week 3").
- Change completion instructions from "paste into your Setup Check issue" to "paste as a
  comment on your Project Proposal issue".
- Mobile fixes in `tutorial.css`: `.hero h2 { overflow-wrap: anywhere; font-size: clamp(24px, 6vw, 36px); }`;
  under the 820px media query collapse `nav.side` to a horizontal scrolling strip or a
  `<details>` toggle so it does not occupy a full screen before content.
- Optional: add a `prefers-color-scheme: dark` block so the tutorials do not flash white
  for dark-mode users of the Quarto site.

### 3.5 GitHub automation and scripts

| Path | Action |
|---|---|
| `.github/workflows/progress-assessment.yml` | Delete |
| `scripts/parse_progress_issue.py`, `scripts/assess_progress_issue.py` | Delete |
| `.github/labels.yml` | Remove `setup`, `progress`, `progress:*`, `submission`, `question-set`, `assignment`, `bug`. Keep `project`, `help`, topic labels, platform labels. Add `week-01` … `week-10` only if you want to label weekly comments (probably not). |
| `.github/workflows/label-sync.yml`, `greetings.yml` | Keep; update greeting text (no Discussions if D4 = no) |
| `.github/ISSUE_TEMPLATE/` | Per 2.5. Fix the hardcoded `course-fish546-2026.github.io` URL wherever it remains. |
| `roster.md` (new) | Header row plus one example line, for the Week 1 PR exercise |
| `.github/PULL_REQUEST_TEMPLATE.md` (new, tiny) | Three checkboxes for the roster PR |

The `fish546-2026-assignments` repo is **not** created.

### 3.6 Student template repository (new, in the org)

Create `course-fish546-2026/project-template` and mark it as a GitHub template repo so
students click "Use this template" and pick the org as owner.

```
project-template/
├── README.md                 # title, question, data source, platform, endpoint (fill-in headings)
├── .gitignore                # data/raw/, *_files/, .Rproj.user, .DS_Store, *_cache/
├── code/README.md
├── data/README.md            # how raw data are recorded but not committed; checksums
├── data/raw/.gitkeep
├── output/README.md
├── notebooks/
│   ├── _template.qmd         # the five-section entry from 2.2 with the checklist in a comment
│   └── week00.qmd            # filled example
└── _quarto.yml               # project: default, so `quarto render notebooks/weekNN.qmd` works
```

Tutorial 1 step 5 changes from "create a new repository named for yourself" to "use the
template".

**Status (Sep 7, 2026):** live at <https://github.com/course-fish546-2026/project-template>, marked as a
template. Local clone at `~/Documents/GitHub/project-template`. It was published with:

```bash
cd ~/Documents/GitHub/project-template
gh repo create course-fish546-2026/project-template --public \
  --description "Starting point for FISH 546 (2026) student repositories" \
  --source . --push
gh repo edit course-fish546-2026/project-template --template
```

### 3.7 Styles

- `styles.css`: change `.schedule-chip` from `inline-flex` to `inline-block` (fixes the
  "OpenSetup Checkissue" whitespace collapse). Add `.schedule-card.current` outline style.

### 3.8 Housekeeping

- `README.md`: rewrite the summary and Structure table for the new layout.
- Move `PLAN.md` and `ASSIGNMENTS-REPO-PLAN.md` to `planning/` with a one-line
  "superseded by SIMPLIFY-PLAN.md" note at the top of each, or delete them.
- `docs/`: re-render; delete stale `docs/edna.html`, `docs/support.html`,
  `docs/turn-in.html`, `docs/rubric.html`, `docs/lectures/edna.html` if aliases are not used.

---

## 4. Phases and effort

| Phase | Work | Est. | Depends on |
|---|---|---:|---|
| 0. Decisions | Answer D1 to D6 below | 30 min | — |
| 1. Site skeleton | `_quarto.yml` navbar/sidebar/footer, `how-we-work.qmd` merge, delete hub pages, chip CSS, `index.qmd` grading | 3 h | 0 |
| 2. Prompts and lectures | Restore/prune `assignments/`, fold questions into lectures, rename eDNA lecture, link references, callouts | 4 h | 1 |
| 3. Schedule | Cards, dates, current-week marker, roster chip | 1.5 h | 2 (needs final assignment file names) |
| 4. Tutorials | Back links, staged kickers, T2→T3 handoff, mobile CSS, completion-block wording | 1.5 h | 0 |
| 5. GitHub org | Create org, `project-template` repo, `roster.md`, prune issue forms/labels/workflows, delete `scripts/` | 2 h | 0 |
| 6. Verify | `quarto render`; link check (script below); browser check of schedule, one lecture, one tutorial at desktop and 375px; open a test issue with each form; "Use this template" as a test student | 1.5 h | 1–5 |
| 7. Launch | Commit, push, confirm Pages; announce on Slack with the one-paragraph loop from section 1 | 30 min | 6 |

Total about two working days. Phases 4 and 5 can run in parallel with 1 to 3.

Link check for phase 6:

```bash
grep -rhoE 'https?://[^) "<>]+' *.qmd lectures assignments tutorials .github | sort -u | \
  while read u; do printf "%s %s\n" "$(curl -s -o /dev/null -w '%{http_code}' -L --max-time 15 "$u")" "$u"; done | sort
```

---

## 5. Decisions needed (instructor)

| # | Decision | Default if no answer |
|---|---|---|
| D1 | ~~Quarter start date and meeting days/times/room~~ **Decided:** Tue 3:00–4:20 PM (Oct 6 – Dec 8), Thu 9:30–11:20 AM (Oct 1 – Dec 10, no class Nov 26), FSH 203. Thu Oct 1 is the Week 0 setup session; Week 8 entry due Mon Nov 30. | — |
| D2 | Keep a Tuesday reading check? (3 questions as an issue comment before class, or in-class, or none) | None; reflection questions live in the Friday entry |
| D3 | Which week assigns the Hyak tutorial: 2 or 3? | Week 3 |
| D4 | Enable GitHub Discussions on the org, or Slack only? | Slack only; remove Discussions links |
| D5 | Where do canned fallback datasets live: `/gscratch/srlab/fish546/` on Klone plus a Raven path, or URLs in each prompt? | Klone + Raven paths listed in each prompt |
| D6 | Keep any automation? A weekly reminder Action that comments "entry due Friday" on every open `project` issue is 20 lines and zero student-facing complexity | No automation in v1 |

---

## 6. Risks and mitigations

- **Students never practice PRs.** Mitigated by the Week 1 roster PR. If more is wanted,
  Week 9 peer review can be a PR comment on a classmate's notebook (optional).
- **Instructor feedback becomes the bottleneck.** One comment per student per week. At 15
  students that is about an hour weekly. If the cohort exceeds ~20, revisit D6 and consider
  restoring a lightweight file-presence check.
- **Track weeks feel unstructured.** Every track week has a canned fallback with the same
  rubric, and the "In your project" prompts are concrete (e.g., "overlap your candidate
  regions with the gene annotation and report counts").
- **Losing the old pages' URLs.** Use Quarto `aliases` on `how-we-work.qmd` so bookmarks
  to `support.html`, `turn-in.html`, and `rubric.html` still resolve.
- **Template repo drift.** Keep the template minimal; students are told once in Week 0 that
  the template is a starting point, not a constraint.

---

## 7. Definition of done

- [ ] A new student can read `how-we-work.qmd` and describe the weekly loop without asking
- [ ] Every link on the live site returns 200 (phase 6 script)
- [ ] Every lecture page has previous/next navigation and a link to its analysis page
- [ ] Every schedule card has dates and exactly one analysis link
- [ ] Tutorials link back to the site and render without horizontal overflow at 375px
- [ ] Issue chooser shows exactly two forms
- [ ] "Use this template" produces a repo where `quarto render notebooks/week00.qmd` succeeds
- [ ] `roster.md` exists and a test PR against it can be opened and merged
- [ ] Old plan files are moved or marked superseded; `README.md` matches the new structure
