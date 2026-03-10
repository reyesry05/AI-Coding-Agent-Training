# AI Coding Agent Training

This workspace contains training materials for technical teams learning to use GitHub Copilot AI agents in Visual Studio Code.
The current training focus is beginner-friendly content for BI, data science, and data engineering teams.

## Audience
- Business intelligence teams
- Data science teams
- Data engineering teams

## Repository Assumptions
- Teams may store code, notebooks, scripts, or infrastructure assets in either GitHub repositories or Azure DevOps repositories.
- Training examples should stay credible for day-to-day analytics, reporting, notebook, pipeline, and data-platform work.
- The workspace is a curriculum/content project, not an application codebase.

## Training Principles
- Use plain, direct language.
- Prefer Ask, then Plan, then Agent for beginner progression.
- Keep examples Windows-first unless a module says otherwise.
- Require visible validation steps and observable outputs.
- Ground guidance in first-party documentation whenever possible.

## Contributor Guide
- `CONTRIBUTING.md`
  - Authoring standards for new modules, labs, slide assets, naming, and validation.

## Module Index

### Materials
- `materials/01-beginner-copilot-agent-best-practices/README.md`
  - Beginner guardrails, prompting habits, context management, and review expectations for BI, DS, and DE learners.
- `materials/02-setup-github-copilot-agents/README.md`
  - Prerequisites, setup steps, agent availability checks, and safe first-session workflow in VS Code.
- `materials/03-first-safe-prompts-ask-plan-agent/README.md`
  - How to write safe first prompts for Ask, Plan, and Agent with realistic BI, DS, and DE scenarios.
- `materials/04-context-and-instructions-for-data-teams/README.md`
  - How to use `#file`, `#codebase`, and reusable instructions to improve Copilot reliability for data teams.
- `materials/05-notebooks-sql-and-pipelines-with-copilot/README.md`
  - Safe Copilot patterns for notebooks, SQL, and pipeline-related workflows.
- `materials/06-review-and-verify-ai-output-for-data-work/README.md`
  - Review and validation methods for AI-generated output in data-team contexts.
- `materials/07-repo-workflows-github-and-azure-devops/README.md`
  - Safe repository-backed workflows for teams using GitHub or Azure DevOps.

### Labs
- `labs/01-beginner-copilot-agent-best-practices/README.md`
  - Hands-on practice for beginner guardrails and prompt improvement.
- `labs/02-setup-github-copilot-agents/README.md`
  - Hands-on setup lab with starter and solution notes.
- `labs/03-first-safe-prompts-ask-plan-agent/README.md`
  - Prompt-writing lab for Ask, Plan, and Agent.
- `labs/04-context-and-instructions-for-data-teams/README.md`
  - Context comparison lab plus instruction-candidate exercise.
- `labs/05-notebooks-sql-and-pipelines-with-copilot/README.md`
  - Safe data-artifact interpretation and support-content lab.
- `labs/06-review-and-verify-ai-output-for-data-work/README.md`
  - Review checklist lab for BI, DS, and DE outputs.
- `labs/07-repo-workflows-github-and-azure-devops/README.md`
  - Repository-backed change and diff review lab.

## Supporting References
- `references/copilot-agent-beginner-best-practices.md`
  - Baseline beginner guidance and official first-party links.
- `references/awesome-copilot-agents-for-presentation-improvement.md`
  - Recommended `awesome-copilot` agents and workflows for improving decks, curriculum structure, and training content.

## Current Sequence
1. Start with `materials/01-beginner-copilot-agent-best-practices/README.md`.
2. Run `labs/01-beginner-copilot-agent-best-practices/README.md`.
3. Continue with `materials/02-setup-github-copilot-agents/README.md`.
4. Run `labs/02-setup-github-copilot-agents/README.md`.
5. Continue with `materials/03-first-safe-prompts-ask-plan-agent/README.md`.
6. Run `labs/03-first-safe-prompts-ask-plan-agent/README.md`.
7. Continue with `materials/04-context-and-instructions-for-data-teams/README.md`.
8. Run `labs/04-context-and-instructions-for-data-teams/README.md`.
9. Continue with `materials/05-notebooks-sql-and-pipelines-with-copilot/README.md`.
10. Run `labs/05-notebooks-sql-and-pipelines-with-copilot/README.md`.
11. Continue with `materials/06-review-and-verify-ai-output-for-data-work/README.md`.
12. Run `labs/06-review-and-verify-ai-output-for-data-work/README.md`.
13. Continue with `materials/07-repo-workflows-github-and-azure-devops/README.md`.
14. Run `labs/07-repo-workflows-github-and-azure-devops/README.md`.

## Curriculum Coverage
- Module 01: beginner guardrails and safe expectations
- Module 02: environment setup and agent availability
- Module 03: safe first prompts for Ask, Plan, and Agent
- Module 04: context management and reusable instructions
- Module 05: notebooks, SQL, and pipeline-oriented workflows
- Module 06: review and verification for AI-generated output
- Module 07: GitHub and Azure DevOps repository workflows

## Slide Assets
- Modules 01 through 07 include slide assets under each module's `slides/` folder.
- Each module includes both `slide-outline.md` and `presenter-deck.md`.