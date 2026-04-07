# CLI Tools And Terminal Workflows

## Learning Objectives

By the end of this module, learners should be able to:

- explain how Copilot Agent mode uses the integrated terminal to run commands
- use Copilot Chat to generate, explain, and troubleshoot CLI commands
- build multi-step terminal workflows with Copilot assistance
- apply terminal auto-approve settings safely for CLI-heavy work
- use CLI tools relevant to BI, DS, and DE workflows (az, git, pip, python, dbt, sqlcmd)

## Prerequisites And Setup

Audience:

- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:

- Modules 01 through 09 completed or equivalent knowledge
- VS Code with integrated terminal configured for PowerShell
- GitHub Copilot Chat enabled
- At least one CLI tool installed (git, python, pip, or az)

Success looks like:

- The learner can ask Copilot to generate and explain CLI commands before running them.
- The learner understands the risk model when Copilot runs terminal commands.

Common failure mode and fix:

- Failure: The learner lets Copilot run commands without reading them first.
- Fix: Use the Balanced approval profile from `references/copilot-agent-approval-settings.md` during learning.

## Walkthrough

### Step 1. How Copilot Uses The Terminal

Goal of the step:

- Understand the mechanics of agent-driven terminal execution.

Exact action:

- In Agent mode, Copilot can:
  - Generate a command and show it to you for approval
  - Run the command in the integrated terminal
  - Read the output and decide what to do next
  - Chain multiple commands to complete a multi-step task

- The approval flow is controlled by `chat.tools.terminal.autoApprove` (see [copilot-agent-approval-settings.md](../../references/copilot-agent-approval-settings.md)).

What success looks like:

- The learner can describe the generate > approve > execute > read output cycle.

Common failure mode and fix:

- Failure: The learner thinks Copilot runs commands outside VS Code.
- Fix: Clarify that all execution happens in the VS Code integrated terminal.

### Step 2. Generate And Explain CLI Commands

Goal of the step:

- Use Copilot as a CLI assistant that explains before executing.

Exact action:

- Ask Copilot to generate commands with explanations:

```text
How do I list all Python packages installed in my current environment, sorted by size?
```

```text
Write a PowerShell command to find all CSV files in this folder modified in the last 7 days
```

```text
Explain what this command does: az storage blob list --account-name myaccount --container-name data --output table
```

What success looks like:

- Copilot generates the command and explains each flag or parameter.

Common failure mode and fix:

- Failure: The learner runs the command without reading the explanation.
- Fix: Ask Copilot to explain first, then generate the runnable command separately.

### Step 3. Multi-Step Terminal Workflows

Goal of the step:

- Chain CLI commands into a workflow using Agent mode.

Exact action:

- Give Copilot a multi-step goal:

```text
Create a new Python virtual environment, install pandas and great-expectations, then verify both packages are installed correctly
```

- Copilot will generate and execute each step, reading output between steps to decide the next action.

What success looks like:

- Copilot completes the full workflow, handling errors if they arise.

Common failure mode and fix:

- Failure: A command fails and Copilot retries the same broken command.
- Fix: Intervene and provide context: "The error says X. Try Y instead."

### Worked Example: GitHub CLI For Teams New To GitHub

This end-to-end example walks through installing the GitHub CLI (`gh`), authenticating, and then using GitHub Copilot to manage repos, issues, and pull requests from the terminal. This is ideal for teams that are new to GitHub or transitioning from Azure DevOps.

#### Part 1. Install The GitHub CLI

The GitHub CLI (`gh`) is a command-line tool for interacting with GitHub repos, issues, PRs, and workflows without leaving the terminal.

**Option A -- WinGet (recommended on Windows)**

```powershell
winget install --id GitHub.cli -e --accept-source-agreements
```

**Option B -- Chocolatey**

```powershell
choco install gh
```

**Option C -- Ask Copilot to help**

In Copilot Chat (Agent mode):

```text
Install the GitHub CLI on my Windows machine using winget and verify it works
```

Copilot generates the install command, runs it, then runs `gh --version` to confirm.

**Verify the installation**

```powershell
gh --version
```

Expected output:

```text
gh version 2.65.0 (2025-12-10)
```

Common failure mode and fix:

- Failure: `gh` is not recognized after installation.
- Fix: Close and reopen the VS Code terminal to pick up the updated PATH.

#### Part 2. Log In To GitHub

**Step 1. Authenticate with your GitHub account**

```powershell
gh auth login
```

The CLI prompts you through an interactive flow:

```text
? What account do you want to log into?  GitHub.com
? What is your preferred protocol for Git operations?  HTTPS
? Authenticate Git with your GitHub credentials?  Yes
? How would you like to authenticate GitHub CLI?  Login with a web browser
```

