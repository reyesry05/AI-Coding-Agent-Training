# Lab: First Safe Prompts For Ask, Edit, Plan, And Agent

## Scenario Context

Your BI, DS, or DE team is new to GitHub Copilot agents and needs a safe way to start.
The goal is to practice writing one good first prompt for Ask, one for Edit, one for Plan, and one for Agent without over-delegating.

## Learner Goal

By the end of this lab, you should be able to:

- write one safe prompt for each mode
- explain why the four prompts are not interchangeable
- compare the outputs from Ask, Edit, Plan, and Agent
- record one validation step before accepting Agent output

## Starter State

You begin with:

- a safe workspace open in VS Code
- Copilot Chat available
- at least one file that can be explained or improved safely

## Target State

You finish with:

- one Ask prompt result
- one Plan response
- one bounded Agent result
- one note explaining why the Agent prompt was safe enough to run

## Prerequisites And Setup

Goal of the step:

- Confirm the workspace is ready for a low-risk prompt exercise.

Exact actions:

- Open a safe workspace in VS Code.
- Pick one file that is easy to understand and review.
- Open Chat.

What success looks like:

- You can point to the file you will use and explain why it is low risk.

Common failure mode and fix:

- Failure: You pick a file that is too complex or too risky to edit.
- Fix: Use a README, notebook README, or a simple supporting file first.

## Lab Tasks

### Task 1. Write An Ask Prompt

Goal of the step:

- Use Ask for orientation and explanation only.

Exact action:

- Ask Copilot to explain the chosen file in plain language for a BI, DS, or DE learner.

What success looks like:

- The result explains the file without making changes.

Common failure mode and fix:

- Failure: Your prompt asks for explanation and edits together.
- Fix: Keep the first prompt explanation-only.

### Task 2. Write A Plan Prompt

Goal of the step:

- Use Plan to structure a safe improvement.

Exact action:

- Ask Copilot to create a short plan for improving the same file for beginner use.

What success looks like:

- The result gives steps, not direct edits.

Common failure mode and fix:

- Failure: The plan is too generic.
- Fix: Add audience, output type, and validation expectations.

### Task 3. Write An Agent Prompt

Goal of the step:

- Use Agent for one bounded, reviewable change.

Exact action:

- Ask Copilot to make one small improvement, such as adding a checklist or prerequisites section.
- Limit the change to one file.

What success looks like:

- The result is a small change set that is easy to review.

Common failure mode and fix:

- Failure: The prompt allows a broad rewrite.
- Fix: Limit file count and specify what must remain unchanged.

### Task 4. Compare The Three Outputs

Goal of the step:

- Understand what changed across the four modes.

Exact action:

- Record how Ask, Edit, Plan, and Agent responded differently.

What success looks like:

- You can explain why Agent was the last mode used.

Common failure mode and fix:

- Failure: You compare only response length.
- Fix: Compare risk, output type, and reviewability.

### Task 5. Review Before Accepting

Goal of the step:

- Practice safe review habits.

Exact action:

- Review the Agent result and record one validation step.

What success looks like:

- You can state one reason to accept, revise, or reject the change.

Common failure mode and fix:

- Failure: You accept the result because it sounds good.
- Fix: Check the exact file, exact scope, and one visible quality condition.

## Suggested Learner Prompts

- Explain this file in plain language for a new BI analyst.
- Create a short plan to improve this file for onboarding a new data team member.
- Add a validation checklist to this file and do not modify any other file.
- Before making changes, ask clarifying questions if the file purpose is ambiguous.

## Expected Observable Output

- One Ask explanation
- One Plan response
- One small Agent result
- One written review note

## Validation Checklist

- I can write one safe prompt for Ask, Edit, Plan, and Agent.
- I can explain why each mode produced a different type of output.
- I can constrain an Agent prompt to one file.
- I can record one validation step before accepting output.

## Reflection Tasks

- Which prompt needed the most revision before it felt safe?
- What made the Agent prompt reviewable?
- Which mode would your team underuse or overuse most often?

## Solution Guidance

A complete solution should show:

- three distinct prompts for three different modes
- one bounded Agent request
- one explicit validation note before accepting output
