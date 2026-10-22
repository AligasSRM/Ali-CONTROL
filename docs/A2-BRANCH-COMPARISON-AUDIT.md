# A2 Branch Comparison and Repository Audit

- **Repository:** `AligasSRM/Ali-Control`
- **Audit date:** 2026-10-22 (UTC)
- **Reference branch:** `main`
- **Reference commit at audit:** `f9ef6b8909e26e708e1c1575578f2fbe67beb7fc`
- **Status:** A2 read-only audit completed; operational branch-retention decisions are explicitly outside this authorization and remain pending separate approval.
- **Scope:** Read-only inspection and comparison. No branches were deleted, no pull requests merged, and no repository protection settings changed as part of this audit.

## 1. Summary

GitHub listed 11 branches at the time of inspection: `main` and ten other branches. Comparing each non-main branch with `main` produced the ahead/behind counts below.

The counts are commit-graph comparison results, not a measure of risk, quality, or whether a branch should be deleted. A branch with zero commits ahead of `main` may still be useful for traceability; deletion requires a separate decision.

## 2. Branch comparison

| Branch | Ahead of main | Behind main | GitHub comparison status | Notes |
|---|---:|---:|---|---|
| `a1/codeowner-enforcement-test` | 1 | 7 | diverged | Contains an additional commit adding `.github/A1-CODEOWNER-ENFORCEMENT-TEST.md`. A1 remains closed by owner direction; do not reopen or alter it without new authorization. |
| `ci/upgrade-checkout-v7-current-main` | 2 | 8 | diverged | Diff reports changes to `.github/workflows/codeql.yml` and `.github/workflows/main.yml`. |
| `ci/validate-control-governance` | 0 | 17 | behind | No unique commits reported ahead of main. |
| `dependabot/github_actions/actions/setup-python-7` | 1 | 10 | diverged | Diff reports a change to `.github/workflows/main.yml`. |
| `docs/control-status-register-draft` | 0 | 1 | behind | No unique commits reported ahead of main; its inspected head is the pre-merge commit associated with PR #10. |
| `fix/ci-governance-validation` | 3 | 16 | diverged | Diff reports changes to the CI workflow and additions of `scripts/validate_governance.py` and `tests/test_governance_validation.py`. |
| `proposal/governance-v2-validation` | 6 | 16 | diverged | Contains proposed governance/workflow and validation files; proposal states it is not approved for publication. Keep separate pending explicit review. |
| `security/add-repository-hardening` | 0 | 11 | behind | No unique commits reported ahead of main. |
| `security/remove-unused-pip-dependabot` | 1 | 10 | diverged | Diff reports a change to `.github/dependabot.yml`. |
| `test/ci-required-check-failure` | 2 | 16 | diverged | Test-related branch; keep classified as a test branch unless separately reviewed. |
| `main` | — | — | reference | Protected branch at the reference commit above. |

## 2A. Pull-request to branch reconciliation (follow-up)

Follow-up read-only checks compared the current branch listing with the source refs recorded on PRs #1–#10. PR #11 is the documentation PR for this report.

