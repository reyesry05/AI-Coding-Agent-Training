# Module 15: Snowflake Cortex AI for Data Teams

## Learning Objectives

By the end of this module, learners will be able to:

- Explain the two forms of Cortex Code (Snowsight and CLI) and choose the right one for a given workflow.
- Install and run Cortex Code CLI in a VS Code terminal, connecting to a Snowflake account.
- Use Cortex Code to explore data, build dbt pipelines, create semantic views, and deploy Cortex Agents.
- Instrument a Snowflake AI application with TruLens for AI Observability tracing.
- Start a Cortex Agent evaluation run using Snowsight or SQL and interpret answer correctness results.
- Connect a Cortex Agent to Microsoft Teams and Microsoft 365 Copilot using the AppSource integration.
- Create a Snowflake-managed MCP server that exposes Cortex Analyst and Cortex Search as tools.

---

## Prerequisites and Setup

**Audience:** Data engineers, analytics engineers, data scientists, and AI/ML engineers who build on Snowflake.

**Required access:**

- A Snowflake account (trial or production) with the ACCOUNTADMIN role available for security integration setup.
- VS Code installed on macOS, Intel Linux, or Windows Subsystem for Linux (WSL). Native Windows is not currently supported for Cortex Code CLI.
- Python 3.9 or later for the AI Observability lab section.
- A Microsoft 365 tenant with Teams and an Azure Global Administrator account (for the Teams integration section only).

**Snowflake feature availability:** All features in this module are Generally Available at time of writing, except where noted as Preview.

---

## Walkthrough

### Part 1: Cortex Code - The Snowflake-Aware AI Coding Agent

#### What Is Cortex Code?

Cortex Code is Snowflake's AI coding agent. It is purpose-built for the Snowflake data stack. It understands your Snowflake environment including catalog objects, RBAC roles, query history, costs, and semantic models, rather than just your repository. Generic coding agents such as Cursor, Claude Code, and Codex stop at the repository boundary. Cortex Code closes the gap between code and governed data.

It ships in two forms:

**Cortex Code in Snowsight / Workspaces (in-platform)**

Use this when you are already inside Snowflake. Common tasks:

- SQL development and review
- Admin and FinOps questions (warehouse costs, credit usage, role privileges)
- Data discovery (catalog search, finding relevant tables and semantic models)
- dbt project management inside Snowflake Workspaces

**Cortex Code CLI (local terminal / IDE terminal)**

Use this from your local machine or VS Code integrated terminal. Common tasks:

- End-to-end dbt projects: models, tests, validation, HTML reports
- Apache Airflow DAG authoring, monitoring, and debugging
- Semantic view creation on gold tables
- Cortex Agent creation and deployment to Snowflake Intelligence

Both forms share the same RBAC model. Cortex Code can only see and act on what your role can access.

#### Install Cortex Code CLI

Cortex Code CLI supports macOS (Apple Silicon and Intel), Intel Linux, and Windows via WSL.

```bash
curl -LsS https://ai.snowflake.com/static/cc-scripts/install.sh | sh
```

After installation, run `cortex` and follow the setup wizard. It reads connection details from `~/.snowflake/connections.toml`. If you already use the Snowflake CLI (`snow`), you can reuse the same connection file.

Keep the CLI current:

```bash
cortex --version
cortex update
```

#### Decision Guide: Cortex Code vs Generic Agents

Use Cortex Code when the work depends on Snowflake:

- Your Snowflake catalog, schemas, semantic views, or search services matter.
- Your RBAC model matters ("what can this role access?").
- You need Snowflake-correct code (Snowpark, Dynamic Tables, Snowflake SQL dialect).
- You want end-to-end automation: dbt changes + tests + validation + reports.
- You are building Cortex Agents, deploying to Snowflake Intelligence, or creating semantic objects.

Use a generic coding agent (Cursor, Codex) when the work lives outside Snowflake:

- Front-end or UI scaffolding
- Polyglot refactors across a large non-Snowflake codebase
- Tasks that do not require Snowflake metadata or account context

**The recommended pattern:** use Cursor or VS Code for editing and repo work, and run Cortex Code CLI in the integrated terminal for all Snowflake-aware execution and pipeline tasks.

#### Core Capabilities and Example Prompts

**Data exploration:**

```text
Find all tables related to customers that I have write access to.
What privileges does my role have on this database?
Why am I getting a permissions error?
```

**Cost and usage:**

