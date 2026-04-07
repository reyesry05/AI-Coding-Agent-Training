# Lab: Safe CI/CD With AI Agents

## Scenario Context

Your team wants to accelerate delivery using AI agents, but leadership requires confidence that production systems cannot be changed without proper controls.

## Learner Goal

By the end of this lab, you should be able to:

- map AI vs human responsibilities across CI/CD
- define enforceable guardrails for merge and deploy
- design environment promotion rules
- produce a rollback playbook and KPI set

## Starter State

You begin with:

- an existing CI/CD flow with partial controls
- no explicit AI-agent policy for release decisions
- no standardized rollback drill process

## Target State

You finish with:

- a stage-by-stage responsibility matrix
- a guardrail checklist mapped to pipeline controls
- a promotion policy for dev/test/prod
- a rollback playbook and KPI dashboard definition

## Prerequisites And Setup

Goal of the step:

- Select one existing pipeline for analysis.

Exact actions:

- Choose one service/pipeline used by your team.
- Gather current controls (reviewers, checks, approvals).

What success looks like:

- Current-state controls are documented.

Common failure mode and fix:

- Failure: Team analyzes multiple pipelines at once.
- Fix: Focus on one representative pipeline first.

## Lab Tasks

### Task 1. Create Responsibility Matrix

Goal of the step:

- Clarify ownership and authority.

Exact action:

- Create a matrix:

| Stage | AI Action | Human Approval Required? | Owner |
| --- | --- | --- | --- |
| Plan | | | |
| Code | | | |
| Validate | | | |
| Release | | | |
| Operate | | | |

What success looks like:

- Every stage has an owner and approval expectation.

Common failure mode and fix:

- Failure: Approval requirement left blank for release stages.
- Fix: Mark release and production promotion as mandatory approval points.

### Task 2. Define Merge And Deploy Guardrails

Goal of the step:

- Turn policy into enforceable controls.

Exact action:

- Define at least 8 guardrails, including:
  - required reviewers
  - required tests
  - secret scanning
  - dependency vulnerability scan
  - IaC policy checks
  - environment approvals

What success looks like:

- Guardrails are linked to concrete pipeline checks.

Common failure mode and fix:

- Failure: Guardrails are principle-only with no enforcement.
- Fix: Add exact check name and blocking behavior.

### Task 3. Define Promotion Rules

Goal of the step:

- Prevent unsafe environment jumps.

Exact action:

- Document promotion requirements:
  - dev -> test prerequisites
  - test -> prod prerequisites
  - exception handling path

What success looks like:

- Promotion policy blocks direct unvalidated production changes.

Common failure mode and fix:

- Failure: Hotfix path bypasses all controls.
- Fix: Define a limited emergency path with retrospective review.

### Task 4. Draft Rollback Playbook

Goal of the step:

- Standardize failure recovery.

Exact action:

- Include:
  - trigger conditions for rollback
  - technical rollback steps
  - communication steps
  - post-incident follow-up

What success looks like:

- Playbook can be executed by an on-call engineer.

Common failure mode and fix:

- Failure: Playbook depends on one expert.
- Fix: Add role-based instructions and shared runbook ownership.

### Task 5. Define KPI Set

Goal of the step:

- Measure impact without sacrificing safety.

Exact action:

- Define 5-7 KPIs balancing speed and risk.

What success looks like:

- KPI set includes both delivery and reliability metrics.

Common failure mode and fix:

- Failure: Only throughput metrics are selected.
- Fix: Add failure rate and recovery metrics.

## Suggested Prompts

```text
Create a CI/CD responsibility matrix for AI-assisted delivery with explicit human approval gates.
```

```text
Generate a guardrail checklist mapped to enforceable pipeline checks.
```

```text
Design a safe environment promotion policy from dev to test to prod.
```

```text
Draft a rollback playbook for AI-assisted release failures.
```

## Expected Observable Output

- Responsibility matrix
- Guardrail checklist with enforcement mapping
- Promotion policy
- Rollback playbook
- Balanced KPI set

## Validation Checklist

- [ ] Responsibility matrix completed
- [ ] At least 8 enforceable guardrails documented
- [ ] Promotion policy includes prerequisites and exceptions
- [ ] Rollback playbook drafted with ownership
- [ ] KPI set balances speed and reliability

## Reflection And Extension Tasks

- Which guardrail is hardest to enforce in your current pipeline?
- How will you review AI policy exceptions quarterly?
- What additional controls are needed for infrastructure changes?
- How should audit evidence be stored for compliance?

## Solution Guidance

See `solution/` for sample templates of matrix, guardrails, promotion policy, and rollback playbook.
