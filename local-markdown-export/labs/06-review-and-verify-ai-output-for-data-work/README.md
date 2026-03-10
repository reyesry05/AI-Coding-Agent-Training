# Lab: Review And Verify AI Output For Data Work

## Scenario Context
Your team wants to use Copilot output productively without lowering quality.
The goal is to review one AI-generated result using data-team-specific checks and document what still needs human validation.

## Learner Goal
By the end of this lab, you should be able to:
- review AI output beyond style and wording
- identify one business, reproducibility, or operational risk
- record one item that requires human approval
- decide whether a result is ready, needs revision, or should be rejected

## Starter State
You begin with:
- one file in the workspace that can be discussed or lightly improved
- one AI-generated output such as a summary, checklist, or small edit

## Target State
You finish with:
- one reviewed AI-generated result
- one review note explaining what is acceptable
- one review note explaining what still needs human validation
- one keep, revise, or reject decision

## Prerequisites And Setup
Goal of the step:
- Prepare one result that can be reviewed with a checklist.

Exact actions:
- Use an existing Copilot result or generate one small draft.
- Open the relevant file or response in VS Code.

What success looks like:
- You have one concrete artifact to review.

Common failure mode and fix:
- Failure: The chosen result is too large to review effectively.
- Fix: Use a smaller draft such as one checklist, section, or explanation.

## Lab Tasks

### Task 1. Review The Result For Meaning
Goal of the step:
- Check whether the output preserves business or workflow meaning.

Exact action:
- Compare the result to the original ask and source material.

What success looks like:
- You can state whether the meaning stayed intact.

Common failure mode and fix:
- Failure: You focus only on grammar or readability.
- Fix: Compare meaning, not just style.

### Task 2. Review The Result For Data-Team Risk
Goal of the step:
- Apply a BI, DS, or DE review lens.

Exact action:
- Check for one of these categories:
  - business correctness
  - reproducibility
  - operational reliability

What success looks like:
- You can identify at least one risk category that matters.

Common failure mode and fix:
- Failure: You name a risk too generically.
- Fix: Tie the risk to a join, prerequisite, dependency, schedule, or validation step.

### Task 3. Record Human Validation Work
Goal of the step:
- Make the boundary of AI assistance explicit.

Exact action:
- Write down one thing that still requires human judgment.

What success looks like:
- The note clearly states what must be checked by a person.

Common failure mode and fix:
- Failure: The note says only `review later`.
- Fix: State exactly what needs confirmation.

### Task 4. Make A Decision
Goal of the step:
- Decide whether the result is acceptable now.

Exact action:
- Mark the result as keep, revise, or reject.
- Give one reason for the decision.

What success looks like:
- The decision is tied to a concrete review point.

Common failure mode and fix:
- Failure: The decision is based on confidence in the AI.
- Fix: Base the decision on evidence from the review.

## Suggested Learner Prompts
- Add a short validation checklist to this file and explicitly list what still needs human review.
- Explain this query and identify assumptions that a BI analyst should verify.
- Summarize this notebook and list any reproducibility risks.
- Review this pipeline documentation and list operational checks that still require a human decision.

## Expected Observable Output
- One AI-generated result
- One review note
- One human-validation note
- One keep, revise, or reject decision

## Validation Checklist
- I can review output for more than wording.
- I can identify one BI, DS, or DE risk.
- I can record one explicit human validation item.
- I can decide whether to keep, revise, or reject the result.

## Reflection Tasks
- What review category mattered most in your example?
- What kind of result should never be accepted without deeper human review?
- What review rule should become standard for your team?

## Solution Guidance
A complete solution should show:
- one reviewed result
- one explicit risk callout
- one human validation note
- one evidence-based decision
