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

You are a first-time GitHub Copilot user in VS Code. You need to improve your prompting and review habits before using higher-autonomy agent workflows.

Available files:

- `materials/01-beginner-copilot-agent-best-practices/README.md`
- `references/copilot-agent-beginner-best-practices.md`

What to do first:

1. Open the module README.
2. Open the Chat view.
3. Confirm Ask, Edit, Plan, and Agent are available.
4. Start Task 1 in the lab README.

Minimum acceptance criteria:

- Chat is available.
- The learner can reference the open file in a prompt.
- The learner can explain the difference between Ask, Edit, Plan, and Agent.

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
- The learner can switch between Ask, Edit, Plan, and Agent.
- The module README is open in the editor.

Common failure mode and fix:

- If the agent picker is not visible, verify GitHub Copilot access and confirm that agents are enabled by policy in the learner's environment.

## Lab Tasks

### Task 1: Choose The Right Mode

Goal of the step:
Practice selecting Ask, Edit, Plan, or Agent based on task risk and scope.

Exact action:

For each scenario below, choose the mode you would start with and record your answer.

- Explain what `#codebase` does to a first-time learner.
- Draft a plan for a new beginner training module.
- Update a README after the structure has already been agreed.

Suggested prompt:

`Explain why Ask, Edit, Plan, or Agent is the best starting mode for each of these three scenarios, and keep the explanation beginner-friendly.`

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

- The learner can explain why they chose Ask, Edit, Plan, or Agent for each scenario.
- The learner improved a vague prompt into a constrained one.
- The learner used explicit context such as `#file`.
- The learner identified what still needed verification.
- The learner produced evidence a facilitator can review without needing access to the learner's machine.

## Reflection Tasks

- Which task changed the most once context was added?
- Which answer felt plausible but still needed verification?
- What is one repeated preference your team should capture in an instruction file?

## Solution Guidance

### Facilitator Notes

This lab is designed to measure beginner behavior, not technical depth. The expected outcome is that learners choose safer modes earlier, improve prompt specificity, add context explicitly, and validate output before accepting it.

### Example Outcomes

#### Task 1: Mode Selection

- Explain `#codebase` to a beginner: start with Ask.
- Draft a plan for a new module: start with Plan.
- Update a README after scope is agreed: start with Agent, or Plan first if the learner is uncertain.

#### Task 2: Improved Prompt

Example:

`Review materials/01-beginner-copilot-agent-best-practices/README.md and add one beginner-friendly validation checklist section. Keep the content Windows-first, do not create new files, and explain the proposed change before editing.`

#### Task 3: Context Use

Expected behavior:

- The learner references `#file` or works with the active README.
- The response is tied to the actual content instead of generic training advice.

#### Task 4: Validation Habit

Expected behavior:

- The learner names one claim that required checking.
- The learner compares the answer against the README and an official source.
- The learner can articulate what remains uncertain.

### Observable Evidence A Facilitator Can Accept

- Screenshot of mode selection answers.
- Screenshot or transcript of the improved prompt.
- Screenshot or transcript of a context-aware review response.
- Short written note listing what was verified.

### Common Failure Modes And Recovery

- Learner chooses Agent for all tasks.
  Recovery: ask them to justify the autonomy level and re-evaluate the risk.
- Learner writes a longer prompt that is still vague.
  Recovery: ask them to add file scope and a measurable expected output.
- Learner accepts answers without verification.
  Recovery: require one checked claim from the references file.
