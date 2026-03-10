# Presenter Deck: First Safe Prompts For Ask, Plan, And Agent

## Slide 1. Title
On-screen content:
- First Safe Prompts For Ask, Plan, And Agent
- Beginner module for BI, DS, and DE teams

Presenter notes:
- Frame this as the habit-building module. Learners are not trying to be clever with prompts. They are trying to be safe, specific, and reviewable.
- Assume module 02 setup is complete. This module turns product access into safer prompt habits and prepares learners for the context controls in module 04.

## Slide 2. Learning Objectives
On-screen content:
- Choose Ask, Plan, or Agent appropriately
- Improve vague prompts into safe prompts
- Add scope, output, and validation criteria
- Review Agent output before accepting it

Presenter notes:
- Reinforce that the first prompt sets the quality bar for the whole interaction.

## Slide 3. Why First Prompts Matter
On-screen content:
- Bad first prompts create bad first habits
- Safer prompts reduce wasted edits and rework
- Prompt quality matters more than prompt length

Presenter notes:
- Explain that AI often follows the level of specificity the user provides.

## Slide 4. Ask, Plan, And Agent At A Glance
On-screen content:
- Ask: explain, orient, summarize
- Plan: break work into reviewable steps
- Agent: perform bounded implementation work

Presenter notes:
- Position Ask as the lowest-risk starting point and Agent as the highest-autonomy option.

## Slide 5. Signs A Prompt Is Too Weak
On-screen content:
- vague goal
- unclear scope
- missing audience
- no validation method
- too much autonomy too early

Presenter notes:
- Give one bad example such as `make this better` and explain why it fails.

## Slide 6. Safe Prompt Formula
On-screen content:
- Goal
- Scope
- Audience
- Expected output
- Validation step

Presenter notes:
- Tell learners this is the easiest reusable template in the module.

## Slide 7. BI Example -- Prompt-Driven DAX Improvement
On-screen content:
- Scenario: Two prompts produce different DAX measure quality. Compare the outputs.

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

- Review: Which output is safer to approve? Why?

Presenter notes:
- The weak prompt produced a valid but uncommented measure with no guard. The specific prompt added a business-definition comment, a zero-revenue guard, and preserved the original logic. Ask learners: which would you feel confident merging into a shared Power BI model?

## Slide 8. DS Example -- Prompt-Driven Notebook Improvement
On-screen content:
- Scenario: Two prompts produce different notebook documentation quality.

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

- Review: Which output helps a teammate reproduce the experiment?

Presenter notes:
- The weak prompt generated a one-line comment that adds almost no value. The specific prompt produced a structured prerequisites block that another data scientist could actually use. Point out that the AI will match the precision of the prompt -- vague in, vague out.

## Slide 9. DE Example -- Prompt-Driven SQL Transformation Fix
On-screen content:
- Scenario: Two prompts produce different quality fixes for a pipeline SQL transform.

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

- Review: Which output is safe to deploy to production?

Presenter notes:
- The weak prompt produced a syntactically valid query but missed the NULL check, test-account filter, and had no operational context. The specific prompt gave the AI enough constraints to produce a production-ready transform. Ask: what would happen if the test-account filter was missing in your pipeline?

## Slide 10. Compare Outputs By Mode
On-screen content:
- Ask output: explanation
- Plan output: sequence
- Agent output: change proposal

Presenter notes:
- The value here is not just different text. The value is different risk and different review burden.

## Slide 11. Review Before Accepting
On-screen content:
- Inspect scope
- Check file count
- Verify one visible condition
- Reject or refine if needed

Presenter notes:
- Repeat the rule: never accept a change you cannot explain.

## Slide 12. Prompt Practice Drill
On-screen content:
- Write one Ask prompt
- Write one Plan prompt
- Write one Agent prompt
- Compare outputs and record one validation step

Presenter notes:
- Keep the exercise small. One file is enough.

## Slide 13. Readiness Check
On-screen content:
- Learner can distinguish modes
- Learner can improve a weak prompt
- Learner can constrain Agent output

Presenter notes:
- Use this as the instructor completion check.

## Slide 14. Team Debrief
On-screen content:
- Which mode feels safest to start with?
- What makes a prompt reviewable?

Presenter notes:
- Encourage examples from BI, DS, and DE work rather than abstract discussion.

## Slide 15. References
On-screen content:
- VS Code chat overview
- VS Code prompt engineering guide
- VS Code AI best practices
- Workspace reference: references/copilot-agent-beginner-best-practices.md

Presenter notes:
- Pair the official docs with the workspace reference so learners have both product guidance and a local baseline they can reuse.