```text
Which 5 service types are using the most credits?
What was our most expensive warehouse over the last 30 days, and what were the top 5 queries?
```

**dbt and pipelines:**

```text
Create a dbt project under /tasty_food that builds a data pipeline to analyze order
information and trends using source data in Database tb_101 Schema RAW.
Add appropriate tests, run a build, validate the output, and generate a shareable
HTML summary. Use --target PM.
```

**Semantic views:**

```text
Create a semantic view named WEEKLY_TRUCK_PERFORMANCE on top of my gold dbt models
(mart layer): DB.SCHEMA.MART_*.
Define dimensions: truck_id, city, week_start_date.
Define measures: weekly_revenue = sum(net_amount), total_orders = count_distinct(order_id).
Use business-friendly names and descriptions.
```

**Cortex Agent creation and deployment:**

```text
Create a Cortex Agent with two tools:
- cortex_analyst: query via MY_SEMANTIC_VIEW
- cortex_search: search the CALL_LOGS_SEARCH service
Persona: Senior Retention Specialist.
Routing: Use Analyst for metrics. Use Search for sentiment and call summaries.
Now optimize and deploy this agent to Snowflake Intelligence.
```

#### Extending Cortex Code

Cortex Code supports three extensibility mechanisms:

- **AGENTS.md:** Bring your project context and conventions with you. The same file format used by GitHub Copilot agents and other tools is recognized.
- **MCP (Model Context Protocol):** Connect external systems and tools via a standard interface.
- **Skills:** Codify repeatable Snowflake workflows and share them across a team. Skills such as `cortex-agent`, `semantic-view`, and `dataset-curation` are built in. Run `$cortex-agent` or ask "what skills are available?" to list them.

#### Best Practices for Prompting

- Speak in outcomes, not implementation steps. Say "Build a churn dashboard" rather than "write a GROUP BY query."
- Use `/plan` for complex multi-step tasks so you can review the approach before execution begins.
- Review diffs and DDL/DML operations carefully before accepting changes, especially in production environments.
- Ask for proof: include validation queries, comparison reports, or tests in your prompt.
- Keep credentials out of code and version control. Never commit secrets.

---

### Part 2: AI Observability with TruLens

#### Overview

Snowflake AI Observability lets you trace, evaluate, and monitor AI applications built on Snowflake Cortex. It uses TruLens, an open-source observability framework, integrated with Snowflake as the storage and compute backend.

Results appear in Snowsight under **AI & ML > Evaluations**.

#### Install Required Packages

```bash
pip install trulens-core trulens-connectors-snowflake trulens-providers-cortex
```

Requires version 2.1.2 or later of the `trulens-providers-cortex` package.

#### Connect TruLens to Snowflake

```python
from trulens.connectors.snowflake import SnowflakeConnector
from trulens.core import TruSession

connector = SnowflakeConnector(
    snowflake_connection_parameters={
        "account": "<your-account>",
        "user": "<your-user>",
        "password": "<your-password>",
        "database": "<your-database>",
        "schema": "<your-schema>",
        "warehouse": "<your-warehouse>",
        "role": "<your-role>"
    }
)

session = TruSession(connector=connector)
session.reset_database()
```

#### Instrument a Custom Application

Use the `@instrument()` decorator to mark functions for tracing. Provide a `span_type` to categorize each span.

```python
from trulens.core.instruments import instrument
from trulens.core.otel.semconv.trace import SpanAttributes

class MyRAGApp:

    @instrument(
        span_type=SpanAttributes.SpanType.RETRIEVAL,
        attributes={"retrieval_source": "cortex_search"}
    )
    def retrieve(self, query: str) -> list[str]:
        # Return relevant documents from Cortex Search
        ...

    @instrument(
        span_type=SpanAttributes.SpanType.GENERATION,
        attributes={"model": "snowflake-arctic"}
    )
    def generate(self, query: str, context: list[str]) -> str:
        # Generate a response using Cortex Complete
        ...

    @instrument(span_type=SpanAttributes.SpanType.RECORD_ROOT)
    def query(self, question: str) -> str:
        context = self.retrieve(question)
        return self.generate(question, context)
```

#### Auto-Instrument Framework Apps

For common frameworks, use the corresponding TruLens wrapper instead of manual decoration:

| Framework | TruLens Class |
|---|---|
| Custom / general Python | `TruApp` |
| LangChain | `TruChain` |
| LangGraph | `TruGraph` |
| LlamaIndex | `TruLlama` |

