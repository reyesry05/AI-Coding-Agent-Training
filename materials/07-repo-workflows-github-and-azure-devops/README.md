# Repo Workflows In GitHub And Azure DevOps

## Learning Objectives
By the end of this module, learners should be able to:
- explain how repository context affects Copilot workflows in VS Code
- work safely in teams using either GitHub or Azure DevOps repositories
- choose prompts that fit documentation, notebook, script, and pipeline changes
- review AI-generated changes before they become commits or pull requests
- recognize where repository workflow differs from local drafting work

## Prerequisites And Setup
Audience:
- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:
- Modules 01 through 06 completed or equivalent knowledge
- A safe local clone or working copy from GitHub or Azure DevOps
- Basic familiarity with source control concepts such as branch, commit, and pull request

Success looks like:
- The learner can explain what repository context adds to an AI workflow.
- The learner can describe how review fits before commit or PR submission.
- The learner can choose prompts that are safe for version-controlled work.

Common failure mode and fix:
- Failure: The learner treats repository-backed work like disposable local experimentation.
- Fix: Add explicit review and source control checkpoints before accepting or committing changes.

## Walkthrough

### Step 1. Understand repository context
Goal of the step:
- See why working in a repo changes the risk profile.

Exact action:
- Compare a loose local draft with a file that will become part of a shared repository.
- Identify where review, commit history, and team conventions matter.

What success looks like:
- The learner can explain why repository changes need stronger discipline.

Common failure mode and fix:
- Failure: The learner assumes any generated change can be committed if it looks useful.
- Fix: Require review against team conventions and intended history.

### Step 2. Work safely in GitHub or Azure DevOps clones
Goal of the step:
- Use Copilot in a real repo without overstepping.

Exact action:
- Open a safe branch or practice clone.
- Limit the prompt to a small, reviewable change.
- Keep the file scope explicit.

What success looks like:
- The learner makes a change that is easy to inspect before commit.

Common failure mode and fix:
- Failure: The learner prompts for broad cross-repo changes without understanding impact.
- Fix: Start with one file or one README change.

### Step 3. Review before commit or PR
Goal of the step:
- Build the habit of reviewing AI output in source control, not only in chat.

Exact action:
- Review the diff.
- Confirm the change matches the stated task.
- Check whether the output would make sense to another reviewer.

What success looks like:
- The learner can state what they would or would not commit.

Common failure mode and fix:
- Failure: The learner accepts output without checking how it will look in a review.
- Fix: View the diff as if another teammate must approve it.

### Step 4. Use prompts that fit repo workflows
Goal of the step:
- Ask Copilot for repo-safe changes.

Exact action:
- Use prompts such as:
  - `Update this README section only. Preserve the existing headings and style.`
  - `Add a validation checklist to this notebook README. Do not modify code cells.`
  - `Improve this pipeline troubleshooting section. Keep deployment steps unchanged.`

What success looks like:
- The prompt results in a narrow, reviewable diff.

Common failure mode and fix:
- Failure: The prompt allows the model to restructure too much at once.
- Fix: Limit file count, change type, and what must stay unchanged.

### Step 5. Respect platform differences without overcomplicating training
Goal of the step:
- Keep the guidance useful regardless of whether the team uses GitHub or Azure DevOps.

Exact action:
- Focus on shared habits: branch safely, review diffs, validate before commit, and keep changes small.
- Mention platform-specific review tools only as implementation details.

What success looks like:
- The learner understands that the core workflow is similar even if the hosting platform differs.

Common failure mode and fix:
- Failure: The learner thinks the training only applies to GitHub.
- Fix: Reinforce that the core VS Code and review habits apply to both repository systems.

## Hands-On Lab
Scenario context:
- Your team keeps data artifacts in GitHub or Azure DevOps and wants to use Copilot without weakening review quality.

Learner goal:
- Make one small repo-safe change and review it before treating it as commit-ready.

Tasks:
1. Open a safe working copy from GitHub or Azure DevOps.
2. Choose one README, notebook README, SQL documentation file, or pipeline note.
3. Ask Copilot for one small, bounded improvement.
4. Review the diff.
5. Decide whether the change is ready, needs revision, or should be rejected.
6. Record the reason for that decision.

Suggested learner prompts:
- `Update this README section only and preserve the existing tone and headings.`
- `Add a short validation checklist to this file without changing any other file.`
- `Improve the troubleshooting section for a new data engineer. Keep the deployment steps unchanged.`
- `Before making changes, ask clarifying questions if the expected repository impact is unclear.`

Expected observable output:
- One small diff
- One written decision to keep, revise, or reject the change
- One reason tied to repo quality or reviewability

## Validation Checklist
- The learner can explain why repository work needs stricter review than a disposable draft.
- The learner can limit a prompt to a small, reviewable scope.
- The learner can review a diff before treating a change as commit-ready.
- The learner can apply the same safe habits in GitHub or Azure DevOps workflows.
- The learner can state one reason to reject an AI-generated change.

## Reflection Tasks
- What makes a generated change feel safe enough to commit?
- What repo habit should never be skipped when using Copilot?
- What kinds of requests should stay local drafts instead of becoming repo changes immediately?
- How similar are the safe review habits between GitHub and Azure DevOps in practice?

## References
- VS Code chat overview: https://code.visualstudio.com/docs/copilot/chat/copilot-chat
- VS Code AI best practices: https://code.visualstudio.com/docs/copilot/best-practices
- GitHub Copilot best practices: https://docs.github.com/en/copilot/get-started/best-practices
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