A browser opens. Enter the one-time code shown in the terminal, then approve access.

**Step 2. Verify your login**

```powershell
gh auth status
```

Expected output:

```text
github.com
  ✓ Logged in to github.com account yourname (keyring)
  - Active account: true
  - Git operations protocol: https
  - Token: gho_****
  - Token scopes: 'gist', 'read:org', 'repo', 'workflow'
```

**Step 3. Set your default repo (optional but helpful)**

If you are working inside a cloned repo, `gh` detects it automatically. Otherwise, set it:

```powershell
gh repo set-default owner/repo-name
```

Common failure mode and fix:

- Failure: `gh auth login` times out waiting for browser approval.
- Fix: Copy the URL from the terminal and paste it in your browser manually. If on a corporate network, check whether the firewall blocks `github.com/login/device`.

> **For Azure DevOps users**: If your team also uses Azure DevOps, note that `gh` only works with GitHub. For Azure DevOps repos, use `az repos` from the Azure CLI. Both can coexist on the same machine.

#### Part 3. Use Copilot To Manage GitHub From The Terminal

Once authenticated, Copilot can use `gh` commands to help you work with repos, issues, and PRs. Here is a realistic workflow for a team getting started with GitHub.

**Scenario**: Your team recently moved a training repo to GitHub. You need to create issues for upcoming work, make a branch, and open a pull request -- all from the terminal with Copilot's help.

**Prompt 1 -- Explore the repo**

```text
Show me the details of my current GitHub repo -- name, description, visibility, default branch, and open issue count
```

Copilot generates:

```powershell
gh repo view --json name,description,visibility,defaultBranchRef,issues --jq '{name, description, visibility, default_branch: .defaultBranchRef.name, open_issues: (.issues | length)}'
```

**Prompt 2 -- List recent issues**

```text
List the 10 most recent open issues in this repo as a table with number, title, author, and labels
```

Copilot generates:

```powershell
gh issue list --limit 10 --state open --json number,title,author,labels --template '{{tablerow "Number" "Title" "Author" "Labels"}}{{range .}}{{tablerow .number .title .author.login (pluck "name" .labels | join ", ")}}{{end}}'
```

Or the simpler version:

```powershell
gh issue list --limit 10 --state open
```

**Prompt 3 -- Create an issue from a description**

```text
Create a GitHub issue titled "Add module 11 MCP content" with the body: "Create materials and lab scaffolds for the Model Context Protocol module. Include install steps, server configuration, and a worked example." and label it "training-content"
```

Copilot generates:

```powershell
gh issue create --title "Add module 11 MCP content" --body "Create materials and lab scaffolds for the Model Context Protocol module. Include install steps, server configuration, and a worked example." --label "training-content"
```

**Prompt 4 -- Create a branch and switch to it**

```text
Create a new branch called "feature/module-11-mcp" from main and switch to it
```

Copilot generates:

```powershell
git checkout -b feature/module-11-mcp main
```

**Prompt 5 -- Open a pull request after making changes**

```text
Create a pull request from my current branch to main with the title "Add module 11 MCP materials" and link it to issue #42. Mark it as draft.
```

Copilot generates:

```powershell
gh pr create --title "Add module 11 MCP materials" --body "Closes #42" --base main --draft
```

**Prompt 6 -- Review a pull request**

```text
Show me the diff and review comments for PR #15 in this repo
```

Copilot generates:

```powershell
gh pr diff 15
gh pr review 15 --comment --body "Looks good. One suggestion: add a validation checklist to the lab README."
```

**Prompt 7 -- Check workflow runs (CI status)**

```text
Show the last 5 GitHub Actions workflow runs for this repo with their status
```

Copilot generates:

```powershell
gh run list --limit 5
```

#### Part 4. Safe vs Unsafe GitHub CLI Commands

Unlike Azure CLI, most `gh` commands are low-risk because GitHub has built-in undo mechanisms (close issues, revert PRs, restore branches). However, some commands still deserve review.

| Safety Level | Commands | Auto-approve? |
| --- | --- | --- |
| **Read-only (safe)** | `gh repo view`, `gh issue list`, `gh pr list`, `gh pr diff`, `gh run list`, `gh auth status` | Yes |
| **Create (low risk)** | `gh issue create`, `gh pr create --draft`, `gh issue comment` | Yes (creates are visible and reversible) |
| **Modify (review)** | `gh pr merge`, `gh pr close`, `gh issue close`, `gh pr review --approve` | Review first |
| **Destructive (dangerous)** | `gh repo delete`, `gh run cancel`, `gh release delete` | Never auto-approve |

