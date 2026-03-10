# Lab: Set Up GitHub Copilot Agents In VS Code

## Scenario Context

You are preparing a Windows-based Visual Studio Code environment for first-time use of GitHub Copilot agents.
The initial learner context is a BI, data science, or data engineering team.
The team may store source or infrastructure assets in GitHub or Azure DevOps.
Your goal is to verify prerequisites, confirm whether agent features are available, and run one safe first interaction without skipping review.

## Learner Goal

By the end of this lab, you should be able to:

- verify the minimum prerequisites for GitHub Copilot agents
- confirm whether Ask, Edit, Plan, and Agent are available in your environment
- open a suitable practice workspace
- run one safe first prompt sequence
- record what you verified before accepting any output

## Starter State

You begin with:

- Visual Studio Code installed
- a GitHub account
- an empty or small practice workspace
- no assumption that Copilot agents are already working

## Target State

You finish with:

- GitHub signed in correctly in VS Code
- GitHub Copilot and GitHub Copilot Chat verified as installed and enabled
- Ask, Edit, Plan, and Agent confirmed as available, or the reason they are unavailable documented
- one safe Ask, Edit, Plan, and Agent interaction completed
- one verified observation recorded before accepting output

## Prerequisites And Setup

Goal of the step:

- Ensure the environment is ready before testing agents.

Exact actions:

- Open VS Code on Windows.
- Sign in to GitHub using the account expected to have Copilot access.
- Open Extensions and verify GitHub Copilot and GitHub Copilot Chat are installed and enabled.
- Open a small practice folder in VS Code, ideally a safe sample cloned from GitHub or Azure DevOps if your team already uses one of those systems.

What success looks like:

- Chat is visible in VS Code.
- The correct GitHub identity is signed in.
- The workspace is small enough that you can explain what it contains.

Common failure mode and fix:

- Failure: You are signed in, but Copilot is unavailable.
- Fix: Verify that the signed-in account has Copilot access or Copilot Free enabled.

## Lab Tasks

### Task 1. Confirm Your Account

Goal of the step:

- Verify that VS Code is using the correct GitHub identity.

Exact action:

- Check the account shown in VS Code and confirm it is the expected GitHub identity.

What success looks like:

- You can state which GitHub account is active.

Common failure mode and fix:

- Failure: The wrong account is active.
- Fix: Sign out and sign back in with the intended account.

### Task 2. Verify Required Extensions

Goal of the step:

- Confirm the environment has the minimum feature set for Copilot chat and agents.

Exact action:

- Verify GitHub Copilot and GitHub Copilot Chat in Extensions.

What success looks like:

- Both extensions are installed and enabled.

Common failure mode and fix:

- Failure: One or both extensions are disabled.
- Fix: Enable them and reload VS Code.

### Task 3. Confirm Agent Availability

Goal of the step:

- Determine whether Ask, Edit, Plan, and Agent are available.

Exact action:

- Open Chat with Ctrl+Alt+I.
- Look for Ask, Edit, Plan, and Agent in the agent picker.

What success looks like:

- You can see the available modes, or you can document that the picker is missing.

Common failure mode and fix:

- Failure: The agent picker is missing.
- Fix: Update VS Code and extensions. If still missing, check whether your organization disables agent features.

### Task 4. Prepare A Good Practice Workspace

Goal of the step:

- Make the workspace useful to the agent.

Exact action:

- Open a small practice folder.
- If it is empty, create a simple README.md that describes the folder purpose.

What success looks like:

- The workspace contains at least one relevant file or description.

Common failure mode and fix:

- Failure: The workspace is empty and results are generic.
- Fix: Add a small file and use explicit context such as #file or #codebase.

### Task 5. Run A Safe First Prompt Sequence

Goal of the step:

- Practice Ask, Edit, Plan, and Agent in a controlled order.

Exact action:

- Run this Ask prompt:

```text
Explain what files are in this workspace and what kind of project it appears to be.
```

- Run this Plan prompt:

```text
Create a short plan for adding a beginner-friendly setup guide for GitHub Copilot agents to this workspace.
```

- Run this Agent prompt:

```text
Create a draft README section that lists the prerequisites for using GitHub Copilot agents in VS Code. Keep it beginner-friendly and Windows-first.
```

What success looks like:

- You can explain what each mode did and why Agent was the last step.

Common failure mode and fix:

- Failure: The prompt is too vague and the answer is generic.
- Fix: Add scope, audience, and expected output to the prompt.

### Task 6. Review Before Accepting

Goal of the step:

- Build the habit of verifying AI output.

Exact action:

- Inspect one response, plan, or file change.
- Record one thing you verified before accepting or trusting the output.

What success looks like:

- You have a written note of one concrete verification step.

Common failure mode and fix:

- Failure: You accept output because it sounds plausible.
- Fix: Compare it to the original request and check at least one visible detail.

## Suggested Learner Prompts

- Explain what prerequisites I need to use GitHub Copilot agents in VS Code on Windows.
- Create a short setup checklist for a beginner using GitHub Copilot agents for the first time.
- Using #codebase, identify whether this workspace has enough context for a useful agent session.
- Create a first-day setup checklist for a BI analyst, data scientist, or data engineer using VS Code with a GitHub or Azure DevOps repository.
- Before making changes, ask clarifying questions if anything about the setup task is ambiguous.

## Expected Observable Output

- Chat opens in VS Code.
- The learner can state whether the agent picker is present.
- A short prerequisite summary or checklist is generated.
- The learner records one thing they verified before accepting the result.

## Validation Checklist

- I can list the minimum prerequisites for GitHub Copilot agents.
- I can verify whether Ask, Edit, Plan, and Agent are available in my environment.
- I can explain the difference between Copilot Chat availability and agent availability.
- I can open a small workspace that gives the agent useful context.
- I can write one safe first prompt.
- I can explain one review step I performed before accepting output.

## Reflection Tasks

- Which prerequisite was hardest to verify in your environment?
- What would make you choose Ask or Plan instead of Agent?
- What is one sign that your workspace does not provide enough context?
- What is one verification habit you want to keep using?

## Solution Guidance

A complete solution should show:

- the correct GitHub account signed in
- Copilot and Copilot Chat verified in Extensions
- Ask, Edit, Plan, and Agent available, or a documented reason they are unavailable
- one safe first interaction completed
- one recorded verification step
