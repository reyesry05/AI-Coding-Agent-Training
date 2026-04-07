# Lab: Understanding MCP Servers

## Scenario Context

Your team wants to use MCP-connected tools with Copilot, but there is no shared understanding of risk boundaries. Some users are running commands without clear read/write guardrails.

## Learner Goal

By the end of this lab, you should be able to:

- connect to an MCP server
- inventory available tools and classify risk
- run read-only operations safely
- define team guardrails for write-capable tools

## Starter State

You begin with:

- VS Code with Copilot Chat available
- access to one MCP server in a non-production context
- no formal MCP guardrails document

## Target State

You finish with:

- an MCP tool inventory with risk tags
- successful execution of one or more read-only MCP tools
- a draft guardrails checklist for team review

## Prerequisites And Setup

Goal of the step:

- Ensure MCP connectivity in a safe environment.

Exact actions:

- Open VS Code and connect the selected MCP server.
- Confirm you are in a sandbox/dev scope.
- List available tools and descriptions.

What success looks like:

- You can see the MCP tool catalog.

Common failure mode and fix:

- Failure: Tool list is empty after connection.
- Fix: Re-check authentication context and workspace permissions.

## Lab Tasks

### Task 1. Build A Tool Inventory

Goal of the step:

- Understand the MCP capability surface before use.

Exact action:

- Record all available tools in a table:

| Tool Name | Description | Risk Level | Why |
| --- | --- | --- | --- |
| | | Low / Medium / High | |

What success looks like:

- A completed inventory with risk classification for each tool.

Common failure mode and fix:

- Failure: Risk levels are assigned without justification.
- Fix: Add one sentence for each classification.

### Task 2. Run Read-Only MCP Queries

Goal of the step:

- Practice safe MCP operations.

Exact action:

- Use prompts like:

```text
Use MCP tools to list resources in my dev environment. Do not modify anything.
```

```text
Use only read-only MCP tools and summarize findings in a table.
```

- Capture the output.

What success looks like:

- Read-only data returned with no state changes.

Common failure mode and fix:

- Failure: Copilot attempts a write action.
- Fix: Stop and restate the constraint: "Read-only tools only."

### Task 3. Simulate A Write Request With Approval

Goal of the step:

- Validate approval behavior for higher-risk operations.

Exact action:

- Prompt Copilot:

```text
Propose how to create a new test item using MCP, but do not run any write operation until I approve.
```

- Confirm Copilot presents a plan first.

What success looks like:

- Copilot pauses for confirmation before any write operation.

Common failure mode and fix:

- Failure: The plan is too vague.
- Fix: Ask Copilot for exact tool name, payload, and expected result before approval.

### Task 4. Draft Team Guardrails

Goal of the step:

- Convert lesson outcomes into an operational standard.

Exact action:

- Draft a checklist with:
  - Allowed environments by role
  - Required approvals by risk level
  - Logging requirements
  - Rollback expectations for writes

What success looks like:

- A draft guardrails checklist ready for lead review.

Common failure mode and fix:

- Failure: Checklist has no enforcement owner.
- Fix: Assign ownership to a role (for example, platform lead or release manager).

## Suggested Prompts

```text
List all available MCP tools and classify each as low, medium, or high risk.
```

```text
Use only read-only MCP tools for this task and provide a summary table.
```

```text
Before any write operation, show the exact tool call and wait for my approval.
```

```text
Create a team guardrails checklist for MCP tools used in dev, test, and prod.
```

## Expected Observable Output

- MCP tool inventory table with risk categories
- Output from read-only MCP queries
- Proposed write-action plan (no execution without approval)
- Team guardrails checklist draft

## Validation Checklist

- [ ] MCP tool inventory completed
- [ ] At least one read-only MCP query executed successfully
- [ ] Write request handled with explicit approval pause
- [ ] Guardrails checklist drafted with ownership and environment boundaries

## Reflection And Extension Tasks

- Which high-risk tools should be disabled entirely?
- What approval chain is realistic for your team size?
- How will you audit MCP actions quarterly?
- What should be automated versus manual in MCP operations?

## Solution Guidance

See `solution/` for a sample tool inventory and guardrails checklist.
