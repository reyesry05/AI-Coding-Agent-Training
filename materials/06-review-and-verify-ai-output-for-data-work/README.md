# Review And Verify AI Output For Data Work

## Learning Objectives
By the end of this module, learners should be able to:
- explain why AI output must be reviewed differently in data work than in generic drafting tasks
- identify data-quality, reproducibility, and operational risks in AI-generated output
- define review checks for BI, DS, and DE scenarios
- build validation into prompts and review steps
- document what still requires human judgment

## Prerequisites And Setup
Audience:
- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:
- Modules 01 through 05 completed or equivalent knowledge
- A safe practice workspace with one or more README, SQL, notebook, or pipeline files
- Copilot Chat available in VS Code

Success looks like:
- The learner can name concrete review checks for a data artifact.
- The learner can identify one risk that AI can introduce even when output sounds correct.
- The learner can document human follow-up items.

Common failure mode and fix:
- Failure: The learner reviews style and wording but not correctness or risk.
- Fix: Use an explicit checklist for business logic, reproducibility, data quality, and operational impact.

## Walkthrough

### Step 1. Understand data-specific review risk
Goal of the step:
- Recognize why data-team outputs need more than surface review.

Exact action:
- Review the difference between checking prose and checking data workflow behavior.
- Discuss examples: wrong join assumptions, missing notebook prerequisites, or incomplete pipeline failure handling.

What success looks like:
- The learner can explain why plausible wording is not enough.

Common failure mode and fix:
- Failure: The learner assumes readable output is correct output.
- Fix: Require checks that tie back to business rules or execution behavior.

### Step 2. Review BI outputs
Goal of the step:
- Apply checks appropriate to reporting and analytics documentation.

Exact action:
- Review whether business definitions changed.
- Check whether metric descriptions remain consistent.
- Confirm that report assumptions are still clear.

What success looks like:
- The learner can identify whether the output changed meaning, not just formatting.

Common failure mode and fix:
- Failure: The learner accepts improved wording that subtly changes report meaning.
- Fix: Compare the generated wording against the original business rule.

### Step 3. Review DS outputs
Goal of the step:
- Apply checks appropriate to notebooks, experiments, and evaluation notes.

Exact action:
- Check that environment assumptions are explicit.
- Check that data dependencies are documented.
- Check whether evaluation or reproducibility steps are missing.

What success looks like:
- The learner can identify missing reproducibility details.

Common failure mode and fix:
- Failure: The learner accepts a notebook summary that skips important setup requirements.
- Fix: Require prerequisites, data inputs, and validation steps in the output.

### Step 4. Review DE outputs
Goal of the step:
- Apply checks appropriate to scripts, pipelines, and operational documentation.

Exact action:
- Check upstream and downstream dependencies.
- Check failure handling and validation points.
- Check whether scheduling or deployment assumptions changed.

What success looks like:
- The learner can identify one operational risk introduced or ignored by the AI output.

Common failure mode and fix:
- Failure: The learner accepts a pipeline change note without checking dependencies.
- Fix: Add a dependency review step before accepting the output.

### Step 5. Build review into the prompt
Goal of the step:
- Reduce risk before output is generated.

Exact action:
- Add prompt requirements such as:
  - preserve business logic
  - identify assumptions explicitly
  - include validation steps
  - do not modify more than one file
  - list what still needs human review

What success looks like:
- The output arrives with clearer boundaries and review cues.

Common failure mode and fix:
- Failure: The learner asks for improvement without review conditions.
- Fix: Include constraints and validation in the original prompt.

## Hands-On Lab
Scenario context:
- Your team wants to rely on Copilot for drafts and documentation support, but only if review standards stay high.

Learner goal:
- Review one AI-generated result using a data-team-specific checklist and document what still needs human approval.

Tasks:
1. Select one file and ask Copilot for a small improvement or explanation.
2. Review the output for business correctness, reproducibility, or operational impact.
3. Record one thing that is acceptable.
4. Record one thing that needs human validation.
5. Record one risk that would matter in production or reporting.

Suggested learner prompts:
- `Add a short validation checklist to this file and explicitly list what still needs human review.`
- `Explain this query and identify assumptions that a BI analyst should verify.`
- `Summarize this notebook and list any reproducibility risks.`
- `Review this pipeline documentation and list operational checks that still require a human decision.`

Expected observable output:
- One AI-generated draft or explanation
- One written review note
- One explicit human follow-up item

## Validation Checklist
- The learner can name a risk specific to BI, DS, or DE work.
- The learner can review more than wording and formatting.
- The learner can identify one assumption that still requires human validation.
- The learner can ask Copilot to list review boundaries explicitly.
- The learner can describe why observable validation matters.

## Reflection Tasks
- What kind of hidden risk worries your team most: wrong business meaning, low reproducibility, or operational failure?
- What review step would you standardize across your team?
- What should always require human approval even if Copilot output looks strong?
- How can your prompts reduce review effort without removing accountability?

## References
- VS Code AI best practices: https://code.visualstudio.com/docs/copilot/best-practices
- GitHub Copilot best practices: https://docs.github.com/en/copilot/get-started/best-practices
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
