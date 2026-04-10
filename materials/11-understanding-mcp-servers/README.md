# Understanding MCP Servers

## Learning Objectives

By the end of this module, learners should be able to:

- explain what an MCP server is and why it matters in Copilot workflows
- describe the difference between base tools and MCP-provided tools
- connect an MCP server safely in VS Code
- evaluate MCP tools for read-only vs write capabilities
- apply approval and governance controls before enabling MCP in team workflows

## Prerequisites And Setup

Audience:

- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:

- Modules 01 through 10 completed or equivalent knowledge
- VS Code with GitHub Copilot Chat enabled
- Access to at least one MCP-enabled environment for demonstration

Success looks like:

- The learner can explain MCP as a capability layer that extends agent tools.
- The learner can classify MCP tools by risk before use.

Common failure mode and fix:

- Failure: The learner enables MCP tools without reviewing what they can write or delete.
- Fix: Require a tool capability inventory before first use.

## Walkthrough

### Step 1. What MCP Servers Are

Goal of the step:

- Build a clear shared definition.

Exact action:

- Define MCP as a protocol that allows Copilot-compatible agents to discover and invoke external tools in a standardized way.
- Explain that MCP servers expose tool endpoints such as `list resources`, `query data`, `create item`, or `deploy`.

What success looks like:

- The learner can explain MCP in one sentence and give two concrete tool examples.

Common failure mode and fix:

- Failure: The learner describes MCP as "just another plugin."
- Fix: Clarify that plugins are packaging/integration choices, while MCP is a tool protocol.

### Step 2. Understand Tool Risk Levels

Goal of the step:

- Separate safe exploration tools from high-impact mutation tools.

Exact action:

- Build a simple risk matrix for MCP tools:

| Risk Level | Tool Pattern | Example |
| --- | --- | --- |
| Low | Read-only | list, show, get, query |
| Medium | Scoped write | create in sandbox, update draft |
| High | Destructive / prod-impacting | delete, deploy, role changes |

What success looks like:

- The learner can categorize each tool before invoking it.

Common failure mode and fix:

- Failure: The learner auto-approves all MCP calls.
- Fix: Keep global auto-approve off for MCP-heavy production workflows.

### Step 3. Connect And Verify MCP Servers

Goal of the step:

- Validate MCP connectivity before running tasks.

Exact action:

- Open the Agents or MCP integration panel in VS Code.
- Connect the intended MCP server.
- Verify available tools and descriptions.
- Run one read-only tool first (for example: list projects, list resources, or show configuration).

What success looks like:

- The learner can list available tools and run one safe query successfully.

Common failure mode and fix:

- Failure: Connection succeeds but tools fail due to missing auth.
- Fix: Re-authenticate and verify token/tenant/subscription context.

### Step 4. Use Copilot Prompts With MCP Tools

Goal of the step:

- Drive MCP usage through specific, constrained prompts.

Exact action:

- Use prompts that include environment and safety boundaries:

```text
Use MCP tools to list all resources in my dev environment only. Do not modify anything.
```

```text
Before using any write-capable MCP tool, show me the exact action plan and wait for confirmation.
```

What success looks like:

- Copilot stays scoped and performs only approved operations.

Common failure mode and fix:

- Failure: The prompt is vague and Copilot chooses broader actions.
- Fix: Add explicit boundaries: environment, resource scope, and "read-only" or "no writes."

### Step 5. Team Guardrails For MCP

Goal of the step:

- Establish governance before scaling usage.

Exact action:

- Create an MCP guardrails checklist:
  - Required approval level by tool risk category
  - Allowed environments per team role
  - Logging and audit requirements
  - Rollback requirements for write operations

What success looks like:

- The team has a written MCP operating model.

Common failure mode and fix:

- Failure: Guardrails exist informally but are not documented.
- Fix: Store the checklist in `references/` and link it from relevant modules.

## Hands-On Lab Reference

See [labs/11-understanding-mcp-servers/README.md](../../labs/11-understanding-mcp-servers/README.md).

## Worked Example: Power BI Semantic Model Maintenance with the Power BI Modeling MCP Server

**Scenario:** The BI team has a Power BI Desktop file containing the company's sales semantic model with 40+ measures across three tables. Measure names are inconsistent (`[Revenue]`, `[Tot Revenue]`, `[Total Rev]`) and no measure has a description. Use the Power BI Modeling MCP Server and GitHub Copilot to fix both problems safely.

**Source:** <https://github.com/microsoft/powerbi-modeling-mcp>

### Install the Power BI Modeling MCP Server

**Recommended path -- VS Code extension:**

1. Open VS Code and go to **Extensions** (`Ctrl+Shift+X`).
2. Search for `Power BI Modeling MCP`.
3. Install the extension published by `analysis-services` (Microsoft).
4. Open GitHub Copilot Chat and confirm `powerbi-modeling-mcp` appears in the tool list.

