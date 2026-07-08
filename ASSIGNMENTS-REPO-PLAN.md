# Plan: Move Assessments & Assignments to a Pull-Request Repo

**Goal.** Replace the Issue-Form + external-student-repo + commit-SHA submission
system with a single, dedicated **assignments repo** that students clone/fork,
work in, and submit to by **pull request**. Each PR is automatically pre-checked
by GitHub Actions and commented on, then the instructor merges (accept) or
requests changes. This collapses five artifacts (issue form, parser,
cross-repo checkout, bot token, label bot) into one legible loop: *branch → work
→ PR → auto-check → review → merge*.

The Quarto **website stays as-is** and becomes purely instructional (syllabus,
schedule, lectures, tutorials, support). All *doing and turning-in* moves to the
new repo.

---

## 1. Two repos, clean split

| Repo | Role | Contains |
|------|------|----------|
| `course-fish546-2026` (this one) | **Teaching site** (Quarto → Pages) | `index`, `schedule`, `setup`, `support`, `lectures/`, `tutorials/`, `edna` hub. Links out to the assignments repo. |
| `fish546-2026-assignments` (new) | **Work + submission + autograding** | assignment/question prompts, per-student work folders, autograder, PR templates, workflows. |

The website links to each week's assignment in the new repo instead of hosting
the prompt itself. `assignments/*.qmd` and `questions/*.qmd` prompt text moves
(or is mirrored) into the new repo as plain Markdown task files.

---

## 2. New repo layout

```
fish546-2026-assignments/
├── README.md                     # how to submit (the whole workflow on one page)
├── assignments/                  # PROMPTS (read-only for students)
│   ├── 01-blast/README.md
│   ├── 02-fastq-qc/README.md
│   └── …
├── questions/                    # weekly question-set PROMPTS
│   ├── week01.md … week10.md
├── submissions/                  # STUDENT WORK — one folder per student
│   └── <github-username>/
│       ├── week01/
│       │   ├── answers.md
│       │   ├── analysis.html         # student-rendered (CI does NOT render)
│       │   ├── output/…
│       │   └── submission.yml        # manifest (reused from current design)
│       └── week02/…
├── templates/
│   └── submission.yml                # manifest template students copy
├── autograder/                       # the reusable checks (ported from scripts/)
│   ├── check_submission.py
│   └── requirements.txt
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       ├── autograde.yml             # runs on PR, produces report artifact
│       └── autograde-comment.yml     # workflow_run: posts comment + status
└── CODEOWNERS                        # optional: route review
```

**Per-student folders are the key design choice.** Every student writes only
under `submissions/<their-username>/`. This means PRs never conflict with each
other, the autograder knows exactly which files to check (the PR diff), and the
instructor can see one folder = one student's whole term.

---

## 3. Student workflow (branch model — recommended)

Two options; **collaborator + branch is recommended over fork** because it gives
the autograder a full-permission token (comments/labels "just work", no
`workflow_run` relay, no fork-sync pain).

**Recommended — students are collaborators on the one repo:**
1. Clone the assignments repo (once).
2. `git switch -c wk02-<username>`; do the work under
   `submissions/<username>/week02/`; commit + push the branch.
3. Open a PR into `main`. The PR template auto-fills the checklist.
4. Autograder runs on the PR, posts a comment, sets a check status.
5. Fix flagged items, push again (PR re-checks). Instructor reviews science, merges.

