# Notebooks, SQL, And Pipelines With Copilot

## Learning Objectives

By the end of this module, learners should be able to:

- use Copilot safely with notebooks, SQL, and pipeline-oriented artifacts
- distinguish explanation, drafting, and implementation tasks in data workflows
- ask for reproducibility, validation, and business-context checks
- avoid common mistakes when using AI around data transformations and analysis
- define observable outputs for BI, DS, and DE tasks

## Prerequisites And Setup

Audience:

- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:

- Modules 01 through 04 completed or equivalent knowledge
- A practice workspace containing at least one notebook, SQL file, or pipeline-related README or script
- Copilot Chat available in VS Code

Success looks like:

- The learner can write targeted prompts for notebooks, SQL, or pipeline docs.
- The learner can ask Copilot for explanation without losing business meaning.
- The learner can define checks for reproducibility and correctness.

Common failure mode and fix:

- Failure: The learner asks Copilot to change data logic without specifying validation or business rules.
- Fix: State the intended behavior, required checks, and what must not change before asking for edits.

## Walkthrough

### Step 1. Choose the right task type

Goal of the step:

- Separate low-risk explanation tasks from higher-risk editing tasks.

Exact action:

- Identify whether the current need is explanation, summarization, checklist generation, or file editing.

What success looks like:

- The learner uses Ask for understanding and reserves Agent for constrained edits.

Common failure mode and fix:

- Failure: The learner starts with implementation before understanding the data artifact.
- Fix: Ask for a summary or plan first.

### Step 2. Use safe notebook prompts

Goal of the step:

- Work with notebooks without losing reproducibility.

Exact action:

- Ask for cell-by-cell summaries.
- Ask for missing prerequisites and environment notes.
- Ask for a reproducibility checklist instead of direct rewriting when the notebook intent is still unclear.

What success looks like:

- The learner gets an explanation or checklist that can be reviewed before any change is made.

Common failure mode and fix:

- Failure: The learner asks for major notebook rewrites without preserving assumptions.
- Fix: State what must remain unchanged and require validation notes.

Before and after example (DS -- forecasting notebook):

**Before:**

```python
from prophet import Prophet

model = Prophet()
model.fit(df)
forecast = model.predict(future)
fig = model.plot(forecast)
```

**After (AI-improved):**

```python
from prophet import Prophet

# Model config: default seasonality, linear growth
# Data: monthly_sales_v3.csv through 2025-12
# Forecast horizon: 12 months
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
)
model.fit(df)

future = model.make_future_dataframe(periods=12, freq="MS")
forecast = model.predict(future)

print(f"Forecast rows: {len(forecast)}")
print(f"Date range: {forecast['ds'].min()} to {forecast['ds'].max()}")
fig = model.plot(forecast)
```

Review question: Is weekly seasonality really irrelevant for your data? Is 12 months the right forecast window?

### Step 3. Use safe SQL prompts

Goal of the step:

- Review or improve SQL without changing business meaning accidentally.

Exact action:

- Ask Copilot to explain filters, joins, aggregations, and output columns.
- Ask for comments or documentation before asking for optimization.
- If asking for changes, require that the business logic remain the same.

What success looks like:

- The learner can explain the query before attempting edits.

Common failure mode and fix:

- Failure: The learner optimizes SQL without validating business output.
- Fix: Ask for preserved behavior and expected output checks.

Before and after example (BI -- monthly revenue report):

**Before:**

```sql
SELECT
    d.fiscal_month,
    SUM(f.net_revenue) AS net_revenue,
    SUM(f.net_revenue) - LAG(SUM(f.net_revenue))
        OVER (ORDER BY d.fiscal_month) AS mom_change
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
GROUP BY d.fiscal_month;
```

**After (AI-improved):**

```sql
-- Monthly revenue report with month-over-month change
-- Business owner: Finance, approved Q1 2026
-- Net Revenue = gross revenue minus returns and discounts
SELECT
    d.fiscal_month,
    SUM(f.net_revenue) AS net_revenue,
    LAG(SUM(f.net_revenue))
        OVER (ORDER BY d.fiscal_month) AS prior_month_revenue,
    SUM(f.net_revenue) - LAG(SUM(f.net_revenue))
        OVER (ORDER BY d.fiscal_month) AS mom_change,
    CASE
        WHEN LAG(SUM(f.net_revenue))
             OVER (ORDER BY d.fiscal_month) = 0 THEN NULL
        ELSE ROUND(
            (SUM(f.net_revenue) - LAG(SUM(f.net_revenue))
             OVER (ORDER BY d.fiscal_month))
            / LAG(SUM(f.net_revenue))
              OVER (ORDER BY d.fiscal_month) * 100, 2)
    END AS mom_change_pct
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
GROUP BY d.fiscal_month;
```

