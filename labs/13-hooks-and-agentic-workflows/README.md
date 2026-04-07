# Lab: Hooks And Agentic Workflows

## Scenario Context

Your team has repeatable release-preparation steps but execution is inconsistent. You will design and test a hook-enabled agentic workflow that standardizes checks and reporting.

## Learner Goal

By the end of this lab, you should be able to:

- map workflow steps to instructions, skills, hooks, and agent orchestration
- define safe pre/post hooks
- capture hook logs and handle failures predictably

## Starter State

You begin with:

- a repeated workflow with manual pre-checks and post-reporting
- no formal hook plan
- no troubleshooting runbook

## Target State

You finish with:

- an agentic workflow blueprint
- at least one pre-hook and one post-hook definition
- a runbook for hook failure diagnosis

## Prerequisites And Setup

Goal of the step:

- Choose one realistic workflow to automate safely.

Exact actions:

- Select one use case (for example, lab publication readiness checks).
- Define start and end states for that workflow.

What success looks like:

- A bounded workflow is selected for testing.

Common failure mode and fix:

- Failure: Workflow scope is too broad.
- Fix: Limit to one input and one expected output.

## Lab Tasks

### Task 1. Build The Workflow Blueprint

Goal of the step:

- Assign clear layer responsibilities.

Exact action:

- Create a table with four layers and responsibilities:

| Layer | Responsibility | Artifact |
| --- | --- | --- |
| Instructions | | |
| Skills | | |
| Hooks | | |
| Agent orchestration | | |

What success looks like:

- Each layer has one non-overlapping responsibility.

Common failure mode and fix:

- Failure: Multiple layers own the same logic.
- Fix: Keep each rule in one primary layer only.

### Task 2. Define Pre-Hook And Post-Hook

Goal of the step:

- Add trigger-based automation points.

Exact action:

- Define one pre-hook (validation) and one post-hook (reporting).
- Document trigger, input, action, and output for each.

What success looks like:

- Two hook definitions with explicit trigger conditions.

Common failure mode and fix:

- Failure: Hook trigger is ambiguous.
- Fix: Tie trigger to a specific event and file pattern.

### Task 3. Add Safety Controls

Goal of the step:

- Ensure hooks fail safely.

Exact action:

- Add controls:
  - logging for every hook run
  - fail-closed on validation failure
  - manual approval before high-impact steps

What success looks like:

- Hook plan includes all three controls.

Common failure mode and fix:

- Failure: Errors are logged but workflow continues.
- Fix: Enforce fail-closed behavior for blocking checks.

### Task 4. Simulate Failure And Troubleshoot

Goal of the step:

- Practice operational recovery.

Exact action:

- Simulate one hook failure (for example, malformed metadata input).
- Use your runbook to isolate and resolve the issue.

What success looks like:

- Root cause identified and documented with fix steps.

Common failure mode and fix:

- Failure: Team cannot reproduce failure.
- Fix: Save failing input and attach it to incident notes.

## Suggested Prompts

```text
Help me design a hook-enabled workflow for release-readiness checks with one pre-hook and one post-hook.
```

```text
Generate a troubleshooting runbook for hook failures in this workflow.
```

```text
List safety controls we should enforce before enabling this automation in production.
```

## Expected Observable Output

- Completed workflow blueprint table
- Pre-hook and post-hook definitions
- Safety-control checklist
- Hook failure runbook with one simulated incident

## Validation Checklist

- [ ] Blueprint completed with non-overlapping layer responsibilities
- [ ] Pre-hook and post-hook definitions documented
- [ ] Logging, fail-closed, and manual-approval controls defined
- [ ] One simulated failure diagnosed and resolved with runbook

## Reflection And Extension Tasks

- What hooks should be mandatory in all team workflows?
- How will hook changes be code-reviewed?
- Which failures must block release by policy?
- What observability signals should be added next?

## Solution Guidance

See `solution/` for a sample blueprint and troubleshooting runbook.
