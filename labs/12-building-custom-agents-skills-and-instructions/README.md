# Lab: Building Custom Agents, Skills, And Instructions

## Scenario Context

Your team sees inconsistent Copilot outputs across similar tasks. You need to standardize behavior using persistent instructions, reusable skills, and a specialized agent.

## Learner Goal

By the end of this lab, you should be able to:

- create one scoped instructions file
- create one reusable skill
- create one specialized agent definition
- validate that customizations improve consistency

## Starter State

You begin with:

- a repo with no custom instructions/skills/agents for this workflow
- one recurring workflow that currently produces inconsistent results

## Target State

You finish with:

- one `*.instructions.md` file
- one `SKILL.md`
- one `*.agent.md`
- a short before/after comparison of output quality

## Prerequisites And Setup

Goal of the step:

- Pick a realistic recurring workflow to customize.

Exact actions:

- Choose one scenario: SQL query review, notebook quality checks, or release-note validation.
- Capture one baseline prompt and output before customization.

What success looks like:

- Baseline output captured for comparison.

Common failure mode and fix:

- Failure: No baseline captured.
- Fix: Re-run the original prompt and save output before continuing.

## Lab Tasks

### Task 1. Create Scoped Instructions

Goal of the step:

- Add persistent file-targeted guidance.

Exact action:

- Create a file like `.github/instructions/sql.instructions.md` with `applyTo` for SQL files.
- Include 3-5 concrete rules.

What success looks like:

- Copilot follows these rules in matching files.

Common failure mode and fix:

- Failure: Rules are ignored.
- Fix: Verify `applyTo` glob and file location.

### Task 2. Create A Reusable Skill

Goal of the step:

- Standardize a repeated workflow.

Exact action:

- Create `.github/skills/<skill-name>/SKILL.md` with name, description, when-to-use, steps, and expected outputs.

What success looks like:

- Skill is invokable and provides structured guidance.

Common failure mode and fix:

- Failure: Skill is too vague.
- Fix: Add explicit step-by-step actions and validation criteria.

### Task 3. Create A Specialized Agent

Goal of the step:

- Add persona-level behavior for multi-step tasks.

Exact action:

- Create `.github/agents/<agent-name>.agent.md` with specialization scope, guardrails, and workflow expectations.

What success looks like:

- Agent responses follow the specialized role and guardrails.

Common failure mode and fix:

- Failure: Agent overreaches outside intended scope.
- Fix: Tighten scope and add explicit "do not" rules.

### Task 4. Run Before/After Comparison

Goal of the step:

- Verify measurable improvement.

Exact action:

- Re-run the baseline prompt with custom artifacts enabled.
- Compare output on consistency, completeness, and safety.

What success looks like:

- A clear before/after delta documented.

Common failure mode and fix:

- Failure: No improvement appears.
- Fix: Refine skill steps and instruction specificity.

## Suggested Prompts

```text
Create a file-scoped instructions file for SQL quality rules in this repo.
```

```text
Generate a SKILL.md for a reusable notebook quality-check workflow.
```

```text
Draft an agent definition for release validation in BI and data engineering workflows.
```

```text
Compare the before and after outputs and summarize improvements.
```

## Expected Observable Output

- A new instructions file in `.github/instructions/`
- A new skill folder containing `SKILL.md`
- A new agent definition in `.github/agents/`
- A before/after comparison note

## Validation Checklist

- [ ] Instructions file created with correct `applyTo` scope
- [ ] Skill file created with actionable steps and expected outputs
- [ ] Agent file created with clear scope and guardrails
- [ ] Before/after comparison completed
- [ ] Improvements documented and reviewed

## Reflection And Extension Tasks

- Which artifact produced the biggest quality gain?
- Where did artifacts overlap or conflict?
- How will your team version and review custom artifacts?
- What governance checks are needed before sharing artifacts broadly?

## Solution Guidance

See `solution/` for sample artifacts and a comparison template.
