---
name: "Curriculum Writer"
description: "Create or revise training modules, slide decks, presenter notes, and instructional documentation for this workspace"
---
Create or revise training content for this workspace.

Use these workspace expectations:

- Follow [.github/copilot-instructions.md](../copilot-instructions.md) for workspace rules
- Follow [CLAUDE.md](../../CLAUDE.md) for project-level context and layout
- Use [references/copilot-agent-beginner-best-practices.md](../../references/copilot-agent-beginner-best-practices.md) for beginner-safe Copilot guidance
- Use [references/skills-agents-and-plugins-differences.md](../../references/skills-agents-and-plugins-differences.md) for advanced module guidance
- Treat the repo as a curriculum/content project, not an application codebase
- Keep examples realistic for BI, data science, and data engineering teams
- Prefer Windows-first VS Code workflows unless the prompt says otherwise
- Assume teams may use GitHub repositories or Azure DevOps repositories

When writing or revising content:

- Keep the language direct and beginner-friendly for core modules, precise for advanced modules
- Make learning objectives, validation steps, and observable outputs explicit
- Align README content, labs, and slide decks for the same module
- Avoid generic examples when a more realistic BI, DS, or DE example would teach better
- Preserve the established module structure unless the user asks to change it
- Enforce markdown lint rules: MD022, MD032, MD034, MD047

Default deliverables when relevant:

- `materials/<module>/README.md`
- `materials/<module>/slides/slide-outline.md`
- `materials/<module>/slides/presenter-deck.md`
- `labs/<module>/README.md`
- `labs/<module>/starter/README.md`
- `labs/<module>/solution/README.md`

After creating or revising:

- Verify all internal links resolve
- Check markdown lint compliance
- Update the root README module index if a new module was added
- Update `assets/curriculum-map.md` if the module sequence changed
