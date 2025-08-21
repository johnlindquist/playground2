This file is a merged representation of a subset of the codebase, containing specifically included files, combined into a single document by Repomix.

<file_summary>
This section contains a summary of this file.

<purpose>
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.
</purpose>

<file_format>
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  - File path as an attribute
  - Full contents of the file
</file_format>

<usage_guidelines>
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.
</usage_guidelines>

<notes>
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: **/*.md
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)
</notes>

</file_summary>

<directory_structure>
.claude/
  commands/
    commit-and-pr.md
.github/
  ISSUE_TEMPLATE/
    bug_report.md
base-action/
  CLAUDE.md
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  MIRROR_DISCLAIMER.md
  README.md
docs/
  capabilities-and-limitations.md
  cloud-providers.md
  configuration.md
  custom-automations.md
  experimental.md
  faq.md
  security.md
  setup.md
  usage.md
test/
  fixtures/
    sample-turns-expected-output.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
README.md
ROADMAP.md
SECURITY.md
</directory_structure>

<files>
This section contains the contents of the repository's files.

<file path=".claude/commands/commit-and-pr.md">
Let's commit the changes. Run tests, typechecks, and format checks. Then commit, push, and create a pull request.
</file>

<file path=".github/ISSUE_TEMPLATE/bug_report.md">
---
name: Bug report
about: Create a report to help us improve
title: ""
labels: bug
assignees: ""
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:

1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Workflow yml file**
If it's not sensitive, consider including a paste of your full Claude workflow.yml file.

**API Provider**

[ ] Anthropic First-Party API (default)
[ ] AWS Bedrock
[ ] GCP Vertex

**Additional context**
Add any other context about the problem here.
</file>

<file path="CODE_OF_CONDUCT.md">
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
- Giving and gracefully accepting constructive feedback
- Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
- Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

- The use of sexualized language or imagery, and sexual attention or
  advances of any kind
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or email
  address, without their explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
claude-code-action-coc@anthropic.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.
</file>

<file path="CONTRIBUTING.md">
# Contributing to Claude Code Action

Thank you for your interest in contributing to Claude Code Action! This document provides guidelines and instructions for contributing to the project.

## Getting Started

### Prerequisites

- [Bun](https://bun.sh/) runtime
- [Docker](https://www.docker.com/) (for running GitHub Actions locally)
- [act](https://github.com/nektos/act) (installed automatically by our test script)
- An Anthropic API key (for testing)

### Setup

1. Fork the repository on GitHub and clone your fork:

   ```bash
   git clone https://github.com/your-username/claude-code-action.git
   cd claude-code-action
   ```

2. Install dependencies:

   ```bash
   bun install
   ```

3. Set up your Anthropic API key:
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

## Development

### Available Scripts

- `bun test` - Run all tests
- `bun run typecheck` - Type check the code
- `bun run format` - Format code with Prettier
- `bun run format:check` - Check code formatting

## Testing

### Running Tests Locally

1. **Unit Tests**:

   ```bash
   bun test
   ```

## Pull Request Process

1. Create a new branch from `main`:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:

   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

3. Run tests and formatting:

   ```bash
   bun test
   bun run typecheck
   bun run format:check
   ```

4. Push your branch and create a Pull Request:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Ensure all CI checks pass

6. Request review from maintainers

## Action Development

### Testing Your Changes

When modifying the action:

1. Test in a real GitHub Actions workflow by:
   - Creating a test repository
   - Using your branch as the action source:
     ```yaml
     uses: your-username/claude-code-action@your-branch
     ```

### Debugging

- Use `console.log` for debugging in development
- Check GitHub Actions logs for runtime issues
- Use `act` with `-v` flag for verbose output:
  ```bash
  act push -v --secret ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY"
  ```

## Common Issues

### Docker Issues

Make sure Docker is running before using `act`. You can check with:

```bash
docker ps
```
</file>

<file path="SECURITY.md">
# Security Policy

Thank you for helping us keep this action and the systems they interact with secure.

## Reporting Security Issues

This repository is maintained by [Anthropic](https://www.anthropic.com/).

The security of our systems and user data is Anthropic’s top priority. We appreciate the work of security researchers acting in good faith in identifying and reporting potential vulnerabilities.

Our security program is managed on HackerOne and we ask that any validated vulnerability in this functionality be reported through their [submission form](https://hackerone.com/anthropic-vdp/reports/new?type=team&report_type=vulnerability).

## Vulnerability Disclosure Program

Our Vulnerability Program Guidelines are defined on our [HackerOne program page](https://hackerone.com/anthropic-vdp).
</file>

<file path="base-action/CLAUDE.md">
# CLAUDE.md

## Common Commands

### Development Commands

- Build/Type check: `bun run typecheck`
- Format code: `bun run format`
- Check formatting: `bun run format:check`
- Run tests: `bun test`
- Install dependencies: `bun install`

### Action Testing

- Test action locally: `./test-local.sh`
- Test specific file: `bun test test/prepare-prompt.test.ts`

## Architecture Overview

This is a GitHub Action that allows running Claude Code within GitHub workflows. The action consists of:

### Core Components

1. **Action Definition** (`action.yml`): Defines inputs, outputs, and the composite action steps
2. **Prompt Preparation** (`src/index.ts`): Runs Claude Code with specified arguments

### Key Design Patterns

- Uses Bun runtime for development and execution
- Named pipes for IPC between prompt input and Claude process
- JSON streaming output format for execution logs
- Composite action pattern to orchestrate multiple steps
- Provider-agnostic design supporting Anthropic API, AWS Bedrock, and Google Vertex AI

## Provider Authentication

1. **Anthropic API** (default): Requires API key via `anthropic_api_key` input
2. **AWS Bedrock**: Uses OIDC authentication when `use_bedrock: true`
3. **Google Vertex AI**: Uses OIDC authentication when `use_vertex: true`

## Testing Strategy

### Local Testing

- Use `act` tool to run GitHub Actions workflows locally
- `test-local.sh` script automates local testing setup
- Requires `ANTHROPIC_API_KEY` environment variable

### Test Structure

- Unit tests for configuration logic
- Integration tests for prompt preparation
- Full workflow tests in `.github/workflows/test-action.yml`

## Important Technical Details

- Uses `mkfifo` to create named pipes for prompt input
- Outputs execution logs as JSON to `/tmp/claude-execution-output.json`
- Timeout enforcement via `timeout` command wrapper
- Strict TypeScript configuration with Bun-specific settings
</file>

<file path="base-action/CODE_OF_CONDUCT.md">
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
- Giving and gracefully accepting constructive feedback
- Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
- Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

- The use of sexualized language or imagery, and sexual attention or
  advances of any kind
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or email
  address, without their explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
claude-code-action-coc@anthropic.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.
</file>

<file path="base-action/CONTRIBUTING.md">
# Contributing to Claude Code Base Action

Thank you for your interest in contributing to Claude Code Base Action! This document provides guidelines and instructions for contributing to the project.

## Getting Started

### Prerequisites

- [Bun](https://bun.sh/) runtime
- [Docker](https://www.docker.com/) (for running GitHub Actions locally)
- [act](https://github.com/nektos/act) (installed automatically by our test script)
- An Anthropic API key (for testing)

### Setup

1. Fork the repository on GitHub and clone your fork:

   ```bash
   git clone https://github.com/your-username/claude-code-base-action.git
   cd claude-code-base-action
   ```

2. Install dependencies:

   ```bash
   bun install
   ```

3. Set up your Anthropic API key:
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

## Development

### Available Scripts

- `bun test` - Run all tests
- `bun run typecheck` - Type check the code
- `bun run format` - Format code with Prettier
- `bun run format:check` - Check code formatting

## Testing

### Running Tests Locally

1. **Unit Tests**:

   ```bash
   bun test
   ```

2. **Integration Tests** (using GitHub Actions locally):

   ```bash
   ./test-local.sh
   ```

   This script:

   - Installs `act` if not present (requires Homebrew on macOS)
   - Runs the GitHub Action workflow locally using Docker
   - Requires your `ANTHROPIC_API_KEY` to be set

   On Apple Silicon Macs, the script automatically adds the `--container-architecture linux/amd64` flag to avoid compatibility issues.

## Pull Request Process

1. Create a new branch from `main`:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:

   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

3. Run tests and formatting:

   ```bash
   bun test
   bun run typecheck
   bun run format:check
   ```

4. Push your branch and create a Pull Request:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Ensure all CI checks pass

6. Request review from maintainers

## Action Development

### Testing Your Changes

When modifying the action:

1. Test locally with the test script:

   ```bash
   ./test-local.sh
   ```

2. Test in a real GitHub Actions workflow by:
   - Creating a test repository
   - Using your branch as the action source:
     ```yaml
     uses: your-username/claude-code-base-action@your-branch
     ```

### Debugging

- Use `console.log` for debugging in development
- Check GitHub Actions logs for runtime issues
- Use `act` with `-v` flag for verbose output:
  ```bash
  act push -v --secret ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY"
  ```

## Common Issues

### Docker Issues

Make sure Docker is running before using `act`. You can check with:

```bash
docker ps
```
</file>

<file path="base-action/MIRROR_DISCLAIMER.md">
# ⚠️ This is a Mirror Repository

This repository is an automated mirror of the `base-action` directory from [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action).

**Do not submit PRs or issues to this repository.** Instead, please contribute to the main repository:

- 🐛 [Report issues](https://github.com/anthropics/claude-code-action/issues)
- 🔧 [Submit pull requests](https://github.com/anthropics/claude-code-action/pulls)
- 📖 [View documentation](https://github.com/anthropics/claude-code-action#readme)

---
</file>

<file path="docs/capabilities-and-limitations.md">
# Capabilities and Limitations

## What Claude Can Do

- **Respond in a Single Comment**: Claude operates by updating a single initial comment with progress and results
- **Answer Questions**: Analyze code and provide explanations
- **Implement Code Changes**: Make simple to moderate code changes based on requests
- **Prepare Pull Requests**: Creates commits on a branch and links back to a prefilled PR creation page
- **Perform Code Reviews**: Analyze PR changes and provide detailed feedback
- **Smart Branch Handling**:
  - When triggered on an **issue**: Always creates a new branch for the work
  - When triggered on an **open PR**: Always pushes directly to the existing PR branch
  - When triggered on a **closed PR**: Creates a new branch since the original is no longer active
- **View GitHub Actions Results**: Can access workflow runs, job logs, and test results on the PR where it's tagged when `actions: read` permission is configured (see [Additional Permissions for CI/CD Integration](./configuration.md#additional-permissions-for-cicd-integration))

## What Claude Cannot Do

- **Submit PR Reviews**: Claude cannot submit formal GitHub PR reviews
- **Approve PRs**: For security reasons, Claude cannot approve pull requests
- **Post Multiple Comments**: Claude only acts by updating its initial comment
- **Execute Commands Outside Its Context**: Claude only has access to the repository and PR/issue context it's triggered in
- **Run Arbitrary Bash Commands**: By default, Claude cannot execute Bash commands unless explicitly allowed using the `allowed_tools` configuration
- **Perform Branch Operations**: Cannot merge branches, rebase, or perform other git operations beyond pushing commits

## How It Works

1. **Trigger Detection**: Listens for comments containing the trigger phrase (default: `@claude`) or issue assignment to a specific user
2. **Context Gathering**: Analyzes the PR/issue, comments, code changes
3. **Smart Responses**: Either answers questions or implements changes
4. **Branch Management**: Creates new PRs for human authors, pushes directly for Claude's own PRs
5. **Communication**: Posts updates at every step to keep you informed

This action is built on top of [`anthropics/claude-code-base-action`](https://github.com/anthropics/claude-code-base-action).
</file>

<file path="docs/cloud-providers.md">
# Cloud Providers

You can authenticate with Claude using any of these three methods:

1. Direct Anthropic API (default)
2. Amazon Bedrock with OIDC authentication
3. Google Vertex AI with OIDC authentication

For detailed setup instructions for AWS Bedrock and Google Vertex AI, see the [official documentation](https://docs.anthropic.com/en/docs/claude-code/github-actions#using-with-aws-bedrock-%26-google-vertex-ai).

**Note**:

- Bedrock and Vertex use OIDC authentication exclusively
- AWS Bedrock automatically uses cross-region inference profiles for certain models
- For cross-region inference profile models, you need to request and be granted access to the Claude models in all regions that the inference profile uses

## Model Configuration

Use provider-specific model names based on your chosen provider:

```yaml
# For direct Anthropic API (default)
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    # ... other inputs

# For Amazon Bedrock with OIDC
- uses: anthropics/claude-code-action@beta
  with:
    model: "anthropic.claude-3-7-sonnet-20250219-beta:0" # Cross-region inference
    use_bedrock: "true"
    # ... other inputs

# For Google Vertex AI with OIDC
- uses: anthropics/claude-code-action@beta
  with:
    model: "claude-3-7-sonnet@20250219"
    use_vertex: "true"
    # ... other inputs
```

## OIDC Authentication for Bedrock and Vertex

Both AWS Bedrock and GCP Vertex AI require OIDC authentication.

```yaml
# For AWS Bedrock with OIDC
- name: Configure AWS Credentials (OIDC)
  uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: ${{ secrets.AWS_ROLE_TO_ASSUME }}
    aws-region: us-west-2

- name: Generate GitHub App token
  id: app-token
  uses: actions/create-github-app-token@v2
  with:
    app-id: ${{ secrets.APP_ID }}
    private-key: ${{ secrets.APP_PRIVATE_KEY }}

- uses: anthropics/claude-code-action@beta
  with:
    model: "anthropic.claude-3-7-sonnet-20250219-beta:0"
    use_bedrock: "true"
    # ... other inputs

  permissions:
    id-token: write # Required for OIDC
```

```yaml
# For GCP Vertex AI with OIDC
- name: Authenticate to Google Cloud
  uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
    service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

- name: Generate GitHub App token
  id: app-token
  uses: actions/create-github-app-token@v2
  with:
    app-id: ${{ secrets.APP_ID }}
    private-key: ${{ secrets.APP_PRIVATE_KEY }}

- uses: anthropics/claude-code-action@beta
  with:
    model: "claude-3-7-sonnet@20250219"
    use_vertex: "true"
    # ... other inputs

  permissions:
    id-token: write # Required for OIDC
```
</file>

<file path="docs/custom-automations.md">
# Custom Automations

These examples show how to configure Claude to act automatically based on GitHub events, without requiring manual @mentions.

## Supported GitHub Events

This action supports the following GitHub events ([learn more GitHub event triggers](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)):

- `pull_request` - When PRs are opened or synchronized
- `issue_comment` - When comments are created on issues or PRs
- `pull_request_comment` - When comments are made on PR diffs
- `issues` - When issues are opened or assigned
- `pull_request_review` - When PR reviews are submitted
- `pull_request_review_comment` - When comments are made on PR reviews
- `repository_dispatch` - Custom events triggered via API (coming soon)
- `workflow_dispatch` - Manual workflow triggers (coming soon)

## Automated Documentation Updates

Automatically update documentation when specific files change (see [`examples/claude-pr-path-specific.yml`](../examples/claude-pr-path-specific.yml)):

```yaml
on:
  pull_request:
    paths:
      - "src/api/**/*.ts"