Recommended auto-approve config for teams new to GitHub:

```jsonc
"chat.tools.terminal.autoApprove": {
    "/^gh (repo view|issue list|pr list|pr diff|pr view|run list|auth status)/": {
        "approve": true,
        "matchCommandLine": true
    },
    "/^gh (issue create|pr create|issue comment)/": {
        "approve": true,
        "matchCommandLine": true
    },
    "/^gh --version/": {
        "approve": true,
        "matchCommandLine": true
    }
}
```

This auto-approves read and create commands while requiring manual approval for merges, closures, approvals, and deletions.

> **Key takeaway**: The GitHub CLI is a great first CLI tool for teams new to GitHub. Most commands are low-risk and reversible, making it safe to practice Copilot-driven terminal workflows before moving to higher-stakes tools like `az` or `terraform`.

### Step 4. CLI Tools For Data Teams

Goal of the step:

- Map common data-team tasks to CLI commands Copilot can help with.

Exact action:

- Review this mapping of team roles to CLI tools:

| Role | Common CLI Tools | Example Tasks |
| --- | --- | --- |
| BI | `sqlcmd`, `az`, `git`, PowerShell | Query databases, deploy reports, manage repos |
| DS | `python`, `pip`, `conda`, `jupyter`, `git` | Manage environments, run experiments, version notebooks |
| DE | `az`, `dbt`, `docker`, `terraform`, `git` | Deploy pipelines, run transformations, manage infrastructure |

- Try asking Copilot for role-specific help:

```text
I'm a data engineer. Generate the dbt commands to run a full refresh of my staging models and then test them.
```

What success looks like:

- The learner can identify 3-5 CLI commands relevant to their role that Copilot can assist with.

Common failure mode and fix:

- Failure: The learner asks for commands for tools that are not installed.
- Fix: Use `Get-Command` or `which` to verify tool availability before asking Copilot to generate commands.

### Step 5. Terminal Approval Settings For CLI Work

Goal of the step:

- Configure terminal auto-approve for productive but safe CLI workflows.

Exact action:

- Review the Balanced profile from [copilot-agent-approval-settings.md](../../references/copilot-agent-approval-settings.md).
- For CLI-heavy data work, consider adding role-specific patterns:

```jsonc
"chat.tools.terminal.autoApprove": {
    "/^python /":          { "approve": true, "matchCommandLine": true },
    "/^pip /":             { "approve": true, "matchCommandLine": true },
    "/^dbt /":             { "approve": true, "matchCommandLine": true },
    "/^git (status|diff|log|branch)/": { "approve": true, "matchCommandLine": true },
    "/^Get-ChildItem/":    { "approve": true, "matchCommandLine": true },
    "/^az (account|group) (show|list)/": { "approve": true, "matchCommandLine": true }
}
```

What success looks like:

- The learner has a terminal approval config tailored to their role.

Common failure mode and fix:

- Failure: The learner auto-approves `az` commands that create or delete resources.
- Fix: Only auto-approve read-only `az` subcommands (show, list, get).

## Hands-On Lab Reference

See [labs/10-cli-tools-and-terminal-workflows/README.md](../../labs/10-cli-tools-and-terminal-workflows/README.md).

## Validation Checklist

- [ ] Learner can explain the generate > approve > execute > read output cycle.
- [ ] Learner generated at least 3 CLI commands using Copilot Chat.
- [ ] Learner completed at least one multi-step terminal workflow.
- [ ] Learner can identify CLI tools relevant to their team role.
- [ ] Learner has a terminal auto-approve configuration appropriate for their risk level.

## Reflection And Extension Tasks

- What CLI commands should never be auto-approved for your team?
- How would you build a team-shared terminal allowlist?
- When should you use Copilot for CLI help versus reading the tool's own documentation?
- What risks exist when Copilot chains commands that modify infrastructure?

## References

- [copilot-agent-approval-settings.md](../../references/copilot-agent-approval-settings.md) -- Terminal approval profiles
- [copilot-chat-quick-commands.md](../../references/copilot-chat-quick-commands.md) -- Chat modes and shortcuts
- [developer-toolbox.md](../../references/developer-toolbox.md) -- Required CLI tools and setup
- [GitHub CLI Manual](https://cli.github.com/manual/) -- Official `gh` command reference
- [GitHub CLI `gh auth login`](https://cli.github.com/manual/gh_auth_login) -- Authentication flow details
- [What are Agents, Skills, and Instructions](https://awesome-copilot.github.com/learning-hub/what-are-agents-skills-instructions/) -- Fundamentals baseline