LangChain example:

```python
from trulens.apps.langchain import TruChain

app = MyLangChainApp()

tru_app = TruChain(
    app=app,
    app_name="my_langchain_app",
    app_version="v1"
)
```

#### Define Evaluation Metrics

Snowflake Cortex provides built-in feedback functions for RAG evaluation:

```python
from trulens.providers.cortex import Cortex

provider = Cortex(
    snowflake_session=session,
    model="mistral-7b"
)

# Groundedness: does the answer stick to the retrieved context?
groundedness = Feedback(provider.groundedness_measure_with_cot_reasons).on_input_output()

# Context relevance: did retrieval return relevant chunks?
context_relevance = Feedback(provider.context_relevance_with_cot_reasons).on_input_output()

# Coherence: is the answer logically well-formed?
coherence = Feedback(provider.coherence).on_output()
```

#### Record and Run Evaluations

```python
from trulens.core import RunConfig

tru_app = TruApp(
    app=MyRAGApp(),
    app_name="rag_app",
    app_version="v1",
    feedbacks=[groundedness, context_relevance, coherence]
)

run = tru_app.run(
    run_name="baseline_eval",
    run_config=RunConfig(deferred_on_num_records=1)
)

run.start()

# Send test queries
with tru_app as recording:
    for question in test_questions:
        tru_app.app.query(question)

run.compute_metrics()
```

#### View Results in Snowsight

Navigate to **AI & ML > Evaluations** in Snowsight. Results include:

- Per-run aggregate scores for each metric.
- Per-record trace details showing input, output, and span-by-span execution.
- Thread details for planning and tool calls.

---

### Part 3: Cortex Agent Evaluations

Cortex Agent evaluations measure agent performance against test datasets using LLM-as-judge scoring. They run as Snowflake tasks and results appear in Snowsight under **AI & ML > Agents > Evaluations**.

#### Built-In Metrics

- **answer_correctness:** Measures how closely the agent's answer matches a provided ground truth. Best used when the underlying data is static.
- **logical_consistency:** Measures consistency across agent instructions, planning, and tool calls. Reference-free: no ground truth required.

Custom metrics can be defined using a prompt template and numeric score ranges.

#### Prepare an Evaluation Dataset

Create a source table with an input query column and an output column containing ground truth as a VARIANT:

```sql
CREATE OR REPLACE TABLE eval_db.eval_schema.agent_eval_data (
    input_query VARCHAR
);

INSERT INTO eval_db.eval_schema.agent_eval_data
SELECT
    'What was total revenue in Q1 2025?',
    PARSE_JSON('{"ground_truth_output": "Total revenue in Q1 2025 was $4.2M"}');
```

#### Define an Evaluation Configuration (YAML)

```yaml
dataset:
  dataset_type: "CORTEX AGENT"
  table_name: "eval_db.eval_schema.agent_eval_data"
  dataset_name: "agent_eval_dataset"
  column_mapping:
    query_text: "input_query"
    ground_truth: "output"

evaluation:
  agent_params:
    agent_name: "my_agent"
    agent_type: "CORTEX AGENT"
  run_params:
    label: "Baseline evaluation"
  source_metadata:
    type: "DATASET"
    dataset_name: "agent_eval_dataset"

metrics:
  - "answer_correctness"
  - "logical_consistency"
```

Upload the YAML file to a stage, then start the evaluation:

```sql
CALL EXECUTE_AI_EVALUATION(
  'START',
  OBJECT_CONSTRUCT('run_name', 'run-1'),
  '@eval_db.eval_schema.eval_config/agent_evaluation_config.yaml'
);
```

Check status:

```sql
CALL EXECUTE_AI_EVALUATION(
  'STATUS',
  OBJECT_CONSTRUCT('run_name', 'run-1'),
  '@eval_db.eval_schema.eval_config/agent_evaluation_config.yaml'
);
```

Using Cortex Code CLI to run and interpret evaluations:

```text
Evaluate my agent DB.SCHEMA.MY_AGENT on my eval set and summarize failures.
```

---

### Part 4: Cortex Agents for Microsoft Teams and Microsoft 365 Copilot

The Teams integration embeds Cortex Agents directly into Microsoft Teams chats and the Microsoft 365 Copilot interface. Business users can query Snowflake data in natural language without leaving Teams.

Key characteristics:

