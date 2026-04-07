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
