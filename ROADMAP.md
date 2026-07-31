# FISH 546 Course Improvement Roadmap

This roadmap turns the student-experience review into a phased improvement plan for the 2026 course website and learning materials. The phases are ordered by student impact and dependency: first establish a reliable course contract and navigation system, then improve onboarding, weekly learning, assessment, accessibility, and long-term maintenance.

## Guiding principles

- Make the next student action obvious.
- Scaffold complex work without hiding authentic bioinformatics practice.
- Align learning outcomes, practice, assignments, and grading criteria.
- Provide feedback before high-stakes submission.
- Design for students with different computing backgrounds and access constraints.
- Treat accessibility, privacy, and reproducibility as core course requirements.

## Phase 0 — Establish the baseline

**Status:** Implemented 2026-07-31. The repository baseline and audit infrastructure are complete; live student feedback will be appended during Week 0/1 using the prepared survey.

**Deliverables:**

- [`maintenance/RESOURCE_INVENTORY.md`](maintenance/RESOURCE_INVENTORY.md)
- [`maintenance/BASELINE_STUDENT_EXPERIENCE.md`](maintenance/BASELINE_STUDENT_EXPERIENCE.md)
- [`maintenance/STUDENT_BASELINE_SURVEY.md`](maintenance/STUDENT_BASELINE_SURVEY.md)
- [`maintenance/EXTERNAL_LINK_REVIEW.md`](maintenance/EXTERNAL_LINK_REVIEW.md)
- [`scripts/audit_course_site.py`](scripts/audit_course_site.py)
- [`.github/workflows/site-audit.yml`](.github/workflows/site-audit.yml)

**Goal:** Create a reliable starting point and prevent improvements from introducing regressions.

### Work

- Inventory every student-facing page, tutorial, repository, issue form, assignment, and external support channel.
- Identify the canonical URL for the course repository, assignments repository, organization, Discussions, issue forms, Slack, Raven, and Hyak.
- Record which materials are authoritative when instructions differ.
- Add a repeatable check for missing internal links and unrendered Quarto changes.
- Review external links before each course offering.
- Collect baseline student feedback on setup difficulty, navigation, weekly workload, and assignment clarity.

### Completion criteria

- Every student-facing destination has one documented canonical URL.
- The generated site has no missing internal targets.
- A short baseline findings summary exists for comparison after the course changes.

## Phase 1 — Make the course immediately usable

**Goal:** Ensure students can answer “What do I do, when is it due, and where do I go?” without searching across multiple systems.

### Work

- Replace schedule placeholders with exact 2026 dates, class meetings, due dates, times, and time zone.
- Add estimated preparation and assignment time for each week.
- Create a prominent **Start Here** section or page with direct links for:
  - preparing for class;
  - finding the current week's materials;
  - submitting question sets and assignments;
  - reporting project progress;
  - requesting help;
  - joining course discussion.
- Clearly distinguish the course organization, course repository, assignments repository, and each student's project repository.
- Link directly to the relevant GitHub issue forms instead of describing them only by name.
- Add instructor contact information, office hours, meeting time and location, prerequisites, expected workload, and required accounts.
- Add accessibility/accommodations, academic integrity, collaboration, generative-AI, privacy, data ethics, and religious-accommodation guidance.
- Remove the empty heading at the end of `index.qmd` and reconcile inconsistent repository links.

### Completion criteria

- A new student can locate every required Week 1 action from the homepage in two clicks or fewer.
- All assessed work has an exact destination and deadline.
- The syllabus contains the essential course logistics and participation policies.
- No placeholder dates or ambiguous repository references remain.

## Phase 2 — Reduce onboarding barriers

**Goal:** Prepare students for the three computing platforms without making access delays or prior experience an early failure point.

### Work

- Divide setup into:
  - essential tasks required before the first class;
  - tasks that may be completed with support during Week 1;
  - optional extension material.
