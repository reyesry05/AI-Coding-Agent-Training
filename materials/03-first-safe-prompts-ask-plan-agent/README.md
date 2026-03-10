# First Safe Prompts For Ask, Edit, Plan, And Agent

## Learning Objectives

By the end of this module, learners should be able to:

- explain when to use Ask, Edit, Plan, and Agent in VS Code
- write safer first prompts for BI, data science, and data engineering work
- add constraints, expected outputs, and validation steps to prompts
- recognize when a prompt is too vague for autonomous execution
- improve weak prompts into specific, reviewable requests

## Prerequisites And Setup

Audience:

- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:

- Module 01 completed or equivalent knowledge of beginner guardrails
- Module 02 completed or equivalent environment setup
- GitHub Copilot Chat available in VS Code
- A small workspace with one or more files that are safe to inspect

Success looks like:

- The learner can explain why Ask is lower risk than Agent.
- The learner can rewrite a vague prompt into a safer one.
- The learner can add expected outputs and validation criteria.

Common failure mode and fix:

- Failure: The learner jumps directly to Agent with a broad request.
- Fix: Restate the task as Ask or Plan first, define output boundaries, then hand off to Agent only if the scope is clear.

## Walkthrough

### Step 1. Understand the four modes

Goal of the step:

- Distinguish the safest starting point for a task.

Exact action:

- Review the roles of Ask, Edit, Plan, and Agent in the Chat view.
- Match each mode to a realistic BI, DS, or DE scenario.

GitHub Copilot in VS Code offers four interaction modes, ordered from least to most autonomous:

| Mode | Autonomy | Best For |
| --- | --- | --- |
| Ask | Lowest | Explanations, concept checks, understanding files |
| Edit | Low | Targeted inline changes to one or a few files |
| Plan | Medium | Multi-step tasks where you review the approach first |
| Agent | Highest | Bounded implementation spanning multiple files |

What success looks like:

- The learner can choose Ask for explanation, Edit for targeted changes, Plan for structure, and Agent for well-scoped implementation.

Common failure mode and fix:

- Failure: The learner treats all modes as interchangeable.
- Fix: Use one concrete example per mode and explain the risk difference.

### Step 2. Spot weak prompts

Goal of the step:

- Learn to identify prompts that are too broad or underspecified.

Exact action:

- Compare prompts such as `make this better` with more specific alternatives.
- Identify what is missing: scope, audience, output, or validation.

What success looks like:

- The learner can name at least three missing prompt elements.

Common failure mode and fix:

- Failure: The learner focuses only on wording style.
- Fix: Check for missing constraints and expected results, not just tone.

### Step 3. Add prompt structure

Goal of the step:

- Turn a broad request into a safe, reviewable prompt.

Exact action:

- Add these elements to a sample request:
  - goal
  - scope
  - audience
  - expected output
  - validation method

What success looks like:

- The rewritten prompt is specific enough that another person could review the result.

Common failure mode and fix:

- Failure: The prompt still leaves too many choices to the model.
- Fix: Constrain the number of files, type of output, and review expectations.

### Step 4. Practice Ask prompts

Goal of the step:

- Use Ask for low-risk orientation and understanding.

Exact action:

- Run Ask prompts such as:
  - `Explain what this SQL file does and summarize the business purpose in plain language.`
  - `Review this notebook and list the major steps without changing anything.`
  - `Describe the likely purpose of this data pipeline README.`

What success looks like:

- The learner gets a useful answer without triggering risky changes.

Common failure mode and fix:

- Failure: The learner asks Ask mode to perform implementation.
- Fix: Move implementation requests to Edit, Plan, or Agent only after understanding the task.

### Step 5. Practice Edit prompts

Goal of the step:

- Use Edit for targeted inline changes with full diff review.

Exact action:

- Run Edit prompts such as:
  - `Add a prerequisites section to this README.`
  - `Fix the column descriptions in this SQL file header comment.`
  - `Update the connection string placeholder in this config to use environment variables.`

What success looks like:

- The learner sees proposed inline diffs and can accept or reject each change.

Common failure mode and fix:

- Failure: The learner uses Edit for tasks that span many files.
- Fix: Switch to Plan or Agent when the scope grows beyond a few targeted files.

### Step 6. Practice Plan prompts

Goal of the step:

- Use Plan to structure work before any edits happen.

Exact action:

- Run Plan prompts such as:
  - `Create a step-by-step plan to improve this Power BI data dictionary README for new analysts.`
  - `Create a plan to add validation notes to this notebook workflow for reproducibility.`
  - `Create a plan to document deployment checks for this data pipeline.`

What success looks like:

- The learner receives a sequence that can be reviewed before execution.

Common failure mode and fix:

- Failure: The plan is too generic to evaluate.
- Fix: Ask for phases, deliverables, and validation checks in the plan.

### Step 7. Practice Agent prompts safely

Goal of the step:

- Use Agent only after the task is bounded and reviewable.

Exact action:

- Run Agent prompts such as:
  - `Create a draft validation checklist for this BI lab README. Do not edit more than one file.`
  - `Add a beginner-friendly prerequisites section to this notebook lab README. Keep the existing structure.`
  - `Update this pipeline lab to include one troubleshooting section and one validation checklist.`

