# Safe CI/CD With AI Agents

## Learning Objectives

By the end of this module, learners should be able to:

- integrate AI agents into CI/CD workflows without bypassing release controls
- define guardrails for code generation, review, validation, and deployment
- enforce separation between suggestion, approval, and execution responsibilities
- design a safe promotion flow from dev to test to production
- define rollback and incident response for AI-assisted release failures

## Prerequisites And Setup

Audience:

- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:

- Modules 01 through 13 completed or equivalent knowledge
- Familiarity with GitHub Actions or Azure DevOps pipelines
- Access to a non-production CI/CD environment

Success looks like:

- The learner can describe a CI/CD flow where AI accelerates work but humans retain release authority.

Common failure mode and fix:

- Failure: The learner gives AI agents production deployment authority by default.
- Fix: Require human approval gates and environment protections for all production promotions.

## Walkthrough

### Step 1. Place AI In The Delivery Lifecycle

Goal of the step:

- Identify where AI should assist and where humans must approve.

Exact action:

- Map CI/CD stages and assign control mode:

| Stage | AI Role | Human Role |
| --- | --- | --- |
| Planning | Draft tasks and acceptance criteria | Approve scope |
| Coding | Generate and refactor code | Review diffs |
| Validation | Propose tests and run checks | Confirm quality gates |
| Release | Prepare release notes and deployment plan | Approve deployment |
| Post-release | Summarize telemetry and incidents | Decide rollback/actions |

What success looks like:

- The learner can show clear ownership per stage.

Common failure mode and fix:

- Failure: AI role and human role overlap ambiguously.
- Fix: Assign a single accountable owner for each gate.

### Step 2. Define Guardrails For AI-Assisted Changes

Goal of the step:

- Prevent unsafe or unreviewed production impact.

Exact action:

- Define mandatory controls:
  - branch protection and required reviewers
  - required CI checks before merge
  - environment approvals before deploy
  - secret scanning and dependency checks
  - policy checks for infrastructure-as-code changes

What success looks like:

- A written guardrail set exists and maps to pipeline controls.

Common failure mode and fix:

- Failure: Guardrails are documented but not enforced in pipeline config.
- Fix: Convert each guardrail into an automated check or required approval.

### Step 3. Build A Safe Promotion Flow

Goal of the step:

- Enforce progressive validation by environment.

Exact action:

- Implement promotion rules:
  - `dev`: AI-assisted rapid iteration
  - `test`: stricter automated checks and human validation
  - `prod`: manual approval plus change ticket reference

What success looks like:

- Promotions are blocked when checks or approvals are missing.

Common failure mode and fix:

- Failure: Direct prod deploys bypass test.
- Fix: Require environment protection rules and branch-based deployment policies.

### Step 4. Add Rollback And Incident Guardrails

Goal of the step:

- Reduce recovery time from bad AI-assisted changes.

Exact action:

- Define rollback playbook:
  - deployment rollback command/procedure
  - data rollback strategy (if applicable)
  - communication template for stakeholders
  - post-incident review steps

What success looks like:

- Team can execute rollback quickly and consistently.

Common failure mode and fix:

- Failure: Rollback exists but has never been tested.
- Fix: Run scheduled rollback drills in non-production.

### Step 5. Measure AI Impact Safely

Goal of the step:

- Track productivity and risk together.

Exact action:

- Define balanced KPIs:
  - lead time to change
  - change failure rate
  - mean time to recovery
  - review rework rate for AI-generated code
  - policy violation count

What success looks like:

- Team has metrics that reward speed and safety simultaneously.

Common failure mode and fix:

- Failure: Team measures speed only.
- Fix: Pair velocity metrics with quality and risk metrics.

## Hands-On Lab Reference

See [labs/14-safe-ci-cd-with-ai-agents/README.md](../../labs/14-safe-ci-cd-with-ai-agents/README.md).

## Validation Checklist

- [ ] Learner mapped AI and human responsibilities per CI/CD stage.
- [ ] Learner defined enforceable guardrails tied to pipeline controls.
- [ ] Learner documented environment promotion rules.
- [ ] Learner drafted a rollback playbook.
- [ ] Learner selected balanced speed/safety KPIs.

## Reflection And Extension Tasks

- Which production controls must never be delegated to AI?
- How will your team handle emergency hotfixes with guardrails still intact?
- What evidence should auditors require for AI-assisted releases?
- How should policy exceptions be documented and approved?

## References

- [copilot-agent-approval-settings.md](../../references/copilot-agent-approval-settings.md)
- [git-and-github-desktop-reference.md](../../references/git-and-github-desktop-reference.md)
- [repository-visibility-and-sharing.md](../../references/repository-visibility-and-sharing.md)
- [What are Agents, Skills, and Instructions](https://awesome-copilot.github.com/learning-hub/what-are-agents-skills-instructions/) -- Foundational artifact model for safe CI/CD layering
- [Agentic Workflows](https://awesome-copilot.github.com/learning-hub/agentic-workflows/)
- [Using the Copilot Coding Agent](https://awesome-copilot.github.com/learning-hub/using-copilot-coding-agent/)