steps:
  - uses: anthropics/claude-code-action@beta
    with:
      direct_prompt: |
        Update the API documentation in README.md to reflect
        the changes made to the API endpoints in this PR.
```

When API files are modified, Claude automatically updates your README with the latest endpoint documentation and pushes the changes back to the PR, keeping your docs in sync with your code.

## Author-Specific Code Reviews

Automatically review PRs from specific authors or external contributors (see [`examples/claude-review-from-author.yml`](../examples/claude-review-from-author.yml)):

```yaml
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review-by-author:
    if: |
      github.event.pull_request.user.login == 'developer1' ||
      github.event.pull_request.user.login == 'external-contributor'
    steps:
      - uses: anthropics/claude-code-action@beta
        with:
          direct_prompt: |
            Please provide a thorough review of this pull request.
            Pay extra attention to coding standards, security practices,
            and test coverage since this is from an external contributor.
```

Perfect for automatically reviewing PRs from new team members, external contributors, or specific developers who need extra guidance.

## Custom Prompt Templates

Use `override_prompt` for complete control over Claude's behavior with variable substitution:

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    override_prompt: |
      Analyze PR #$PR_NUMBER in $REPOSITORY for security vulnerabilities.

      Changed files:
      $CHANGED_FILES

      Focus on:
      - SQL injection risks
      - XSS vulnerabilities
      - Authentication bypasses
      - Exposed secrets or credentials

      Provide severity ratings (Critical/High/Medium/Low) for any issues found.
```

The `override_prompt` feature supports these variables:

- `$REPOSITORY`, `$PR_NUMBER`, `$ISSUE_NUMBER`
- `$PR_TITLE`, `$ISSUE_TITLE`, `$PR_BODY`, `$ISSUE_BODY`
- `$PR_COMMENTS`, `$ISSUE_COMMENTS`, `$REVIEW_COMMENTS`
- `$CHANGED_FILES`, `$TRIGGER_COMMENT`, `$TRIGGER_USERNAME`
- `$BRANCH_NAME`, `$BASE_BRANCH`, `$EVENT_TYPE`, `$IS_PR`
</file>

<file path="docs/setup.md">
# Setup Guide

## Manual Setup (Direct API)

**Requirements**: You must be a repository admin to complete these steps.

1. Install the Claude GitHub app to your repository: https://github.com/apps/claude
2. Add authentication to your repository secrets ([Learn how to use secrets in GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)):
   - Either `ANTHROPIC_API_KEY` for API key authentication
   - Or `CLAUDE_CODE_OAUTH_TOKEN` for OAuth token authentication (Pro and Max users can generate this by running `claude setup-token` locally)
3. Copy the workflow file from [`examples/claude.yml`](../examples/claude.yml) into your repository's `.github/workflows/`

