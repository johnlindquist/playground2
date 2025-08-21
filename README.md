# Claude Workflow Examples (Manual-Only)

This directory contains 30 copy/pasteable GitHub Actions that integrate Claude Code to automate useful maintenance and collaboration tasks. Every workflow here is:

- Manual-only (triggered with `workflow_dispatch`), never auto-runs by default
- Safe by design with conservative permissions and narrow `allowed_tools`
- Heavily documented in-file so you can customize prompts, inputs, tools, and outputs

If you want one of these to run automatically (e.g., on PRs), edit the `on:` section explicitly after you’ve reviewed the behavior and safety notes. Until then, they only run when manually dispatched.

## Get a Token + Add Secret (start here)

1) Get a Claude Code OAuth token
- Run in your terminal: `claude setup-token`
- Follow the prompts. Copy the printed token value when it completes.

2) Add the token to your repo with GitHub CLI
- Ensure you’re authenticated: `gh auth status`
- Set a repository secret named `CLAUDE_CODE_OAUTH_TOKEN`:
  - If you exported the token as an env var: `gh secret set CLAUDE_CODE_OAUTH_TOKEN --body "$CLAUDE_CODE_OAUTH_TOKEN"`
  - Or pipe it directly: `echo -n "<paste-token-here>" | gh secret set CLAUDE_CODE_OAUTH_TOKEN`

Notes
- Use org- or environment-level secrets if you prefer broader reuse: `gh secret set --org <org> ...` or `gh secret set --env <env> ...`
- The workflows below assume the secret name `CLAUDE_CODE_OAUTH_TOKEN`.

## Quick Setup

Verify permissions in each workflow match your intent. Most examples use:
- `contents: read` or `write` (only if the flow commits/opens PRs)
- `pull-requests: read` or `write` (only if commenting/opening PRs)
- `issues: read` or `write` (only if commenting on issues)
- `id-token: write` (required by the action runtime)
- Occasionally `actions: read` for CI context

Optional: GitHub CLI access for comments/PRs
- Workflows that post comments or open PRs use `gh`. They pass `GH_TOKEN: ${{ github.token }}` automatically when needed.

Review Claude action docs
- See `docs/claude-code-action.md` in this repo for setup details and options.

## Running a Workflow

- From GitHub UI: Actions → pick the workflow → Run workflow → fill inputs → Run
- From CLI (example):
  - `gh workflow run diff-aware-pr-reviewer.yml -f pr_number=123 -f post_comment=true`

All workflows take simple inputs and write their outputs under predictable folders such as `reports/`, `tests/`, `scripts/`, or `tools/`.

## Safety Model

- Manual triggers only. No schedules or automatic events configured.
- Minimal permissions and tight `allowed_tools` to limit side effects.
- Write paths are constrained to `reports/`, and scoped folders like `tests/`, `scripts/`, `tools/`, `benchmarks/`, `repro/`.
- Workflows that change code do so on new branches and can optionally open PRs for human review.

## Customizing

- Prompts: Edit the `override_prompt` text for behavior, tone, guardrails, and output formats.
- Tools: Expand or restrict `allowed_tools` for what Claude can do. Default sets are conservative.
- Inputs/Outputs: Add new `workflow_dispatch.inputs` and redirect outputs to paths that fit your repo structure.
- Models/Settings: You can set `model`, add `additional_permissions`, or environment variables (`claude_env`) as needed.

---

## Catalog

Below is a brief description of each workflow, its inputs, outputs, and common customizations. Open the YAML files for deeper, inline guidance.

