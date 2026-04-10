# Lab 15: Snowflake Cortex AI for Data Teams

## Scenario Context

Your data team has been invited to a hands-on session with the Snowflake team. The goal of the session is to show how Cortex Code CLI, AI Observability, Cortex Agent evaluations, and the Microsoft Teams integration work together to reduce context switching and bring AI-assisted workflows directly into the tools your team already uses.

This lab walks through three progressive tracks. Complete the tracks in order or choose the one most relevant to your role.

- **Track A:** Cortex Code CLI for data exploration and pipeline work
- **Track B:** AI Observability tracing with TruLens
- **Track C:** MCP server setup and agent evaluation

---

## Learner Goal

By the end of this lab, you should be able to:

- Use Cortex Code CLI to discover data, generate synthetic datasets, and create a dbt pipeline.
- Instrument a Python AI app with TruLens and view evaluation results in Snowsight.
- Create a Snowflake-managed MCP server with a Cortex Analyst tool and invoke it from a client.
- Run a Cortex Agent evaluation and interpret answer correctness results.

---

## Prerequisites and Setup

**Before starting, confirm:**

- [ ] Cortex Code CLI is installed. Run `cortex --version` to verify.
- [ ] You have an active Snowflake connection configured in `~/.snowflake/connections.toml`.
- [ ] Python 3.9 or later is installed (Track B only).
- [ ] You have ACCOUNTADMIN or SYSADMIN access to your Snowflake account.
- [ ] You have at least one database and schema you can write to.

**Install CLI:**

```bash
curl -LsS https://ai.snowflake.com/static/cc-scripts/install.sh | sh
```

**Install Python packages (Track B):**

```bash
pip install trulens-core trulens-connectors-snowflake trulens-providers-cortex
```

---

## Starter State

- No data, no pipelines, no agents. You start with access to a Snowflake account and an empty working schema.
- For Track B, the starter code is provided inline below.
- For Track C, you need at least one Cortex Agent object or Cortex Analyst semantic view in your account.

---

## Target State

**Track A:** A synthetic customer churn dataset exists in your Snowflake schema. A dbt project produces a mart model with tests. Cortex Code has generated a summary report in HTML.

**Track B:** A TruLens-instrumented RAG application has been run against a test question set. Groundedness, context relevance, and coherence scores are visible in Snowsight under AI & ML > Evaluations.

**Track C:** A Snowflake-managed MCP server is created with a Cortex Analyst tool. An evaluation run has completed for a Cortex Agent and shows answer correctness scores in Snowsight.

---

## Lab Tasks

### Track A: Cortex Code CLI for Data Work

#### Task A1: Connect and Explore

1. Open a terminal (VS Code integrated terminal, macOS terminal, or WSL).
2. Run `cortex` and connect to your Snowflake account.
3. Use the following prompt to explore your environment:

```text
What databases and schemas do I have access to? Which ones can I write to?
```

**What success looks like:** Cortex Code lists databases and schemas with your write permissions.

**Common failure:** If you see a connection error, confirm your `~/.snowflake/connections.toml` has a valid account identifier and matching credentials. Run `snow connection test` to verify the connection separately.

#### Task A2: Generate a Synthetic Dataset

Use this prompt to create a practice dataset:

```text
Create a customer churn dataset for a telecom company showing customer usage
for 10,000 customers. Include fake names, phone numbers, US city and state.
Include data usage in GB, call minutes, contract length, and whether they
cancelled (churn). Include a unique customer_id column.
Create the data locally and upload it to <your-database>.<your-schema>.CHURN_CUSTOMERS.
```

Replace `<your-database>` and `<your-schema>` with actual values.

**What success looks like:** Cortex Code creates and uploads the table, then confirms the row count.

**Common failure:** If the upload fails, ask "Why am I getting a permissions error?" and follow the suggested role or privilege fix.

#### Task A3: Analyze the Data

After the dataset is loaded, run these iterative prompts:

```text
Calculate churn rate grouped by state and contract length.
Order by highest churn rate first.
```

```text
I want to identify the heaviest data users who are also churning.
```

**What success looks like:** Query results are returned in the terminal with accurate SQL generated for your Snowflake data.