- Add a short access preflight covering GitHub organization membership, Raven credentials, UW VPN, Hyak allocation, Duo, and required software.
- Provide an explicit fallback when Raven or Hyak access is not ready.
- Schedule or document a live setup/help session.
- Add troubleshooting decision trees for authentication, Git, paths, permissions, Conda, and SLURM.
- Replace discouraging or all-or-nothing language with clear urgency plus a route to help.
- Make the Raven exercise reproducible:
  - save analysis code in an `.R` or `.qmd` file;
  - use project-relative paths;
  - set the random seed;
  - record software/session information;
  - commit both source and output.
- Replace outdated `.Rmd` examples with `.qmd` where Quarto is the course standard.
- Add copy controls for commands and completion blocks, plus a way to reset or export tutorial checklist progress.

### Completion criteria

- Students blocked by account provisioning have a documented alternative and do not lose credit solely because access is pending.
- Each tutorial produces verifiable evidence of a completed workflow.
- The Raven tutorial demonstrates the same reproducibility practices expected in graded work.
- Setup instructions use consistent file formats, vocabulary, and repository structure.

## Phase 3 — Build a consistent weekly learning experience

**Goal:** Turn each weekly topic page from a concise outline into a complete learning module with practice and feedback.

### Standard weekly module

Each week should include:

1. **Orientation** — why the topic matters and how it connects to prior and future weeks.
2. **Preparation** — prerequisite knowledge, required reading, files, and estimated time.
3. **Learning outcomes** — observable actions students should be able to perform.
4. **Worked example** — an environmental or fisheries bioinformatics example using realistic data or output.
5. **Guided practice** — a small interpretation or command task with prompts.
6. **Feedback** — an explanation, model answer, or diagnostic checklist.
7. **Common mistakes** — conceptual and computational failure modes.
8. **Project connection** — how students apply the topic to different project tracks.
9. **Knowledge check** — two to four retrieval or interpretation questions.
10. **Definition of done** — evidence students should have by the end of the week.
11. **References** — direct, descriptive links to required and optional resources.

### Rollout order

1. Pilot the template with Week 02 (FASTQ/QC), because it supports nearly every sequencing workflow.
2. Apply lessons from the pilot to Weeks 03–07.
3. Expand Weeks 01, 08, 09, and 10.
4. Review the complete sequence for repetition, gaps, and workload balance.

### Completion criteria

- Every stated learning outcome is supported by an example, practice opportunity, or assignment task.
- Every weekly module contains formative feedback before submission.
- Weekly project checkpoints identify concrete evidence rather than broad activity.
- Required references are linked and separated from optional enrichment.

## Phase 4 — Align assessment and feedback

**Goal:** Make success criteria visible before students begin and ensure automated checks support learning rather than merely enforce file structure.

### Work

- Publish concise common rubrics for weekly question sets and class assignments, which together account for 60% of the course grade.
- Map weekly learning outcomes to assignment tasks and rubric criteria.
- Add an annotated example submission showing source, rendered report, outputs, manifest, interpretation, and caveats.
- Add a “ready to submit” checklist to each assignment.
- Clearly separate:
  - automatic structural checks;
  - scientific criteria requiring instructor judgment;
  - opportunities to revise after feedback.
- Rewrite automatic check messages so each failure explains why it matters and how to fix it.
- Add a transparent extension and exceptional-circumstances process alongside the late-work policy.
- Calibrate the project rubric with sample evidence representing Excellent, Complete, Developing, and Incomplete work.
- Define the timing and expected form of feedback on pull requests and progress issues.

### Completion criteria

- All graded components have student-facing criteria and examples.
- Students can self-check a submission before opening a pull request.
- Automated feedback includes a specific corrective action for every reported problem.
- Grading criteria use the same vocabulary as weekly outcomes and instructions.

## Phase 5 — Improve accessibility and interface usability

**Goal:** Make the site and tutorials usable with keyboard navigation, assistive technology, reduced motion, small screens, and printing.

### Work

