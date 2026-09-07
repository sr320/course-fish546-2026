# FISH 546 Course Improvement Roadmap

**Updated:** 2026-09-07. The July 2026 student-experience review led to a course simplification, implemented in September and recorded in [SIMPLIFY-PLAN.md](SIMPLIFY-PLAN.md): one weekly notebook entry, one student repository, two issue forms, staged platforms, and every instructional page on one site. This roadmap records which of the original phases that simplification completed and what remains before and during Autumn 2026.

## Guiding principles

- Make the next student action obvious.
- Scaffold complex work without hiding authentic bioinformatics practice.
- Align learning outcomes, practice, assignments, and grading criteria.
- Provide feedback before high-stakes submission.
- Design for students with different computing backgrounds and access constraints.
- Treat accessibility, privacy, and reproducibility as core course requirements.
- Prefer removing a system to documenting it.

## Phase 0 — Establish the baseline

**Status:** Complete (2026-07-31 baseline; inventory refreshed 2026-09-07).

- [`maintenance/RESOURCE_INVENTORY.md`](maintenance/RESOURCE_INVENTORY.md) is the canonical destination map.
- [`maintenance/BASELINE_STUDENT_EXPERIENCE.md`](maintenance/BASELINE_STUDENT_EXPERIENCE.md) records the pre-simplification state for comparison.
- [`scripts/audit_course_site.py`](scripts/audit_course_site.py) runs on every push via [`.github/workflows/site-audit.yml`](.github/workflows/site-audit.yml) and covers `assignments/` and tutorial back-links.

**Remaining:** administer [`maintenance/STUDENT_BASELINE_SURVEY.md`](maintenance/STUDENT_BASELINE_SURVEY.md) in Week 0 and append results to the baseline. Update the survey's workflow questions to the notebook-entry vocabulary first.

## Phase 1 — Make the course immediately usable

**Status:** Complete.

Done by the simplification:

- Exact Autumn 2026 dates, meeting times, room, and due dates on every schedule card; current week outlined automatically.
- "Where things live" table and the five-step weekly loop on [How We Work](https://sr320.github.io/course-fish546-2026/how-we-work.html); one repository per student replaces the organization/course/assignments/student distinction.
- Direct links to the two issue forms; the Setup Check form and its broken URL removed.
- Empty heading and inconsistent repository links removed from the syllabus.

**Remaining:** add instructor contact, office hours, prerequisites, expected weekly workload, and policy text (accommodations, academic integrity, collaboration, generative AI, privacy and data ethics, religious accommodation) to `index.qmd`. These are syllabus content, not structure.

## Phase 2 — Reduce onboarding barriers

**Status:** Mostly complete.

Done:

- Setup staged: Tutorial 1 before Oct 1, Raven in the Week 1 Thursday session, Hyak in Week 3.
- Tutorial 1 creates the repository from the template; each tutorial links back to the site and hands off to the next with its week.
- Discouraging all-or-nothing language removed; Help Request is the documented route when access is pending.
- Tutorials collapse to a compact menu on narrow screens and follow the reader's dark or light theme.

**Remaining:**

- Access preflight checklist (organization membership, Raven credentials, VPN, Hyak allocation, Duo) on `setup.qmd`, and an explicit "credit is not lost while access is pending" statement.
- Make the Raven exercise a rendered `.qmd` rather than console commands, with a seed and session information, so it demonstrates the notebook-entry practice.
- Troubleshooting index by symptom and platform (the Hyak tutorial has one; extend to Git, paths, Conda, and Quarto rendering) in the How We Work skills reference.

## Phase 3 — Build a consistent weekly learning experience

**Status:** Structure complete; content depth remains.

Done:

- Every week has a topic page and an analysis page, grouped in the sidebar with previous/next navigation, a due-date callout, reflection questions, "This week in your project," and linked references.
- Weeks 5 to 8 give a concrete "in your project" version for each project track plus a canned fallback, so every student has an explicit project connection.

**Remaining, in rollout order:**

1. Place the provided datasets for Weeks 2 to 8 and record their paths on the analysis pages and in the inventory (decision D5).
2. Add a worked example with real output to each topic page, starting with Week 02 (FASTQ/QC) because it supports every workflow.
3. Add a short "common mistakes" list per week.
4. Publish each week's material at least two weeks before students reach it.

## Phase 4 — Align assessment and feedback

**Status:** Complete for criteria; exemplar remains.

Done:

- One weekly entry rubric (100 points) covers the 60% of the grade that previously had no published criteria; compendium and presentation rubrics retained.
- The notebook template carries the pre-push checklist; the analysis pages state what goes in the entry.
- Automated structural checks and manifests retired; feedback is one instructor comment per student per week on the Project Proposal issue, which is stated on the site.
- Best 8 of 9 entries count, which replaces an exceptional-circumstances process for a single missed week.

**Remaining:**

- One annotated exemplar entry (a filled `weekNN.qmd` with outputs) linked from How We Work, ideally the instructor's own Week 02.
- State the feedback turnaround ("within a few days" is implied; write it down).
- Extension process for multi-week disruptions beyond the dropped entry.

## Phase 5 — Improve accessibility and interface usability

**Status:** Partially complete.

Done: mobile tutorial menu, heading overflow fix, dark-mode tutorials, schedule tables that scroll rather than overflow.

**Remaining:**

- Visible focus styles and a skip-to-content link on the tutorials (Quarto pages already have Bootstrap defaults).
- `role="progressbar"` with min/max/now on the tutorial progress bar; a reset button for checklist state.
- `prefers-reduced-motion` for smooth scrolling and the progress animation.
- Contrast check of the orange syllabus callout and the muted past-week cards in both themes.
- Print styles for the syllabus, schedule, and How We Work.
- One keyboard-only pass and one automated checker run on a topic page, an analysis page, and a tutorial.

## Phase 6 — Strengthen navigation and course continuity

**Status:** Complete for navigation; two content items remain.

Done: previous/next and sidebar on all weekly pages, current-week marker, project-track pathways in Weeks 5 to 8, final-report skeleton required in Week 7, `docs/` folder in the template for the report.

**Remaining:**

- Glossary of recurring terms and file formats (one page, linked from How We Work).
- A one-paragraph "project arc" on the syllabus mapping Week 0 proposal → Week 3 endpoint sentence → Week 5 update → Week 7 skeleton → Week 8 mock figure → Week 10 tag.

## Phase 7 — Evaluate and maintain

**Status:** Not started (the quarter has not begun).

- Week 0 baseline survey and a Week 1 pulse; mid-quarter and final surveys.
- Review Help Requests for recurring instructional gaps; convert into edits to the analysis pages or skills reference.
- Track which fallback exercises are used in Weeks 5 to 8; heavy fallback use in a week signals a track without a good project mapping.
- End-of-course maintenance review; record remaining work as repository issues.
- Pre-course release checklist: render, `--write-manifest`, `--external` link review, confirm the Pages deployment, test "Use this template" as a student, open a test issue with each form.

## Sequence

### Before Thu Oct 1

- Phase 1 syllabus content (contact, workload, policies).
- Phase 3 item 1: provided datasets for at least Weeks 2 to 4.
- Phase 4 exemplar entry.
- Phase 2 access preflight.
- Pre-course release checklist.

### During the quarter

- Provided datasets for Weeks 5 to 8 by Week 3.
- Worked examples added at least two weeks ahead.
- Week 1 pulse and mid-quarter survey.
- Phase 5 accessibility items as time allows; none block students.

### After the quarter

- Final survey and maintenance review.
- Revise analysis pages from Help Request patterns and fallback usage.
- Decide whether Week 8 (single session, Thanksgiving) should swap with a lighter topic.

## Measures of success

- Every student has a repository from the template and a Project Proposal issue by Fri Oct 2.
- No Help Request in Weeks 0 to 2 is about where to put work or how to submit.
- Weekly entries arrive by Friday from most students without reminders; the dropped-entry rule absorbs the rest.
- In Weeks 5 to 8, most students use the "in your project" version rather than the canned fallback.
- Weekly entries show interpretation, caveats, and evidence links improving across the quarter under the same rubric.
- The final compendium can be rerun from the repository by the instructor for most students.
- Surveys report that workload, expectations, and help routes are clear.