- Installed from <https://appsource.microsoft.com/> by searching "Snowflake Cortex Agents".
- All data queried by the agent stays within Snowflake. Only the user prompt and the agent response cross the integration boundary.
- Full Snowflake RBAC is enforced. Agents execute with the user's default Snowflake role.
- Users authenticate via Microsoft Entra ID (Azure AD). OAuth 2.0 tokens map Entra users to Snowflake users.
- You can reuse existing Snowflake Intelligence agents. No reconfiguration is needed.

#### Setup Overview

Setup requires three phases performed by different administrators:

1. **Azure administrator:** Grant tenant-wide OAuth consent for two Snowflake application service principals in Entra ID.
2. **Snowflake administrator:** Create a security integration that maps Entra ID tokens to Snowflake users.
3. **Snowflake administrator:** Install the Teams app and connect your Snowflake account.

**Create the Snowflake security integration** (replace `<tenant-id>` with your Microsoft Tenant ID):

```sql
CREATE OR REPLACE SECURITY INTEGRATION entra_id_cortex_agents_integration
    TYPE = EXTERNAL_OAUTH
    ENABLED = TRUE
    EXTERNAL_OAUTH_TYPE = AZURE
    EXTERNAL_OAUTH_ISSUER = 'https://login.microsoftonline.com/<tenant-id>/v2.0'
    EXTERNAL_OAUTH_JWS_KEYS_URL = 'https://login.microsoftonline.com/<tenant-id>/discovery/v2.0/keys'
    EXTERNAL_OAUTH_AUDIENCE_LIST = ('5a840489-78db-4a42-8772-47be9d833efe')
    EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM = ('email', 'upn')
    EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE = 'email_address'
    EXTERNAL_OAUTH_ANY_ROLE_MODE = 'ENABLE';
```

**User mapping requirement:** Every Entra ID user must map one-to-one to a Snowflake user. The Entra ID primary email must exactly match the Snowflake user's `EMAIL_ADDRESS` attribute (or UPN must match `LOGIN_NAME` for UPN mapping).

#### Current Limitations

- Requires Microsoft Entra ID as the identity provider. Other IdPs (Okta, SAML) can participate via Entra ID federation.
- Private Link is not supported. You must disable Private Link to use this integration.
- The user's default Snowflake role governs all query permissions. Administrative roles (ACCOUNTADMIN) are blocked from the security integration by default.

---

### Part 5: Snowflake-Managed MCP Server

The Snowflake-managed MCP server lets AI agents (Cursor, Claude, GitHub Copilot, and others) discover and invoke Snowflake tools without deploying separate infrastructure.

Supported tool types:

| Type | Wraps |
|---|---|
| `CORTEX_ANALYST_MESSAGE` | Cortex Analyst semantic view |
| `CORTEX_SEARCH_SERVICE_QUERY` | Cortex Search service |
| `CORTEX_AGENT_RUN` | Cortex Agent object |
| `SYSTEM_EXECUTE_SQL` | Raw SQL execution |
| `GENERIC` | Snowflake UDF or stored procedure |

#### Create an MCP Server

```sql
CREATE OR REPLACE MCP SERVER my_data_mcp_server
  FROM SPECIFICATION $$
    tools:
      - name: "revenue-analyst"
        type: "CORTEX_ANALYST_MESSAGE"
        identifier: "my_db.my_schema.revenue_semantic_view"
        description: "Answer revenue and sales metric questions using the semantic view"
        title: "Revenue Analyst"

      - name: "support-search"
        type: "CORTEX_SEARCH_SERVICE_QUERY"
        identifier: "my_db.my_schema.support_search_service"
        description: "Search customer support transcripts and tickets"
        title: "Support Search"
  $$;
```

#### Configure OAuth Authentication

```sql
CREATE OR REPLACE SECURITY INTEGRATION mcp_oauth_integration
  TYPE = OAUTH
  OAUTH_CLIENT = CUSTOM
  ENABLED = TRUE
  OAUTH_CLIENT_TYPE = 'CONFIDENTIAL'
  OAUTH_REDIRECT_URI = '<your-redirect-uri>';

-- Retrieve client ID and secret for MCP client configuration
SELECT SYSTEM$SHOW_OAUTH_CLIENT_SECRETS('MCP_OAUTH_INTEGRATION');
```

#### Grant Access

