# FISH 546 Resource Inventory

**Inventory date:** 2026-07-31

**Review owner:** Course instructor

**Next required review:** Before the 2026 course site is published

This inventory identifies every student-facing course resource and records which location is authoritative. Generated files under `docs/` are published copies; their corresponding source files are authoritative.

## Canonical destinations

| Destination | Canonical URL or address | Purpose | Authority note |
|---|---|---|---|
| Published course site | <https://sr320.github.io/course-fish546-2026/> | Student-facing syllabus and course materials | Expected Pages URL based on the repository owner and prior course sites; confirm after the first 2026 deployment. The different setup-page URL currently embedded in the Setup Check form returned `404` on 2026-07-31. |
| Course source and central workflow repository | <https://github.com/sr320/course-fish546-2026> | Website source, central issue forms, labels, and progress automation | The configured Git remote; authoritative for course infrastructure. |
| Course GitHub organization | <https://github.com/course-fish546-2026> | Home for student project repositories | This is an organization, not the course source repository. |
| Assignments repository | <https://github.com/sr320/fish546-2026-assignments> | Question sets, assignment prompts, templates, and pull-request submissions | Authoritative for assessed weekly question sets and assignments. |
| Course Discussions | <https://github.com/orgs/course-fish546-2026/discussions> | Open-ended questions, ideas, and peer discussion | Use for conversation that does not require a structured issue form. |
| Course Slack | <https://genefish.slack.com> | Quick, informal course communication | Access requires membership in the workspace. |
| Roberts Lab Handbook | <https://robertslab.github.io/resources/> | Computing, data-management, Raven, and Hyak reference standard | Authoritative for platform operations unless a course page explicitly overrides it. |
| Raven | <http://raven.fish.washington.edu:8787> | RStudio Server | May require UW network or VPN access. |
| Hyak OnDemand | <https://ondemand.hyak.uw.edu> | Browser access to Hyak services | Requires UW and allocation credentials. |
| Klone SSH | `ssh <UWNetID>@klone.hyak.uw.edu` | Command-line Hyak access | Requires UW, Duo, and allocation credentials. |

### Repository roles

- The **central workflow repository** hosts the issue forms and the workflow that assesses weekly progress.
- A **student project repository** under the course organization contains that student's project code, documentation, and evidence.
- The **assignments repository** contains prompts and receives question-set and assignment pull requests.
- Central issue-form submissions should link to evidence in the student's project repository; the evidence itself does not belong in the central repository.

## Central issue forms

| Form | Direct URL | Evidence expected |
|---|---|---|
| Setup Check | <https://github.com/sr320/course-fish546-2026/issues/new?template=00-setup-check.yml> | Tutorial completion blocks and student repository links |
| Project Proposal | <https://github.com/sr320/course-fish546-2026/issues/new?template=10-project-proposal.yml> | Question, data, project track, platform, endpoint, and risks |
| Weekly Research Progress | <https://github.com/sr320/course-fish546-2026/issues/new?template=20-weekly-progress.yml> | Project issue, commit/compare URL, evidence, goals, and blockers |
| Help Request | <https://github.com/sr320/course-fish546-2026/issues/new?template=30-help-request.yml> | Goal, attempted fixes, exact error, and platform |
| Technical Blocker/Bug | <https://github.com/sr320/course-fish546-2026/issues/new?template=40-blocker-bug.yml> | Reproduction steps, expected/actual result, environment, and code/log link |

The forms currently exist only in the central workflow repository. References to opening one “in your course repository” are ambiguous and should be corrected during Phase 1.

## Student-facing site pages

| Source | Published path | Purpose | Authority |
|---|---|---|---|
| `index.qmd` | `/index.html` | Syllabus, course format, grading, and weekly arc | Authoritative course overview |
| `schedule.qmd` | `/schedule.html` | Weekly topics, questions, assignments, and project checkpoints | Authoritative weekly sequence; exact dates are still pending Phase 1 |
| `setup.qmd` | `/setup.html` | Landing page for the three setup tutorials | Authoritative setup sequence |
| `support.qmd` | `/support.html` | Self-directed tool and platform skills | Course summary; handbook remains authoritative for platform details |
| `turn-in.qmd` | `/turn-in.html` | Pull-request submission contract and progress workflow | Authoritative course submission explanation |
| `rubric.qmd` | `/rubric.html` | Project progress, presentation, and compendium rubric | Authoritative project-facing rubric |
| `edna.qmd` | `/edna.html` | eDNA topic hub | Navigation hub; lecture page contains instructional content |
| `about.qmd` | `/about.html` | Instructor/course and site information | Authoritative site metadata |