#### Task A4: Build a dbt Pipeline

```text
Create a dbt project that uses CHURN_CUSTOMERS as a source table.
Build a mart model called CHURN_ANALYSIS_MART that calculates:
- churn rate by state
- average data usage for churned vs retained customers
- average call minutes for churned vs retained customers
Add appropriate tests for nulls and unique keys, run a build, validate the
output, and generate a shareable HTML summary of the results.
```

**What success looks like:** A dbt project is created under a local folder, `dbt run` succeeds, `dbt test` passes, and an HTML report is generated. Cortex Code provides a path or link to the report.

**Common failure:** If dbt cannot find your Snowflake connection, confirm you do not have conflicting `profiles.yml` entries. Add "Do not create a profiles.yml file; I already have a Snowflake connection via
`~/.dbt`" to your prompt if needed.

#### Task A5: Suggested Copilot Prompts for Learners

Try these prompts in GitHub Copilot agent mode after completing the Cortex Code tasks. These bridge Cortex Code workflows into VS Code:

```text
@workspace Review the dbt project in /churn_project. List any models that have
no downstream dependents and could be candidates for removal.
```

```text
@workspace Create a GitHub Actions workflow that runs dbt test on every pull
request targeting the main branch.
```

---

### Track B: AI Observability with TruLens

#### Task B1: Set Up the TruLens Session

Create a new file `observability_demo.py` in your working directory. Add the following starter code, replacing the connection parameters with your Snowflake credentials:

```python
from trulens.connectors.snowflake import SnowflakeConnector
from trulens.core import TruSession

connector = SnowflakeConnector(
    snowflake_connection_parameters={
        "account": "<account>",
        "user": "<user>",
        "password": "<password>",
        "database": "<database>",
        "schema": "<schema>",
        "warehouse": "<warehouse>",
        "role": "<role>"
    }
)

session = TruSession(connector=connector)
session.reset_database()
print("TruLens session connected to Snowflake.")
```

Run the file:

```bash
python observability_demo.py
```

**What success looks like:** The script prints the confirmation message without errors.

**Common failure:** `ImportError` for `trulens_connectors_snowflake` means the package was not installed. Run `pip install trulens-connectors-snowflake` and retry.

#### Task B2: Instrument a Simple RAG Application

Add the following class to `observability_demo.py`. This simulates a retrieval-augmented generation pipeline using stub functions you will replace with real Cortex Search and Cortex Complete calls in the extension task.

```python
from trulens.core.instruments import instrument
from trulens.core.otel.semconv.trace import SpanAttributes

class SimpleRAGApp:

    @instrument(span_type=SpanAttributes.SpanType.RETRIEVAL)
    def retrieve(self, question: str) -> list:
        # Stub: replace with Cortex Search call
        return [
            "Customer churn rate in Q1 2025 was 3.2 percent.",
            "Highest churn was in states with month-to-month contracts."
        ]

    @instrument(span_type=SpanAttributes.SpanType.GENERATION)
    def generate(self, question: str, context: list) -> str:
        # Stub: replace with SNOWFLAKE.CORTEX.COMPLETE call
        context_str = " ".join(context)
        return f"Based on the available data: {context_str}"

    @instrument(span_type=SpanAttributes.SpanType.RECORD_ROOT)
    def answer(self, question: str) -> str:
        context = self.retrieve(question)
        return self.generate(question, context)
```

#### Task B3: Define Metrics and Record Traces

```python
from trulens.core import Feedback, TruApp, RunConfig
from trulens.providers.cortex import Cortex

provider = Cortex(snowflake_session=session, model="mistral-7b")

groundedness = Feedback(
    provider.groundedness_measure_with_cot_reasons,
    name="Groundedness"
).on_input_output()

context_relevance = Feedback(
    provider.context_relevance_with_cot_reasons,
    name="Context Relevance"
).on_input_output()

coherence = Feedback(
    provider.coherence,
    name="Coherence"
).on_output()

app = SimpleRAGApp()

tru_app = TruApp(
    app=app,
    app_name="churn_rag_demo",
    app_version="v1",
    feedbacks=[groundedness, context_relevance, coherence]
)

test_questions = [
    "What is the overall churn rate?",
    "Which states have the highest churn?",
    "What contract type has the most churn?",
]

run = tru_app.run(
    run_name="baseline_eval",
    run_config=RunConfig(deferred_on_num_records=1)
)

run.start()

with tru_app as recording:
    for question in test_questions:
        tru_app.app.answer(question)

run.compute_metrics()
print("Evaluation run complete. Check Snowsight AI & ML > Evaluations.")
```

