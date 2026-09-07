# FISH 546 Resource Inventory

**Inventory date:** 2026-09-07 (supersedes the 2026-07-31 inventory)

**Review owner:** Course instructor

**Next required review:** Week 0 (Thu Oct 1, 2026), then before the next offering

This inventory identifies every student-facing course resource and records which location is authoritative. Generated files under `docs/` are published copies; their corresponding source files are authoritative. The course design these resources implement is recorded in [`SIMPLIFY-PLAN.md`](../SIMPLIFY-PLAN.md).

## Canonical destinations

| Destination | Canonical URL or address | Purpose | Authority note |
|---|---|---|---|
| Published course site | <https://sr320.github.io/course-fish546-2026/> | Syllabus, schedule, weekly topics and analyses, How We Work | Confirmed live 2026-09-07. The only student-facing instructional source. |
| Course repository | <https://github.com/sr320/course-fish546-2026> | Site source, the two issue forms, labels, `roster.md` | The configured Git remote. Students open issues here and make exactly one pull request here (Week 1 roster). |
| Course GitHub organization | <https://github.com/course-fish546-2026> | Home for student project repositories | Created 2026-09-07. An organization, not a repository. |
| Project template | <https://github.com/course-fish546-2026/project-template> | Starting point for every student repository ("Use this template") | Authoritative repository layout and notebook-entry template. Local clone at `~/Documents/GitHub/project-template`. |
| Student project repository | `https://github.com/course-fish546-2026/<student-repo>` | All of a student's work: code, outputs, weekly notebook entries, final compendium | The submission. The commit link posted on the Project Proposal issue identifies what is assessed. |
| Course Slack | <https://genefish.slack.com> | Quick, informal communication and announcements | Access requires workspace membership. Anything needing a record goes in an issue instead. |
| Roberts Lab Handbook | <https://robertslab.github.io/resources/> | Computing, data-management, Raven, and Hyak reference standard | Authoritative for platform operations unless a course page explicitly overrides it. |
| Raven | <http://raven.fish.washington.edu:8787> | RStudio Server; home for most weekly work from Week 1 | May require UW network or VPN access. |
| Hyak OnDemand | <https://ondemand.hyak.uw.edu> | Browser access to Hyak services | Requires UW and allocation credentials. Introduced Week 3. |
| Klone SSH | `ssh <UWNetID>@klone.hyak.uw.edu` | Command-line Hyak access | Requires UW, Duo, and `srlab` allocation. |

Retired in September 2026 and no longer referenced anywhere student-facing: the separate assignments repository, GitHub Discussions, the Setup Check and Weekly Progress issue forms, the Blocker/Bug form, and the progress-assessment workflow.

### Repository roles

- The **course repository** publishes the site and hosts the Project Proposal and Help Request forms. Students touch it twice: the Week 1 roster pull request, and issues.
- Each **student project repository** is created from the template into the organization and holds everything the student produces. Weekly entries live in `notebooks/weekNN.qmd`; outputs in `output/weekNN/`; the final report in `docs/`.
- The **Project Proposal issue** is the per-student home base: the weekly commit link, tutorial completion blocks, and instructor feedback all live in its comment thread.

## Issue forms

| Form | Direct URL | Evidence expected |
|---|---|---|
| Project Proposal | <https://github.com/sr320/course-fish546-2026/issues/new?template=10-project-proposal.yml> | Repository link, question, track, data, platform, endpoint, risks. One per student; weekly commit links and tutorial completion blocks are posted as comments. |
| Help Request | <https://github.com/sr320/course-fish546-2026/issues/new?template=30-help-request.yml> | Platform, goal, what was tried, exact error, optional reproduction steps and link |

The issue chooser also links Slack, the Handbook, and the course site. Blank issues are disabled.

## Student-facing site pages

| Source | Published path | Purpose | Authority |
|---|---|---|---|
| `index.qmd` | `/index.html` | Syllabus: meeting times, format, platforms, grading, weekly arc | Authoritative course overview |
| `schedule.qmd` | `/schedule.html` | Dated weekly cards with Topic, Analysis, and Project lines; current week outlined by script | Authoritative dates and weekly sequence |
| `setup.qmd` | `/setup.html` | The three platform tutorials and when each is required | Authoritative setup sequence |
| `how-we-work.qmd` | `/how-we-work.html` | Weekly loop, where things live, notebook template and checklist, all three rubrics, skills reference | Authoritative submission contract and grading criteria |
| `about.qmd` | `/about.html` | Instructor and site information (footer link) | Site metadata |
| (aliases) | `/support.html`, `/turn-in.html`, `/rubric.html` | Redirect to `/how-we-work.html` | Kept so old bookmarks resolve |

