# Student-Experience Baseline

**Assessment date:** 2026-07-31

**Scope:** Course website source, generated site, setup tutorials, central issue forms, and workflow documentation

**Method:** Expert walkthrough, structural inventory, local-link audit, content comparison, and workflow trace

This baseline records the state before the improvement roadmap is implemented. It is not a substitute for student feedback; the companion survey should be administered before or during Week 1 and its results appended here.

## Resource counts

| Resource | Count |
|---|---:|
| Top-level student-facing Quarto pages | 8 |
| Weekly lecture/module pages | 11 |
| Standalone setup tutorials | 3 |
| Weekly assignment destinations | 11 |
| Weekly question-set destinations | 10 |
| Structured central issue forms | 5 |
| Main computing environments | 3 |

## Initial audit results

- Generated-site local targets checked during the review: no missing relative targets found.
- The standalone tutorial sources and published copies are expected to remain byte-for-byte identical and are now checked automatically.
- The published-site render is represented by a source-hash manifest because Quarto is not installed in the current workspace. Future editors must update the manifest only after a successful render.
- Canonical destination ambiguity exists among the instructor repository, course organization, and Pages hostname; the resource inventory now distinguishes their roles.
- A networked external review found a broken setup-page URL plus anonymous-access failures for the course organization, Discussions, and assignments repository. Authentication-dependent destinations require manual student-path verification; full results are recorded in `EXTERNAL_LINK_REVIEW.md`.

## Strengths to preserve

- A coherent progression from sequence identification and raw reads to analysis, interpretation, and synthesis.
- Weekly project checkpoints that connect course topics to a quarter-long research product.
- Strong emphasis on provenance, intermediate checks, evidence, reproducibility, and appropriately limited claims.
- Stepwise setup tutorials with completion checklists and persistent progress.
- GitHub-native submission and progress workflows that create inspectable evidence trails.
- A project rubric that rewards scientific judgment, reproducibility, communication, and honest limitations.

## Baseline risks and friction points

| Area | Baseline observation | Student impact | Roadmap phase |
|---|---|---|---:|
| Schedule | Dates remain placeholders and weekly effort is not estimated. | Students cannot build a reliable term plan. | 1 |
| Navigation | Organization, source repository, assignments repository, student repository, and issue destinations are not consistently distinguished. | Students may submit or request help in the wrong place. | 1 |
| Onboarding | Approximately 3.5–4 hours of setup across three platforms is expected before Week 1. | Access delays and prior-experience differences may create an early participation gap. | 2 |
| Weekly learning | Most lecture pages state outcomes but provide limited worked examples, guided practice, or formative feedback. | Students must bridge concept-to-application gaps during graded work. | 3 |
| Assessment | The project rubric is detailed, but common criteria for question sets and weekly assignments are not published on this site. | Sixty percent of the course grade has less visible common guidance. | 4 |
| Accessibility | Tutorial progress is visual rather than semantic, keyboard focus is not customized, and mobile navigation is long. | Some students encounter avoidable interaction barriers. | 5 |
| Continuity | Weekly modules lack consistent previous/next/schedule navigation and explicit project-track pathways. | Students may lose the relationship between weekly work and the final compendium. | 6 |

## Baseline measures for student feedback

Collect the following during the first course offering after this baseline:

- Percentage of students with GitHub, Raven, and Hyak access before the first meeting.
- Median and range of time required for each setup tutorial.
- Percentage of students who can correctly identify where each type of work is submitted.
- Self-rated confidence with shell, Git/GitHub, Raven, Hyak, Quarto, and interpretation of bioinformatics output.
- Number and category of Week 0–2 help requests.
- Number of pull requests failing for preventable structure or destination errors.
- Student ratings of workload clarity, assignment clarity, feedback usefulness, and sense of support.

## Baseline feedback procedure

1. Administer `STUDENT_BASELINE_SURVEY.md` before students begin the tutorials.
2. Repeat the access, time, confidence, and clarity questions at the end of Week 1.
3. Summarize aggregate results in this file; do not publish identifiable student responses.
4. Convert common access or instruction problems into scoped repository issues.
5. Use the same core measures after Phase 2 so improvement can be compared with this baseline.

## Student-data handling

- Collect only information needed to improve course support.
- Report aggregated results when the cohort is large enough to protect privacy.
- Do not publish identifiable confidence ratings, disability information, access problems, or help-seeking history.
- Tell students how their feedback will be used and whether responses affect grades; the recommended baseline survey is ungraded.