```sql
-- Allow a role to connect and discover tools
GRANT USAGE ON MCP SERVER my_db.my_schema.my_data_mcp_server TO ROLE analyst_role;

-- Allow the role to invoke the Cortex Analyst tool
GRANT SELECT ON SEMANTIC VIEW my_db.my_schema.revenue_semantic_view TO ROLE analyst_role;

-- Allow the role to invoke the Cortex Search tool
GRANT USAGE ON CORTEX SEARCH SERVICE my_db.my_schema.support_search_service TO ROLE analyst_role;
```

#### Client Endpoint

```text
https://<account_url>/api/v2/databases/<database>/schemas/<schema>/mcp-servers/<name>
```

Replace `<account_url>` with your Snowflake account identifier formatted as `<organization>-<account>.snowflakecomputing.com`.

#### Security Recommendations

- Use OAuth (not hardcoded tokens) for authentication.
- Grant access using the least-privileged role that the integration requires.
- Access to the MCP server itself does not automatically grant access to underlying tools. Permissions must be granted for each tool separately.
- Verify third-party MCP servers before connecting. Tool poisoning is possible when consuming unverified MCP servers.
- Use hyphens (`-`) rather than underscores (`_`) in MCP server hostnames. Underscores cause connection errors in some MCP clients.

---

## Hands-On Lab Reference

See [labs/15-snowflake-cortex-ai-for-data-teams/README.md](../../labs/15-snowflake-cortex-ai-for-data-teams/README.md) for the guided lab.

---

## Validation Checklist

- [ ] Cortex Code CLI is installed and connects to a Snowflake account.
- [ ] A data exploration prompt returns table metadata from the Snowflake catalog.
- [ ] A dbt project is created or updated with at least one test added by Cortex Code.
- [ ] A TruLens-instrumented app records traces visible in Snowsight AI & ML > Evaluations.
- [ ] An agent evaluation run completes and shows answer_correctness scores in Snowsight.
- [ ] A Cortex Agent responds to a question in Microsoft Teams (if tenant access is available).
- [ ] An MCP server is created with at least one Cortex Analyst or Cortex Search tool.
- [ ] MCP tool discovery succeeds from a local MCP client using the OAuth endpoint.

---

## Reflection and Extension Tasks

**Reflection:**

1. Where does your current data team spend the most time context-switching between tools? Which Cortex Code workflow could reduce that friction?
2. Which AI Observability metrics (groundedness, context relevance, coherence) are most critical for your team's AI applications and why?
3. What are the trade-offs between deploying a Cortex Agent to Microsoft Teams versus exposing it through an MCP server?

**Extension tasks:**

- Build a Cortex Agent with two tools (Analyst and Search) and evaluate it using a 15-question dataset. Iterate on the system prompt to improve answer_correctness above 0.80.
- Create a Cortex Code skill file (`.md` playbook) that codifies your team's dbt model review and deployment workflow.
- Configure an MCP server and connect it to GitHub Copilot agent mode in VS Code using an OAuth token. Test a natural language query routed through Cortex Analyst.

---

## References

- [Snowflake Cortex Code: What it is, why it matters, and when to use it](https://medium.com/snowflake/snowflake-cortex-code-what-it-is-why-it-matters-and-when-to-use-it-35152de8edca) (Medium, Daniel Myers)
- [Best Practices for Cortex Code CLI](https://www.snowflake.com/en/developers/guides/best-practices-cortex-code-cli/) (Snowflake Developer Guide)
- [AI Observability in Snowflake Cortex](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability) (Snowflake Docs)
- [Evaluate AI applications with TruLens](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability/evaluate-ai-applications) (Snowflake Docs)
- [Cortex Agent evaluations](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-evaluations) (Snowflake Docs)
- [Cortex Agents for Microsoft Teams and Microsoft 365 Copilot](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-teams-integration) (Snowflake Docs)
- [Snowflake-managed MCP server](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) (Snowflake Docs)
- [Getting Started with Cortex Agents for Microsoft Teams](https://quickstarts.snowflake.com/guide/getting_started_with_the_microsoft_teams_and_365_copilot_cortex_app) (Snowflake Quickstart)
- [claude_code_snowflake_cortexapi quickstart on GitHub](https://github.com/sfc-gh-tjia/claude_code_snowflake_cortexapi/tree/main)
- [Emerging Solutions Toolbox: helper-stellar-bi](https://github.com/Snowflake-Labs/emerging-solutions-toolbox/tree/main/helper-stellar-bi)