## Weekly modules

Each week has a topic page (`lectures/`) and an analysis page (`assignments/`), grouped in the site sidebar with previous/next navigation. Reflection questions live on the topic page; the analysis page states what goes in section 1 of the notebook entry.

| Week | Topic source | Analysis source | Mode |
|---:|---|---|---|
| 00 | `lectures/00-before.qmd` | `assignments/00-bash.qmd` | Setup session Thu Oct 1; entry ungraded |
| 01 | `lectures/01-start-up.qmd` | `assignments/01-blast.qmd` | Shared exercise; roster pull request |
| 02 | `lectures/02-raw-reads-qc.qmd` | `assignments/02-fastq-qc.qmd` | Shared exercise |
| 03 | `lectures/03-mapping-quantification.qmd` | `assignments/03-mapping-quantification.qmd` | Shared exercise; Hyak tutorial assigned |
| 04 | `lectures/04-rna-seq-dge.qmd` | `assignments/04-dge.qmd` | Shared exercise |
| 05 | `lectures/05-annotation-ranges.qmd` | `assignments/05-annotation-ranges.qmd` | Own project, canned fallback; mid-quarter update |
| 06 | `lectures/06-variants.qmd` | `assignments/06-variants.qmd` | Own project, canned fallback |
| 07 | `lectures/07-methylation.qmd` | `assignments/07-methylation.qmd` | Own project, canned fallback |
| 08 | `lectures/08-edna.qmd` | `assignments/08-edna.qmd` | Own project, canned fallback; no Thursday (Thanksgiving) |
| 09 | `lectures/09-synthesis.qmd` | `assignments/09-synthesis.qmd` | Own project |
| 10 | `lectures/10-lastmile.qmd` | `assignments/10-compendium.qmd` | Compendium tag `v1.0`; final talks |

`assignments/provided-query.fasta` is the Week 01 practice query and is copied to `docs/assignments/`.

**Provided datasets** for Weeks 2 to 8 (FASTQ, reference, count matrix, BED/GFF, VCF, methylation table, amplicon run) are not yet placed. Each analysis page says "paths on Slack." Decision D5 in `SIMPLIFY-PLAN.md`: put them under a shared Raven path and `/gscratch/srlab/fish546/` on Klone and record the paths here once they exist.

## Setup tutorials

| Order | Source | When required | Completion evidence |
|---:|---|---|---|
| 1 | `tutorials/01-your-computer.html` | Before Thu Oct 1 | Repository created from the template; README personalized; first push |
| 2 | `tutorials/02-raven.html` | Week 1 Thursday session (Oct 8) | Output committed from Raven |
| 3 | `tutorials/03-hyak.html` | Week 3 (assigned Oct 20) | Job ID and output tail |

Completion blocks are posted as comments on the student's Project Proposal issue. `tutorials/tutorial.css` and `tutorials/progress.js` are shared authoritative assets; copies under `docs/tutorials/` must match exactly (the audit checks this). Tutorial links to site pages (`../setup.html`) resolve against the published copy.

## Automation and derived resources

| Resource | Role |
|---|---|
| `.github/workflows/site-audit.yml` | Runs `scripts/audit_course_site.py` on pushes and pull requests |
| `.github/workflows/label-sync.yml` | Synchronizes labels from `.github/labels.yml` (does not delete) |
| `.github/workflows/greetings.yml` | Greets a student's first issue with the proposal-issue loop |
| `.github/PULL_REQUEST_TEMPLATE.md` | Checklist for the Week 1 roster pull request |
| `scripts/audit_course_site.py` | Checks source links, generated links and anchors, tutorial copies, and the render-source manifest |
| `maintenance/render-source-manifest.json` | Hashes of every render source at the last accepted render; rewrite with `--write-manifest` after `quarto render` |
| `docs/` | Published output; never the primary editing location |

There is no automated assessment. Weekly feedback is one instructor comment per student per week on the Project Proposal issue.

## Authority rules

1. Edit `.qmd` sources and `tutorials/` assets, not their copies under `docs/`. Re-render, then rewrite the manifest.
2. `how-we-work.qmd` controls the submission contract and all grading criteria.
3. Each week's `assignments/NN-*.qmd` page controls that week's analysis requirements; the schedule card summarizes it.
4. `project-template` controls the repository layout and the notebook entry structure.
5. The Roberts Lab Handbook controls platform procedures unless the course explicitly documents a temporary exception.
6. The commit link posted on the Project Proposal issue identifies the version of a weekly entry that is assessed.
7. When two student-facing sources conflict, record and fix the conflict; do not rely on students to infer precedence.
