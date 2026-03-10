# Contributing Guide

## Purpose
Use this guide when creating or updating training materials in this workspace.
The goal is to keep modules consistent, beginner-friendly, reproducible, and aligned to BI, data science, and data engineering workflows.

## Audience Defaults
Unless a module says otherwise, assume the audience is:
- business intelligence teams
- data science teams
- data engineering teams

Unless a module says otherwise, also assume:
- Windows-first VS Code workflows
- GitHub or Azure DevOps repository usage
- beginner or early-intermediate Copilot users

## Required Structure
Every new module should normally include:
- `materials/<module-name>/README.md`
- `materials/<module-name>/slides/slide-outline.md`
- `materials/<module-name>/slides/presenter-deck.md`
- `labs/<module-name>/README.md`
- `labs/<module-name>/starter/README.md`
- `labs/<module-name>/solution/README.md`

## Required Sections For Material READMEs
Each material README should include:
1. Learning objectives
2. Prerequisites and setup
3. Walkthrough
4. Hands-on lab
5. Validation checklist
6. Reflection tasks
7. References

## Required Sections For Lab READMEs
Each lab README should include:
1. Scenario context
2. Learner goal
3. Starter state
4. Target state
5. Prerequisites and setup
6. Lab tasks
7. Suggested learner prompts
8. Expected observable output
9. Validation checklist
10. Reflection tasks
11. Solution guidance

## Writing Standards
Use plain, direct language.
Prefer short paragraphs and concrete examples.
Do not assume advanced coding experience unless the module explicitly targets it.
Keep examples credible for analytics, notebooks, SQL, pipelines, reporting, or adjacent data-platform work.

## Copilot-Specific Standards
Prefer Ask, then Plan, then Agent for beginner progression.
Require visible validation steps and observable outputs.
Avoid prompts that encourage broad or unreviewable edits.
Ground guidance in first-party documentation whenever possible.
Make review expectations explicit.

## Good Module Design Rules
A strong module should:
- teach one main behavior or capability clearly
- include at least one common failure mode and fix
- include suggested prompts learners can try immediately
- make the human review step explicit
- be understandable without hidden setup knowledge

## Naming Conventions
Use kebab-case and numeric ordering when sequence matters.
Examples:
- `materials/03-first-safe-prompts-ask-plan-agent/`
- `labs/05-notebooks-sql-and-pipelines-with-copilot/`

## Quality Checks Before Finalizing
Before considering a module complete, verify:
- headings are consistent
- commands or actions are accurate for the stated environment
- prompts are specific and safe
- references point to official first-party docs when possible
- the lab has observable evidence of completion
- the root README index is updated if a new module was added

## When To Update Workspace Instructions
Update `.github/copilot-instructions.md` when a new workspace-wide rule appears repeatedly across modules.
Do not overload workspace instructions with one-off module details.

## When To Create New References
Create or extend a file in `references/` when:
- the same baseline guidance is reused across many modules
- the guidance needs a stable reference point
- first-party links should be collected in one place

## Pull Request Or Review Expectations
When reviewing a new module, check:
- Is the audience clear?
- Is the module sequence logical?
- Are the prompts safe and reviewable?
- Are BI, DS, or DE examples realistic?
- Are validation steps observable?
- Are the references sufficient and current?
