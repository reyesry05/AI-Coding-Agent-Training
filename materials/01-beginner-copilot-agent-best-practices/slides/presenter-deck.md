# Presenter Deck

## Slide 1: Beginner Best Practices For GitHub Copilot Agents In VS Code

On-screen content:

- Audience: BI, DS, and DE practitioners
- Focus: effective beginner workflows in VS Code
- Outcome: better prompts, better review, safer usage

Presenter notes:

Open by framing Copilot as a collaborator, not an authority. State that this module is intentionally about habits and workflow, not product marketing.

## Slide 2: Why Beginners Need A Method

On-screen content:

- Vague prompts lead to vague output
- More autonomy increases review responsibility
- Good habits reduce rework and confusion

Presenter notes:

Explain that beginner frustration often comes from using the most powerful mode too early or asking for too much in one turn.

## Slide 3: The Three Built-In Modes

On-screen content:

- Ask: explain and orient
- Plan: propose steps before changes
- Agent: execute across files and tools

Presenter notes:

Clarify that the safest beginner pattern is Ask, then Plan, then Agent. This reduces surprise and improves teachability.

## Slide 4: Choose The Lightest Tool That Works

On-screen content:

- Use Ask for understanding
- Use Plan for shaping work
- Use Agent for clear, bounded execution

Presenter notes:

Give one example per audience:

- BI: Ask for an explanation of a reporting workflow.
- DS: Plan a notebook cleanup before any edits.
- DE: Agent can update a pipeline README after scope is agreed.

## Slide 5: What A Good Beginner Prompt Includes

On-screen content:

- Goal
- Scope
- Constraints
- Expected output
- Relevant context

Presenter notes:

Show how a short but precise prompt beats a long but vague request. Emphasize that clarity matters more than verbosity.

## Slide 6: Context Improves Quality

On-screen content:

- Active file and selection
- `#file`, `#folder`, `#codebase`
- `#fetch` for official docs
- `@vscode` for product-specific questions

Presenter notes:

Explain that context is one of the fastest ways to reduce generic or incorrect answers. Mention that official documentation is the safest anchor for training material.

## Slide 7: Demo Or Hands-On Moment

On-screen content:

- Weak prompt: `Make this training better`
- Better prompt: `Review #file and add a beginner validation checklist. Keep it Windows-first and change only this file.`
- Result: smaller, reviewable output

Presenter notes:

This slide sits in the middle third of the deck and should be interactive. Ask the audience to identify what improved in the second prompt. If time permits, run the prompt live in VS Code.

## Slide 8: Review Before You Accept

On-screen content:

- Read the diffs
- Check the command implications
- Compare output to the request
- Reject changes you cannot explain

Presenter notes:

Reinforce the core beginner rule: never accept a change you cannot explain. This is the habit that keeps enthusiasm from becoming hidden risk.

## Slide 9: BI Before And After -- SQL KPI View

On-screen content:

- Scenario: Copilot improves a sales KPI view. Review the diff before approving.

**Before (original):**
```sql
CREATE VIEW vw_sales_kpis AS
SELECT
    region,
    SUM(revenue) AS revenue,
    SUM(cost) AS cost,
    SUM(revenue) - SUM(cost) AS margin
FROM sales
GROUP BY region;
```

**After (AI-improved):**
```sql
CREATE VIEW vw_sales_kpis AS
SELECT
    region,
    SUM(revenue)              AS total_revenue,
    SUM(cost)                 AS total_cost,
    SUM(revenue) - SUM(cost)  AS gross_margin,
    CASE
        WHEN SUM(revenue) = 0 THEN 0
        ELSE ROUND((SUM(revenue) - SUM(cost))
             / SUM(revenue) * 100, 2)
    END                       AS gross_margin_pct
FROM sales
GROUP BY region;
```

- Review: Did the AI change the **definition** of margin or just add clarity?
- Decision: Keep, Revise, or Reject?

Presenter notes:

