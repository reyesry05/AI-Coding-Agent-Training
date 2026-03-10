# Presenter Deck: Notebooks, SQL, And Pipelines With Copilot

## Slide 1. Title
On-screen content:
- Notebooks, SQL, And Pipelines With Copilot
- Safe data-team workflows

Presenter notes:
- This module is where Copilot starts touching higher-risk artifacts. The message is simple: explain first, edit later.
- Connect this module to the prior two by stating that prompt quality and context quality now have to survive contact with real notebook, SQL, and pipeline artifacts. The next module turns those edits into formal review decisions.

## Slide 2. Learning Objectives
On-screen content:
- Use Copilot safely with notebooks, SQL, and pipelines
- Separate explanation from editing work
- Require reproducibility and validation checks
- Preserve business and operational meaning

Presenter notes:
- Reinforce that data workflows often look simple on the surface but hide important assumptions.

## Slide 3. Why Data Artifacts Need Extra Care
On-screen content:
- plausible output can still be wrong
- data work has hidden assumptions
- reproducibility and operations matter

Presenter notes:
- Emphasize that readable AI output is not the same as correct data behavior.

## Slide 4. Start With Explanation
On-screen content:
- explain first
- identify assumptions
- ask for missing prerequisites

Presenter notes:
- This is the default safe move before any change request.

## Slide 5. Notebook Workflow (DS) -- Before And After
On-screen content:
- Scenario: Copilot improves a forecasting notebook cell. Review before running.

**Before (original cell):**
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

- Review: Are the **data version**, **seasonality settings**, and **horizon** correct?
- Decision: Keep, Revise, or Reject?

Presenter notes:
- The AI added config comments, explicit seasonality flags, and a shape check. Ask: is weekly seasonality really irrelevant for your data? Is 12 months the right forecast window? The AI made reasonable defaults, but the data scientist must confirm they match the experiment design.

## Slide 6. SQL Workflow (BI) -- Before And After
On-screen content:
- Scenario: Copilot adds documentation and a guard to a revenue report query.

**Before (original):**
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

- Review: Is the **net revenue definition** correct? Is `prior_month_revenue` useful or noise?
- Decision: Keep, Revise, or Reject?

Presenter notes:
- The AI added a business-definition comment, a prior-month column for context, a percentage calculation, and a divide-by-zero guard. Ask: does your team want the percentage column, or does it create confusion in the dashboard? More columns are not always better. The BI analyst must decide what the end report actually needs.

## Slide 7. Pipeline Workflow (DE) -- Before And After
On-screen content:
- Scenario: Copilot improves an Azure Data Factory pipeline activity definition.

**Before (original YAML):**
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

- Review: Is `SELECT *` removal correct? Is the 3-day lookback right for your load pattern?
- Decision: Keep, Revise, or Reject?

Presenter notes:
- The AI replaced `SELECT *` with explicit columns, added a date filter with a 3-day lookback, date-partitioned the sink path, and added retry and timeout policies. Ask: is 3 days the right window? Does your team use date-partitioned paths? The changes look professional but every parameter needs validation against the actual pipeline SLA.

## Slide 8. Safe Improvement Types
On-screen content:
- checklist
- prerequisites section
- troubleshooting note
- validation note

Presenter notes:
- These are useful because they improve clarity without changing core logic.

## Slide 9. What Not To Delegate Too Early
On-screen content:
- major logic rewrites
- business rule changes
- dependency-sensitive pipeline edits

Presenter notes:
- Tell learners that the point is not to avoid AI. The point is to sequence AI use correctly.

## Slide 10. Observable Outputs
On-screen content:
- explanation
- assumptions list
- checklist
- human validation note

Presenter notes:
- Observable outputs create a reviewable trail.

## Slide 11. Review Questions
On-screen content:
- what changed
- what stayed the same
- what still needs human validation

Presenter notes:
- These three questions work across notebooks, SQL, and pipeline documentation.

## Slide 12. Artifact Risk Exercise
On-screen content:
- choose one artifact
- explain it
- identify risks
- add one low-risk improvement

Presenter notes:
- Keep the artifact small enough to review fully in the session.

## Slide 13. Readiness Check
On-screen content:
- learner can distinguish safe vs risky edits
- learner can preserve meaning
- learner can record human review items

Presenter notes:
- Use this to check that learners are not drifting into over-delegation.

## Slide 14. Risk Debrief
On-screen content:
- which artifact felt riskiest?
- what review rule matters most?

Presenter notes:
- Pull examples from BI, DS, and DE work separately if possible.

## Slide 15. References
On-screen content:
- VS Code prompt engineering guide
- VS Code AI best practices
- GitHub Copilot best practices
- Workspace module: materials/05-notebooks-sql-and-pipelines-with-copilot/README.md
- Workspace reference: references/copilot-agent-beginner-best-practices.md

Presenter notes:
- Pair the first-party docs with the local module and workspace reference so learners know where to find the examples used in training.
