# External Link Review

**Review cadence:** Before publishing each course offering and once near mid-quarter

**Authoritative command:** `python3 scripts/audit_course_site.py --external`

External links change independently of this repository. The audit reports HTTP responses and redirects but does not fail by default because authenticated services such as Slack, Raven, and Hyak may reject automated requests while remaining available to students.

## Review procedure

1. Run the standard offline audit:

   ```bash
   python3 scripts/audit_course_site.py
   ```

2. From a networked environment, run the external review:

   ```bash
   python3 scripts/audit_course_site.py --external
   ```

3. Manually verify URLs reporting `401`, `403`, `405`, a timeout, or another connection error when they are expected to require authentication.
4. Treat `404` and `410` as broken unless the destination owner confirms otherwise.
5. Check that redirects still reach the intended resource rather than a generic homepage.
6. Record the review below, including any corrections or intentionally accepted restricted links.

## Review log

| Date | Reviewer | Result | Follow-up |
|---|---|---|---|
| 2026-07-31 | Course-maintenance baseline | Networked automated review completed. The central course repository, textbook resources, public handbook pages, DADA2, MarineOmics, Quarto, Slack landing page, and instructor page responded successfully. | Resolve the launch blockers and access checks below before publication. |

## 2026-07-31 findings

### Launch blockers

- `https://course-fish546-2026.github.io/setup.html`, currently embedded in the Setup Check issue form, returned `404`.
- `https://github.com/course-fish546-2026` returned `404` to an anonymous request. Confirm that the organization exists, that enrolled students have access, and that the intended student repository workflow is ready.
- The organization Discussions URL returned `404` anonymously. Confirm whether Discussions is enabled and visible to enrolled students.
- The assignments repository and every linked weekly question/assignment path returned `404` anonymously. Confirm that the repository is intentionally private or not yet published, then test all paths with an enrolled-student account.

### Manual access checks

- Raven did not resolve from the audit environment; test it from the UW network and through the documented VPN route.
- Hyak OnDemand timed out; test it with an allocated UW account.
- The GitHub account-creation URL redirects to GitHub's current signup route and rejects the automated request. Verify it manually but do not classify the automated `403` as a broken student destination.

### Passed public references

- The central `sr320/course-fish546-2026` repository responded successfully.
- The Roberts Lab Handbook landing page and every linked computing/platform guide responded successfully.
- The DADA2 tutorial, MarineOmics, Quarto, textbook listing, textbook supplementary repository, and GitHub Desktop destination responded successfully.

These results describe anonymous HTTP access on the review date. Authentication-dependent destinations still require the manual student-path checks above.

## Expected restricted destinations

- Raven may require the UW network or VPN.
- Hyak OnDemand and Klone require UW credentials and an allocation.
- Slack requires workspace membership.
- Private or not-yet-published GitHub repositories may return `404` to anonymous requests.

Do not replace a working authenticated destination solely because an anonymous automated request cannot access it. Document the restriction and verify it using the same access path students will use.