### 1) Diff‑Aware PR Reviewer
- File: `.github/workflows/diff-aware-pr-reviewer.yml`
- Purpose: Review a PR diff, write a concise analysis, optionally post a comment.
- Inputs: `pr_number` (required), `post_comment` (default: false)
- Outputs: `reports/pr-<PR>-review.md`
- Customize: Tighten/relax review scope; change report format; disable `gh` comment.
 - Jump to: [inputs](./diff-aware-pr-reviewer.yml#L30) · [allowed_tools](./diff-aware-pr-reviewer.yml#L63) · [override_prompt](./diff-aware-pr-reviewer.yml#L69)

### 2) Design Doc Gatekeeper
- File: `.github/workflows/design-doc-gatekeeper.yml`
- Purpose: Check RFCs against a template; consolidate feedback.
- Inputs: `rfc_glob`, `issue_number`, `post_comment`
- Outputs: `reports/design-doc-review.md`
- Customize: Template sections; whether to comment on issues.
 - Jump to: [inputs](./design-doc-gatekeeper.yml#L19) · [allowed_tools](./design-doc-gatekeeper.yml#L50) · [override_prompt](./design-doc-gatekeeper.yml#L55)

### 3) Pattern Police
- File: `.github/workflows/pattern-police.yml`
- Purpose: Flag architecture/layering drift using a rules file.
- Inputs: `pr_number`, `rules_path`
- Outputs: `reports/pattern-drift-pr-<PR>.md`
- Customize: Project rules and examples of banned imports/dependencies.
 - Jump to: [inputs](./pattern-police.yml#L17) · [allowed_tools](./pattern-police.yml#L46) · [override_prompt](./pattern-police.yml#L52)

### 4) Commit Message Fixer (Conventional Commits)
- File: `.github/workflows/commit-message-fixer.yml`
- Purpose: Reword commits on a new branch to Conventional Commits; optional PR.
- Inputs: `base_branch`, `target_branch`, `open_pr`
- Outputs: New branch + PR (optional)
- Customize: Types/scopes, default branches, whether to create a PR.
 - Jump to: [inputs](./commit-message-fixer.yml#L18) · [allowed_tools](./commit-message-fixer.yml#L51) · [override_prompt](./commit-message-fixer.yml#L61)

### 5) API Contract Enforcer
- File: `.github/workflows/api-contract-enforcer.yml`
- Purpose: Compare API spec vs base branch; flag potential breaking changes; optional test scaffolds.
- Inputs: `contract_path`, `base_branch`, `generate_tests`
- Outputs: `reports/api-contract-diff.md`, `tests/generated/`
- Customize: Spec path, test generation on/off, output dirs.
 - Jump to: [inputs](./api-contract-enforcer.yml#L14) · [allowed_tools](./api-contract-enforcer.yml#L44) · [override_prompt](./api-contract-enforcer.yml#L48)

### 6) Flaky Test Hunter‑Killer
- File: `.github/workflows/flaky-test-hunter.yml`
- Purpose: Re-run a test N times; log flakiness; propose quarantine plan.
- Inputs: `test_command`, `reruns`, `quarantine_label`
- Outputs: `reports/flaky-test-log.txt`, `reports/flaky-test-summary.md`, `reports/flaky-quarantine-plan.md`
- Customize: Test command, reruns, quarantine policy.
 - Jump to: [inputs](./flaky-test-hunter.yml#L14) · [allowed_tools](./flaky-test-hunter.yml#L42) · [override_prompt](./flaky-test-hunter.yml#L48)

### 7) Failure Explainer → Patch PR
- File: `.github/workflows/failure-explainer-patch.yml`
- Purpose: Analyze failure logs, draft minimal fix on a new branch, optional PR.
- Inputs: `log_path`, `branch_name`, `open_pr`
- Outputs: `reports/failure-analysis.md`, new branch + PR (optional)
- Customize: Scope of permitted edits; diff size limits.
 - Jump to: [inputs](./failure-explainer-patch.yml#L14) · [allowed_tools](./failure-explainer-patch.yml#L46) · [override_prompt](./failure-explainer-patch.yml#L55)

### 8) Fuzz/Property Testing on Hot Paths
- File: `.github/workflows/fuzz-property-testing.yml`
- Purpose: Suggest property-based tests and scaffolding; prioritize hot code paths.
- Inputs: `target_dirs`, `coverage_path?`
- Outputs: `tests/property/`, `reports/property-testing-plan.md`
- Customize: Test framework, coverage signal, invariants.
 - Jump to: [inputs](./fuzz-property-testing.yml#L14) · [allowed_tools](./fuzz-property-testing.yml#L38) · [override_prompt](./fuzz-property-testing.yml#L42)

### 9) Cross‑Platform Repro Bot (Playwright/Electron)
- File: `.github/workflows/cross-platform-repro.yml`
- Purpose: Create Playwright repro scaffold with trace/video.
- Inputs: `scenario_desc`
- Outputs: `repro/playwright/`, `reports/repro-instructions.md`
- Customize: Framework/tool; scenario specificity; install steps.
 - Jump to: [inputs](./cross-platform-repro.yml#L14) · [allowed_tools](./cross-platform-repro.yml#L34) · [override_prompt](./cross-platform-repro.yml#L38)

### 10) Performance Regression Sentinel
- File: `.github/workflows/performance-regression-sentinel.yml`
- Purpose: Identify perf risks in a PR; suggest benchmarks.
- Inputs: `pr_number`
- Outputs: `benchmarks/`, `reports/perf-assessment-pr-<PR>.md`
- Customize: Benchmark tool/framework; file-type filters.
 - Jump to: [inputs](./performance-regression-sentinel.yml#L14) · [allowed_tools](./performance-regression-sentinel.yml#L38) · [override_prompt](./performance-regression-sentinel.yml#L43)

### 11) Auto‑triage CVEs with Fix PR
- File: `.github/workflows/cve-triage-fix-pr.yml`
- Purpose: Propose safe dependency upgrades; optional PR.
- Inputs: `package_manager`, `branch_name`
- Outputs: `reports/deps-cve-summary.md`, branch + PR (optional)
- Customize: Allowed version bumps; ecosystems; risk notes.
 - Jump to: [inputs](./cve-triage-fix-pr.yml#L14) · [allowed_tools](./cve-triage-fix-pr.yml#L43) · [override_prompt](./cve-triage-fix-pr.yml#L52)

### 12) Secret Hygiene Coach
- File: `.github/workflows/secret-hygiene-coach.yml`
- Purpose: Scan for potential secrets; write remediation steps.
- Inputs: `search_globs`
- Outputs: `reports/secret-hygiene.md`
- Customize: Patterns and globs; link to org scanners.
 - Jump to: [inputs](./secret-hygiene-coach.yml#L14) · [allowed_tools](./secret-hygiene-coach.yml#L35) · [override_prompt](./secret-hygiene-coach.yml#L40)

### 13) Policy‑as‑Code Explainer
- File: `.github/workflows/policy-as-code-explainer.yml`
- Purpose: Explain policy violations; suggest minimal diffs to comply.
- Inputs: `violations_path`
- Outputs: `reports/policy-explanations.md`
- Customize: Policy framework and fix strategy options.
 - Jump to: [inputs](./policy-as-code-explainer.yml#L14) · [allowed_tools](./policy-as-code-explainer.yml#L34) · [override_prompt](./policy-as-code-explainer.yml#L37)

### 14) Executable Docs Doctor
- File: `.github/workflows/executable-docs-doctor.yml`
- Purpose: Parse docs for code blocks; reason about outputs; generate `_generated` artifacts.
- Inputs: `docs_glob`
- Outputs: `docs/_generated/`, `reports/docs-doctor-summary.md`
- Customize: Language filters; safe/no-network execution constraints.
 - Jump to: [inputs](./executable-docs-doctor.yml#L14) · [allowed_tools](./executable-docs-doctor.yml#L35) · [override_prompt](./executable-docs-doctor.yml#L39)

### 15) Tutorial Freshness Checker
- File: `.github/workflows/tutorial-freshness-checker.yml`
- Purpose: Detect stale tutorials; propose updates.
- Inputs: `tutorials_glob`
- Outputs: `reports/tutorial-freshness.md`
- Customize: Version maps; issue templates.
 - Jump to: [inputs](./tutorial-freshness-checker.yml#L14) · [allowed_tools](./tutorial-freshness-checker.yml#L35) · [override_prompt](./tutorial-freshness-checker.yml#L38)

### 16) Changelog & Release Notes Author
- File: `.github/workflows/changelog-release-notes.yml`
- Purpose: Draft release notes and update `CHANGELOG.md` from git history.
- Inputs: `since_ref`, `until_ref?`
- Outputs: `reports/release-notes.md`, `CHANGELOG.md`
- Customize: Sections, formatting, link styles.
 - Jump to: [inputs](./changelog-release-notes.yml#L14) · [allowed_tools](./changelog-release-notes.yml#L39) · [override_prompt](./changelog-release-notes.yml#L43)

### 17) Contributor Concierge
- File: `.github/workflows/contributor-concierge.yml`
- Purpose: Post friendly guidance to a PR.
- Inputs: `pr_number`, `post_comment`
- Outputs: PR comment (optional)
- Customize: Tone, house style, setup checklist.
 - Jump to: [inputs](./contributor-concierge.yml#L14) · [allowed_tools](./contributor-concierge.yml#L41) · [override_prompt](./contributor-concierge.yml#L45)

### 18) Issue De‑duplicator & Triager
- File: `.github/workflows/issue-de-duplicator.yml`
- Purpose: Suggest duplicates and workarounds.
- Inputs: `issue_number`, `post_comment`
- Outputs: `reports/issue-<ISSUE>-dedupe.md`, optional comment
- Customize: Search filters, number of candidates.
 - Jump to: [inputs](./issue-de-duplicator.yml#L14) · [allowed_tools](./issue-de-duplicator.yml#L40) · [override_prompt](./issue-de-duplicator.yml#L45)

### 19) Roadmap Synchronizer
- File: `.github/workflows/roadmap-synchronizer.yml`
- Purpose: Propose milestone/label updates and a weekly digest.
- Inputs: `milestone_title?`
- Outputs: `reports/roadmap-sync.md`
- Customize: Label conventions; mutation vs report-only.
 - Jump to: [inputs](./roadmap-synchronizer.yml#L14) · [allowed_tools](./roadmap-synchronizer.yml#L37) · [override_prompt](./roadmap-synchronizer.yml#L41)

### 20) Spec → Test Plan Synthesizer
- File: `.github/workflows/spec-to-test-plan.yml`
- Purpose: Convert spec to Gherkin plan and optional test stubs.
- Inputs: `spec_path`, `create_stubs`
- Outputs: `tests/plans/plan.feature`, `tests/stubs/`
- Customize: Test framework and language.
 - Jump to: [inputs](./spec-to-test-plan.yml#L14) · [allowed_tools](./spec-to-test-plan.yml#L37) · [override_prompt](./spec-to-test-plan.yml#L41)

### 21) Cache Strategy Optimizer
- File: `.github/workflows/cache-strategy-optimizer.yml`
- Purpose: Improve `actions/cache` usage.
- Inputs: `workflow_glob`
- Outputs: `reports/cache-optimization.md`
- Customize: Key composition; before/after timing hypotheses.
 - Jump to: [inputs](./cache-strategy-optimizer.yml#L14) · [allowed_tools](./cache-strategy-optimizer.yml#L35) · [override_prompt](./cache-strategy-optimizer.yml#L38)

### 22) Selective CI (Monorepo Brain)
- File: `.github/workflows/selective-ci-monorepo.yml`
- Purpose: Generate `scripts/affected.sh` and a usage guide.
- Inputs: `base_ref`
- Outputs: `scripts/affected.sh`, `reports/selective-ci-audit.md`
- Customize: Monorepo tooling (Nx/Turbo/Bazel) integration.
 - Jump to: [inputs](./selective-ci-monorepo.yml#L14) · [allowed_tools](./selective-ci-monorepo.yml#L37) · [override_prompt](./selective-ci-monorepo.yml#L42)

### 23) Infra Change Simulator
- File: `.github/workflows/infra-change-simulator.yml`
- Purpose: Draft IaC plan/diff and cost-estimation guidance.
- Inputs: `iac_dir`
- Outputs: `reports/infra-plan.md`
- Customize: Tooling (Terraform/CDK/Pulumi); cloud specifics.
 - Jump to: [inputs](./infra-change-simulator.yml#L14) · [allowed_tools](./infra-change-simulator.yml#L35) · [override_prompt](./infra-change-simulator.yml#L38)

### 24) Schema Migration Dry‑Runner
- File: `.github/workflows/schema-migration-dry-runner.yml`
- Purpose: Generate DB dry-run script and guidance.
- Inputs: `migrations_dir`
- Outputs: `scripts/db-dry-run.sh`, `reports/migration-dry-run.md`
- Customize: DB type, container runtime, compose vs script.
 - Jump to: [inputs](./schema-migration-dry-runner.yml#L14) · [allowed_tools](./schema-migration-dry-runner.yml#L35) · [override_prompt](./schema-migration-dry-runner.yml#L39)

### 25) Canary Bot with Rollback Plan
- File: `.github/workflows/canary-rollback-bot.yml`
- Purpose: Prepare rollback playbook and PR.
- Inputs: `service_name`
- Outputs: `reports/<service>-rollback-plan.md`, branch + PR
- Customize: Dashboards/alerts links; SLOs; PR label conventions.
 - Jump to: [inputs](./canary-rollback-bot.yml#L14) · [allowed_tools](./canary-rollback-bot.yml#L39) · [override_prompt](./canary-rollback-bot.yml#L47)

### 26) Design Pattern Propagator
- File: `.github/workflows/design-pattern-propagator.yml`
- Purpose: Draft codemods and propagation plan from an approved pattern doc.
- Inputs: `pattern_doc`
- Outputs: `tools/codemods/`, `reports/pattern-propagation-plan.md`
- Customize: Languages; repo structures; batching.
 - Jump to: [inputs](./design-pattern-propagator.yml#L14) · [allowed_tools](./design-pattern-propagator.yml#L34) · [override_prompt](./design-pattern-propagator.yml#L38)

### 27) License & Header Normalizer
- File: `.github/workflows/license-header-normalizer.yml`
- Purpose: Audit/add headers; optional PR on new branch.
- Inputs: `header_text`, `file_glob`, `create_branch`
- Outputs: `reports/header-audit.md`, branch + PR (optional)
- Customize: Headers; churn avoidance; file types.
 - Jump to: [inputs](./license-header-normalizer.yml#L14) · [allowed_tools](./license-header-normalizer.yml#L45) · [override_prompt](./license-header-normalizer.yml#L54)

### 28) Dependency Baseline Aligner
- File: `.github/workflows/dependency-baseline-aligner.yml`
- Purpose: Plan staged upgrades to meet baseline.
- Inputs: `baseline_doc`
- Outputs: `reports/dependency-baseline-plan.md`
- Customize: Ecosystem rules; batching; CI gates.
 - Jump to: [inputs](./dependency-baseline-aligner.yml#L14) · [allowed_tools](./dependency-baseline-aligner.yml#L34) · [override_prompt](./dependency-baseline-aligner.yml#L37)

### 29) Bug → Dataset Creator
- File: `.github/workflows/bug-to-dataset.yml`
- Purpose: Turn bug report into fixtures and failing test scaffold.
- Inputs: `issue_number`
- Outputs: `fixtures/`, `tests/failing/`
- Customize: Test harness; anonymization; repro script.
 - Jump to: [inputs](./bug-to-dataset.yml#L14) · [allowed_tools](./bug-to-dataset.yml#L36) · [override_prompt](./bug-to-dataset.yml#L41)

### 30) Log‑to‑Hypothesis Bot
- File: `.github/workflows/log-to-hypothesis.yml`
- Purpose: Derive concrete hypotheses and checks from logs/metrics.
- Inputs: `logs_path`
- Outputs: `reports/log-hypotheses.md`
- Customize: Signal formats; runbook links; mitigation vs investigation.
 - Jump to: [inputs](./log-to-hypothesis.yml#L14) · [allowed_tools](./log-to-hypothesis.yml#L34) · [override_prompt](./log-to-hypothesis.yml#L37)

---

## Common Issues
- Missing secret: Ensure `CLAUDE_CODE_OAUTH_TOKEN` is set in repo secrets.
- Permissions too strict: If a step needs to comment or open PRs, add `issues: write` or `pull-requests: write` and include the corresponding `gh` tool in `allowed_tools`.
- Overly broad tools: If you see an action doing too much, remove unneeded `Bash(...)` entries and keep only the minimal set.
- Large repos: Consider narrowing globs or paths in inputs and prompts to keep execution tight.

## FAQ
- Can I run these automatically on PRs? Yes—change `on:` to the appropriate event after you review safety controls.
- Can I use models other than the default? Yes—set the `model` input on the action if desired.
- How do I prevent code changes? Ensure `allowed_tools` excludes write/commit/push operations and confirm the prompt explicitly forbids edits.
- How do I add my own workflow? Copy one of these, change the name, inputs, and prompt. Keep manual trigger and conservative tools until you’ve validated behavior.

Happy automating—safely and intentionally.