- Add visible keyboard focus styles and a skip-to-content link.
- Give tutorial progress indicators semantic `progressbar` roles, accessible names, and current/minimum/maximum values.
- Announce checklist progress changes appropriately without creating excessive screen-reader output.
- Respect `prefers-reduced-motion` for smooth scrolling and animated progress.
- Replace the full mobile tutorial sidebar with a compact, collapsible section menu.
- Check light- and dark-theme color contrast, including the orange syllabus callout.
- Verify heading hierarchy, landmarks, table headers, link names, and image alternative text.
- Ensure commands, tables, and long paths remain readable at narrow widths and high zoom.
- Add print styles for the syllabus, schedule, rubric, and tutorials.
- Test representative pages with keyboard-only navigation and at least one automated accessibility checker.

### Completion criteria

- All interactive elements are reachable and understandable from the keyboard.
- Progress state is available to assistive technology.
- The site remains usable at mobile width and 200% zoom.
- No known high-severity accessibility violations remain on representative pages.

## Phase 6 — Strengthen navigation and course continuity

**Goal:** Help students maintain context across weeks and see how individual tasks contribute to the final compendium.

### Work

- Add previous week, next week, and return-to-schedule navigation to each module.
- Add a visible current-week marker to the schedule during the course.
- Show the project arc from proposal through final compendium, including milestone evidence.
- Provide project-track pathways for RNA-seq, eDNA, methylation, variants, and annotation/sequence discovery.
- Add a glossary for recurring terms, platforms, file formats, and course workflow language.
- Add a single troubleshooting index organized by symptom and platform.
- Provide a final-compendium template early enough for students to build into it throughout the quarter.

### Completion criteria

- Students can move between adjacent weeks and the schedule without using browser navigation.
- Every weekly checkpoint visibly contributes to a final-compendium component.
- Students outside the featured weekly data type have an explicit project connection.

## Phase 7 — Evaluate and maintain

**Goal:** Treat the course materials as an evidence-informed resource that improves each offering.

### Work

- Add a short Week 1 pulse survey about setup, confidence, and navigation.
- Add a mid-quarter survey about workload, scaffolding, feedback, and project progress.
- Add a final survey that asks which examples, tutorials, and feedback mechanisms most supported learning.
- Review help requests and automated-check failures for recurring instructional gaps.
- Track completion and resubmission patterns without using them as the sole measure of learning.
- Hold an end-of-course maintenance review and convert findings into repository issues.
- Assign an owner and review date to time-sensitive pages and external links.
- Document the pre-course release checklist for future instructors or teaching assistants.

### Completion criteria

- Student feedback is collected at least three times and results in documented decisions.
- Recurring technical failures produce improvements to instructions or tooling.
- A dated maintenance checklist is completed before each offering.

## Suggested implementation sequence

### Before publishing the next course site

- Complete Phases 0 and 1.
- Complete the essential portions of Phase 2.
- Fix the highest-impact accessibility issues from Phase 5.

### Before Week 1

- Finish Phase 2.
- Publish the common assessment criteria and exemplar from Phase 4.
- Complete the Week 02 module pilot from Phase 3.

### During the quarter

- Expand weekly modules at least two weeks before students use them.
- Add navigation and project-track improvements from Phase 6.
- Collect the Week 1 and mid-quarter feedback from Phase 7.

### After the quarter

- Complete the final evaluation and maintenance review.
- Revise modules based on student work, help requests, and feedback.
- Record remaining work as scoped repository issues for the next offering.

## Measures of success

Use multiple indicators rather than a single metric:

- Fewer students are blocked by account or platform access in Week 1.
- Students can correctly identify where and how to submit each type of work.
- Fewer pull requests fail for preventable structural or navigation-related reasons.
- Weekly work demonstrates stronger interpretation, caveats, and evidence trails.
- Students report that workload, expectations, and help routes are clear.
- Project checkpoints show steady progress toward the final compendium.
- Accessibility checks and student reports reveal fewer barriers.
