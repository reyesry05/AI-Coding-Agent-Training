# CLAUDE.md

Project-level instructions for AI assistants working in this workspace.
This file is read automatically by Claude Code and Claude in VS Code.
For GitHub Copilot-specific instructions, see `.github/copilot-instructions.md`.

## Project Identity

This is a **curriculum and content project**, not an application codebase.
It produces training materials for technical teams learning to use GitHub Copilot AI agents in Visual Studio Code.

- **Primary audiences**: business intelligence, data science, and data engineering teams.
- **Assumed environments**: Windows, VS Code, GitHub or Azure DevOps repositories.
- **Content types**: instructional READMEs, slide outlines, presenter decks, hands-on labs, and reference documents.

## Workspace Layout

```text
AI Coding Agent Training/
  .claude/                 # Claude-specific config (worktrees, settings)
  .github/
    copilot-instructions.md   # Workspace-wide rules for GitHub Copilot
    agents/                    # Reusable agent definitions (.agent.md)
    instructions/              # File-scoped instruction overlays (.instructions.md)
    prompts/                   # Reusable prompt templates (.prompt.md)
  assets/                  # Curriculum maps, diagrams, shared media
  html-slides/             # Reveal.js HTML slide decks (generated)
  labs/<module-name>/      # Lab content: README.md, starter/, solution/
  materials/<module-name>/ # Module content: README.md, slides/
  pptx-output/             # PowerPoint slide decks (generated)
  references/              # Shared reference documents and best-practice guides
  generate_pptx.py         # Presenter-deck to styled PPTX converter
  generate_revealjs.py     # Presenter-deck to Reveal.js HTML converter
  CONTRIBUTING.md          # Authoring standards for contributors
  README.md                # Root index with module list and sequence
```

## Module Conventions

### Naming

- Use kebab-case with numeric ordering: `01-agent-fundamentals`, `02-context-and-instructions`.
- Materials and labs share the same module name.

### Required Files Per Module

| Path | Purpose |
| --- | --- |
| `materials/<module>/README.md` | Instructional walkthrough with objectives, prerequisites, steps, validation, reflection |
| `materials/<module>/slides/slide-outline.md` | Numbered slide titles and key points |
| `materials/<module>/slides/presenter-deck.md` | Full slide content with speaker notes |
| `labs/<module>/README.md` | Hands-on lab with scenario, tasks, prompts, observable outputs, validation |
| `labs/<module>/starter/README.md` | Starting scenario and materials for learners |
| `labs/<module>/solution/README.md` | Example solution and explanation |

### Required Sections

**Material READMEs**: learning objectives, prerequisites and setup, walkthrough, hands-on lab reference, validation checklist, reflection tasks, references.

**Lab READMEs**: scenario context, learner goal, starter state, target state, prerequisites and setup, lab tasks, suggested prompts, expected observable output, validation checklist, reflection tasks, solution guidance.

## Writing Style

- Plain, direct language. Define terms on first use.
- Short paragraphs. Concrete examples over abstract explanation.
- ASCII only unless there is a clear reason for Unicode.
- Every procedure must include: goal, exact action or command, what success looks like, one common failure mode and fix.
- Prefer Research > Ask > Edit > Plan > Agent as the full beginner workflow. Research is a project-inception step (search top GitHub repos and review Azure Well-Architected Framework before writing code); Ask/Edit/Plan/Agent are the per-task loop.
- Keep examples realistic for BI, data science, and data engineering workflows.
- Assume Windows + PowerShell unless a module explicitly targets another environment.

## Markdown Standards

These rules are enforced across all Markdown files:

- **MD022**: Blank lines above and below every heading.
- **MD032**: Blank lines above and below every list.
- **MD034**: No bare URLs; always wrap in angle brackets or Markdown links.
- **MD047**: Files must end with a single trailing newline.
- Heading hierarchy must not skip levels (no `## ` directly under `# ` then `#### `).
- Use ATX-style headings (`#`, not underlines).

