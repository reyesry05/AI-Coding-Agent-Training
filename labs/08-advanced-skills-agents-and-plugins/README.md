# Lab: Advanced Skills, Agents, And Plugins

## Scenario Context
Your team wants to formalize one advanced Copilot workflow.
The team keeps mixing up reusable guidance, execution behavior, and external integration needs.

## Learner Goal
By the end of this lab, you should be able to:
- classify a workflow into skill, agent, and plugin responsibilities
- justify why each part is needed or not needed
- define one governance rule and one manual checkpoint
- produce a reviewable advanced workflow outline

## Starter State
You begin with:
- a safe BI, DS, or DE workflow that your team repeats
- modules 01 through 07 completed or equivalent knowledge
- no final decision yet about which advanced mechanism to use

## Target State
You finish with:
- one workflow classification note
- one explanation of the chosen mechanism mix
- one governance rule
- one human approval step
- one manual step that should remain outside automation

## Prerequisites And Setup
Goal of the step:
- Choose a realistic workflow that is valuable but safe to discuss.

Exact actions:
- Pick a reporting, notebook, SQL, validation, or pipeline workflow.
- Write the expected outcome in one sentence.
- Open Chat.

What success looks like:
- You can describe the workflow clearly enough to classify it.

Common failure mode and fix:
- Failure: The workflow is too broad to reason about safely.
- Fix: Narrow it to one observable outcome.

## Lab Tasks

### Task 1. Define The Workflow Outcome
Goal of the step:
- Anchor the design to one concrete outcome.

Exact action:
- Write the workflow outcome in one sentence.

What success looks like:
- The outcome is specific, observable, and reviewable.

Common failure mode and fix:
- Failure: The outcome is too vague, such as automate BI reporting.
- Fix: Rewrite it as one bounded result.

### Task 2. Separate Skill, Agent, And Plugin Needs
Goal of the step:
- Distinguish guidance, execution, and integration responsibilities.

Exact action:
- Label which parts belong in a skill, which belong in an agent, and which require plugin access.

What success looks like:
- Each mechanism has a clear role.

Common failure mode and fix:
- Failure: The same responsibility appears in all three categories.
- Fix: Reassign each responsibility to one primary owner.

### Task 3. Justify The Design
Goal of the step:
- Make the design reviewable.

Exact action:
- Write one reason for each selected mechanism.

What success looks like:
- Another reviewer can understand why the design is shaped this way.

Common failure mode and fix:
- Failure: The reasons only describe preference.
- Fix: Tie each reason to repeatability, execution complexity, or capability access.

### Task 4. Add Governance Rules
Goal of the step:
- Prevent unsafe or unreviewable automation.

Exact action:
- Define one validation rule, one human approval checkpoint, and one step that must remain manual.

What success looks like:
- The workflow has clear control points.

Common failure mode and fix:
- Failure: The controls are generic, such as review everything.
- Fix: Name the exact checkpoint and artifact to review.

### Task 5. Review The Final Classification
Goal of the step:
- Confirm the design still uses the smallest safe mechanism mix.

Exact action:
- Ask whether any chosen mechanism can be removed without losing capability or control.

What success looks like:
- The final design is simpler or more defensible.

Common failure mode and fix:
- Failure: You keep extra complexity because it sounds advanced.
- Fix: Remove anything that does not add clear value.

## Suggested Learner Prompts
- For this workflow, separate what belongs in a skill, an agent, and a plugin.
- Help me decide whether this repeated notebook review should stay a checklist or become an agent workflow.
- Design a safe advanced Copilot workflow for a pipeline failure investigation with clear validation and approval steps.

## Expected Observable Output
- One written workflow outcome
- One classification note with skill, agent, and plugin roles
- One justification for each selected role
- One validation rule
- One human approval step
- One manual step

## Validation Checklist
- I can define the workflow outcome clearly.
- I can separate skill, agent, and plugin responsibilities.
- I can justify the mechanism mix.
- I can define a specific governance control.
- I can identify at least one step that should remain manual.

## Reflection Tasks
- What part of your workflow needed a skill more than an agent?
- What integration access would create the most risk?
- What is the smallest version of this advanced workflow you could pilot first?

## Solution Guidance
A complete solution should show:
- one bounded workflow outcome
- one role breakdown for skill, agent, and plugin
- one clear governance rule
- one explicit manual checkpoint