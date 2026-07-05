# FISH 546 (2026) — Build Plan

Bioinformatics for Environmental Sciences. This document is the blueprint for the
2026 course website. It carries forward the working parts of
[`course-fish546-2025`](https://github.com/sr320/course-fish546-2025) and changes
five things deliberately:

1. **Stay Quarto** — same publish-to-`docs/`, GitHub Pages workflow, refreshed theme.
2. **Lean on GitHub Issues** — Issue *Forms* (YAML), labels, a project board, and
   templates drive weekly progress, help requests, and project tracking. Issues become
   the assessed artifact, not an afterthought.
3. **Bioinformatics-first schedule** — weekly topics follow the data arc from sequence
   search to raw reads, mapping/quantification, assay-specific analysis, ecological and
   genomic interpretation, and final synthesis. Tool mechanics are support skills, not
   the subject of entire weeks.
4. **More eDNA** — a dedicated eDNA module (metabarcoding, DADA2/OTU→ASV, taxonomic
   assignment, occupancy) added alongside the existing RNA-seq / methylation / variants
   content, plus an eDNA project track.
5. **Three self-directed pre-course tutorials (HTML)** — one per compute platform the
   students use (own computer, Raven, Hyak/Klone), completed *before* week 1. Hyak gets
   the deepest treatment because it has the steepest learning curve.

Core competencies are anchored to the **Roberts Lab Handbook**
(`../resources`, published at <https://robertslab.github.io/resources/>). Every tutorial
and module maps to specific handbook pages so the course and the lab's living
documentation stay in sync.

---

## 1. Platforms & the three-tier compute story

Students work across three environments. The course is explicit about *what runs where*
and *why*, and the pre-course tutorials get each student a verified working setup on all
three before week 1.

| Tier | Environment | Used for | Handbook anchor |
|------|-------------|----------|-----------------|
| 1 | **Own computer** | Git/GitHub, shell, editing, small tasks, writing | `Computing-Best-Practices.md`, `Data-Management.md`, `github-tutorial.html`, `bash-tutorial.html` |
| 2 | **Raven** (`raven.fish.washington.edu:8787`) | RStudio Server, interactive R/bioinformatics, moderate jobs | `raven_RStudio-Server.md`, `raven_Conda.md` |
| 3 | **Hyak / Klone** (`klone.hyak.uw.edu`) | SLURM batch jobs, containers, big compute | `klone_*` pages (Logging-In, Running-a-Job, containers, File-Transfers, Conda, quick-start) |

**Design principle:** difficulty ramps with the tier. Tier 3 (Hyak) is where students
struggle, so it gets its own tutorial, the most scaffolding, and an explicit "you will
hit walls — here's how to get unstuck" posture.

---

## 2. Three self-directed pre-course tutorials (HTML)

Standalone, self-paced HTML files (no build step, open in any browser), styled to match
the handbook's existing tutorials (`github-tutorial.html`, `bash-tutorial.html`,
`agentic-ai-bootcamp.html`) — ocean theme, sticky sidebar, a progress bar, and
copy-paste command blocks. Each ends with a **completion checklist** and a **"paste this
into your setup issue"** block so completion is verifiable via GitHub (see §3).

Live at `tutorials/` and linked from a `setup.qmd` landing page.

### Tutorial 1 — `01-your-computer.html` · Local Setup, Shell & Git/GitHub
- **Goal:** a working local environment and fluency in the daily version-control loop.
- **Covers:** installing Git + GitHub Desktop + a terminal; `~/GitHub/` convention and
  the "don't put repos in iCloud/Dropbox" rule; project directory layout
  (`code/ data/ output/` each with a `README.md`); shell navigation (`pwd cd ls`),
  moving/inspecting files; clone → edit → commit → push; what a good commit message is.
- **Competency source:** `Computing-Best-Practices.md`, `Data-Management.md`,
  `github-tutorial.html`, `bash-tutorial.html`.
- **Done when:** student has a personal repo, a correct directory tree, and one pushed commit.

### Tutorial 2 — `02-raven.html` · Raven & Reproducible Analysis
- **Goal:** run an interactive analysis on the lab's RStudio Server and understand
  server vs. laptop.
- **Covers:** logging into Raven RStudio Server; where files live on a shared server;
  cloning a repo on the server; Conda/environments on Raven; running a small R
  bioinformatics task; pushing results back to GitHub; data hygiene (don't commit big
  files; `.gitignore`; hashes/manifests).
- **Competency source:** `raven_RStudio-Server.md`, `raven_Conda.md`, `Data-Management.md`,
  `Computing-Best-Practices.md`.
- **Done when:** student rendered/ran something on Raven and pushed the output.

### Tutorial 3 — `03-hyak.html` · Hyak / Klone HPC (steepest curve — deepest tutorial)
- **Goal:** de-mystify HPC so a first SLURM job isn't terrifying. This is the flagship tutorial.
- **Covers:** what an HPC cluster *is* (login vs. compute nodes, the scheduler, why you
  never compute on the login node); `ssh` into Klone; the `/gscratch/srlab/` storage
  layout; moving data (`scp`/`rsync`, Globus); modules & **Apptainer containers** (the
  lab's standard); anatomy of a SLURM script (the header + the commands script);
  `chmod +x`; `sbatch`, `squeue`, `scancel`, reading `slurm-*.out`; Klone on-demand /
  RStudio-on-Klone as an escape hatch; a **troubleshooting/"getting unstuck"** section
  and an explicit "how to ask for help via a GitHub issue" pointer.
- **Competency source:** `klone_quick-start.md`, `klone_Logging-In.md`,
  `klone_Running-a-Job.md`, `klone_containers.md`,
  `klone_Data-Storage-and-System-Organization.md`, `klone_File-Transfers.md`,
  `klone_Conda.md`, `klone_Node-Types.md`.
- **Done when:** student submitted one trivial `sbatch` job and pasted the job ID +
  output tail into their setup issue.

All three share `tutorials/tutorial.css` and a tiny `tutorials/progress.js`
(localStorage-backed checkbox progress bar).

---

## 3. Making better use of GitHub Issue features

The 2025 course used a Discussion board. 2026 keeps discussions for open-ended Q&A but
moves **structured, trackable work into Issues**, using features the old course didn't:

### 3a. Issue Forms (YAML) in `.github/ISSUE_TEMPLATE/`
Modern web forms (not just markdown) with required fields, dropdowns, and auto-labels:

| Template | Purpose | Auto-labels |
|----------|---------|-------------|
| `00-setup-check.yml` | Pre-course: confirm the 3 tutorials done (paste completion blocks) | `setup`, `week-00` |
| `10-project-proposal.yml` | One issue per student's research project; endpoint, data, platform, eDNA?/RNA-seq?/etc. | `project` |
| `20-weekly-progress.yml` | Weekly self-assessed progress (goals set / met), tied to the schedule | `progress` |
| `30-help-request.yml` | "I'm stuck" — platform dropdown (own/Raven/Hyak), what I tried, error text | `help` |
| `40-blocker-bug.yml` | Reproducible technical blocker with environment + steps | `bug`, `help` |
| `config.yml` | Turns off blank issues; routes open chat to Discussions & Slack | — |

### 3b. Labels (`.github/labels.yml` + a sync action)
`week-00`…`week-10`, `setup`, `project`, `progress`, `help`, `bug`, `edna`, `rna-seq`,
`methylation`, `variants`, `platform:own`, `platform:raven`, `platform:hyak`,
`needs-review`, `resolved`. Applied automatically by the forms above.

### 3c. Project board (GitHub Projects v2)
A course-org project with a per-student view; weekly-progress and project issues appear
as cards moving Todo → In progress → Review → Done. Gives the instructor a
single at-a-glance status across the cohort.

### 3d. Automation (`.github/workflows/`)
- `greetings.yml` — welcome message on a student's first issue (mirrors the handbook repo).
- `auto-label.yml` / label-sync — keep labels consistent from `labels.yml`.
- (Optional) an action that comments the weekly schedule row when a `week-NN` issue opens.

**Assessment tie-in:** "Weekly Research Project Progress" (20% in 2025) is now assessed
directly from the weekly-progress issues and the project board, making the grade legible
and the paper-trail automatic.

---

## 4. More eDNA content

eDNA becomes a first-class topic alongside the existing molecular-ecology content, with
both a **lecture/module** and a supported **project track**.

### 4a. New module: `lectures/edna.qmd` (+ assignment `assignments/edna-metabarcoding.qmd`)
- eDNA/eRNA concepts: what environmental nucleic acids are, sampling, contamination control.
- Metabarcoding workflow: primers/markers (COI, 12S, 16S, 18S), amplicon data.
- From reads to biology: QC → **DADA2** (ASVs) vs. OTU clustering → taxonomic assignment
  (reference databases) → an abundance/occurrence table.
- Ecological readouts: diversity, detection/occupancy, community comparison.
- Reproducibility & caveats specific to eDNA (false positives/negatives, index hopping).
- Competency anchor: `bio_Basics.md`, `bio-Annotation.md`, `Genomic-Resources.md`,
  `Data-Management.md`; run heavy steps on Hyak (ties the eDNA track to Tutorial 3).

### 4b. eDNA project track
A supported alternative to the RNA-seq/DGE default project so a student can take an eDNA
dataset end-to-end (raw amplicons → community table → figure/report), reusing the same
GitHub/issue/compendium machinery.

### 4c. Schedule placement
Slot the eDNA lecture after students have seen raw-read QC, mapping/quantification,
annotation, variants, and methylation, so metabarcoding feels like an applied workflow
rather than a disconnected topic.

---

## 5. Bioinformatics-first weekly arc

The core schedule should read as a coherent progression:

| Week | Focus | Why it belongs here |
|------|-------|---------------------|
| 00 | Bioinformatics habits and data provenance | Establish repository, data, and issue-tracking expectations. |
| 01 | Sequence databases and BLAST | First sequence-to-interpretation workflow. |
| 02 | Raw reads, FASTQ, QC, trimming | All sequencing workflows depend on read quality and provenance. |
| 03 | Mapping, assembly, quantification | Converts reads into intermediate biological data products. |
| 04 | RNA-seq and differential expression | Full expression-analysis example. |
| 05 | Genome annotation and genomic ranges | Connects outputs to genomic context. |
| 06 | Variants and population signals | Adds genotype/population interpretation. |
| 07 | Epigenetics and DNA methylation | Adds regulatory genomics and genome-browser inspection. |
| 08 | eDNA and metabarcoding | Applies read/QC/database logic to ecological community data. |
| 09 | Project synthesis and biological interpretation | Turns outputs into defensible claims. |
| 10 | Final compendium and presentations | Publishes the full reproducible project. |

RStudio, Quarto, GitHub Issues, Hyak, containers, and archiving live in `support.qmd`
and are invoked by assignments as needed.

---

## 6. GitHub-native submission and automatic assessment

Students submit question sets and assignments through GitHub Issue Forms. Each submission
issue points to:

- Student repository URL.
- Exact commit SHA.
- Week number.
- Path to a `submission.yml` manifest.
- Rendered report path.
- Key output paths for assignments.

The automatic assessment workflow checks the evidence packet and comments on the issue
with a report. It can verify required files, manifests, rendered outputs, non-empty
tables/figures, raw-data hygiene, and basic metadata. It does **not** replace human
review of biological reasoning, interpretation, caveats, or writing quality.

This creates a useful distinction:

- **Automatic checks:** structure, completeness, reproducibility evidence.
- **Instructor review:** scientific quality and judgment.

### Topics intentionally not made core weeks

These are valuable, but the 10-week course will become scattered if all are treated as
full weekly units:

- Workflow managers such as Snakemake or Nextflow.
- Functional enrichment and pathway analysis.
- Metagenomics and genome-resolved metagenomics.
- Phylogenetics and tree thinking.
- Protein structure and comparative protein analysis.
- Advanced statistics beyond the models needed for weekly assignments.

These can be used as project-specific extensions, readings, or Thursday working-session
mini-lessons when they directly support student projects.

---

## 7. Repository / site structure

```
course-fish546-2026/
├── _quarto.yml              # website config, publishes to docs/
├── index.qmd                # syllabus (updated platforms, grading, comms → Issues)
├── schedule.qmd             # 10-week schedule incl. eDNA + pre-course setup row
├── setup.qmd                # pre-course landing → the 3 HTML tutorials + setup issue
├── support.qmd              # self-directed RStudio, Quarto, GitHub, Hyak, archiving
├── turn-in.qmd              # GitHub submission contract + automatic assessment
├── edna.qmd                 # eDNA topic hub (links lecture + assignment + resources)
├── about.qmd
├── styles.css
├── tutorials/
│   ├── tutorial.css         # shared ocean theme
│   ├── progress.js          # localStorage progress bar
│   ├── 01-your-computer.html
│   ├── 02-raven.html
│   └── 03-hyak.html
├── lectures/                # 00-before … 10-lastmile (+ edna.qmd)
├── assignments/             # blast, DGE, knit, hyak, … , edna-metabarcoding.qmd
├── questions/               # weekly question sets
├── .github/
│   ├── ISSUE_TEMPLATE/      # the YAML forms + config.yml from §3a
│   ├── labels.yml           # §3b
│   └── workflows/           # greetings, label-sync, submission assessment
├── scripts/                 # submission parsing and assessment helpers
└── docs/                    # rendered site (GitHub Pages)
```

## 8. Build sequence (checklist)

- [x] **Scaffold** Quarto site (`_quarto.yml`, `index`, `schedule`, `about`, `setup`, `styles`).
- [x] **Tutorials** — shared CSS/JS + the three HTML files; verify each opens standalone.
- [x] **Issues** — author the five Issue Forms + `config.yml`; add `labels.yml`; wire workflows.
- [ ] **Project board** — create org Project v2, add the per-student view (manual, one-time).
- [x] **eDNA** — draft `lectures/edna.qmd`, `assignments/edna-metabarcoding.qmd`, `edna.qmd` hub.
- [x] **Content migration** — add first-pass 2026 lectures, assignments, and question sets for every scheduled week.
- [x] **Refocus schedule** — make weekly topics bioinformatics-first and move RStudio/Quarto/archiving to self-directed support.
- [x] **Submission workflow** — add submission issue forms, assessment labels, `turn-in.qmd`, and starter GitHub Actions checker.
- [x] **Schedule** — insert setup (week 0) + eDNA rows; linked weekly materials now exist.
- [ ] **Publish** — `quarto render`, confirm Pages serves `docs/`, set the course GitHub org.
- [ ] **Dry run** — walk all 3 tutorials on a clean machine; open a test setup issue end-to-end.

## 9. Open decisions (instructor input)
- Course GitHub org name for 2026 (e.g. `course-fish546-2026`) + Pages URL.
- Meeting times / room / Zoom for 2026.
- Whether eDNA is an *elective* project track or a shared week-long assignment for all.
- Keep JupyterHub (`jupyter.rttl.uw.edu`) in the mix, or Raven + Hyak only?
- Grading weights if project-board assessment changes the progress component.
```