**Alternative — fork model** (if you don't want ~25 collaborators): students
fork, PR from fork. Same UX for students, but autograding must use the
`pull_request` (build report) + `workflow_run` (post comment) two-stage pattern
because fork PRs get a read-only token with no secrets.

Either way: **one repo the student pulls from, PRs into, and gets auto-assessed** —
exactly the requested model.

---

## 4. Autograding design

**Reuse** the logic already in [scripts/assess_submission.py](scripts/assess_submission.py):
required files exist, manifest `type`/`week` match, source + rendered present,
outputs non-empty, `questions_answered >= 5`, `project_connection` set, and no
`data/raw/` files committed. Port it to `autograder/check_submission.py`, but
change the input from "checkout external repo at SHA" to **"inspect the files the
PR changed."**

What the workflow does on each PR:
1. Compute the diff (`git diff --name-only origin/main...HEAD`).
2. **Ownership check:** every changed path must start with
   `submissions/<pr-author>/` — reject cross-folder edits (protects other
   students; also catches accidental edits to prompts).
3. Locate the touched `submission.yml`, run the structural checks against the
   files in the working tree.
4. Emit a Markdown report + a `pass|warn|fail` status.
5. Post the report as a PR comment; set a commit **check** (green/red) so the PR
   list shows status at a glance; apply `auto:pass|warn|fail` labels.

**Security posture (unchanged from current design):** CI does **not** execute or
render student code. Students commit their own rendered `.html`; CI only verifies
structure/evidence. This keeps untrusted code out of the runner and matches what
`turn-in.qmd` already promises. Human review still owns biological reasoning,
interpretation, caveats, and writing.

The `pass|warn|fail` split maps cleanly onto the existing `auto:*` labels and the
"automatic checks vs. instructor review" distinction the course already teaches.

---

## 5. What migrates, what retires

**Migrates to the new repo:**
- Assignment prompts (`assignments/*.qmd` → `assignments/<slug>/README.md`).
- Question-set prompts (`questions/week*.qmd` → `questions/weekNN.md`).
- Manifest schema + `submission.yml` examples (from `turn-in.qmd`).
- The checking logic in `scripts/assess_submission.py`.

**Retires (folded into the PR loop):**
- `.github/ISSUE_TEMPLATE/50-question-set-submission.yml` and
  `60-assignment-submission.yml` → replaced by the PR template.
- `scripts/parse_submission_issue.py` → no issue to parse; the PR *is* the
  submission and the diff *is* the manifest pointer.
- `.github/workflows/submission-assessment.yml` → replaced by `autograde.yml`.
- `COURSE_BOT_TOKEN` cross-repo checkout → gone (work lives in-repo).

**Stays on the website / lightweight in the org:**
- Help requests + blocker/bug issue forms (`30-*`, `40-*`) — still useful; keep
  as Issues (they aren't submissions).
- Weekly research-progress: decide (see §7) whether to keep it as an Issue Form
  or convert to a `submissions/<username>/progress/weekNN.md` PR. Recommend
  keeping progress as an **Issue** — it's a narrative checkpoint, not a file
  packet, and the current [progress workflow](.github/workflows/progress-assessment.yml)
  already fits Issues.

---

## 6. Instructor experience

- **The PR list replaces the project board.** Open PRs = outstanding
  submissions; `auto:*` labels + check marks = triage at a glance; filter by
  label `week-02` or by author.
- One folder per student under `submissions/` = the whole term's paper trail in
  one place, browsable and `git blame`-able.
- Merging is the accept action; "request changes" is the rework loop. No
  separate label dance to track state — PR state (open/changes-requested/merged)
  carries it.

---

## 7. Build sequence

1. **Create** `fish546-2026-assignments` (in the same org). Decide public vs.
   private (private = FERPA-safer; public = simplest).
2. **Scaffold** the layout in §2; write the one-page `README.md` submission guide
   and the PR template.
3. **Port** `assess_submission.py` → `autograder/check_submission.py`; switch
   its input to the PR diff; add the ownership check.
4. **Write** `autograde.yml` (+ `autograde-comment.yml` only if using forks).
5. **Migrate** assignment + question prompts; keep `submission.yml` schema.
6. **Seed** `submissions/<username>/` folders (script from the roster) and add
   students as collaborators (branch model) or send fork instructions.
7. **Dry run:** one fake student, one PR, confirm the comment + check + labels.
8. **Point the website at it:** update `turn-in.qmd`, `schedule.qmd`, and the
   per-week assignment links to the new repo; add a short "how to submit" note.
9. **Retire** the issue-form submission templates + the cross-repo workflow +
   the bot token.

---

## 8. Open decisions (need instructor input)

- **Collaborators-on-one-repo vs. forks.** Recommend collaborators+branch for
  simpler autograding; forks if you'd rather not add ~25 collaborators.
- **Public vs. private repo** (student privacy / FERPA vs. simplicity).
- **Weekly progress:** keep as an Issue (recommended) or fold into PRs.
- **Where prompts live:** single source of truth in the new repo (recommended),
  or authored in the Quarto site and mirrored.
- **Deadlines:** enforce via the commit timestamp on the PR head, or trust the
  PR-open time. (The old design froze a SHA; a PR head SHA does the same.)
```