If the tool does not appear, verify that **MCP servers in Copilot** is enabled in your GitHub Copilot settings at github.com. Enterprise accounts have this disabled by default and require an administrator to enable it.

**Alternative -- npx (any MCP client):**

```json
{
  "powerbi-modeling-mcp": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@microsoft/powerbi-modeling-mcp@latest", "--start"]
  }
}
```

### Risk Classification for Power BI MCP Tools

Apply the risk matrix from Step 2 of this module before invoking any tool:

| Risk Level | Tool Category | Example Operations |
| --- | --- | --- |
| Low | `dax_query_operations` (read) | Execute a DAX query to check measure output |
| Low | `measure_operations` (list/get) | List all measures, get a single measure's DAX |
| Medium | `measure_operations` (update) | Add descriptions, rename measures |
| Medium | `column_operations` (rename) | Rename a column for naming convention |
| High | `measure_operations` (delete) | Delete a measure |
| High | `database_operations` (deploy) | Deploy model to Fabric workspace |

The MCP server prompts for confirmation before the first write operation on each connected model. Never use `--skipconfirmation` in a shared or production environment. Use `--readonly` mode for exploratory or training sessions.

### Step-By-Step: Fix the Sales Model

**Step 1 -- Connect and verify (read-only)**

Open the Power BI Desktop file. In Copilot Chat, run the built-in prompt:

```text
/ConnectToPowerBIDesktop
```

Then confirm the connection is live:

```text
List all tables and the number of measures in each table in the connected sales semantic model.
```

**What success looks like:** Copilot returns a table showing table names (for example: Sales, Products, Customers) and measure counts for each. No model changes have been made yet.

**Step 2 -- Analyze naming inconsistencies (still read-only)**

```text
Analyze the naming conventions of all measures in the Sales table. Identify groups of measures that refer to the same concept but use different naming patterns. List each group with the current names and a suggested consistent name.
```

Copilot calls `measure_operations` (list) and uses the LLM to identify patterns. Example output:

| Group | Current Names | Suggested Consistent Name |
| --- | --- | --- |
| Revenue total | `[Revenue]`, `[Tot Revenue]`, `[Total Rev]` | `[Total Revenue]` |
| Prior year | `[PY Sales]`, `[Prior Yr Sales]` | `[PY Total Revenue]` |

**Step 3 -- Review the rename plan before approving any writes**

```text
Generate the full list of rename operations needed to standardize measure naming across all tables, but do not execute any renames yet. Show me the before and after names as a table.
```

This is the human review checkpoint. Inspect the table carefully before proceeding.

**Step 4 -- Execute renames with confirmation**

```text
Apply the naming convention renames from the previous step. Wait for my confirmation before starting.
```

The MCP server surfaces a confirmation dialog before the first modification. Select Confirm to proceed. This single confirmation covers the entire batch.

**Step 5 -- Add descriptions to all measures**

```text
Add descriptions to all measures in the Sales table. For each measure, write a plain-language description of what the metric represents and include a brief note on the DAX logic used.
```

**Step 6 -- Validate with a DAX query**

```text
Run a DAX query that returns [Total Revenue], [PY Total Revenue], and the year-over-year percentage change for the last 3 full years. Show me the results.
```

Copilot uses `dax_query_operations` to execute the query against the live model and returns results directly in chat without requiring you to open a report.

### Data Privacy Reminder

When using the Power BI Modeling MCP Server with GitHub Copilot, semantic model metadata (table names, measure DAX expressions, column names, query results) is sent to the configured LLM provider as part of the conversation. This is the same metadata visible to any Power BI developer with model access. For regulated environments, review your organization's AI data-handling policy before connecting to a production semantic model.

## Validation Checklist

- [ ] Learner can explain MCP and how it extends agent capabilities.
- [ ] Learner categorized tools into low, medium, and high risk.
- [ ] Learner connected an MCP server and ran a read-only tool.
- [ ] Learner used at least one constrained MCP prompt.
- [ ] Learner produced an MCP guardrails checklist.

## Reflection And Extension Tasks

- Which MCP tools should be restricted to senior engineers only?
- How should your team approve high-risk MCP actions?
- What logging evidence should be retained for audit?
- How will you separate sandbox and production MCP access?

## References

- [skills-agents-and-plugins-differences.md](../../references/skills-agents-and-plugins-differences.md)
- [copilot-agent-approval-settings.md](../../references/copilot-agent-approval-settings.md)
- [What are Agents, Skills, and Instructions](https://awesome-copilot.github.com/learning-hub/what-are-agents-skills-instructions/) -- Foundational model for layering artifacts
- [Understanding MCP Servers](https://awesome-copilot.github.com/learning-hub/understanding-mcp-servers/)
