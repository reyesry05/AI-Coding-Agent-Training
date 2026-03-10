# Presenter Deck: Review And Verify AI Output For Data Work

## Slide 1. Title
On-screen content:
- Review And Verify AI Output For Data Work
- BI, DS, and DE review habits

Presenter notes:
- This module is about keeping accountability where it belongs: with the team using the output.
- Start by recapping the artifact-level risks from module 05, then shift the conversation from editing safely to deciding what can actually be kept, revised, or rejected before repo-backed work begins.

## Slide 2. Learning Objectives
On-screen content:
- identify data-team-specific risks
- review beyond wording and style
- document human validation work
- make keep, revise, or reject decisions

Presenter notes:
- State clearly that style review is not enough for data work.

## Slide 3. Why Review Is Different In Data Work
On-screen content:
- business meaning can drift
- reproducibility can break
- operational assumptions can be missed

Presenter notes:
- Use one short example from each audience if possible.

## Slide 4. Review Categories
On-screen content:
- business correctness
- reproducibility
- operational reliability
- scope and fit

Presenter notes:
- This gives learners a reusable review checklist.

## Slide 5. BI Review Lens -- Spot The Business Logic Error
On-screen content:
- Scenario: Copilot rewrote a DAX measure. Find the mistake before approving.

**Original (approved definition):**
```dax
Net Revenue =
    SUM(Sales[GrossRevenue]) - SUM(Sales[Returns]) - SUM(Sales[Discounts])
```

**AI-rewritten version:**
```dax
Net Revenue =
    SUM(Sales[GrossRevenue]) - SUM(Sales[Returns])
```

- What changed? The AI **dropped the Discounts subtraction**.
- Impact: Net revenue will be overstated in every report using this measure.
- Verdict: **Reject.** The AI simplified the formula but broke the business definition.

Presenter notes:
- This is a realistic and dangerous scenario. The AI-rewritten measure looks cleaner and is syntactically valid. A style-only review would approve it. But comparing to the original reveals that Discounts was silently dropped. Ask learners: how would you catch this without the side-by-side? Answer: always compare to the approved definition, not just to syntax.

## Slide 6. DS Review Lens -- Spot The Reproducibility Gap
On-screen content:
- Scenario: Copilot added a preprocessing step to a notebook. Find the reproducibility risk.

**Original cell:**
```python
df = pd.read_csv("experiment_data.csv")
df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
```

**AI-modified cell:**
```python
df = pd.read_csv("experiment_data.csv")
df = df.sample(frac=1).reset_index(drop=True)  # shuffle data
df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
```

- What changed? The AI added `df.sample(frac=1)` **without a random seed**.
- Impact: Every run produces a different shuffle before the split. `random_state=42` in `train_test_split` no longer guarantees the same split.
- Verdict: **Revise.** Add `random_state=42` to `df.sample()` or remove the shuffle since `train_test_split` already randomizes.

Presenter notes:
- This is subtle. The AI added a preprocessing step that looks reasonable but defeats the existing reproducibility guard. The `random_state` in `train_test_split` becomes meaningless if the input data order changes every run. Ask learners: would a code-only review catch this? Usually not -- you need to think about the data flow.

## Slide 7. DE Review Lens -- Spot The Dependency Issue
On-screen content:
- Scenario: Copilot optimized a pipeline SQL query. Find the operational risk.

**Original query:**
```sql
INSERT INTO warehouse.fact_orders
SELECT o.order_id, o.amount, c.segment
FROM staging.orders o
JOIN staging.customers c ON o.customer_id = c.customer_id
WHERE o.load_date = CURRENT_DATE;
```

**AI-optimized query:**
```sql
INSERT INTO warehouse.fact_orders
SELECT o.order_id, o.amount, c.segment
FROM staging.orders o
JOIN staging.customers c ON o.customer_id = c.customer_id
JOIN staging.products p ON o.product_id = p.product_id
WHERE o.load_date = CURRENT_DATE;
```

- What changed? The AI added a **JOIN to staging.products** that was not in the original.
- Impact: If `staging.products` is not refreshed before this job runs, the join produces stale or missing data. The pipeline now has an **undeclared upstream dependency**.
- Verdict: **Reject.** The new join adds a dependency that is not in the DAG schedule.

Presenter notes:
- The AI added a join that looks useful (product info enrichment) but introduced a dependency the pipeline scheduler does not know about. If `staging.products` loads at 06:00 and this job runs at 05:00, you get yesterday's product data or missing rows. Ask: how does your team track which tables a job depends on? That is the review question for DE work.

## Slide 8. What Counts As Evidence
On-screen content:
- source file comparison
- explicit checklist
- visible validation note
- diff review

Presenter notes:
- Confidence in the AI is not evidence. Observable review is evidence.

## Slide 9. Human Validation Boundaries
On-screen content:
- what AI can draft
- what humans must still decide

Presenter notes:
- Ask learners to name one decision AI should not make for their team.

## Slide 10. Keep, Revise, Or Reject
On-screen content:
- keep when bounded and correct
- revise when useful but incomplete
- reject when meaning or risk is unclear

Presenter notes:
- Encourage decisive review instead of default acceptance.

## Slide 11. Build Review Into Prompts
On-screen content:
- preserve meaning
- include validation
- list assumptions
- limit scope

Presenter notes:
- Better prompts reduce review effort but do not remove review responsibility.

## Slide 12. Review Decision Exercise
On-screen content:
- review one AI result
- identify one risk
- identify one human follow-up
- make a decision

Presenter notes:
- Keep the artifact small and specific.

## Slide 13. Decision Readiness Check
On-screen content:
- learner can name a risk category
- learner can review beyond style
- learner can justify a decision

Presenter notes:
- Require evidence for the decision.

## Slide 14. Approval Debrief
On-screen content:
- what risk matters most for your team?
- what should always need human approval?

Presenter notes:
- This is where team standards start to emerge.

## Slide 15. References
On-screen content:
- VS Code AI best practices
- GitHub Copilot best practices
- Workspace module: materials/06-review-and-verify-ai-output-for-data-work/README.md
- Workspace reference: references/copilot-agent-beginner-best-practices.md

Presenter notes:
- Encourage teams to turn repeatable review rules into standard practice and record them where new learners can find them.