**What success looks like:** The script completes without errors. In Snowsight, navigate to **AI & ML > Evaluations** and find the `churn_rag_demo` app with a `baseline_eval` run showing scores for Groundedness, Context Relevance, and Coherence.

**Common failure:** If metrics show as 0 or null, verify the `trulens-providers-cortex` package is version 2.1.2 or later. Run `pip show trulens-providers-cortex` to check.

#### Task B4: Suggested Copilot Prompts for Learners

```text
@workspace In observability_demo.py, replace the retrieve stub with a real
Snowflake Cortex Search call querying the CHURN_CUSTOMERS table for relevant
context. Use the Snowflake Python connector.
```

```text
@workspace Add a fourth feedback metric to the TruLens setup that measures
answer relevance (how well the output directly addresses the question asked).
Use the provider pattern already established in the file.
```

---

### Track C: MCP Server and Agent Evaluation

#### Task C1: Create a Semantic View for Cortex Analyst

If you completed Track A, use your CHURN_ANALYSIS_MART as the basis. Otherwise, use any mart-layer table you have access to. Run this SQL in Snowsight or a Snowflake notebook:

```sql
CREATE OR REPLACE SEMANTIC VIEW my_db.my_schema.CHURN_ANALYTICS
  TABLES (
    my_db.my_schema.CHURN_ANALYSIS_MART AS CHURN_MART
  )
  DIMENSIONS (
    CHURN_MART.state AS "State",
    CHURN_MART.contract_length AS "Contract Length"
  )
  METRICS (
    churn_rate AS (
      COUNT_IF(CHURN_MART.churn = TRUE)::FLOAT /
      COUNT(*)::FLOAT
    ) COMMENT 'Proportion of customers who cancelled'
  );
```

#### Task C2: Create an MCP Server

```sql
CREATE OR REPLACE MCP SERVER my_db.my_schema.churn_mcp_server
  FROM SPECIFICATION $$
    tools:
      - name: "churn-analyst"
        type: "CORTEX_ANALYST_MESSAGE"
        identifier: "my_db.my_schema.CHURN_ANALYTICS"
        description: "Answer churn and retention questions using telecom customer data"
        title: "Churn Analyst"
  $$;

GRANT USAGE ON MCP SERVER my_db.my_schema.churn_mcp_server TO ROLE <your-role>;
GRANT SELECT ON SEMANTIC VIEW my_db.my_schema.CHURN_ANALYTICS TO ROLE <your-role>;
```

**What success looks like:** `SHOW MCP SERVERS IN SCHEMA my_db.my_schema;` returns one row for `churn_mcp_server`.

#### Task C3: Test Tool Discovery

Using any HTTP client (`curl`, Postman, or Python `requests`), call the tools/list endpoint after authenticating with your OAuth token:

```
POST https://<account-url>/api/v2/databases/my_db/schemas/my_schema/mcp-servers/churn_mcp_server
Authorization: Bearer <oauth_token>
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

**What success looks like:** The response includes a tool with `"name": "churn-analyst"` and the description you provided.

#### Task C4: Run a Cortex Agent Evaluation

If you have a Cortex Agent in your account, create a small evaluation dataset and run it:

```sql
-- Create evaluation table
CREATE OR REPLACE TABLE my_db.my_schema.agent_eval_data (
    user_question VARCHAR,
    expected_output VARIANT
);

INSERT INTO my_db.my_schema.agent_eval_data
SELECT 'What is the churn rate for month-to-month contracts?',
       PARSE_JSON('{"ground_truth_output": "Month-to-month contract churn rate is approximately 5.1 percent."}');