## Using a Custom GitHub App

If you prefer not to install the official Claude app, you can create your own GitHub App to use with this action. This gives you complete control over permissions and access.

**When you may want to use a custom GitHub App:**

- You need more restrictive permissions than the official app
- Organization policies prevent installing third-party apps
- You're using AWS Bedrock or Google Vertex AI

**Steps to create and use a custom GitHub App:**

1. **Create a new GitHub App:**

   - Go to https://github.com/settings/apps (for personal apps) or your organization's settings
   - Click "New GitHub App"
   - Configure the app with these minimum permissions:
     - **Repository permissions:**
       - Contents: Read & Write
       - Issues: Read & Write
       - Pull requests: Read & Write
     - **Account permissions:** None required
   - Set "Where can this GitHub App be installed?" to your preference
   - Create the app

2. **Generate and download a private key:**

   - After creating the app, scroll down to "Private keys"
   - Click "Generate a private key"
   - Download the `.pem` file (keep this secure!)

3. **Install the app on your repository:**

   - Go to the app's settings page
   - Click "Install App"
   - Select the repositories where you want to use Claude

4. **Add the app credentials to your repository secrets:**

   - Go to your repository's Settings → Secrets and variables → Actions
   - Add these secrets:
     - `APP_ID`: Your GitHub App's ID (found in the app settings)
     - `APP_PRIVATE_KEY`: The contents of the downloaded `.pem` file

5. **Update your workflow to use the custom app:**

   ```yaml
   name: Claude with Custom App
   on:
     issue_comment:
       types: [created]
     # ... other triggers

   jobs:
     claude-response:
       runs-on: ubuntu-latest
       steps:
         # Generate a token from your custom app
         - name: Generate GitHub App token
           id: app-token
           uses: actions/create-github-app-token@v1
           with:
             app-id: ${{ secrets.APP_ID }}
             private-key: ${{ secrets.APP_PRIVATE_KEY }}

         # Use Claude with your custom app's token
         - uses: anthropics/claude-code-action@beta
           with:
             anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
             github_token: ${{ steps.app-token.outputs.token }}
             # ... other configuration
   ```

**Important notes:**

- The custom app must have read/write permissions for Issues, Pull Requests, and Contents
- Your app's token will have the exact permissions you configured, nothing more

