# Slide Outline: Repo Workflows In GitHub And Azure DevOps

## Slide 1. Title
- Repo Workflows In GitHub And Azure DevOps
- Safe repository-backed Copilot use

Speaker note:
- Assume learners can already justify keep, revise, or reject decisions from module 06 and frame this module as the transfer of those habits into shared repository workflows.

## Slide 2. Learning Objectives
- work safely in repo-backed workspaces
- constrain Copilot changes to reviewable scope
- review diffs before commit or PR
- apply the same habits in GitHub and Azure DevOps

## Slide 3. Why Repo Context Changes The Risk
- shared history
- review by teammates
- branch and PR expectations
- less room for vague edits

## Slide 4. Shared Safe Habits Across Platforms
- small changes
- explicit scope
- diff review
- validation before commit

## Slide 5. Good Repo-Safe Prompt Patterns
- update one section only
- preserve headings and tone
- do not modify other files
- ask clarifying questions if scope is unclear

## Slide 6. BI Example -- Repo Diff Review
- Diff scenario: AI expanded Gross Margin definition and added unapproved Gross Margin % metric
- Review: did the AI clarify the definition or change it?
- Governance question: who owns the authority to add new KPIs?
- Decision: Keep, Revise, or Reject the PR?

## Slide 7. DS Example -- Repo Diff Review
- Diff scenario: AI bumped Python version from 3.10 to 3.12 and added prerequisite details
- Review: is the Python version bump intentional or a side effect?
- Useful additions: pinned packages, data path, random seed
- Decision: likely Revise -- keep new lines, revert the version change

## Slide 8. DE Example -- Repo Diff Review
- Diff scenario: AI replaced vague "retry manually" with structured troubleshooting steps
- Review: is the escalation path (page on-call DE) correct for your team?
- Improvement: numbered steps with staging check, retry limit, escalation
- Decision: Keep, Revise, or Reject the PR?

## Slide 9. Review The Diff, Not Just The Response
- inspect exact changes
- compare to request
- check reviewability

## Slide 10. Keep, Revise, Or Reject In Repo Work
- ready for commit
- needs another pass
- not safe to merge

## Slide 11. Platform-Agnostic Message
- GitHub and Azure DevOps differ in tooling details
- safe habits are largely the same

## Slide 12. Repo Change Exercise
- make one small repo-backed change
- review the diff
- decide keep, revise, or reject

## Slide 13. Merge-Readiness Check
- learner can constrain repo scope
- learner can review diff quality
- learner can justify readiness

## Slide 14. Team Workflow Debrief
- what makes a change commit-ready?
- what should never skip review?

## Slide 15. References
- VS Code chat overview
- VS Code AI best practices
- GitHub Copilot best practices
- Workspace module: `materials/07-repo-workflows-github-and-azure-devops/README.md`
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
