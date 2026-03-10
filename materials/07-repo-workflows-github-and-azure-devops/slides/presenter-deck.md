# Presenter Deck: Repo Workflows In GitHub And Azure DevOps

## Slide 1. Title
On-screen content:
- Repo Workflows In GitHub And Azure DevOps
- Safe repository-backed Copilot use

Presenter notes:
- This module connects local Copilot use to real team workflows. The emphasis is on discipline, not automation for its own sake.
- Open by framing this as the final transfer step: the same keep, revise, or reject discipline from module 06 now has to hold up when changes are visible to teammates in GitHub or Azure DevOps.

## Slide 2. Learning Objectives
On-screen content:
- work safely in repo-backed workspaces
- constrain Copilot changes to reviewable scope
- review diffs before commit or PR
- apply the same habits in GitHub and Azure DevOps

Presenter notes:
- Explain that repository-backed work raises the review bar.

## Slide 3. Why Repo Context Changes The Risk
On-screen content:
- shared history
- review by teammates
- branch and PR expectations
- less room for vague edits

Presenter notes:
- A local draft can be messy. A repo change affects everyone who reads the history.

## Slide 4. Shared Safe Habits Across Platforms
On-screen content:
- small changes
- explicit scope
- diff review
- validation before commit

Presenter notes:
- Keep the training platform-agnostic where possible.

## Slide 5. Good Repo-Safe Prompt Patterns
On-screen content:
- update one section only
- preserve headings and tone
- do not modify other files
- ask clarifying questions if scope is unclear

Presenter notes:
- These patterns reduce the chance of broad, hard-to-review diffs.

## Slide 6. BI Example -- Repo Diff Review
On-screen content:
- Scenario: Copilot updated a KPI glossary in a shared repo. Review the diff before merge.

**Diff (what the PR shows):**
```diff
 ## KPI Glossary

- **Gross Margin**: Revenue minus cost.
+ **Gross Margin**: Total revenue minus cost of goods sold (COGS),
+ excluding returns and allowances.
+
+ **Gross Margin %**: Gross Margin divided by Total Revenue,
+ expressed as a percentage. Returns BLANK for zero-revenue periods.

  **YTD Revenue**: Calendar year-to-date sum of net revenue.
```

- Review: Did the AI **change** the Gross Margin definition or **clarify** it?
- Is the new Gross Margin % metric approved by Finance?
- Decision: Keep, Revise, or Reject the PR?

Presenter notes:
- Walk through the diff format. The `-` lines are removals, `+` lines are additions. The AI expanded the Gross Margin definition (likely an improvement) and added a new metric (Gross Margin %) that may not be approved. Ask: who owns the authority to add new KPIs? This is a real governance question that a code review alone cannot answer.

## Slide 7. DS Example -- Repo Diff Review
On-screen content:
- Scenario: Copilot updated a notebook prerequisites section. Review before merge.

**Diff (what the PR shows):**
```diff
 ## Prerequisites

- Python 3.10+
+ Python 3.12+
+ Packages: pandas==2.2, scikit-learn==1.5, prophet==1.1
+ Data: data/monthly_sales_v3.csv (exported 2026-02-15)
+ Random seed: 42
+
+ Run `pip install -r requirements.txt` before executing.
```

- Review: Is the Python version bump from 3.10 to 3.12 intentional or a side effect?
- Are the pinned package versions correct for this experiment?
- Decision: Keep, Revise, or Reject the PR?

Presenter notes:
- The AI upgraded Python 3.10 to 3.12 and added useful prerequisite details. But the version bump may break CI or team environments still on 3.10. Ask: did anyone request the Python upgrade? The data and seed additions are clearly helpful. The right call may be Revise -- keep the new lines but revert the Python version change.

## Slide 8. DE Example -- Repo Diff Review
On-screen content:
- Scenario: Copilot updated a pipeline runbook in the repo. Review before merge.

**Diff (what the PR shows):**
```diff
 ## Troubleshooting: Daily Order Load

  1. Check Airflow logs for the `load_orders` task.
- 2. Retry the task manually if it failed.
+ 2. Verify `staging.raw_orders` refresh completed (check load_date).
+ 3. Retry the task from the Airflow UI.
+ 4. If retry fails after 3 attempts, page the on-call DE.
+ 5. Do NOT skip the staging check -- stale data propagates downstream.

  ## Rollback
  - Restore from the previous partition snapshot.
```

- Review: Is the **escalation path** (page on-call DE) correct for your team?
- Should step 5 be a warning or a hard gate?
- Decision: Keep, Revise, or Reject the PR?

Presenter notes:
- The AI replaced a vague "retry manually" step with a structured troubleshooting sequence. This is a clear improvement. But ask: is 3 retries correct? Is paging the on-call DE the right escalation, or should it go to the team lead first? Operational runbooks must match the actual incident process. The diff looks great, but the DE must verify every step against reality.

## Slide 9. Review The Diff, Not Just The Response
On-screen content:
- inspect exact changes
- compare to request
- check reviewability

Presenter notes:
- The response text is not the deliverable. The diff is the deliverable.

## Slide 10. Keep, Revise, Or Reject In Repo Work
On-screen content:
- ready for commit
- needs another pass
- not safe to merge

Presenter notes:
- Encourage learners to reject confidently when the scope or meaning is off.

## Slide 11. Platform-Agnostic Message
On-screen content:
- GitHub and Azure DevOps differ in tooling details
- safe habits are largely the same

Presenter notes:
- This matters because many teams overfocus on platform differences and miss the shared review habits.

## Slide 12. Repo Change Exercise
On-screen content:
- make one small repo-backed change
- review the diff
- decide keep, revise, or reject

Presenter notes:
- One file is enough for the exercise.

## Slide 13. Merge-Readiness Check
On-screen content:
- learner can constrain repo scope
- learner can review diff quality
- learner can justify readiness

Presenter notes:
- Require a reason for any keep decision.

## Slide 14. Team Workflow Debrief
On-screen content:
- what makes a change commit-ready?
- what should never skip review?

Presenter notes:
- Pull examples from each audience group.

## Slide 15. References
On-screen content:
- VS Code chat overview
- VS Code AI best practices
- GitHub Copilot best practices
- Workspace module: materials/07-repo-workflows-github-and-azure-devops/README.md
- Workspace reference: references/copilot-agent-beginner-best-practices.md

Presenter notes:
- Encourage teams to turn the repo-safe prompt patterns into standard practice and store those rules where both GitHub and Azure DevOps teams can find them.