INSERT INTO my_db.my_schema.agent_eval_data
SELECT 'Which state has the lowest churn rate?',
       PARSE_JSON('{"ground_truth_output": "Oregon has the lowest churn rate at 1.3 percent."}');
```

Navigate to **Snowsight > AI & ML > Agents**, select your agent, choose the **Evaluations** tab, then select **New evaluation run**. Use the table above as the source for a new dataset and select `answer_correctness` as the metric.

**What success looks like:** The run completes with a status of success and shows an answer correctness score between 0 and 1 for each input row.

**Common failure:** If the evaluation job shows a warning status, check the role permissions. The running role needs `EXECUTE TASK ON ACCOUNT` and the privileges listed in the [Cortex Agent evaluations access control section](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-evaluations#access-control-requirements).

#### Task C5: Suggested Copilot Prompts for Learners

```text
@workspace Create a Python script that reads a CSV of test questions and
ground truth answers, inserts them into the agent_eval_data table, then calls
EXECUTE_AI_EVALUATION to start an evaluation run and polls STATUS every 30
seconds until the run completes.
```

```text
@workspace Review the YAML specification format for a Cortex Agent evaluation.
Add a custom metric named "tone_appropriateness" that scores whether the agent
response uses professional language appropriate for a business analyst audience,
on a scale of 1 to 10.
```

---

## Expected Observable Output

| Task | Observable Evidence |
|---|---|
| A2 – Dataset creation | `CHURN_CUSTOMERS` table exists in your schema with 10,000 rows |
| A4 – dbt pipeline | `dbt test` passes; HTML report file generated locally |
| B3 – TruLens tracing | Run visible in Snowsight AI & ML > Evaluations with three metric scores |
| C2 – MCP server | Server listed in `SHOW MCP SERVERS IN SCHEMA` output |
| C3 – Tool discovery | `tools/list` response includes the `churn-analyst` tool |
| C4 – Agent evaluation | Evaluation run in Snowsight > Agents > Evaluations shows answer_correctness scores |

---

## Validation Checklist

- [ ] Cortex Code CLI returns Snowflake catalog metadata for a data exploration prompt.
- [ ] `CHURN_CUSTOMERS` table is loaded in Snowflake with the correct shape.
- [ ] dbt project folder exists locally with at least one model and one test.
- [ ] TruLens `baseline_eval` run appears in Snowsight Evaluations with non-zero metric scores.
- [ ] `churn_mcp_server` is visible in SHOW MCP SERVERS output.
- [ ] Tool discovery request returns a valid MCP tools/list response.
- [ ] Agent evaluation run shows a completed status with answer_correctness scores.

---

## Reflection Tasks

1. Compare the TruLens groundedness scores between the stub retrieval and a real Cortex Search retrieval. What changed and why?
2. What would happen to the agent evaluation results if you added a third ground truth row with a deliberately wrong expected answer? How does LLM-as-judge scoring differ from exact match scoring?
3. When would you prefer to expose a Cortex Agent via MCP rather than via the Teams integration? What is the key trade-off in governance and user experience?

---

## Solution Guidance

Complete worked solutions for Track B are not provided because the metric scores depend on the specific model and Snowflake account configuration. Use the following as acceptance criteria instead:

- Groundedness > 0.70 indicates the generated answer stays within the retrieved context.
- Context Relevance > 0.65 indicates retrieval is returning useful chunks.
- Coherence > 0.80 indicates the output is logically well-formed.

If any metric falls below these thresholds, revisit the retrieval logic or the generation prompt in your `generate()` method.

For MCP server and agent evaluation tasks, the SQL and YAML patterns provided in the tasks are the solution. Adapt identifiers to match your Snowflake objects.

---

## References

- [materials/15-snowflake-cortex-ai-for-data-teams/README.md](../../materials/15-snowflake-cortex-ai-for-data-teams/README.md)
- [Best Practices for Cortex Code CLI](https://www.snowflake.com/en/developers/guides/best-practices-cortex-code-cli/)
- [AI Observability in Snowflake Cortex](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability)
- [Cortex Agent evaluations](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-evaluations)
- [Snowflake-managed MCP server](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp)
