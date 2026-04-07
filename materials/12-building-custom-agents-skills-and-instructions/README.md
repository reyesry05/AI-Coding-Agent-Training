# Building Custom Agents, Skills, And Instructions

## Learning Objectives

By the end of this module, learners should be able to:

- explain how instructions, skills, and agents work as complementary layers
- choose the correct artifact for a given workflow need
- author a basic `.instructions.md`, `SKILL.md`, and `*.agent.md`
- test each artifact in VS Code and verify behavior changes
- avoid common anti-patterns (overly broad instructions, vague skills, over-privileged agents)

## Prerequisites And Setup

Audience:

- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:

- Modules 01 through 11 completed or equivalent knowledge
- VS Code with Copilot Chat enabled
- A sample repo where you can create customization files

Success looks like:

- The learner creates one artifact of each type and explains why each exists.

Common failure mode and fix:

- Failure: The learner puts all rules into one giant instruction file.
- Fix: Split by purpose: persistent rules in instructions, reusable workflows in skills, persona-level behavior in agents.

## Walkthrough

### Quick Summary: When To Use These Advanced Skills

Use this as a fast decision guide before creating artifacts:

| Situation | Use | Why |
| --- | --- | --- |
| You need persistent standards across files | Instructions | Always-on guidance via `applyTo` scopes |
| You repeat the same workflow and want consistency | Skill | Reusable method with optional bundled assets |
| You need multi-step task execution with a persona | Agent | Scoped orchestration and decision flow |
| You need external tools or systems | Plugin or MCP | Capability access beyond local prompt context |

Decision order:

1. Start with instructions.
2. Add a skill for repeated workflows.
3. Add an agent when execution becomes multi-step.
4. Add plugin or MCP access only if external capability is required.

### Step 1. Choose The Right Artifact

Goal of the step:

- Build decision clarity before authoring files.

Exact action:

- Use this decision table:

| Need | Best Artifact | Why |
| --- | --- | --- |
| Persistent repo rules | `*.instructions.md` | Always-on guidance scoped by files/globs |
| Reusable workflow with assets | `SKILL.md` in a skill folder | Discoverable, portable, and can bundle templates/scripts |
| Opinionated assistant persona with tool setup | `*.agent.md` | Specialized behavior and integrated tool/MCP context |

What success looks like:

- The learner can classify three scenarios into the correct artifact type.

Common failure mode and fix:

- Failure: The learner uses an agent for a simple static coding rule.
- Fix: Use instructions for static rules and reserve agents for opinionated execution behavior.

### Step 2. Author File-Scoped Instructions

Goal of the step:

- Encode stable team standards.

Exact action:

- Create `.github/instructions/sql.instructions.md`:

```yaml
---
applyTo: "**/*.sql"
---

Use uppercase SQL keywords.
Always include an explicit column list in SELECT statements.
Never use SELECT * in production queries.
```

What success looks like:

- Copilot starts following SQL formatting and safety rules in SQL files.

Common failure mode and fix:

- Failure: `applyTo` pattern is too broad.
- Fix: Start narrow and expand only when validated.

### Step 3. Author A Reusable Skill

Goal of the step:

- Package a repeated workflow with guidance and optional assets.

Exact action:

- Create `.github/skills/data-quality-check/SKILL.md` with:
  - name
  - description
  - when to use
  - step-by-step execution guidance
  - references to any templates/scripts

What success looks like:

- The skill can be invoked and drives a consistent data-quality workflow.

Common failure mode and fix:

- Failure: Skill instructions are generic and non-actionable.
- Fix: Add concrete steps, expected outputs, and failure handling.

### Step 4. Author A Specialized Agent

Goal of the step:

- Build a persona-level assistant for a team workflow.

Exact action:

- Create `.github/agents/data-release-agent.agent.md` that defines:
  - specialty scope (release validation for BI/DS/DE artifacts)
  - preferred workflow (Research > Ask > Edit > Plan > Agent)
  - required checks before proposing production-impacting changes
  - allowed tools and escalation points

What success looks like:

- The agent exhibits consistent persona behavior and guardrails.

Common failure mode and fix:

- Failure: Agent instructions conflict with repo instructions.
- Fix: Make repo instructions the baseline and keep agent behavior additive.

### Step 5. Test And Verify Artifact Behavior

Goal of the step:

- Confirm artifacts change outcomes in predictable ways.

Exact action:

- Run a controlled test:
  - prompt once without custom artifacts
  - prompt again after adding artifacts
  - compare behavior and output quality

What success looks like:

- A measurable improvement in consistency, safety, or speed.

Common failure mode and fix:

- Failure: No behavior change observed.
- Fix: Check file locations, naming conventions, and `applyTo` patterns.

## Hands-On Lab Reference

See [labs/12-building-custom-agents-skills-and-instructions/README.md](../../labs/12-building-custom-agents-skills-and-instructions/README.md).

## Validation Checklist

- [ ] Learner classified scenarios into instructions, skills, and agents correctly.
- [ ] Learner authored one `*.instructions.md` file with scoped `applyTo`.
- [ ] Learner authored one `SKILL.md` with concrete workflow instructions.
- [ ] Learner authored one `*.agent.md` with clear specialization.
- [ ] Learner verified behavior difference before and after customization.

## Reflection And Extension Tasks

- Which team workflows should be standardized first with skills?
- How will you review and approve new custom agents?
- What process will prevent instruction-file sprawl?
- How will you measure customization effectiveness over time?

## References

- [skills-agents-and-plugins-differences.md](../../references/skills-agents-and-plugins-differences.md)
- [copilot-agent-beginner-best-practices.md](../../references/copilot-agent-beginner-best-practices.md)
- [What are Agents, Skills, and Instructions](https://awesome-copilot.github.com/learning-hub/what-are-agents-skills-instructions/) -- Core definitions and layering model
- [Defining Custom Instructions](https://awesome-copilot.github.com/learning-hub/defining-custom-instructions/)
- [Creating Effective Skills](https://awesome-copilot.github.com/learning-hub/creating-effective-skills/)
- [Building Custom Agents](https://awesome-copilot.github.com/learning-hub/building-custom-agents/)
