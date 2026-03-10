# Lab: Notebooks, SQL, And Pipelines With Copilot

## Scenario Context
Your BI, DS, or DE team wants to use Copilot with data artifacts safely.
The goal is to understand one notebook, SQL file, or pipeline-related file and request one low-risk supporting improvement.

## Learner Goal
By the end of this lab, you should be able to:
- use Copilot to explain a data artifact
- request one low-risk improvement such as a checklist or troubleshooting note
- identify one thing that still requires human validation
- preserve business or operational meaning during the exercise

## Starter State
You begin with:
- a safe notebook, SQL file, pipeline README, or related script
- Copilot Chat available in VS Code
- no assumption that the file is ready for direct editing

## Target State
You finish with:
- one explanation of the chosen artifact
- one supporting improvement or checklist
- one recorded human validation item

## Prerequisites And Setup
Goal of the step:
- Choose a data artifact that can be reviewed safely.

Exact actions:
- Open a notebook, SQL file, or pipeline-related file.
- Make sure the file is safe to inspect and improve in a limited way.

What success looks like:
- You can explain what kind of artifact you chose and why it matters.

Common failure mode and fix:
- Failure: The selected artifact is too sensitive or too large for a first lab.
- Fix: Use a small supporting file or a representative sample instead.

## Lab Tasks

### Task 1. Ask For A Plain-Language Explanation
Goal of the step:
- Understand the artifact before asking for changes.

Exact action:
- Ask Copilot to explain the artifact for a BI analyst, data scientist, or data engineer.

What success looks like:
- You receive a useful explanation without changing the artifact.

Common failure mode and fix:
- Failure: The explanation is too generic.
- Fix: Mention the audience and artifact type explicitly.

### Task 2. Ask For Risks Or Assumptions
Goal of the step:
- Surface what still needs human understanding.

Exact action:
- Ask Copilot to list assumptions, dependencies, or reproducibility gaps.

What success looks like:
- You get a short list of things to verify.

Common failure mode and fix:
- Failure: The answer stays descriptive and avoids risks.
- Fix: Ask explicitly for assumptions, dependencies, or gaps.

### Task 3. Request One Low-Risk Improvement
Goal of the step:
- Add one reviewable improvement without changing core logic.

Exact action:
- Ask Copilot to add a checklist, prerequisites section, or troubleshooting note.

What success looks like:
- The output improves support content without changing business rules or core workflow.

Common failure mode and fix:
- Failure: The prompt invites logic changes.
- Fix: State that behavior and business meaning must remain unchanged.

### Task 4. Record One Human Validation Item
Goal of the step:
- Preserve accountability.

Exact action:
- Write down one thing a human still must verify.

What success looks like:
- You have one concrete review item tied to business logic, reproducibility, or operations.

Common failure mode and fix:
- Failure: The review note is vague.
- Fix: Tie it to a real dependency, filter, input, or operational check.

## Suggested Learner Prompts
- Explain this notebook for a new data scientist and list reproducibility gaps.
- Explain this SQL query for a BI analyst and identify any assumptions about joins or filters.
- Summarize this pipeline README and create a validation checklist for a data engineer.
- Add a short troubleshooting section to this file without changing the core workflow.

## Expected Observable Output
- One explanation
- One checklist, prerequisites section, or troubleshooting note
- One written human validation item

## Validation Checklist
- I can explain a data artifact before requesting edits.
- I can ask Copilot for assumptions or risks.
- I can request a low-risk supporting improvement.
- I can record one thing that still requires human review.

## Reflection Tasks
- Which artifact type felt safest or riskiest?
- What kind of human validation matters most for your work?
- What should Copilot help draft but not decide on its own?

## Solution Guidance
A complete solution should show:
- one plain-language explanation
- one safe supporting improvement
- one explicit human validation note