For more information on creating GitHub Apps, see the [GitHub documentation](https://docs.github.com/en/apps/creating-github-apps).

## Security Best Practices

**⚠️ IMPORTANT: Never commit API keys directly to your repository! Always use GitHub Actions secrets.**

To securely use your Anthropic API key:

1. Add your API key as a repository secret:

   - Go to your repository's Settings
   - Navigate to "Secrets and variables" → "Actions"
   - Click "New repository secret"
   - Name it `ANTHROPIC_API_KEY`
   - Paste your API key as the value

2. Reference the secret in your workflow:
   ```yaml
   anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
   ```

**Never do this:**

```yaml
# ❌ WRONG - Exposes your API key
anthropic_api_key: "sk-ant-..."
```

**Always do this:**

```yaml
# ✅ CORRECT - Uses GitHub secrets
anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

This applies to all sensitive values including API keys, access tokens, and credentials.
We also recommend that you always use short-lived tokens when possible

## Setting Up GitHub Secrets

1. Go to your repository's Settings
2. Click on "Secrets and variables" → "Actions"
3. Click "New repository secret"
4. For authentication, choose one:
   - API Key: Name: `ANTHROPIC_API_KEY`, Value: Your Anthropic API key (starting with `sk-ant-`)
   - OAuth Token: Name: `CLAUDE_CODE_OAUTH_TOKEN`, Value: Your Claude Code OAuth token (Pro and Max users can generate this by running `claude setup-token` locally)
5. Click "Add secret"

### Best Practices for Authentication

1. ✅ Always use `${{ secrets.ANTHROPIC_API_KEY }}` or `${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}` in workflows
2. ✅ Never commit API keys or tokens to version control
3. ✅ Regularly rotate your API keys and tokens
4. ✅ Use environment secrets for organization-wide access
5. ❌ Never share API keys or tokens in pull requests or issues
6. ❌ Avoid logging workflow variables that might contain keys
</file>

<file path="test/fixtures/sample-turns-expected-output.md">
## Claude Code Report

## 🚀 System Initialization

**Available Tools:** 8 tools loaded

---

I'll help you with this task. Let me start by examining the file to understand what needs to be changed.

### 🔧 `Read`

**Parameters:**
```json
{
  "file_path": "/path/to/sample/file.py"
}
```

**Result:**
```python
def example_function():
    print("Debug message")  # This should be removed
    return "Hello World"

if __name__ == "__main__":
    result = example_function()
    print(result)
```

*Token usage: 150 input, 75 output*

---

I can see the debug print statement that needs to be removed. Let me fix this by editing the file.

### 🔧 `Edit`

**Parameters:**
```json
{
  "file_path": "/path/to/sample/file.py",
  "old_string": "def example_function():\n    print(\"Debug message\")  # This should be removed\n    return \"Hello World\"",
  "new_string": "def example_function():\n    return \"Hello World\""
}
```

**→** File successfully edited. The debug print statement has been removed.

*Token usage: 300 input, 50 output*

---

Perfect! I've successfully removed the debug print statement from the function. Let me now create a pull request comment to document this change.

### 🔧 `mcp__github__add_pull_request_review_comment`

**Parameters:**
```json
{
  "owner": "example-org",
  "repo": "example-repo",
  "pull_number": 123,
  "body": "Removed debug print statement as requested.",
  "commit_id": "abc123def456",
  "path": "sample/file.py",
  "line": 2
}
```

**→** Successfully posted review comment to PR #123

*Token usage: 225 input, 80 output*

---

Great! I've successfully completed the requested task:

1. ✅ Located the debug print statement in the file
2. ✅ Removed the print statement while preserving the function logic
3. ✅ Added a review comment documenting the change

The debug print statement has been removed as requested by the reviewers.

*Token usage: 270 input, 60 output*

---

## ✅ Final Result

Successfully removed debug print statement from file and added review comment to document the change.

**Cost:** $0.0347 | **Duration:** 18.8s
</file>

<file path="ROADMAP.md">
# Claude Code GitHub Action Roadmap

Thank you for trying out the beta of our GitHub Action! This document outlines our path to `v1.0`. Items are not necessarily in priority order.

## Path to 1.0

- ~**Ability to see GitHub Action CI results** - This will enable Claude to look at CI failures and make updates to PRs to fix test failures, lint errors, and the like.~
- **Cross-repo support** - Enable Claude to work across multiple repositories in a single session
- **Ability to modify workflow files** - Let Claude update GitHub Actions workflows and other CI configuration files
- **Support for workflow_dispatch and repository_dispatch events** - Dispatch Claude on events triggered via API from other workflows or from other services
- **Ability to disable commit signing** - Option to turn off GPG signing for environments where it's not required. This will enable Claude to use normal `git` bash commands for committing. This will likely become the default behavior once added.
- **Better code review behavior** - Support inline comments on specific lines, provide higher quality reviews with more actionable feedback
- ~**Support triggering @claude from bot users** - Allow automation and bot accounts to invoke Claude~
- **Customizable base prompts** - Full control over Claude's initial context with template variables like `$PR_COMMENTS`, `$PR_FILES`, etc. Users can replace our default prompt entirely while still accessing key contextual data

---

**Note:** This roadmap represents our current vision for reaching `v1.0` and is subject to change based on user feedback and development priorities.

We welcome feedback on these planned features! If you're interested in contributing to any of these features, please open an issue to discuss implementation details with us. We're also open to suggestions for new features not listed here.
</file>

<file path="base-action/README.md">
# Claude Code Base Action

This GitHub Action allows you to run [Claude Code](https://www.anthropic.com/claude-code) within your GitHub Actions workflows. You can use this to build any custom workflow on top of Claude Code.

For simply tagging @claude in issues and PRs out of the box, [check out the Claude Code action and GitHub app](https://github.com/anthropics/claude-code-action).

## Usage

Add the following to your workflow file:

```yaml
# Using a direct prompt
- name: Run Claude Code with direct prompt
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Or using a prompt from a file
- name: Run Claude Code with prompt file
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt_file: "/path/to/prompt.txt"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Or limiting the conversation turns
- name: Run Claude Code with limited turns
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    max_turns: "5" # Limit conversation to 5 turns
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Using custom system prompts
- name: Run Claude Code with custom system prompt
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Build a REST API"
    system_prompt: "You are a senior backend engineer. Focus on security, performance, and maintainability."
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Or appending to the default system prompt
- name: Run Claude Code with appended system prompt
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Create a database schema"
    append_system_prompt: "After writing code, be sure to code review yourself."
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Using custom environment variables
- name: Run Claude Code with custom environment variables
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Deploy to staging environment"
    claude_env: |
      ENVIRONMENT: staging
      API_URL: https://api-staging.example.com
      DEBUG: true
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Using fallback model for handling API errors
- name: Run Claude Code with fallback model
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Review and fix TypeScript errors"
    model: "claude-opus-4-1-20250805"
    fallback_model: "claude-sonnet-4-20250514"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Using OAuth token instead of API key
- name: Run Claude Code with OAuth token
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Update dependencies"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
```

## Inputs

| Input                     | Description                                                                                       | Required | Default                      |
| ------------------------- | ------------------------------------------------------------------------------------------------- | -------- | ---------------------------- |
| `prompt`                  | The prompt to send to Claude Code                                                                 | No\*     | ''                           |
| `prompt_file`             | Path to a file containing the prompt to send to Claude Code                                       | No\*     | ''                           |
| `allowed_tools`           | Comma-separated list of allowed tools for Claude Code to use                                      | No       | ''                           |
| `disallowed_tools`        | Comma-separated list of disallowed tools that Claude Code cannot use                              | No       | ''                           |
| `max_turns`               | Maximum number of conversation turns (default: no limit)                                          | No       | ''                           |
| `mcp_config`              | Path to the MCP configuration JSON file, or MCP configuration JSON string                         | No       | ''                           |
| `settings`                | Path to Claude Code settings JSON file, or settings JSON string                                   | No       | ''                           |
| `system_prompt`           | Override system prompt                                                                            | No       | ''                           |
| `append_system_prompt`    | Append to system prompt                                                                           | No       | ''                           |
| `claude_env`              | Custom environment variables to pass to Claude Code execution (YAML multiline format)             | No       | ''                           |
| `model`                   | Model to use (provider-specific format required for Bedrock/Vertex)                               | No       | 'claude-4-0-sonnet-20250219' |
| `anthropic_model`         | DEPRECATED: Use 'model' instead                                                                   | No       | 'claude-4-0-sonnet-20250219' |
| `fallback_model`          | Enable automatic fallback to specified model when default model is overloaded                     | No       | ''                           |
| `timeout_minutes`         | Timeout in minutes for Claude Code execution                                                      | No       | '10'                         |
| `anthropic_api_key`       | Anthropic API key (required for direct Anthropic API)                                             | No       | ''                           |
| `claude_code_oauth_token` | Claude Code OAuth token (alternative to anthropic_api_key)                                        | No       | ''                           |
| `use_bedrock`             | Use Amazon Bedrock with OIDC authentication instead of direct Anthropic API                       | No       | 'false'                      |
| `use_vertex`              | Use Google Vertex AI with OIDC authentication instead of direct Anthropic API                     | No       | 'false'                      |
| `use_node_cache`          | Whether to use Node.js dependency caching (set to true only for Node.js projects with lock files) | No       | 'false'                      |

\*Either `prompt` or `prompt_file` must be provided, but not both.

## Outputs

| Output           | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| `conclusion`     | Execution status of Claude Code ('success' or 'failure')   |
| `execution_file` | Path to the JSON file containing Claude Code execution log |

## Environment Variables

The following environment variables can be used to configure the action:

| Variable       | Description                                           | Default |
| -------------- | ----------------------------------------------------- | ------- |
| `NODE_VERSION` | Node.js version to use (e.g., '18.x', '20.x', '22.x') | '18.x'  |

Example usage:

```yaml
- name: Run Claude Code with Node.js 20
  uses: anthropics/claude-code-base-action@beta
  env:
    NODE_VERSION: "20.x"
  with:
    prompt: "Your prompt here"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Custom Environment Variables

You can pass custom environment variables to Claude Code execution using the `claude_env` input. This allows Claude to access environment-specific configuration during its execution.

The `claude_env` input accepts YAML multiline format with key-value pairs:

```yaml
- name: Deploy with custom environment
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Deploy the application to the staging environment"
    claude_env: |
      ENVIRONMENT: staging
      API_BASE_URL: https://api-staging.example.com
      DATABASE_URL: ${{ secrets.STAGING_DB_URL }}
      DEBUG: true
      LOG_LEVEL: debug
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Features:

- **YAML Format**: Use standard YAML key-value syntax (`KEY: value`)
- **Multiline Support**: Define multiple environment variables in a single input
- **Comments**: Lines starting with `#` are ignored
- **GitHub Secrets**: Can reference GitHub secrets using `${{ secrets.SECRET_NAME }}`
- **Runtime Access**: Environment variables are available to Claude during execution

### Example Use Cases:

```yaml
# Development configuration
claude_env: |
  NODE_ENV: development
  API_URL: http://localhost:3000
  DEBUG: true

# Production deployment
claude_env: |
  NODE_ENV: production
  API_URL: https://api.example.com
  DATABASE_URL: ${{ secrets.PROD_DB_URL }}
  REDIS_URL: ${{ secrets.REDIS_URL }}

# Feature flags and configuration
claude_env: |
  FEATURE_NEW_UI: enabled
  MAX_RETRIES: 3
  TIMEOUT_MS: 5000
```

## Using Settings Configuration

You can provide Claude Code settings configuration in two ways:

### Option 1: Settings Configuration File

Provide a path to a JSON file containing Claude Code settings:

```yaml
- name: Run Claude Code with settings file
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    settings: "path/to/settings.json"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Option 2: Inline Settings Configuration

Provide the settings configuration directly as a JSON string:

```yaml
- name: Run Claude Code with inline settings
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    settings: |
      {
        "model": "claude-opus-4-1-20250805",
        "env": {
          "DEBUG": "true",
          "API_URL": "https://api.example.com"
        },
        "permissions": {
          "allow": ["Bash", "Read"],
          "deny": ["WebFetch"]
        },
        "hooks": {
          "PreToolUse": [{
            "matcher": "Bash",
            "hooks": [{
              "type": "command",
              "command": "echo Running bash command..."
            }]
          }]
        }
      }
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

The settings file supports all Claude Code settings options including:

- `model`: Override the default model
- `env`: Environment variables for the session
- `permissions`: Tool usage permissions
- `hooks`: Pre/post tool execution hooks
- `includeCoAuthoredBy`: Include co-authored-by in git commits
- And more...

**Note**: The `enableAllProjectMcpServers` setting is always set to `true` by this action to ensure MCP servers work correctly.

## Using MCP Config

You can provide MCP configuration in two ways:

### Option 1: MCP Configuration File

Provide a path to a JSON file containing MCP configuration:

```yaml
- name: Run Claude Code with MCP config file
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    mcp_config: "path/to/mcp-config.json"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Option 2: Inline MCP Configuration

Provide the MCP configuration directly as a JSON string:

```yaml
- name: Run Claude Code with inline MCP config
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    mcp_config: |
      {
        "mcpServers": {
          "server-name": {
            "command": "node",
            "args": ["./server.js"],
            "env": {
              "API_KEY": "your-api-key"
            }
          }
        }
      }
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

The MCP config file should follow this format:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "node",
      "args": ["./server.js"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

You can combine MCP config with other inputs like allowed tools:

```yaml
# Using multiple inputs together
- name: Run Claude Code with MCP and custom tools
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Access the custom MCP server and use its tools"
    mcp_config: "mcp-config.json"
    allowed_tools: "Bash(git:*),View,mcp__server-name__custom_tool"
    timeout_minutes: "15"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Example: PR Code Review

```yaml
name: Claude Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  code-review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run Code Review with Claude
        id: code-review
        uses: anthropics/claude-code-base-action@beta
        with:
          prompt: "Review the PR changes. Focus on code quality, potential bugs, and performance issues. Suggest improvements where appropriate. Write your review as markdown text."
          allowed_tools: "Bash(git diff --name-only HEAD~1),Bash(git diff HEAD~1),View,GlobTool,GrepTool,Write"
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

      - name: Extract and Comment PR Review
        if: steps.code-review.outputs.conclusion == 'success'
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          script: |
            const fs = require('fs');
            const executionFile = '${{ steps.code-review.outputs.execution_file }}';
            const executionLog = JSON.parse(fs.readFileSync(executionFile, 'utf8'));

            // Extract the review content from the execution log
            // The execution log contains the full conversation including Claude's responses
            let review = '';

            // Find the last assistant message which should contain the review
            for (let i = executionLog.length - 1; i >= 0; i--) {
              if (executionLog[i].role === 'assistant') {
                review = executionLog[i].content;
                break;
              }
            }

            if (review) {
              github.rest.issues.createComment({
                issue_number: context.issue.number,
                owner: context.repo.owner,
                repo: context.repo.repo,
                body: "## Claude Code Review\n\n" + review + "\n\n*Generated by Claude Code*"
              });
            }
```

Check out additional examples in [`./examples`](./examples).

## Using Cloud Providers

You can authenticate with Claude using any of these methods:

1. Direct Anthropic API (default) - requires API key or OAuth token
2. Amazon Bedrock - requires OIDC authentication and automatically uses cross-region inference profiles
3. Google Vertex AI - requires OIDC authentication

**Note**:

- Bedrock and Vertex use OIDC authentication exclusively
- AWS Bedrock automatically uses cross-region inference profiles for certain models
- For cross-region inference profile models, you need to request and be granted access to the Claude models in all regions that the inference profile uses
- The Bedrock API endpoint URL is automatically constructed using the AWS_REGION environment variable (e.g., `https://bedrock-runtime.us-west-2.amazonaws.com`)
- You can override the Bedrock API endpoint URL by setting the `ANTHROPIC_BEDROCK_BASE_URL` environment variable

### Model Configuration

Use provider-specific model names based on your chosen provider:

```yaml
# For direct Anthropic API (default)
- name: Run Claude Code with Anthropic API
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    model: "claude-3-7-sonnet-20250219"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# For Amazon Bedrock (requires OIDC authentication)
- name: Configure AWS Credentials (OIDC)
  uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: ${{ secrets.AWS_ROLE_TO_ASSUME }}
    aws-region: us-west-2

- name: Run Claude Code with Bedrock
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    model: "anthropic.claude-3-7-sonnet-20250219-v1:0"
    use_bedrock: "true"

# For Google Vertex AI (requires OIDC authentication)
- name: Authenticate to Google Cloud
  uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
    service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

- name: Run Claude Code with Vertex AI
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    model: "claude-3-7-sonnet@20250219"
    use_vertex: "true"
```

## Example: Using OIDC Authentication for AWS Bedrock

This example shows how to use OIDC authentication with AWS Bedrock:

```yaml
- name: Configure AWS Credentials (OIDC)
  uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: ${{ secrets.AWS_ROLE_TO_ASSUME }}
    aws-region: us-west-2

- name: Run Claude Code with AWS OIDC
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    use_bedrock: "true"
    model: "anthropic.claude-3-7-sonnet-20250219-v1:0"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
```

## Example: Using OIDC Authentication for GCP Vertex AI

This example shows how to use OIDC authentication with GCP Vertex AI:

```yaml
- name: Authenticate to Google Cloud
  uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
    service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

- name: Run Claude Code with GCP OIDC
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    use_vertex: "true"
    model: "claude-3-7-sonnet@20250219"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
```

## Security Best Practices

**⚠️ IMPORTANT: Never commit API keys directly to your repository! Always use GitHub Actions secrets.**

To securely use your Anthropic API key:

1. Add your API key as a repository secret:

   - Go to your repository's Settings
   - Navigate to "Secrets and variables" → "Actions"
   - Click "New repository secret"
   - Name it `ANTHROPIC_API_KEY`
   - Paste your API key as the value

2. Reference the secret in your workflow:
   ```yaml
   anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
   ```

**Never do this:**

```yaml
# ❌ WRONG - Exposes your API key
anthropic_api_key: "sk-ant-..."
```

**Always do this:**

```yaml
# ✅ CORRECT - Uses GitHub secrets
anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

This applies to all sensitive values including API keys, access tokens, and credentials.
We also recommend that you always use short-lived tokens when possible

## License

This project is licensed under the MIT License—see the LICENSE file for details.
</file>

<file path="docs/experimental.md">
# Experimental Features

**Note:** Experimental features are considered unstable and not supported for production use. They may change or be removed at any time.

## Execution Modes

The action supports three execution modes, each optimized for different use cases:

### Tag Mode (Default)

The traditional implementation mode that responds to @claude mentions, issue assignments, or labels.

- **Triggers**: `@claude` mentions, issue assignment, label application
- **Features**: Creates tracking comments with progress checkboxes, full implementation capabilities
- **Use case**: General-purpose code implementation and Q&A

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    # mode: tag is the default
```

### Agent Mode

**Note: Agent mode is currently in active development and may undergo breaking changes.**

For automation with workflow_dispatch and scheduled events only.

- **Triggers**: Only works with `workflow_dispatch` and `schedule` events - does NOT work with PR/issue events
- **Features**: Perfect for scheduled tasks, works with `override_prompt`
- **Use case**: Maintenance tasks, automated reporting, scheduled checks

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    mode: agent
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    override_prompt: |
      Check for outdated dependencies and create an issue if any are found.
```

### Experimental Review Mode

**Warning: This is an experimental feature that may change or be removed at any time.**

For automated code reviews on pull requests.

- **Triggers**: Pull request events (`opened`, `synchronize`) or `@claude review` comments
- **Features**: Provides detailed code reviews with inline comments and suggestions
- **Use case**: Automated PR reviews, code quality checks

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    mode: experimental-review
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    custom_instructions: |
      Focus on code quality, security, and best practices.
```

See [`examples/claude-modes.yml`](../examples/claude-modes.yml) and [`examples/claude-experimental-review-mode.yml`](../examples/claude-experimental-review-mode.yml) for complete examples of each mode.

## Network Restrictions

For enhanced security, you can restrict Claude's network access to specific domains only. This feature is particularly useful for:

- Enterprise environments with strict security policies
- Preventing access to external services
- Limiting Claude to only your internal APIs and services

When `experimental_allowed_domains` is set, Claude can only access the domains you explicitly list. You'll need to include the appropriate provider domains based on your authentication method.

### Provider-Specific Examples

#### If using Anthropic API or subscription

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    # Or: claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
    experimental_allowed_domains: |
      .anthropic.com
```

#### If using AWS Bedrock

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    use_bedrock: "true"
    experimental_allowed_domains: |
      bedrock.*.amazonaws.com
      bedrock-runtime.*.amazonaws.com
```

#### If using Google Vertex AI

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    use_vertex: "true"
    experimental_allowed_domains: |
      *.googleapis.com
      vertexai.googleapis.com
```

### Common GitHub Domains

In addition to your provider domains, you may need to include GitHub-related domains. For GitHub.com users, common domains include:

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    experimental_allowed_domains: |
      .anthropic.com  # For Anthropic API
      .github.com
      .githubusercontent.com
      ghcr.io
      .blob.core.windows.net
```

For GitHub Enterprise users, replace the GitHub.com domains above with your enterprise domains (e.g., `.github.company.com`, `packages.company.com`, etc.).

To determine which domains your workflow needs, you can temporarily run without restrictions and monitor the network requests, or check your GitHub Enterprise configuration for the specific services you use.
</file>

<file path="docs/faq.md">
# Frequently Asked Questions (FAQ)

This FAQ addresses common questions and gotchas when using the Claude Code GitHub Action.

## Triggering and Authentication

### Why doesn't tagging @claude from my automated workflow work?

The `github-actions` user cannot trigger subsequent GitHub Actions workflows. This is a GitHub security feature to prevent infinite loops. To make this work, you need to use a Personal Access Token (PAT) instead, which will act as a regular user, or use a separate app token of your own. When posting a comment on an issue or PR from your workflow, use your PAT instead of the `GITHUB_TOKEN` generated in your workflow.

### Why does Claude say I don't have permission to trigger it?

Only users with **write permissions** to the repository can trigger Claude. This is a security feature to prevent unauthorized use. Make sure the user commenting has at least write access to the repository.

### Why can't I assign @claude to an issue on my repository?

If you're in a public repository, you should be able to assign to Claude without issue. If it's a private organization repository, you can only assign to users in your own organization, which Claude isn't. In this case, you'll need to make a custom user in that case.

### Why am I getting OIDC authentication errors?

If you're using the default GitHub App authentication, you must add the `id-token: write` permission to your workflow:

```yaml
permissions:
  contents: read
  id-token: write # Required for OIDC authentication
```

The OIDC token is required in order for the Claude GitHub app to function. If you wish to not use the GitHub app, you can instead provide a `github_token` input to the action for Claude to operate with. See the [Claude Code permissions documentation][perms] for more.

## Claude's Capabilities and Limitations

### Why won't Claude update workflow files when I ask it to?

The GitHub App for Claude doesn't have workflow write access for security reasons. This prevents Claude from modifying CI/CD configurations that could potentially create unintended consequences. This is something we may reconsider in the future.

### Why won't Claude rebase my branch?

By default, Claude only uses commit tools for non-destructive changes to the branch. Claude is configured to:

- Never push to branches other than where it was invoked (either its own branch or the PR branch)
- Never force push or perform destructive operations

You can grant additional tools via the `allowed_tools` input if needed:

```yaml
allowed_tools: "Bash(git rebase:*)" # Use with caution
```

### Why won't Claude create a pull request?

Claude doesn't create PRs by default. Instead, it pushes commits to a branch and provides a link to a pre-filled PR submission page. This approach ensures your repository's branch protection rules are still adhered to and gives you final control over PR creation.

### Can Claude see my GitHub Actions CI results?

Yes! Claude can access GitHub Actions workflow runs, job logs, and test results on the PR where it's tagged. To enable this:

1. Add `actions: read` permission to your workflow:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
     issues: write
     actions: read
   ```

2. Configure the action with additional permissions:
   ```yaml
   - uses: anthropics/claude-code-action@beta
     with:
       additional_permissions: |
         actions: read
   ```

Claude will then be able to analyze CI failures and help debug workflow issues. For running tests locally before commits, you can still instruct Claude to do so in your request.

### Why does Claude only update one comment instead of creating new ones?

Claude is configured to update a single comment to avoid cluttering PR/issue discussions. All of Claude's responses, including progress updates and final results, will appear in the same comment with checkboxes showing task progress.

## Branch and Commit Behavior

### Why did Claude create a new branch when commenting on a closed PR?

Claude's branch behavior depends on the context:

- **Open PRs**: Pushes directly to the existing PR branch
- **Closed/Merged PRs**: Creates a new branch (cannot push to closed PR branches)
- **Issues**: Always creates a new branch with a timestamp

### Why are my commits shallow/missing history?

For performance, Claude uses shallow clones:

- PRs: `--depth=20` (last 20 commits)
- New branches: `--depth=1` (single commit)

If you need full history, you can configure this in your workflow before calling Claude in the `actions/checkout` step.

```
- uses: actions/checkout@v4
  depth: 0 # will fetch full repo history
```

## Configuration and Tools

### What's the difference between `direct_prompt` and `custom_instructions`?

These inputs serve different purposes in how Claude responds:

- **`direct_prompt`**: Bypasses trigger detection entirely. When provided, Claude executes this exact instruction regardless of comments or mentions. Perfect for automated workflows where you want Claude to perform a specific task on every run (e.g., "Update the API documentation based on changes in this PR").

- **`custom_instructions`**: Additional context added to Claude's system prompt while still respecting normal triggers. These instructions modify Claude's behavior but don't replace the triggering comment. Use this to give Claude standing instructions like "You have been granted additional tools for ...".

Example:

```yaml
# Using direct_prompt - runs automatically without @claude mention
direct_prompt: "Review this PR for security vulnerabilities"

# Using custom_instructions - still requires @claude trigger
custom_instructions: "Focus on performance implications and suggest optimizations"
```

### Why doesn't Claude execute my bash commands?

The Bash tool is **disabled by default** for security. To enable individual bash commands:

```yaml
allowed_tools: "Bash(npm:*),Bash(git:*)" # Allows only npm and git commands
```

### Can Claude work across multiple repositories?

No, Claude's GitHub app token is sandboxed to the current repository only. It cannot push to any other repositories. It can, however, read public repositories, but to get access to this, you must configure it with tools to do so.

### Why aren't comments posted as claude[bot]?

Comments appear as claude[bot] when the action uses its built-in authentication. However, if you provide a `github_token` in your workflow, the action will use that token's authentication instead, causing comments to appear under a different username.

**Solution**: Remove `github_token` from your workflow file unless you're using a custom GitHub App.

**Note**: The `use_sticky_comment` feature only works with claude[bot] authentication. If you're using a custom `github_token`, sticky comments won't update properly since they expect the claude[bot] username.

## MCP Servers and Extended Functionality

### What MCP servers are available by default?

Claude Code Action automatically configures two MCP servers:

1. **GitHub MCP server**: For GitHub API operations
2. **File operations server**: For advanced file manipulation

However, tools from these servers still need to be explicitly allowed via `allowed_tools`.

## Troubleshooting

### How can I debug what Claude is doing?

Check the GitHub Action log for Claude's run for the full execution trace.

### Why can't I trigger Claude with `@claude-mention` or `claude!`?

The trigger uses word boundaries, so `@claude` must be a complete word. Variations like `@claude-bot`, `@claude!`, or `claude@mention` won't work unless you customize the `trigger_phrase`.

## Best Practices

1. **Always specify permissions explicitly** in your workflow file
2. **Use GitHub Secrets** for API keys - never hardcode them
3. **Be specific with `allowed_tools`** - only enable what's necessary
4. **Test in a separate branch** before using on important PRs
5. **Monitor Claude's token usage** to avoid hitting API limits
6. **Review Claude's changes** carefully before merging

## Getting Help

If you encounter issues not covered here:

1. Check the [GitHub Issues](https://github.com/anthropics/claude-code-action/issues)
2. Review the [example workflows](https://github.com/anthropics/claude-code-action#examples)

[perms]: https://docs.anthropic.com/en/docs/claude-code/settings#permissions
</file>

<file path="docs/security.md">
# Security

## Access Control

- **Repository Access**: The action can only be triggered by users with write access to the repository
- **Bot User Control**: By default, GitHub Apps and bots cannot trigger this action for security reasons. Use the `allowed_bots` parameter to enable specific bots or all bots
- **Token Permissions**: The GitHub app receives only a short-lived token scoped specifically to the repository it's operating in
- **No Cross-Repository Access**: Each action invocation is limited to the repository where it was triggered
- **Limited Scope**: The token cannot access other repositories or perform actions beyond the configured permissions

## GitHub App Permissions

The [Claude Code GitHub app](https://github.com/apps/claude) requires these permissions:

- **Pull Requests**: Read and write to create PRs and push changes
- **Issues**: Read and write to respond to issues
- **Contents**: Read and write to modify repository files

## Commit Signing

All commits made by Claude through this action are automatically signed with commit signatures. This ensures the authenticity and integrity of commits, providing a verifiable trail of changes made by the action.

## ⚠️ Authentication Protection

**CRITICAL: Never hardcode your Anthropic API key or OAuth token in workflow files!**

Your authentication credentials must always be stored in GitHub secrets to prevent unauthorized access:

```yaml
# CORRECT ✅
anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
# OR
claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}

# NEVER DO THIS ❌
anthropic_api_key: "sk-ant-api03-..." # Exposed and vulnerable!
claude_code_oauth_token: "oauth_token_..." # Exposed and vulnerable!
```
</file>

<file path="CLAUDE.md">
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Tools

- Runtime: Bun 1.2.11
- TypeScript with strict configuration

## Common Development Tasks

### Available npm/bun scripts from package.json:

```bash
# Test
bun test

# Formatting
bun run format          # Format code with prettier
bun run format:check    # Check code formatting

# Type checking
bun run typecheck       # Run TypeScript type checker
```

## Architecture Overview

This is a GitHub Action that enables Claude to interact with GitHub PRs and issues. The action operates in two main phases:

### Phase 1: Preparation (`src/entrypoints/prepare.ts`)

1. **Authentication Setup**: Establishes GitHub token via OIDC or GitHub App
2. **Permission Validation**: Verifies actor has write permissions
3. **Trigger Detection**: Uses mode-specific logic to determine if Claude should respond
4. **Context Creation**: Prepares GitHub context and initial tracking comment

### Phase 2: Execution (`base-action/`)

The `base-action/` directory contains the core Claude Code execution logic, which serves a dual purpose:

- **Standalone Action**: Published separately as `@anthropic-ai/claude-code-base-action` for direct use
- **Inner Logic**: Used internally by this GitHub Action after preparation phase completes

Execution steps:

1. **MCP Server Setup**: Installs and configures GitHub MCP server for tool access
2. **Prompt Generation**: Creates context-rich prompts from GitHub data
3. **Claude Integration**: Executes via multiple providers (Anthropic API, AWS Bedrock, Google Vertex AI)
4. **Result Processing**: Updates comments and creates branches/PRs as needed

### Key Architectural Components

#### Mode System (`src/modes/`)

- **Tag Mode** (`tag/`): Responds to `@claude` mentions and issue assignments
- **Agent Mode** (`agent/`): Automated execution for workflow_dispatch and schedule events only
- Extensible registry pattern in `modes/registry.ts`

#### GitHub Integration (`src/github/`)

- **Context Parsing** (`context.ts`): Unified GitHub event handling
- **Data Fetching** (`data/fetcher.ts`): Retrieves PR/issue data via GraphQL/REST
- **Data Formatting** (`data/formatter.ts`): Converts GitHub data to Claude-readable format
- **Branch Operations** (`operations/branch.ts`): Handles branch creation and cleanup
- **Comment Management** (`operations/comments/`): Creates and updates tracking comments

#### MCP Server Integration (`src/mcp/`)

- **GitHub Actions Server** (`github-actions-server.ts`): Workflow and CI access
- **GitHub Comment Server** (`github-comment-server.ts`): Comment operations
- **GitHub File Operations** (`github-file-ops-server.ts`): File system access
- Auto-installation and configuration in `install-mcp-server.ts`

#### Authentication & Security (`src/github/`)

- **Token Management** (`token.ts`): OIDC token exchange and GitHub App authentication
- **Permission Validation** (`validation/permissions.ts`): Write access verification
- **Actor Validation** (`validation/actor.ts`): Human vs bot detection

### Project Structure

```
src/
├── entrypoints/           # Action entry points
│   ├── prepare.ts         # Main preparation logic
│   ├── update-comment-link.ts  # Post-execution comment updates
│   └── format-turns.ts    # Claude conversation formatting
├── github/               # GitHub integration layer
│   ├── api/              # REST/GraphQL clients
│   ├── data/             # Data fetching and formatting
│   ├── operations/       # Branch, comment, git operations
│   ├── validation/       # Permission and trigger validation
│   └── utils/            # Image downloading, sanitization
├── modes/                # Execution modes
│   ├── tag/              # @claude mention mode
│   ├── agent/            # Automation mode
│   └── registry.ts       # Mode selection logic
├── mcp/                  # MCP server implementations
├── prepare/              # Preparation orchestration
└── utils/                # Shared utilities
```

## Important Implementation Notes

### Authentication Flow

- Uses GitHub OIDC token exchange for secure authentication
- Supports custom GitHub Apps via `APP_ID` and `APP_PRIVATE_KEY`
- Falls back to official Claude GitHub App if no custom app provided

### MCP Server Architecture

- Each MCP server has specific GitHub API access patterns
- Servers are auto-installed in `~/.claude/mcp/github-{type}-server/`
- Configuration merged with user-provided MCP config via `mcp_config` input

### Mode System Design

- Modes implement `Mode` interface with `shouldTrigger()` and `prepare()` methods
- Registry validates mode compatibility with GitHub event types
- Agent mode only works with workflow_dispatch and schedule events

### Comment Threading

- Single tracking comment updated throughout execution
- Progress indicated via dynamic checkboxes
- Links to job runs and created branches/PRs
- Sticky comment option for consolidated PR comments

## Code Conventions

- Use Bun-specific TypeScript configuration with `moduleResolution: "bundler"`
- Strict TypeScript with `noUnusedLocals` and `noUnusedParameters` enabled
- Prefer explicit error handling with detailed error messages
- Use discriminated unions for GitHub context types
- Implement retry logic for GitHub API operations via `utils/retry.ts`
</file>

<file path="docs/configuration.md">
# Advanced Configuration

## Using Custom MCP Configuration

The `mcp_config` input allows you to add custom MCP (Model Context Protocol) servers to extend Claude's capabilities. These servers merge with the built-in GitHub MCP servers.

### Basic Example: Adding a Sequential Thinking Server

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    mcp_config: |
      {
        "mcpServers": {
          "sequential-thinking": {
            "command": "npx",
            "args": [
              "-y",
              "@modelcontextprotocol/server-sequential-thinking"
            ]
          }
        }
      }
    allowed_tools: "mcp__sequential-thinking__sequentialthinking" # Important: Each MCP tool from your server must be listed here, comma-separated
    # ... other inputs
```

### Passing Secrets to MCP Servers

For MCP servers that require sensitive information like API keys or tokens, use GitHub Secrets in the environment variables:

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    mcp_config: |
      {
        "mcpServers": {
          "custom-api-server": {
            "command": "npx",
            "args": ["-y", "@example/api-server"],
            "env": {
              "API_KEY": "${{ secrets.CUSTOM_API_KEY }}",
              "BASE_URL": "https://api.example.com"
            }
          }
        }
      }
    # ... other inputs
```

### Using Python MCP Servers with uv

For Python-based MCP servers managed with `uv`, you need to specify the directory containing your server:

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    mcp_config: |
      {
        "mcpServers": {
          "my-python-server": {
            "type": "stdio",
            "command": "uv",
            "args": [
              "--directory",
              "${{ github.workspace }}/path/to/server/",
              "run",
              "server_file.py"
            ]
          }
        }
      }
    allowed_tools: "my-python-server__<tool_name>" # Replace <tool_name> with your server's tool names
    # ... other inputs
```

For example, if your Python MCP server is at `mcp_servers/weather.py`, you would use:

```yaml
"args":
  ["--directory", "${{ github.workspace }}/mcp_servers/", "run", "weather.py"]
```

**Important**:

- Always use GitHub Secrets (`${{ secrets.SECRET_NAME }}`) for sensitive values like API keys, tokens, or passwords. Never hardcode secrets directly in the workflow file.
- Your custom servers will override any built-in servers with the same name.

## Additional Permissions for CI/CD Integration

The `additional_permissions` input allows Claude to access GitHub Actions workflow information when you grant the necessary permissions. This is particularly useful for analyzing CI/CD failures and debugging workflow issues.

### Enabling GitHub Actions Access

To allow Claude to view workflow run results, job logs, and CI status:

1. **Grant the necessary permission to your GitHub token**:

   - When using the default `GITHUB_TOKEN`, add the `actions: read` permission to your workflow:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
     issues: write
     actions: read # Add this line
   ```

2. **Configure the action with additional permissions**:

   ```yaml
   - uses: anthropics/claude-code-action@beta
     with:
       anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
       additional_permissions: |
         actions: read
       # ... other inputs
   ```

3. **Claude will automatically get access to CI/CD tools**:
   When you enable `actions: read`, Claude can use the following MCP tools:
   - `mcp__github_ci__get_ci_status` - View workflow run statuses
   - `mcp__github_ci__get_workflow_run_details` - Get detailed workflow information
   - `mcp__github_ci__download_job_log` - Download and analyze job logs

### Example: Debugging Failed CI Runs

```yaml
name: Claude CI Helper
on:
  issue_comment:
    types: [created]

permissions:
  contents: write
  pull-requests: write
  issues: write
  actions: read # Required for CI access

jobs:
  claude-ci-helper:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@beta
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          additional_permissions: |
            actions: read
          # Now Claude can respond to "@claude why did the CI fail?"
```

**Important Notes**:

- The GitHub token must have the `actions: read` permission in your workflow
- If the permission is missing, Claude will warn you and suggest adding it
- Currently, only `actions: read` is supported, but the format allows for future extensions

## Custom Environment Variables

You can pass custom environment variables to Claude Code execution using the `claude_env` input. This is useful for CI/test setups that require specific environment variables:

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    claude_env: |
      NODE_ENV: test
      CI: true
      DATABASE_URL: postgres://test:test@localhost:5432/test_db
    # ... other inputs
```

The `claude_env` input accepts YAML format where each line defines a key-value pair. These environment variables will be available to Claude Code during execution, allowing it to run tests, build processes, or other commands that depend on specific environment configurations.

## Limiting Conversation Turns

You can use the `max_turns` parameter to limit the number of back-and-forth exchanges Claude can have during task execution. This is useful for:

- Controlling costs by preventing runaway conversations
- Setting time boundaries for automated workflows
- Ensuring predictable behavior in CI/CD pipelines

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    max_turns: "5" # Limit to 5 conversation turns
    # ... other inputs
```

When the turn limit is reached, Claude will stop execution gracefully. Choose a value that gives Claude enough turns to complete typical tasks while preventing excessive usage.

## Custom Tools

By default, Claude only has access to:

- File operations (reading, committing, editing files, read-only git commands)
- Comment management (creating/updating comments)
- Basic GitHub operations

Claude does **not** have access to execute arbitrary Bash commands by default. If you want Claude to run specific commands (e.g., npm install, npm test), you must explicitly allow them using the `allowed_tools` configuration:

**Note**: If your repository has a `.mcp.json` file in the root directory, Claude will automatically detect and use the MCP server tools defined there. However, these tools still need to be explicitly allowed via the `allowed_tools` configuration.

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    allowed_tools: "Bash(npm install),Bash(npm run test),Edit,Replace,NotebookEditCell"
    disallowed_tools: "TaskOutput,KillTask"
    # ... other inputs
```

**Note**: The base GitHub tools are always included. Use `allowed_tools` to add additional tools (including specific Bash commands), and `disallowed_tools` to prevent specific tools from being used.

## Custom Model

Use a specific Claude model:

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    # model: "claude-3-5-sonnet-20241022"  # Optional: specify a different model
    # ... other inputs
```

## Claude Code Settings

You can provide Claude Code settings to customize behavior such as model selection, environment variables, permissions, and hooks. Settings can be provided either as a JSON string or a path to a settings file.

### Option 1: Settings File

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    settings: "path/to/settings.json"
    # ... other inputs
```

### Option 2: Inline Settings

```yaml
- uses: anthropics/claude-code-action@beta
  with:
    settings: |
      {
        "model": "claude-opus-4-1-20250805",
        "env": {
          "DEBUG": "true",
          "API_URL": "https://api.example.com"
        },
        "permissions": {
          "allow": ["Bash", "Read"],
          "deny": ["WebFetch"]
        },
        "hooks": {
          "PreToolUse": [{
            "matcher": "Bash",
            "hooks": [{
              "type": "command",
              "command": "echo Running bash command..."
            }]
          }]
        }
      }
    # ... other inputs
```

The settings support all Claude Code settings options including:

- `model`: Override the default model
- `env`: Environment variables for the session
- `permissions`: Tool usage permissions
- `hooks`: Pre/post tool execution hooks
- And more...

For a complete list of available settings and their descriptions, see the [Claude Code settings documentation](https://docs.anthropic.com/en/docs/claude-code/settings).

**Notes**:

- The `enableAllProjectMcpServers` setting is always set to `true` by this action to ensure MCP servers work correctly.
- If both the `model` input parameter and a `model` in settings are provided, the `model` input parameter takes precedence.
- The `allowed_tools` and `disallowed_tools` input parameters take precedence over `permissions` in settings.
- In a future version, we may deprecate individual input parameters in favor of using the settings file for all configuration.
</file>

<file path="docs/usage.md">
# Usage

Add a workflow file to your repository (e.g., `.github/workflows/claude.yml`):

```yaml
name: Claude Assistant
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
  issues:
    types: [opened, assigned, labeled]
  pull_request_review:
    types: [submitted]

jobs:
  claude-response:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@beta
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          # Or use OAuth token instead:
          # claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          # Optional: set execution mode (default: tag)
          # mode: "tag"
          # Optional: add custom trigger phrase (default: @claude)
          # trigger_phrase: "/claude"
          # Optional: add assignee trigger for issues
          # assignee_trigger: "claude"
          # Optional: add label trigger for issues
          # label_trigger: "claude"
          # Optional: add custom environment variables (YAML format)
          # claude_env: |
          #   NODE_ENV: test
          #   DEBUG: true
          #   API_URL: https://api.example.com
          # Optional: limit the number of conversation turns
          # max_turns: "5"
          # Optional: grant additional permissions (requires corresponding GitHub token permissions)
          # additional_permissions: |
          #   actions: read
          # Optional: allow bot users to trigger the action
          # allowed_bots: "dependabot[bot],renovate[bot]"
```

## Inputs

| Input                          | Description                                                                                                                           | Required | Default   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------- |
| `mode`                         | Execution mode: 'tag' (default - triggered by mentions/assignments), 'agent' (for automation), 'experimental-review' (for PR reviews) | No       | `tag`     |
| `anthropic_api_key`            | Anthropic API key (required for direct API, not needed for Bedrock/Vertex)                                                            | No\*     | -         |
| `claude_code_oauth_token`      | Claude Code OAuth token (alternative to anthropic_api_key)                                                                            | No\*     | -         |
| `direct_prompt`                | Direct prompt for Claude to execute automatically without needing a trigger (for automated workflows)                                 | No       | -         |
| `override_prompt`              | Complete replacement of Claude's prompt with custom template (supports variable substitution)                                         | No       | -         |
| `base_branch`                  | The base branch to use for creating new branches (e.g., 'main', 'develop')                                                            | No       | -         |
| `max_turns`                    | Maximum number of conversation turns Claude can take (limits back-and-forth exchanges)                                                | No       | -         |
| `timeout_minutes`              | Timeout in minutes for execution                                                                                                      | No       | `30`      |
| `use_sticky_comment`           | Use just one comment to deliver PR comments (only applies for pull_request event workflows)                                           | No       | `false`   |
| `github_token`                 | GitHub token for Claude to operate with. **Only include this if you're connecting a custom GitHub app of your own!**                  | No       | -         |
| `model`                        | Model to use (provider-specific format required for Bedrock/Vertex)                                                                   | No       | -         |
| `fallback_model`               | Enable automatic fallback to specified model when primary model is unavailable                                                        | No       | -         |
| `anthropic_model`              | **DEPRECATED**: Use `model` instead. Kept for backward compatibility.                                                                 | No       | -         |
| `use_bedrock`                  | Use Amazon Bedrock with OIDC authentication instead of direct Anthropic API                                                           | No       | `false`   |
| `use_vertex`                   | Use Google Vertex AI with OIDC authentication instead of direct Anthropic API                                                         | No       | `false`   |
| `allowed_tools`                | Additional tools for Claude to use (the base GitHub tools will always be included)                                                    | No       | ""        |
| `disallowed_tools`             | Tools that Claude should never use                                                                                                    | No       | ""        |
| `custom_instructions`          | Additional custom instructions to include in the prompt for Claude                                                                    | No       | ""        |
| `mcp_config`                   | Additional MCP configuration (JSON string) that merges with the built-in GitHub MCP servers                                           | No       | ""        |
| `assignee_trigger`             | The assignee username that triggers the action (e.g. @claude). Only used for issue assignment                                         | No       | -         |
| `label_trigger`                | The label name that triggers the action when applied to an issue (e.g. "claude")                                                      | No       | -         |
| `trigger_phrase`               | The trigger phrase to look for in comments, issue/PR bodies, and issue titles                                                         | No       | `@claude` |
| `branch_prefix`                | The prefix to use for Claude branches (defaults to 'claude/', use 'claude-' for dash format)                                          | No       | `claude/` |
| `claude_env`                   | Custom environment variables to pass to Claude Code execution (YAML format)                                                           | No       | ""        |
| `settings`                     | Claude Code settings as JSON string or path to settings JSON file                                                                     | No       | ""        |
| `additional_permissions`       | Additional permissions to enable. Currently supports 'actions: read' for viewing workflow results                                     | No       | ""        |
| `experimental_allowed_domains` | Restrict network access to these domains only (newline-separated).                                                                    | No       | ""        |
| `use_commit_signing`           | Enable commit signing using GitHub's commit signature verification. When false, Claude uses standard git commands                     | No       | `false`   |
| `allowed_bots`                 | Comma-separated list of allowed bot usernames, or '\*' to allow all bots. Empty string (default) allows no bots                       | No       | ""        |

\*Required when using direct Anthropic API (default and when not using Bedrock or Vertex)

> **Note**: This action is currently in beta. Features and APIs may change as we continue to improve the integration.

## Ways to Tag @claude

These examples show how to interact with Claude using comments in PRs and issues. By default, Claude will be triggered anytime you mention `@claude`, but you can customize the exact trigger phrase using the `trigger_phrase` input in the workflow.

Claude will see the full PR context, including any comments.

### Ask Questions

Add a comment to a PR or issue:

```
@claude What does this function do and how could we improve it?
```

Claude will analyze the code and provide a detailed explanation with suggestions.

### Request Fixes

Ask Claude to implement specific changes:

```
@claude Can you add error handling to this function?
```

### Code Review

Get a thorough review:

```
@claude Please review this PR and suggest improvements
```

Claude will analyze the changes and provide feedback.

### Fix Bugs from Screenshots

Upload a screenshot of a bug and ask Claude to fix it:

```
@claude Here's a screenshot of a bug I'm seeing [upload screenshot]. Can you fix it?
```

Claude can see and analyze images, making it easy to fix visual bugs or UI issues.
</file>

<file path="README.md">
![Claude Code Action responding to a comment](https://github.com/user-attachments/assets/1d60c2e9-82ed-4ee5-b749-f9e021c85f4d)

# Claude Code Action

A general-purpose [Claude Code](https://claude.ai/code) action for GitHub PRs and issues that can answer questions and implement code changes. This action listens for a trigger phrase in comments and activates Claude act on the request. It supports multiple authentication methods including Anthropic direct API, Amazon Bedrock, and Google Vertex AI.

## Features

- 🤖 **Interactive Code Assistant**: Claude can answer questions about code, architecture, and programming
- 🔍 **Code Review**: Analyzes PR changes and suggests improvements
- ✨ **Code Implementation**: Can implement simple fixes, refactoring, and even new features
- 💬 **PR/Issue Integration**: Works seamlessly with GitHub comments and PR reviews
- 🛠️ **Flexible Tool Access**: Access to GitHub APIs and file operations (additional tools can be enabled via configuration)
- 📋 **Progress Tracking**: Visual progress indicators with checkboxes that dynamically update as Claude completes tasks
- 🏃 **Runs on Your Infrastructure**: The action executes entirely on your own GitHub runner (Anthropic API calls go to your chosen provider)

## ⚠️ **BREAKING CHANGES COMING IN v1.0** ⚠️

**We're planning a major update that will significantly change how this action works.** The new version will:

- ✨ Automatically select the appropriate mode (no more `mode` input)
- 🔧 Simplify configuration with unified `prompt` and `claude_args`
- 🚀 Align more closely with the Claude Code SDK capabilities
- 💥 Remove multiple inputs like `direct_prompt`, `custom_instructions`, and others

**[→ Read the full v1.0 roadmap and provide feedback](https://github.com/anthropics/claude-code-action/discussions/428)**

---

## Quickstart

The easiest way to set up this action is through [Claude Code](https://claude.ai/code) in the terminal. Just open `claude` and run `/install-github-app`.

This command will guide you through setting up the GitHub app and required secrets.

**Note**:

- You must be a repository admin to install the GitHub app and add secrets
- This quickstart method is only available for direct Anthropic API users. For AWS Bedrock or Google Vertex AI setup, see [docs/cloud-providers.md](./docs/cloud-providers.md).

## Documentation

- [Setup Guide](./docs/setup.md) - Manual setup, custom GitHub apps, and security best practices
- [Usage Guide](./docs/usage.md) - Basic usage, workflow configuration, and input parameters
- [Custom Automations](./docs/custom-automations.md) - Examples of automated workflows and custom prompts
- [Configuration](./docs/configuration.md) - MCP servers, permissions, environment variables, and advanced settings
- [Experimental Features](./docs/experimental.md) - Execution modes and network restrictions
- [Cloud Providers](./docs/cloud-providers.md) - AWS Bedrock and Google Vertex AI setup
- [Capabilities & Limitations](./docs/capabilities-and-limitations.md) - What Claude can and cannot do
- [Security](./docs/security.md) - Access control, permissions, and commit signing
- [FAQ](./docs/faq.md) - Common questions and troubleshooting

## 📚 FAQ

Having issues or questions? Check out our [Frequently Asked Questions](./docs/faq.md) for solutions to common problems and detailed explanations of Claude's capabilities and limitations.

## License

This project is licensed under the MIT License—see the LICENSE file for details.
</file>

</files>