Walk through line by line. The AI renamed `margin` to `gross_margin` and added a percentage column. Ask: does your finance team define margin as gross or net? If the approved term is `margin`, the rename could break downstream reports. This is the core approval skill -- the code looks better, but the reviewer must confirm business meaning is preserved.

## Slide 10: DS Before And After -- Notebook Cell

On-screen content:

- Scenario: Copilot adds reproducibility guards to a churn-model notebook cell.

**Before (original):**
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("churn_data.csv")
X_train, X_test, y_train, y_test = train_test_split(
    df.drop("churned", axis=1), df["churned"], test_size=0.2
)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
print(f"Accuracy: {model.score(X_test, y_test):.3f}")
```

**After (AI-improved):**
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

RANDOM_SEED = 42
DATA_PATH = "churn_data.csv"  # v2.1, exported 2026-02-15

df = pd.read_csv(DATA_PATH)
print(f"Rows: {len(df)}, Columns: {list(df.columns)}")

X_train, X_test, y_train, y_test = train_test_split(
    df.drop("churned", axis=1), df["churned"],
    test_size=0.2, random_state=RANDOM_SEED
)
model = RandomForestClassifier(
    n_estimators=100, random_state=RANDOM_SEED
)
model.fit(X_train, y_train)
print(f"Accuracy: {model.score(X_test, y_test):.3f}")
```

- Review: Are the **seed** and **data version comment** correct for your experiment?
- Decision: Keep, Revise, or Reject?

Presenter notes:

The AI added `random_state`, a data version comment, and a shape check. These are good reproducibility practices. But ask: is seed 42 your team standard? Is that really data version 2.1? The AI guessed plausible values -- the reviewer must verify. This shows why even helpful changes need human confirmation.

## Slide 11: DE Before And After -- Pipeline Task

On-screen content:

- Scenario: Copilot adds retry logic and operational notes to an Airflow task.

**Before (original):**
```python
load_orders = PythonOperator(
    task_id="load_orders",
    python_callable=load_orders_to_warehouse,
    dag=dag,
)
```

**After (AI-improved):**
```python
load_orders = PythonOperator(
    task_id="load_orders",
    python_callable=load_orders_to_warehouse,
    retries=3,
    retry_delay=timedelta(minutes=5),
    dag=dag,
)
# Upstream: staging.raw_orders must be fresh (< 6 hrs)
# On failure: check Airflow logs, verify source system
# Escalation: page on-call DE after 3 retries exhausted
```

- Review: Are the **retry count**, **delay**, and **escalation path** correct for your SLA?
- Decision: Keep, Revise, or Reject?

Presenter notes:

The AI added retries, delay, and operational comments. Ask: does your team use 3 retries or 2? Is 5 minutes the right delay for your data volume? Is the escalation path accurate? Emphasize that operational defaults that look reasonable but are wrong can cause silent failures in production.

## Slide 12: Reuse What Works

On-screen content:

- Workspace instructions for shared defaults
- Prompt files for repeatable tasks
- New sessions when context drifts

Presenter notes:

Connect this to team onboarding. Once the same guidance is repeated several times, capture it in `.github/copilot-instructions.md` or prompt files.

## Slide 13: Common Mistakes

On-screen content:

- Asking for too much at once
- Picking Agent too early
- Missing context
- Skipping review
- Staying in one noisy session too long

Presenter notes:

Keep this slide practical. Ask learners which mistake they expect to make first, then show the corresponding recovery step.

## Slide 14: Validation And Reflection

On-screen content:

- Can you choose Ask vs Plan vs Agent?
- Can you refine a vague prompt?
- Can you name what still needs verification?
- Which team habit should become an instruction?

Presenter notes:

Use this slide to bridge to the lab. The goal is not just tool familiarity, but observable behavior change.

## Slide 15: References

On-screen content:

- Shared reference file in `references/`
- Official GitHub Docs
- Official VS Code Docs

Presenter notes:

Close by pointing learners to the reference file and to the accompanying prompt pack. Encourage them to copy the prompt templates and adapt them to their own repositories.