## Weekly modules

| Week | Source | Topic |
|---:|---|---|
| 00 | `lectures/00-before.qmd` | Bioinformatics habits and data provenance |
| 01 | `lectures/01-start-up.qmd` | Sequence databases and BLAST |
| 02 | `lectures/02-raw-reads-qc.qmd` | Raw reads, FASTQ, QC, and trimming |
| 03 | `lectures/03-mapping-quantification.qmd` | Mapping, assembly, and quantification |
| 04 | `lectures/04-rna-seq-dge.qmd` | RNA-seq and differential expression |
| 05 | `lectures/05-annotation-ranges.qmd` | Genome annotation and genomic ranges |
| 06 | `lectures/06-variants.qmd` | Variants and population signals |
| 07 | `lectures/07-methylation.qmd` | Epigenetics and DNA methylation |
| 08 | `lectures/edna.qmd` | eDNA and metabarcoding |
| 09 | `lectures/09-synthesis.qmd` | Project synthesis and biological interpretation |
| 10 | `lectures/10-lastmile.qmd` | Presentations and final compendium |

## Setup tutorials

| Order | Source | Purpose | Completion evidence |
|---:|---|---|---|
| 1 | `tutorials/01-your-computer.html` | Local shell, Git/GitHub, and project structure | Repository and first commit |
| 2 | `tutorials/02-raven.html` | Raven/RStudio workflow and server data hygiene | Output committed from Raven |
| 3 | `tutorials/03-hyak.html` | Hyak/Klone, storage, containers, and SLURM | Job ID and output tail |

`tutorials/tutorial.css` and `tutorials/progress.js` are shared authoritative assets. Copies under `docs/tutorials/` are generated/published resources and must match exactly.

## Weekly assessed materials

All paths below are relative to <https://github.com/sr320/fish546-2026-assignments>.

| Week | Question set | Assignment |
|---:|---|---|
| 00 | None | `assignments/00-bash/` |
| 01 | `questions/week01.md` | `assignments/01-blast/` |
| 02 | `questions/week02.md` | `assignments/02-fastq-qc/` |
| 03 | `questions/week03.md` | `assignments/03-mapping-quantification/` |
| 04 | `questions/week04.md` | `assignments/04-dge/` |
| 05 | `questions/week05.md` | `assignments/05-annotation-ranges/` |
| 06 | `questions/week06.md` | `assignments/06-variants/` |
| 07 | `questions/week07.md` | `assignments/07-methylation/` |
| 08 | `questions/week08.md` | `assignments/08-edna-metabarcoding/` |
| 09 | `questions/week09.md` | `assignments/09-synthesis/` |
| 10 | `questions/week10.md` | `assignments/10-compendium/` |

The assignments repository is authoritative if its prompt conflicts with a summary on the course schedule. Conflicts should still be treated as defects and reconciled.

## Automation and derived resources

| Resource | Role |
|---|---|
| `.github/workflows/progress-assessment.yml` | Assesses central weekly-progress issues and applies triage labels |
| `.github/workflows/label-sync.yml` | Synchronizes course labels |
| `.github/workflows/greetings.yml` | Greets a student's first central issue |
| `.github/workflows/site-audit.yml` | Runs the offline course-site audit on pushes and pull requests |
| `scripts/parse_progress_issue.py` | Extracts structured issue-form content |
| `scripts/assess_progress_issue.py` | Produces progress reports and status labels |
| `scripts/audit_course_site.py` | Checks links, generated tutorial copies, and render-source freshness |
| `docs/` | Published output; never the primary editing location |

## Authority rules

1. Edit `.qmd` sources and `tutorials/` assets, not their copies under `docs/`.
2. The assignments repository controls assignment and question-set requirements.
3. `rubric.qmd` controls project grading expectations.
4. The Roberts Lab Handbook controls platform procedures unless the course explicitly documents a temporary exception.
5. The exact submitted commit and manifest control what is evaluated for a weekly submission.
6. When two student-facing sources conflict, record and fix the conflict; do not rely on students to infer precedence.