| PR | Outcome at check | Source branch recorded on PR | Reconciliation result |
|---|---|---|---|
| [#1](https://github.com/AligasSRM/Ali-Control/pull/1) | Merged | `ci/validate-control-governance` | Exact current branch-head SHA match: `5f4d89a1e39e26928f1216807d929535c3cb2007`. |
| [#2](https://github.com/AligasSRM/Ali-Control/pull/2) | Closed, not merged | `test/ci-required-check-failure` | Branch exists, but its current head `ef5771573ceb280a85a4a995b5c3d596682ee78b` is one commit ahead of PR head `f7e0e0747532f5b8ca2b05e84fc741b2339311a2`. The comparison shows the PR head is an ancestor of the current branch head; the branch was not missing. |
| [#3](https://github.com/AligasSRM/Ali-Control/pull/3) | Merged | `fix/ci-governance-validation` | Exact current branch-head SHA match: `636bd0d80dc76ee42cbf6d6d878aaef5e3e04bcb`. |
| [#4](https://github.com/AligasSRM/Ali-Control/pull/4) | Merged | `security/add-repository-hardening` | Exact current branch-head SHA match: `6f612c3bee59b7a0c52524da2ad0fa41912474fe`. |
| [#5](https://github.com/AligasSRM/Ali-Control/pull/5) | Closed, not merged | `dependabot/github_actions/actions/checkout-7` | This source branch is absent from the current branch listing. Its PR history remains accessible; head SHA was `1a1df7bc2c9bda92ce611718748b67d16cd2a674`. The current `ci/upgrade-checkout-v7-current-main` branch is related by topic but diverges from that head, so it is not treated as the same branch. |
| [#6](https://github.com/AligasSRM/Ali-Control/pull/6) | Merged | `dependabot/github_actions/actions/setup-python-7` | Exact current branch-head SHA match: `9f04f64c4613b10c43c3a25d887a95e9ba17660b`. |
| [#7](https://github.com/AligasSRM/Ali-Control/pull/7) | Merged | `security/remove-unused-pip-dependabot` | Exact current branch-head SHA match: `bbc0aec77b5ce069501baf940c3db8a2d54139d0`. |
| [#8](https://github.com/AligasSRM/Ali-Control/pull/8) | Merged | `ci/upgrade-checkout-v7-current-main` | Exact current branch-head SHA match: `b62b87e6d4b5a9a5c6ba7aa2a3fdce48745e0a8c`. |
| [#9](https://github.com/AligasSRM/Ali-Control/pull/9) | Closed, not merged | `a1/codeowner-enforcement-test` | Exact current branch-head SHA match: `dda149967531be73ac489ad0173342bbc5391d63`. A1 remains closed; this mapping does not authorize reopening or editing it. |
| [#10](https://github.com/AligasSRM/Ali-Control/pull/10) | Merged | `docs/control-status-register-draft` | Exact current branch-head SHA match: `689a87564d62a5212318bf0a35a07ca764bb7427`. |
| [#11](https://github.com/AligasSRM/Ali-Control/pull/11) | Open draft | `docs/a2-branch-audit-report` | This report's branch; head SHA at this follow-up check is the audit-documentation commit. |

### Reconciliation conclusions

- PRs #1–#10 each have an identifiable source ref recorded in their PR metadata.
- Nine of those ten source branches are present in the current branch listing. PR #2's source branch remains present but has advanced one commit since the PR head.
- The only source branch not present in the current branch listing is PR #5's `dependabot/github_actions/actions/checkout-7`. The available evidence establishes its absence from the current list, not who removed it or why.
- PR #8's checkout-v7 work is related by subject to PR #5, but the commit comparison is divergent; do not claim they are identical or that one is a direct continuation of the other.
- The follow-up branch listing now includes `docs/a2-branch-audit-report`, created for PR #11. The original comparison table above remains a historical snapshot of the ten non-main branches present before this report branch was created.

### Comparison links

- [A1 enforcement test](https://github.com/AligasSRM/Ali-Control/compare/main...a1/codeowner-enforcement-test)
- [Checkout action upgrade](https://github.com/AligasSRM/Ali-Control/compare/main...ci/upgrade-checkout-v7-current-main)
- [Governance validation](https://github.com/AligasSRM/Ali-Control/compare/main...ci/validate-control-governance)
- [setup-python update](https://github.com/AligasSRM/Ali-Control/compare/main...dependabot/github_actions/actions/setup-python-7)
- [Control status draft](https://github.com/AligasSRM/Ali-Control/compare/main...docs/control-status-register-draft)
- [CI validation fix](https://github.com/AligasSRM/Ali-Control/compare/main...fix/ci-governance-validation)
- [Governance v2 proposal](https://github.com/AligasSRM/Ali-Control/compare/main...proposal/governance-v2-validation)
- [Repository hardening](https://github.com/AligasSRM/Ali-Control/compare/main...security/add-repository-hardening)
- [Remove unused pip Dependabot config](https://github.com/AligasSRM/Ali-Control/compare/main...security/remove-unused-pip-dependabot)
- [Required-check failure test](https://github.com/AligasSRM/Ali-Control/compare/main...test/ci-required-check-failure)

## 3. Last commit timestamps observed

These are the committer timestamps returned by GitHub for the inspected branch-head commits. They indicate commit metadata, not proof that a branch is currently active.

| Branch | Last commit (UTC) | Head commit |
|---|---|---|
| `a1/codeowner-enforcement-test` | 2026-10-22 12:58:59 | `dda149967531be73ac489ad0173342bbc5391d63` |
| `ci/upgrade-checkout-v7-current-main` | 2026-10-22 01:20:02 | `b62b87e6d4b5a9a5c6ba7aa2a3fdce48745e0a8c` |
| `ci/validate-control-governance` | 2026-10-21 22:55:14 | `5f4d89a1e39e26928f1216807d929535c3cb2007` |
| `dependabot/github_actions/actions/setup-python-7` | 2026-10-22 00:22:50 | `9f04f64c4613b10c43c3a25d887a95e9ba17660b` |
| `docs/control-status-register-draft` | 2026-10-22 13:24:22 | `689a87564d62a5212318bf0a35a07ca764bb7427` |
| `fix/ci-governance-validation` | 2026-10-22 00:04:23 | `636bd0d80dc76ee42cbf6d6d878aaef5e3e04bcb` |
| `proposal/governance-v2-validation` | 2026-10-21 23:55:40 | `1db16c5a4a9c569fb70a8ac8730d0150ea5637ff` |
| `security/add-repository-hardening` | 2026-10-22 00:11:17 | `6f612c3bee59b7a0c52524da2ad0fa41912474fe` |
| `security/remove-unused-pip-dependabot` | 2026-10-22 00:56:13 | `bbc0aec77b5ce069501baf940c3db8a2d54139d0` |
| `test/ci-required-check-failure` | 2026-10-22 00:00:48 | `ef5771573ceb280a85a4a995b5c3d596682ee78b` |

## 4. Protection and governance observations

- GitHub's branch listing reported `main` as protected and the other ten listed branches as not protected.
- The repository ruleset inspected during the audit is named `ALI-CONTROL-MAIN-PROTECTION`. The observed settings include pull-request review requirements, code-owner review, resolution of review conversations, and a required governance validation check.
- `.github/CODEOWNERS`, `.github/workflows/main.yml`, `.github/workflows/codeql.yml`, `scripts/validate_governance.py`, `tests/test_governance_validation.py`, `SECURITY.md`, `README.md`, and `docs/CONTROL-STATUS-AND-ROADMAP.md` were inspected for existence/content.
- GitHub Actions showed successful governance-validation and CodeQL runs for the audited main commit. This is evidence for those runs only; it is not proof of full production readiness.
- PRs #1, #3, #4, #6, #7, #8, and #10 were observed merged; PRs #2, #5, and #9 were observed closed without merge. The branch list did not include a branch identifiable as the source of PR #5. The cause of that absence was not established.

## 5. Decisions and unresolved items

1. **No branch deletion is authorized by this report.** Decide separately whether to retain or delete merged/stale branches after any required historical review.
2. **A1 stays closed.** Do not reopen or modify the A1 test branch or A1 files without new explicit authorization.
3. **Do not merge `proposal/governance-v2-validation` automatically.** Its changes are divergent and the proposal is explicitly unapproved; review and approval are required before any adoption.
4. **Investigate PR #5 branch traceability** if needed; current evidence establishes only that the source branch was not present in the inspected branch list.
5. **No repository changes are proposed by this report other than this documentation file and this report's follow-up documentation update.** Protection settings, access, workflows, and application code are outside this audit's write scope.

## 6. A2 status and closeout

**A2 read-only audit is complete for the authorized scope.** The branch comparison and PR-to-branch reconciliation for PRs #1–#10 are documented, with evidence links and commit identifiers. The initial branch comparison is a dated snapshot of ten non-main branches; the follow-up listing also includes this report's documentation branch.

The following are recorded as **out-of-scope decisions**, not unfinished audit steps:
- Whether to delete or retain individual branches. No branch is deleted or recommended for deletion solely from ahead/behind counts.
- Who deleted or why the source branch for PR #5 is absent from the current branch list. The available evidence does not establish cause.
- Whether to adopt `proposal/governance-v2-validation`. It remains unapproved and requires a separate owner decision.

A1 remains closed. No protection settings or access controls were changed. This report does not claim production readiness. Any cleanup, proposal adoption, or merge of this report requires the appropriate separate approval; this audit did not perform those actions.

## 7. Evidence sources

All sources below are within `AligasSRM/Ali-Control`:

- [Branches API listing](https://api.github.com/repos/AligasSRM/Ali-Control/branches?per_page=100)
- [Pull requests](https://github.com/AligasSRM/Ali-Control/pulls?q=is%3Apr)
- [Main branch rules](https://github.com/AligasSRM/Ali-Control/rules/25596528)
- [CODEOWNERS](https://github.com/AligasSRM/Ali-Control/blob/main/.github/CODEOWNERS)
- [Governance workflow](https://github.com/AligasSRM/Ali-Control/blob/main/.github/workflows/main.yml)
- [CodeQL workflow](https://github.com/AligasSRM/Ali-Control/blob/main/.github/workflows/codeql.yml)
- [Control status and roadmap](https://github.com/AligasSRM/Ali-Control/blob/main/docs/CONTROL-STATUS-AND-ROADMAP.md)
- [Governance validation run](https://github.com/AligasSRM/Ali-Control/actions/runs/39801437636)
- [CodeQL run](https://github.com/AligasSRM/Ali-Control/actions/runs/39801437613)
