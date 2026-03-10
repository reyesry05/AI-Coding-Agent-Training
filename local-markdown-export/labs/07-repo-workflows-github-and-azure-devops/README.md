# Lab: Repo Workflows In GitHub And Azure DevOps

## Scenario Context
Your team stores notebooks, scripts, documentation, or pipeline assets in GitHub or Azure DevOps.
The goal is to make one small Copilot-assisted change in a repository-backed workspace and review it before treating it as commit-ready.

## Learner Goal
By the end of this lab, you should be able to:
- make one bounded repo-safe change
- review the resulting diff
- decide whether the change should be kept, revised, or rejected
- explain how the same safe habits apply in GitHub and Azure DevOps

## Starter State
You begin with:
- a safe working copy from GitHub or Azure DevOps
- one file suitable for a small improvement
- Copilot Chat available in VS Code

## Target State
You finish with:
- one small repository-backed change
- one diff review
- one keep, revise, or reject decision with justification

## Prerequisites And Setup
Goal of the step:
- Prepare a repo-backed exercise that remains low risk.

Exact actions:
- Open a safe branch or practice working copy.
- Choose one README, notebook README, SQL documentation file, or pipeline support file.

What success looks like:
- You know exactly which file will be touched and why.

Common failure mode and fix:
- Failure: The scope is too large for one review cycle.
- Fix: Reduce the task to one file and one improvement.

## Lab Tasks

### Task 1. Define A Small Repo-Safe Change
Goal of the step:
- Bound the work before you ask Copilot to edit anything.

Exact action:
- Pick one small improvement such as a checklist, wording improvement, or troubleshooting note.

What success looks like:
- The change fits in one file and is easy to review.

Common failure mode and fix:
- Failure: The task implies a broad rewrite.
- Fix: Limit the task to one section.

### Task 2. Prompt Copilot For The Change
Goal of the step:
- Ask for a repository-safe edit.

Exact action:
- Use a prompt that preserves headings, tone, and unchanged sections.

What success looks like:
- The result is focused and does not wander into unrelated files.

Common failure mode and fix:
- Failure: The prompt allows too much restructuring.
- Fix: Specify exactly what must stay unchanged.

### Task 3. Review The Diff
Goal of the step:
- Evaluate the change as if another reviewer will see it.

Exact action:
- Open the diff and inspect the change line by line.

What success looks like:
- You can explain whether the change is clear, bounded, and consistent.

Common failure mode and fix:
- Failure: You review only the final file and not the diff.
- Fix: Review the actual change set.

### Task 4. Decide Whether It Is Commit-Ready
Goal of the step:
- Make an explicit quality decision.

Exact action:
- Mark the change as keep, revise, or reject and write one reason.

What success looks like:
- Your decision is tied to quality, scope, or reviewability.

Common failure mode and fix:
- Failure: You treat any useful draft as commit-ready.
- Fix: Ask whether another teammate would approve it as-is.

## Suggested Learner Prompts
- Update this README section only and preserve the existing tone and headings.
- Add a short validation checklist to this file without changing any other file.
- Improve the troubleshooting section for a new data engineer. Keep the deployment steps unchanged.
- Before making changes, ask clarifying questions if the expected repository impact is unclear.

## Expected Observable Output
- One small diff
- One explicit review decision
- One written reason for that decision

## Validation Checklist
- I can constrain a repository-backed change to one file.
- I can review the diff instead of trusting the response text alone.
- I can explain whether the change is commit-ready.
- I can apply the same review habit in GitHub or Azure DevOps workflows.

## Reflection Tasks
- What made the change safe enough to review quickly?
- What would have made you reject it immediately?
- Which repo habit should your team standardize when using Copilot?

## Solution Guidance
A complete solution should show:
- one bounded repo-safe change
- one diff review
- one reasoned keep, revise, or reject decision