## Git And Branching

- Repository: the corporate GitHub repository for this training project (public-facing).
- A separate personal development repo exists and is not synced with the corporate repo.
- Working branch for training: `ai-coding-agent-training-20260309`.
- Commit messages: imperative mood, scoped to training content (e.g., "Add module 08 advanced curriculum").

## Validation

Until automated tooling is added, validate every change with:

1. **Markdown lint**: check MD022, MD032, MD034, MD047 across all changed files.
2. **Command accuracy**: verify shell commands work on Windows PowerShell.
3. **Link integrity**: confirm internal file references resolve correctly.
4. **Structural completeness**: use the required-sections lists above as a checklist.
5. **Audience fit**: examples should feel realistic for BI, DS, or DE practitioners.

## Key References

| File | Purpose |
| --- | --- |
| `references/copilot-agent-beginner-best-practices.md` | Baseline beginner guidance from official docs |
| `references/skills-agents-and-plugins-differences.md` | Skill vs agent vs plugin definitions and decision guide |
| `references/copilot-agent-approval-settings.md` | VS Code approval settings, YOLO mode profiles, and risk guidance |
| `references/awesome-copilot-agents-for-presentation-improvement.md` | Review rubric and improvement strategies |
| `CONTRIBUTING.md` | Full authoring standards |
| `generate_revealjs.py` | Presenter-deck to Reveal.js HTML slide converter |
| `generate_pptx.py` | Presenter-deck to styled PowerPoint converter |

## Presentation Generation

Two generator scripts convert `materials/*/slides/presenter-deck.md` files into presentation formats:

- **Reveal.js HTML** (`html-slides/`): Modern browser-based slides with transitions, speaker notes (press `S`), and responsive design. Preferred for presenting.
- **PowerPoint PPTX** (`pptx-output/`): Styled slides with colored bands, accent bars, and presenter notes. For teams that require .pptx files.

```powershell
# Generate Reveal.js HTML slides (requires no extra install)
.venv/Scripts/python.exe generate_revealjs.py

# Generate PowerPoint slides (requires python-pptx in .venv)
.venv/Scripts/python.exe generate_pptx.py
```

Both scripts parse two presenter-deck markdown patterns:

- `On-screen content:` / `Presenter notes:` (modules 01-07)
- `Key points:` / `Presenter note:` (module 08)

Re-run the scripts after editing any presenter deck to regenerate output.

## Things To Avoid

- Do not treat this workspace as an application codebase. There is no build system or test suite.
- Do not add code examples that require languages or runtimes beyond what the target audience uses (Python, SQL, PowerShell, DAX, notebooks).
- Do not duplicate long reference content across modules; link to `references/` files instead.
- Do not create files outside the established folder structure without justification.
- Do not assume GitHub-only workflows; always mention Azure DevOps where repository workflow matters.
- Do not use vague prompts as examples. Every example prompt should be specific, constrained, and safe.
- Do not use the deprecated `github.copilot.chat.agent.*` settings namespace. The current keys are `chat.tools.global.autoApprove`, `chat.tools.terminal.autoApprove`, `chat.tools.urls.autoApprove`, and `chat.editing.confirmEditRequestRetry`. See `references/copilot-agent-approval-settings.md`.

## Quick Commands

```powershell
# Check markdown lint (if markdownlint-cli is installed)
markdownlint "**/*.md" --config .markdownlint.json

# View git status scoped to training content
git status --short -- "AI Coding Agent Training"

# Stage and commit training changes only
git add -- "AI Coding Agent Training"
git commit -m "Your message here"

# Push to the training branch
git push origin HEAD:refs/heads/ai-coding-agent-training-20260309

# Regenerate all presentation decks
.venv/Scripts/python.exe generate_revealjs.py
.venv/Scripts/python.exe generate_pptx.py
```
