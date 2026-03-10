# Project Guidelines

## Mission

This workspace produces high-quality training materials for a technical workforce learning to use GitHub Copilot AI agents in Visual Studio Code.
Prioritize clarity, reproducibility, and practical hands-on outcomes over theory-only content.
Treat this as a curriculum/content project, not an application codebase.

For Claude-specific project context, see `CLAUDE.md` at the workspace root.

## Audience And Outcomes

Assume learners are technical practitioners (developers, architects, engineers, BI specialists, data scientists, and data engineers) with mixed AI-assistant experience.
Initial target audiences are business intelligence teams, data science teams, and data engineering teams.
Assume teams may store their code or infrastructure assets in either GitHub repositories or Azure DevOps repositories.
Each module should help learners do three things:

- Understand what the agent can and cannot do
- Practice a realistic workflow in VS Code
- Apply guardrails for safety, quality, and verification

## Content Structure

Use a consistent module shape for all training assets:

1. Learning objectives
2. Prerequisites and setup
3. Instructor or self-paced walkthrough
4. Hands-on lab with expected outputs
5. Validation checklist
6. Reflection and extension tasks

When creating a new module, prefer this folder pattern:

- `materials/<module-name>/README.md`
- `materials/<module-name>/slides/slide-outline.md`
- `materials/<module-name>/slides/presenter-deck.md`
- `labs/<module-name>/README.md`
- `labs/<module-name>/starter/README.md`
- `labs/<module-name>/solution/README.md`
- `assets/<module-name>/` (optional, for diagrams or media)

## Writing And Style

Use plain, direct language and define terms the first time they appear.
Prefer short paragraphs, step-by-step instructions, and concrete examples.
Use ASCII unless there is a clear reason to include Unicode.

For every procedure, include:

- Goal of the step
- Exact command or action
- What success looks like
- Common failure mode and fix

## Markdown Standards

These formatting rules apply to all Markdown files in this workspace:

- **MD022**: Blank lines above and below every heading.
- **MD032**: Blank lines above and below every list.
- **MD034**: No bare URLs. Always use angle brackets (`<URL>`) or `[text](URL)`.
- **MD047**: Files must end with exactly one trailing newline.
- Use ATX-style headings (`#`, not underline style).
- Do not skip heading levels (for example, do not jump from `##` to `####`).
- Keep lines under 200 characters when practical.

When editing existing files, fix any lint violations in content you touch.

## Agent Workflow Expectations
When generating or updating training content:
- Keep examples realistic and runnable on a default Windows VS Code setup unless the module explicitly targets another environment
- Prefer examples and scenarios that feel credible for BI analytics, data science experimentation, or data engineering workflows when no other audience is specified
- Include verification steps after content changes (format checks, link checks, command checks, and manual validation)
- Call out assumptions when repository structure or tooling is missing
- Avoid hidden magic; always show key commands and files used

For coding labs, include:
- Starter state
- Target state
- Minimal acceptance criteria
- Suggested prompts learners can try with Copilot Chat

For non-coding labs, include:
- Scenario context and learner goal
- Required VS Code actions and prompts
- Observable output evidence (screenshots, generated files, logs, or checklist results)
- Reflection prompts that assess understanding and safe usage

## Build And Test

This project is currently bootstrapping and has no global software build/test tooling yet.
Until tooling is added, validate each module using:

- Markdown quality review (headings, links, formatting consistency, lint rules above)
- Command accuracy check on stated shell (PowerShell for Windows-first labs)
- Lab completion checklist with expected observable output
- Internal link verification (all cross-references resolve to existing files)

When automation is introduced (for docs quality or lab validation), document canonical commands in this file and module READMEs.

## Git Conventions

- Training content lives under the `AI Coding Agent Training/` subdirectory of the parent repository.
- Stage only the training directory to avoid touching unrelated files.
- Use imperative mood for commit messages, scoped to what changed (e.g., "Add module 08 advanced curriculum").
- The current working branch for training pushes is `ai-coding-agent-training-20260309`.

## Conventions

Name modules with kebab-case and numeric ordering when sequence matters.
Examples:

- `materials/01-agent-fundamentals/`
- `labs/02-context-and-instructions/`

Keep prompts and instruction assets discoverable:

- Workspace instructions: `.github/copilot-instructions.md`
- Claude instructions: `CLAUDE.md` (project root)
- File-specific instructions: `.github/instructions/*.instructions.md`
- Reusable prompts: `.github/prompts/*.prompt.md`
- Agent definitions: `.github/agents/*.agent.md`
- Skills: `.github/skills/<skill-name>/SKILL.md`

Do not duplicate long reference content across files; link to source files instead.

For beginner-facing GitHub Copilot agent guidance, use `references/copilot-agent-beginner-best-practices.md` as the baseline reference.
For advanced skill/agent/plugin guidance, use `references/skills-agents-and-plugins-differences.md`.

## Quality Bar

A training module is complete only when:

- Objectives map to the lab tasks
- Steps are reproducible from a clean environment
- Validation checks are explicit
- Learner-facing prompts are included
- Known pitfalls and troubleshooting tips are documented
- Markdown lint rules (MD022, MD032, MD034, MD047) pass on all files
- The root README module index is updated