What success looks like:

- The learner gets a focused change set they can review easily.

Common failure mode and fix:

- Failure: The agent changes more than expected.
- Fix: Reduce the prompt scope and specify file limits before rerunning.

## Hands-On Lab

Scenario context:

- You are helping a BI, DS, or DE team write better first prompts so they can use Copilot without over-delegating.

Learner goal:

- Compare Ask, Edit, Plan, and Agent prompts and produce one safe prompt for each mode.

Tasks:

1. Find one file in the workspace that is safe to inspect.
2. Write one Ask prompt for explanation only.
3. Write one Edit prompt for a targeted inline change.
4. Write one Plan prompt for a structured improvement.
5. Write one Agent prompt with clear scope and validation.
6. Run the prompts and compare the results.
7. Record which prompt felt safest and why.

Suggested learner prompts:

- `Explain this README in plain language for a first-time BI analyst.`
- `Add a prerequisites section to this notebook README.` (Edit mode)
- `Create a plan to improve this notebook README for reproducibility and onboarding.`
- `Add a short validation checklist to this data pipeline lab README. Do not change any other file.`
- `Before making changes, ask clarifying questions if the file purpose is ambiguous.`

Expected observable output:

- One Ask response
- One Edit diff review
- One Plan response
- One constrained Agent result or draft
- A short note explaining why the Agent prompt was safe enough to run

## Prompt Quality Examples

Each example below shows what a weak prompt and a specific prompt produce. The specific prompt gives the AI enough constraints to produce reviewable output.

### BI Example -- DAX Measure Improvement

**Weak prompt:** `make this measure better`

**AI output from weak prompt:**

```dax
Gross Margin =
SUMX(Sales, Sales[Revenue] - Sales[Cost])
```

**Specific prompt:** `Add error handling for zero-revenue months and a comment explaining the business definition. Do not change the calculation logic.`

**AI output from specific prompt:**

```dax
-- Gross Margin: Revenue minus Cost of Goods Sold.
-- Finance-approved definition as of Q1 2026.
Gross Margin =
VAR _revenue = SUM(Sales[Revenue])
VAR _cost = SUM(Sales[Cost])
RETURN
    IF(_revenue = 0, BLANK(), _revenue - _cost)
```

Review question: Which output is safer to approve for a shared Power BI model?

### DS Example -- Notebook Prerequisites Cell

**Weak prompt:** `add documentation to this notebook`

**AI output from weak prompt:**

```python
# This notebook trains a model and prints accuracy.
```

**Specific prompt:** `Add a prerequisites cell listing the Python version, required packages with versions, data source path, and random seed. Do not modify any existing cells.`

**AI output from specific prompt:**

```python
"""
Prerequisites
-------------
Python: 3.12+
Packages: pandas==2.2, scikit-learn==1.5, matplotlib==3.9
Data: data/churn_v2.1.csv (exported 2026-02-15)
Random seed: 42 (used in train_test_split and model init)

Run `pip install -r requirements.txt` before executing.
"""
```

Review question: Which output helps a teammate reproduce the experiment?

### DE Example -- SQL Pipeline Transform

**Weak prompt:** `fix this query`

**AI output from weak prompt:**

```sql
SELECT
    order_id, customer_id, order_date,
    COALESCE(amount, 0) AS amount
FROM staging.raw_orders
WHERE order_date >= '2026-01-01';
```

**Specific prompt:** `This query loads from staging.raw_orders into warehouse.fact_orders. Add a NULL check for order_id, filter out test accounts (customer_id < 1000), and add a comment noting the upstream dependency and refresh schedule.`

**AI output from specific prompt:**

```sql
-- Source: staging.raw_orders (refreshed daily at 04:00 UTC)
-- Upstream dependency: raw_orders must complete before this runs
SELECT
    order_id,
    customer_id,
    order_date,
    COALESCE(amount, 0) AS amount
FROM staging.raw_orders
WHERE order_id IS NOT NULL       -- reject incomplete records
  AND customer_id >= 1000        -- exclude test accounts
  AND order_date >= '2026-01-01';
```

Review question: What would happen if the test-account filter was missing in your pipeline?

## Validation Checklist

- The learner can explain the difference between Ask, Edit, Plan, and Agent.
- The learner can identify at least three elements of a strong first prompt.
- The learner can rewrite a vague request into a safer one.
- The learner can create one low-risk prompt for each mode.
- The learner can describe one validation check before accepting Agent output.

## Reflection Tasks

- Which mode felt most appropriate for your first task, and why?
- What changed most when you added constraints to the prompt?
- What is one sign that a prompt is too vague for Agent mode?
- Which kind of work in your team should usually start with Plan instead of Agent?

## References

- VS Code chat overview: <https://code.visualstudio.com/docs/copilot/chat/copilot-chat>
- VS Code prompt engineering guide: <https://code.visualstudio.com/docs/copilot/guides/prompt-engineering-guide>
- VS Code AI best practices: <https://code.visualstudio.com/docs/copilot/best-practices>
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
- [GitHub Copilot Reimagine Overview](../../references/github-copilot-reimagine-overview.md)
