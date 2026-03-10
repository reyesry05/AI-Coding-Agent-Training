# Lab: Beginner Copilot Agent Best Practices

## Scenario Context

You are onboarding a mixed technical team to GitHub Copilot in VS Code. The team includes BI analysts, data scientists, and data engineers. They need a safe beginner workflow that improves prompt quality and review habits without relying on deep coding tasks.

## Learner Goal

Use Copilot Chat in VS Code to:

- choose the right mode for a task,
- improve weak prompts,
- add the right context, and
- review AI output before accepting it.

## Starter State

- The learner has this training workspace open in VS Code.
- The module README exists at `materials/01-beginner-copilot-agent-best-practices/README.md`.
- The learner has GitHub Copilot Chat available in VS Code.

## Target State

By the end of the lab, the learner has:

- written one improved prompt,
- chosen an appropriate Copilot mode for three scenarios,
- captured observable evidence of review and validation,
- completed the validation checklist.

## Prerequisites And Setup

Goal of the step:
Confirm that the learner can access Copilot Chat and use a real workspace as context.

Exact action:

1. Open the Chat view in VS Code.
2. Confirm the agent picker is visible.
3. Open `materials/01-beginner-copilot-agent-best-practices/README.md`.

What success looks like:

- Chat opens.
- The learner can switch between Ask, Plan, and Agent.
- The module README is open in the editor.

Common failure mode and fix:

- If the agent picker is not visible, verify GitHub Copilot access and confirm that agents are enabled by policy in the learner's environment.

## Lab Tasks

### Task 1: Choose The Right Mode

Goal of the step:
Practice selecting Ask, Plan, or Agent based on task risk and scope.

Exact action:

For each scenario below, choose the mode you would start with and record your answer.

- Explain what `#codebase` does to a first-time learner.
- Draft a plan for a new beginner training module.
- Update a README after the structure has already been agreed.

Suggested prompt:

`Explain why Ask, Plan, or Agent is the best starting mode for each of these three scenarios, and keep the explanation beginner-friendly.`

Observable output:

- A short written answer in the chat transcript or a screenshot of the response.

Common failure mode and fix:

- If the answer is too generic, ask Copilot to justify each choice using risk, scope, and need for review.

### Task 2: Improve A Weak Prompt

Goal of the step:
Turn a vague request into a specific, constrained prompt.

Exact action:

Start from this weak prompt:

`Make this training better.`

Refine it so it includes a goal, scope, constraints, and expected output.

Suggested prompt:

`Rewrite this prompt for a beginner Copilot user. The task is to improve the open README, keep the change Windows-first, and change only one file: Make this training better.`

Observable output:

- The rewritten prompt saved in a note, screenshot, or chat transcript.

Common failure mode and fix:

- If the rewritten prompt is still broad, ask Copilot to make the output measurable and to name the exact file it should edit.

### Task 3: Add Context Explicitly

Goal of the step:
Practice using workspace context instead of relying on guesswork.

Exact action:

Ask Copilot to review the module README and suggest one improvement by referencing the file directly.

Suggested prompt:

`Review #file and suggest one improvement for first-time BI, DS, or DE learners. Do not edit anything yet.`

Observable output:

- A response that clearly references the open file and gives one focused suggestion.

Common failure mode and fix:

- If Copilot responds generically, use `#file` or paste the exact section you want reviewed.

### Task 4: Validate Before Accepting

Goal of the step:
Build the habit of reviewing AI output before treating it as correct.

Exact action:

Take one Copilot answer from the earlier tasks and verify it against the module README and one official source from the references file.

Suggested prompt:

`Compare your previous answer with the open README and summarize what still needs human verification.`

Observable output:

- A short list of what was confirmed and what still needs checking.

Common failure mode and fix:

- If the learner only restates the AI answer, require them to name at least one claim they checked against a source.

## Expected Observable Output

- A mode-selection response for three scenarios.
- One improved prompt.
- One context-aware review response tied to the module README.
- One short verification summary.

## Validation Checklist

- The learner can explain why they chose Ask, Plan, or Agent for each scenario.
- The learner improved a vague prompt into a constrained one.
- The learner used explicit context such as `#file`.
- The learner identified what still needed verification.
- The learner produced evidence a facilitator can review without needing access to the learner's machine.

## Reflection Tasks

- Which task changed the most once context was added?
- Which answer felt plausible but still needed verification?
- What is one repeated preference your team should capture in an instruction file?

## Solution Guidance

See `solution/README.md` for an example outcome and facilitator guidance.
