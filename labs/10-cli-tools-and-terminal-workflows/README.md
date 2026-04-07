# Lab: CLI Tools And Terminal Workflows

## Scenario Context

Your team relies on several CLI tools daily (git, python, pip, az, dbt, sqlcmd). You want to use Copilot Agent mode to speed up terminal work while keeping guardrails in place.

## Learner Goal

By the end of this lab, you should be able to:

- generate and explain CLI commands using Copilot Chat
- complete a multi-step terminal workflow with Copilot
- configure terminal auto-approve settings for your role
- identify commands that should always require manual approval

## Starter State

You begin with:

- VS Code open with the integrated terminal set to PowerShell
- At least `git` and `python` available on PATH
- Default Copilot approval settings (ask every time)
- No custom terminal auto-approve rules

## Target State

You finish with:

- at least 5 CLI commands generated and explained by Copilot
- one completed multi-step terminal workflow
- a role-appropriate terminal auto-approve configuration
- a "never auto-approve" list for your team

## Prerequisites And Setup

Goal of the step:

- Verify your CLI tools are available.

Exact actions:

- Open the VS Code integrated terminal.
- Run these checks:

```powershell
Get-Command git, python, pip | Select-Object Name, Source
```

- Note which tools are available and which are missing.

What success looks like:

- You know which CLI tools are on your PATH.

Common failure mode and fix:

- Failure: `python` is not found.
- Fix: Check `py` as an alternative, or install Python from <https://python.org>.

## Lab Tasks

### Task 1. Generate And Explain Commands

Goal of the step:

- Practice using Copilot as a CLI assistant.

Exact action:

- Ask Copilot Chat to generate commands for these scenarios. Review each explanation before running:

```text
List all git branches, showing the last commit date for each
```

```text
Show the top 10 largest files in the current directory, sorted by size
```

```text
Check which Python version is active and list all installed packages
```

```text
Find all .sql files in this workspace that contain the word "CREATE"
```

```text
Show my current Azure subscription and resource group (read-only)
```

- For each command, note: what it does, whether it is safe to run, and whether you would auto-approve it.

What success looks like:

- 5 commands generated, each with a one-line explanation and a safe/unsafe classification.

Common failure mode and fix:

- Failure: Copilot generates a command for a tool that is not installed.
- Fix: Tell Copilot which tools are available: "I only have git, python, and pip installed."

### Task 2. Multi-Step Terminal Workflow

Goal of the step:

- Let Copilot chain commands to complete a real task.

Exact action:

- Give Copilot a multi-step goal in Agent mode:

```text
Create a Python virtual environment called lab10-env, activate it, install pandas and pytest, then run pytest --version to verify the install
```

- Watch Copilot generate and execute each step. Approve or correct as needed.

What success looks like:

- A working virtual environment with pandas and pytest installed.

Common failure mode and fix:

- Failure: Activation fails because PowerShell execution policy blocks scripts.
- Fix: Run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` first.

### Task 3. Configure Terminal Auto-Approve

Goal of the step:

- Build a role-appropriate terminal allowlist.

Exact action:

- Create or update `.vscode/settings.json` in this workspace with auto-approve rules for your role.
- Use the Balanced profile from [copilot-agent-approval-settings.md](../../references/copilot-agent-approval-settings.md) as a starting point.
- Add patterns for tools you use daily. Remove patterns for tools you do not use.

What success looks like:

- A `.vscode/settings.json` with at least 3 role-specific auto-approve patterns.

Common failure mode and fix:

- Failure: The learner auto-approves everything with `/.*/`.
- Fix: Replace with specific patterns. Ask: "Would I run this command without reading it first?"

### Task 4. Build A Never-Auto-Approve List

Goal of the step:

- Identify commands that should always require manual approval.

Exact action:

- Create a list of commands your team should never auto-approve. Start with these:

| Command Pattern | Why |
| --- | --- |
| `rm -rf`, `Remove-Item -Recurse` | Irreversible file deletion |
| `git push --force` | Overwrites remote history |
| `DROP TABLE`, `DROP DATABASE` | Irreversible data loss |
| `az group delete` | Deletes entire resource groups |
| `pip install` (unknown packages) | Supply chain risk |

- Add at least 2 entries specific to your team's tools.

What success looks like:

- A documented never-auto-approve list with at least 7 entries.

Common failure mode and fix:

- Failure: The list is generic and does not reflect the team's actual tools.
- Fix: Review the last month of terminal history and identify risky commands that were actually used.

## Suggested Prompts

```text
How do I list all git branches, showing the last commit date for each?
```

```text
Create a Python virtual environment, install pandas and pytest, then verify
```

```text
Explain what this command does: [paste command]
```

```text
What PowerShell commands should I auto-approve for a data engineering workflow?
```

```text
Generate a .vscode/settings.json terminal auto-approve config for a BI team
```

## Expected Observable Output

- 5 CLI commands with explanations and safe/unsafe classifications
- One completed multi-step workflow (virtual environment with packages)
- A `.vscode/settings.json` with role-specific terminal auto-approve patterns
- A documented never-auto-approve list with at least 7 entries

## Validation Checklist

- [ ] At least 5 CLI commands generated and explained
- [ ] Each command classified as safe or unsafe to auto-approve
- [ ] Multi-step terminal workflow completed successfully
- [ ] `.vscode/settings.json` has at least 3 role-specific auto-approve patterns
- [ ] Never-auto-approve list has at least 7 entries including 2 team-specific ones
- [ ] Learner can explain why certain commands should never be auto-approved

## Reflection And Extension Tasks

- How did Copilot handle errors during the multi-step workflow?
- What CLI commands do you run most often that Copilot could help with?
- How would you share your auto-approve config across your team?
- What is the risk of auto-approving `pip install` for unknown packages?

## Solution Guidance

See `solution/` for an example auto-approve configuration and never-auto-approve list.
