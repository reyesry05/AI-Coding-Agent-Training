# Skills, Agents, And Plugins: Differences And How To Use Them

This reference gives the working definitions used in this curriculum.
It is intended to help learners choose the right advanced Copilot building block without mixing responsibilities.

## Short Definitions

- Skill:
  - Reusable guidance for a class of tasks.
  - A skill teaches method, standards, steps, or guardrails.
- Agent:
  - A task-oriented workflow that can reason across multiple steps and carry a scoped objective forward.
  - An agent performs work, not just describe it.
- Plugin:
  - An external capability source, usually a VS Code extension, integration, MCP server, or tool provider.
  - A plugin gives access to systems, data, or tools beyond prompt text alone.

## Quick Comparison

| Mechanism | Main Purpose | Best Use | Avoid When | Typical Output |
| --- | --- | --- | --- | --- |
| Skill | Reusable method | Repeated workflow guidance | You need task execution or external access | Checklist, pattern, standard, reusable instructions |
| Agent | Multi-step execution | Scoped task completion with iteration | A simple checklist or reference is enough | Review summary, generated artifacts, updates, decisions |
| Plugin | External capability access | Access to systems, tools, data, or services | The task can be solved with local context and prompts | Tool results, external data, system actions |

## Decision Guide

Ask these questions in order:

1. Does the team repeat this kind of work often enough to need a standard method?
   - If yes, start with a skill.
2. Does the task require planning, multiple steps, or continued execution?
   - If yes, add an agent.
3. Does the task require access to external systems, tools, or data?
   - If yes, add a plugin.

## How They Work Together

The safest advanced pattern is usually layered:

- Skill:
  - defines the method or checklist
- Agent:
  - performs the task using that method
- Plugin:
  - provides the capability access the task depends on

Example:

- A notebook reproducibility skill defines what must be checked.
- A review agent applies that checklist across notebook files and docs.
- A plugin exposes experiment metadata from an external system.

## BI, DS, And DE Examples

### Business Intelligence

- Skill:
  - KPI glossary and release-review checklist
- Agent:
  - release review agent for README, glossary, and release notes
- Plugin:
  - metadata or semantic-model integration

### Data Science

- Skill:
  - notebook reproducibility and experiment-review checklist
- Agent:
  - notebook review agent for narrative, seeds, dependencies, and data snapshot notes
- Plugin:
  - experiment registry or model metadata integration

### Data Engineering

- Skill:
  - failed-pipeline triage checklist
- Agent:
  - incident summary agent that gathers runbook, logs, and validation evidence
- Plugin:
  - orchestration, logging, or data-quality integration

## GA And Preview Features As Real Examples

The following GitHub Copilot capabilities illustrate how skills, agents, and plugins appear in practice.
For a complete feature overview, see [GitHub Copilot Reimagine Overview](github-copilot-reimagine-overview.md).

| Feature | Status | Category | What It Is |
| --- | --- | --- | --- |
| Coding Agent | GA | Agent | Assigns a GitHub issue to Copilot for autonomous implementation in a draft PR |
| Code Review | GA | Agent | Automated PR reviewer that posts inline suggestions and change requests |
| Copilot Spaces | GA | Skill-like | Curated knowledge collections that provide shared context for a team |
| Agent HQ | Preview | Plugin hub | Central dashboard to configure and monitor all AI agents across your org |
| Custom Agents | Preview | Agent | User-defined agents with custom instructions and tool access |
| MCP Servers | GA | Plugin | Model Context Protocol servers that expose external tools (GitHub MCP, Azure MCP) |
| Metrics Dashboard | GA | Governance | Organization-level usage, adoption, and impact metrics |

When designing advanced workflows, map each feature to the skill-agent-plugin framework:

- A **Copilot Space** acts like a shared skill: it defines context, not execution.
- The **Coding Agent** and **Code Review** are specialized agents that execute scoped tasks autonomously.
- **MCP servers** and **Agent HQ integrations** are plugins that provide external capability access.
- The **Metrics Dashboard** supports governance by making agent activity observable.

## Common Mistakes

- Building an agent when a checklist is enough
- Adding plugin access before defining the method
- Letting the skill, agent, and plugin all own the same responsibility
- Expanding permissions before defining validation and approval rules

## Governance Checks

Before rollout, confirm:

- scope is explicit
- expected output is observable
- validation steps are written down
- plugin permissions are minimal
- a human approval checkpoint exists for risky steps

## Reference Use In This Workspace

Use this file when:

- introducing advanced curriculum after modules 01 through 07
- reviewing whether a new capability should be a skill or an agent
- designing labs about advanced automation
- explaining why an integration layer is not the same as an execution workflow

## References

- [GitHub Copilot Reimagine Overview](github-copilot-reimagine-overview.md)
- GitHub Copilot coding agent guidance: <https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results>
- VS Code AI best practices: <https://code.visualstudio.com/docs/copilot/best-practices>
- VS Code custom instructions: <https://code.visualstudio.com/docs/copilot/customization/custom-instructions>
- VS Code extensions overview: <https://code.visualstudio.com/docs/editor/extension-marketplace>
