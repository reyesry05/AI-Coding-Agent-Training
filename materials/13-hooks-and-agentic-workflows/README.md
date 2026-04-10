# Hooks And Agentic Workflows

## Learning Objectives

By the end of this module, learners should be able to:

- explain what hooks are and when to use them in Copilot workflows
- distinguish between hooks, skills, and agents
- design an agentic workflow that combines instructions, skills, hooks, and tools
- identify safe automation boundaries for pre/post actions
- troubleshoot hook failures and avoid hidden automation risks

## Prerequisites And Setup

Audience:

- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:

- Modules 01 through 12 completed or equivalent knowledge
- VS Code with Copilot Chat enabled
- A sandbox repo for automation experiments

Success looks like:

- The learner can design an end-to-end workflow that uses hooks intentionally.

Common failure mode and fix:

- Failure: The learner uses hooks for logic that should stay in a skill or script.
- Fix: Reserve hooks for trigger-based automation around workflow events.

## Walkthrough

### Step 1. What Hooks Are

Goal of the step:

- Establish the role of hooks in automation.

Exact action:

- Define hooks as automated actions triggered before or after specific events in agent workflows.
- Explain examples:
  - pre-action checks (lint, schema validation)
  - post-action reporting (summary generation, artifact update)
  - safety gates (policy checks before deployment)

What success looks like:

- The learner can explain where hooks fit in an agentic system.

Common failure mode and fix:

- Failure: Hooks are treated as a replacement for instructions.
- Fix: Clarify that instructions are guidance, while hooks are executable triggers.

### Step 2. Hook Placement Patterns

Goal of the step:

- Use hooks where they add value without obscuring workflow logic.

Exact action:

- Apply this pattern:

| Phase | Hook Type | Example |
| --- | --- | --- |
| Before action | validation hook | Check file naming and metadata completeness |
| During workflow | checkpoint hook | Record progress and enforce mandatory review point |
| After action | reporting hook | Write summary log and validation results |

What success looks like:

- Hook points are explicit and testable.

Common failure mode and fix:

- Failure: Too many hooks make the workflow hard to debug.
- Fix: Start with one pre-hook and one post-hook.

### Step 3. Build An Agentic Workflow Blueprint

Goal of the step:

- Combine layers into one coherent design.

Exact action:

- Create a blueprint with four layers:
  - Instructions for persistent constraints
  - Skills for reusable task execution
  - Hooks for trigger-based automation
  - Agent orchestration for multi-step decision flow

What success looks like:

- The blueprint maps each layer to a clear responsibility.

Common failure mode and fix:

- Failure: Responsibilities overlap across layers.
- Fix: Assign one primary owner role for each layer.

### Step 4. Add Safety Guardrails To Hooks

Goal of the step:

- Prevent hidden destructive automation.

Exact action:

- Add mandatory controls:
  - explicit logging for every hook execution
  - non-production default environment
  - fail-closed behavior when checks fail
  - manual approval before high-impact steps

What success looks like:

- Hooks fail safely and produce traceable logs.

Common failure mode and fix:

- Failure: Hooks continue on failure and hide errors.
- Fix: Configure fail-closed and surface errors immediately.

### Step 5. Troubleshoot Hooked Workflows

Goal of the step:

- Diagnose failures quickly.

Exact action:

- Use a runbook:
  - verify trigger condition
  - inspect hook logs
  - reproduce with minimal input
  - isolate by disabling hooks one at a time

What success looks like:

- The learner can isolate root cause within a few iterations.

Common failure mode and fix:

- Failure: Team debugs entire workflow at once.
- Fix: Disable non-essential hooks and test incrementally.

## Hands-On Lab Reference

See [labs/13-hooks-and-agentic-workflows/README.md](../../labs/13-hooks-and-agentic-workflows/README.md).

## Worked Example: Hooks for the PBIP Semantic Model Change Workflow

**Scenario:** The BI team stores their Power BI semantic model as Power BI Project (PBIP) files in a GitHub repository. They add a pre-hook and a post-hook to the Copilot workflow so that every agent-driven model change is validated before it runs and documented after it completes.

**Pre-hook -- Validate measure naming before any model modification**

Before the agent calls any `measure_operations` (update or create), a pre-hook checks that proposed measure names follow the team's PascalCase convention:

```python
# pre-hook: validate_measure_names.py
import re, sys, json

changes = json.load(sys.stdin)  # agent passes proposed changes as JSON
pattern = re.compile(r'^[A-Z][a-zA-Z]+\[[A-Z][a-zA-Z ]+\]$')
violations = [
    name for name in changes.get('measure_names', [])
    if not pattern.match(name)
]

if violations:
    print(f"HOOK FAILED: Non-conforming measure names: {violations}")
    sys.exit(1)
print("HOOK PASSED: All measure names conform to convention.")
```

**What success looks like:** The hook runs before any MCP write operation and blocks the change if names do not conform, surfacing the violation to the developer before the model is touched.

**Common failure mode and fix:**

- Failure: The hook blocks a valid name because the regex does not account for measures in display-format tables like `[Total Revenue YTD]`.
- Fix: Test the regex against your team's actual measure name library before deploying the hook. Ask Copilot: "Write a test suite for this regex pattern using these 10 measure names from our model."

**Post-hook -- Generate a model change summary**

After the agent completes a batch of model modifications, a post-hook appends an entry to the team changelog:

```python
# post-hook: generate_model_changelog.py
import json, sys
from datetime import date

changes = json.load(sys.stdin)
today = date.today().isoformat()

entry = f"""
## {today}

**Modified by:** Copilot agent session
**Tables affected:** {', '.join(changes.get('tables', []))}
**Measures added:** {len(changes.get('measures_added', []))}
**Measures renamed:** {len(changes.get('measures_renamed', []))}
**Descriptions updated:** {len(changes.get('descriptions_updated', []))}
"""

with open('MODEL_CHANGELOG.md', 'a') as f:
    f.write(entry)
print("Changelog entry written to MODEL_CHANGELOG.md.")
```

**What success looks like:** After each agent session, `MODEL_CHANGELOG.md` is updated automatically. The git diff shows AI-generated model changes alongside a human-readable summary, creating a clear audit trail for the team.

**Common failure mode and fix:**

- Failure: The changelog is written but never staged, so it does not appear in the PR.
- Fix: Add `git add MODEL_CHANGELOG.md` as the final line of the hook, or add it to the agent's instruction file as a required post-action.

## Validation Checklist

- [ ] Learner can explain the difference between hooks, skills, and agents.
- [ ] Learner created a workflow blueprint with all four layers.
- [ ] Learner defined at least one pre-hook and one post-hook.
- [ ] Learner added logging and fail-closed behavior.
- [ ] Learner completed a troubleshooting runbook exercise.

## Reflection And Extension Tasks

- Which hook actions should be disallowed in production?
- How should hook logs be retained and reviewed?
- What is the right hook complexity level for your team maturity?
- How will you prevent automation drift over time?

## References

- [skills-agents-and-plugins-differences.md](../../references/skills-agents-and-plugins-differences.md)
- [copilot-agent-approval-settings.md](../../references/copilot-agent-approval-settings.md)
- [What are Agents, Skills, and Instructions](https://awesome-copilot.github.com/learning-hub/what-are-agents-skills-instructions/) -- Layering model before adding hooks
- [Automating with Hooks](https://awesome-copilot.github.com/learning-hub/automating-with-hooks/)
- [Agentic Workflows](https://awesome-copilot.github.com/learning-hub/agentic-workflows/)