Review question: Is the net revenue definition correct? Does the team want the percentage column, or does it create confusion in the dashboard?

### Step 4. Use safe pipeline prompts

Goal of the step:

- Handle scripts and pipeline docs without creating operational surprises.

Exact action:

- Ask for a step-by-step explanation of the flow.
- Ask for validation checkpoints, failure points, and dependencies.
- Ask for safer documentation before changing orchestration logic.

What success looks like:

- The learner can identify upstream dependencies, outputs, and validation points.

Common failure mode and fix:

- Failure: The learner asks for pipeline changes without identifying dependencies.
- Fix: First request a dependency and validation map.

Before and after example (DE -- Azure Data Factory pipeline activity):

**Before:**

```yaml
activities:
  - name: copy_orders
    type: Copy
    source:
      type: AzureSqlSource
      query: "SELECT * FROM staging.orders"
    sink:
      type: ParquetSink
      path: "raw/orders/"
```

**After (AI-improved):**

```yaml
activities:
  - name: copy_orders
    type: Copy
    description: >-
      Daily copy from staging.orders to raw landing zone.
      Upstream: staging refresh must complete by 05:00 UTC.
    source:
      type: AzureSqlSource
      query: >
        SELECT order_id, customer_id, order_date, amount
        FROM staging.orders
        WHERE order_date >= '@{formatDateTime(
          adddays(utcnow(), -3), ''yyyy-MM-dd'')}'
    sink:
      type: ParquetSink
      path: "raw/orders/@{formatDateTime(utcnow(), 'yyyy/MM/dd')}/"
    policy:
      retry: 3
      retryIntervalInSeconds: 300
      timeout: "01:00:00"
```

Review question: Is `SELECT *` removal correct for your schema? Is the 3-day lookback right for your load pattern? Does your team use date-partitioned paths?

### Step 5. Require observable outputs

Goal of the step:

- Make data work reviewable.

Exact action:

- Add expected outputs such as:
  - documented assumptions
  - a validation checklist
  - sample result shape
  - reproducibility steps
  - known failure modes

What success looks like:

- The learner can verify whether the output is useful without relying on confidence alone.

Common failure mode and fix:

- Failure: The output sounds plausible but cannot be checked.
- Fix: Ask for explicit validation criteria and example outputs.

## Hands-On Lab

Scenario context:

- Your team wants to use Copilot safely with a notebook, SQL artifact, or pipeline file without losing context or data quality expectations.

Learner goal:

- Use Copilot to understand one data artifact and add one safe improvement or checklist.

Tasks:

1. Select one notebook, SQL file, or pipeline-related file.
2. Ask Copilot to explain it in plain language.
3. Ask Copilot to identify assumptions, dependencies, or reproducibility risks.
4. Ask for one safe supporting artifact such as a checklist, prerequisites section, or troubleshooting note.
5. Review the result and record one thing that still needs human validation.

Suggested learner prompts:

- `Explain this notebook for a new data scientist and list reproducibility gaps.`
- `Explain this SQL query in plain language for a BI analyst and identify any assumptions about joins or filters.`
- `Summarize this pipeline README and create a validation checklist for a data engineer.`
- `Add a short troubleshooting section to this file without changing the core workflow.`

Expected observable output:

- A plain-language explanation
- One checklist, prerequisites section, or troubleshooting note
- One recorded human validation item that still requires review

## Validation Checklist

- The learner can distinguish explanation tasks from editing tasks.
- The learner can write a safe prompt for a notebook, SQL file, or pipeline file.
- The learner can require reproducibility or validation details in the prompt.
- The learner can identify one aspect of the result that still needs human review.
- The learner can keep business rules or pipeline behavior explicit during edits.

## Reflection Tasks

- Which artifact type felt riskiest to edit with AI, and why?
- What validation rule matters most for your team: reproducibility, business correctness, or operational reliability?
- What type of explanation was most helpful before requesting edits?
- What would you never want Copilot to change without stronger review?

## References

- VS Code prompt engineering guide: <https://code.visualstudio.com/docs/copilot/guides/prompt-engineering-guide>
- VS Code AI best practices: <https://code.visualstudio.com/docs/copilot/best-practices>
- GitHub Copilot best practices: <https://docs.github.com/en/copilot/get-started/best-practices>
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
