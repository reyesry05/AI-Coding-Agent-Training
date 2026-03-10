# Contributing Guide

## Purpose

Use this guide when creating or updating training materials in this workspace.
The goal is to keep modules consistent, beginner-friendly, reproducible, and aligned to BI, data science, and data engineering workflows.

For project-level AI assistant context, see `CLAUDE.md` at the workspace root.
For workspace-wide agent rules, see `.github/copilot-instructions.md`.

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
- `labs/<module-name>/README.md`

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

## Markdown Standards

These formatting rules apply to all Markdown files:

- **MD022**: Blank lines above and below every heading.
- **MD032**: Blank lines above and below every list.
- **MD034**: No bare URLs. Always use angle brackets (`<URL>`) or `[text](URL)`.
- **MD047**: Files must end with exactly one trailing newline.
- Use ATX-style headings (`#`, not underlines).
- Do not skip heading levels.
- Keep lines under 200 characters when practical.

When editing existing files, fix any lint violations you encounter in the content you touch.

## Copilot-Specific Standards

Prefer Research (project start), then Ask, then Edit, then Plan, then Agent for beginner progression. Research means searching top GitHub repos for proven patterns and reviewing Azure Well-Architected Framework guidance; it is a project-inception step, not repeated per task.
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

- Headings are consistent and lint-clean (MD022, MD032, MD034, MD047)
- Commands or actions are accurate for the stated environment
- Prompts are specific and safe
- References point to official first-party docs when possible
- The lab has observable evidence of completion
- The root README index is updated if a new module was added

## Git Conventions

- This workspace is now a standalone repository.
- The default branch is `main` unless the repository settings change.
- Use imperative mood for commit messages, scoped to what changed.

## Repository Visibility

- This repository is currently intended to be public.
- Only publish generic training material that does not contain Reyes Holdings-specific code, architecture, credentials, customer information, or internal operating details.
- If a module becomes company-specific, either redact the sensitive content or move that material to a private repository.
- Before publishing new content, confirm that examples, screenshots, and prompts do not reveal internal systems or private data.

## When To Update Workspace Instructions

Update `.github/copilot-instructions.md` when a new workspace-wide rule appears repeatedly across modules.
Do not overload workspace instructions with one-off module details.
Update `CLAUDE.md` when a project-level fact changes (audience, layout, git conventions).

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
- Do all Markdown files pass the lint rules above?
