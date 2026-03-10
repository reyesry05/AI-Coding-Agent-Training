# Awesome Copilot Agents For Presentation Improvement

This reference summarizes the most relevant agents and skills found in the `github/awesome-copilot` repository for improving training presentations, slide decks, curriculum structure, and instructional content.

## Best-Fit Agents

### 1. gem-documentation-writer
Source:
- `plugins/gem-team/agents/gem-documentation-writer.md`

Why it is relevant:
- Designed to generate technical documentation, walkthroughs, and diagrams.
- Strong fit for improving slide text, presenter notes, curriculum summaries, and supporting documentation.

Best use in this workspace:
- rewrite slide decks for clarity
- improve presenter notes
- keep module README, labs, and slides aligned
- suggest diagrams or visual structure improvements

### 2. technical-content-evaluator
Source:
- `agents/technical-content-evaluator.agent.md`

Why it is relevant:
- Best fit for reviewing educational content quality.
- Focuses on structure, prerequisite clarity, progression, missing diagrams, and exercise quality.

Best use in this workspace:
- review slide decks for clarity and flow
- find weak transitions between modules
- identify missing learner checkpoints
- check whether labs are concrete and observable

### 3. gem-researcher
Source:
- `plugins/gem-team/agents/gem-researcher.md`

Why it is relevant:
- Useful for structured analysis before rewriting content.
- Can identify duplication, patterns, and missing coverage.

Best use in this workspace:
- analyze current curriculum for overlap or gaps
- compare BI, DS, and DE audience coverage
- identify missing examples or reference needs

### 4. gem-planner
Source:
- `plugins/gem-team/agents/gem-planner.md`

Why it is relevant:
- Strong planning agent for turning vague improvement requests into structured revision plans.

Best use in this workspace:
- create a revision plan for modules and decks
- decompose presentation improvements into steps
- identify likely failure points in the learning flow

### 5. se-technical-writer
Source:
- `plugins/software-engineering-team/README.md`

Why it is relevant:
- Strong fit for instructional writing, tutorials, and educational content refinement.

Best use in this workspace:
- simplify wording for beginner audiences
- improve tutorial flow
- rewrite technical explanations for teaching clarity

### 6. QA
Source:
- `agents/qa-subagent.agent.md`

Why it is relevant:
- Good final-pass review agent for verification and gap-finding.

Best use in this workspace:
- validate that labs are testable
- find ambiguous or incomplete steps
- identify learner failure points before delivery

## Helpful Supporting Agents And Skills

### plan
Source:
- `agents/plan.agent.md`

Use when:
- you want a simpler planning step before rewriting modules or slides

### structured-autonomy-plan
Source:
- `plugins/structured-autonomy/skills/structured-autonomy-plan/SKILL.md`

Use when:
- you want a more disciplined, commit-like planning workflow for curriculum changes

### documentation-writer
Source:
- `docs/README.skills.md`

Use when:
- you want documentation-writing guidance rather than a custom agent workflow

### prompt-builder
Source:
- `agents/prompt-builder.agent.md`

Use when:
- you want stronger prompts for curriculum creation, slide improvement, or review workflows

### power-bi-visualization-expert
Source:
- `plugins/power-bi-development/README.md`

Use when:
- you want BI examples in slides or labs to feel more authentic and useful to reporting teams

## Recommended Workflow For Improving This Presentation

### Option 1. Full content-improvement workflow
1. Use `gem-researcher` to analyze current curriculum quality, gaps, and duplication.
2. Use `gem-planner` to create a revision plan for modules, labs, and slides.
3. Use `gem-documentation-writer` or `se-technical-writer` to rewrite or expand the deck.
4. Use `technical-content-evaluator` to review the revised material.
5. Use `QA` to test labs and check learner-facing clarity.

### Option 2. Lightweight workflow
1. Use `technical-content-evaluator` to identify the biggest presentation issues.
2. Use `gem-documentation-writer` to improve the weak areas.
3. Use `QA` to validate the result.

## Best Immediate Candidates For This Workspace
If only a small number of agents are added or mimicked, start with:
- `gem-documentation-writer`
- `technical-content-evaluator`
- `gem-planner`
- `gem-researcher`
- `QA`

These five cover research, planning, writing, evaluation, and validation, which is the full loop needed to improve training presentations.

## Suggested Next Custom Agents For This Workspace
Based on the research above, the most useful custom agents to create locally would be:
- `presentation-reviewer.agent.md`
  - Review slide decks for structure, clarity, missing diagrams, and weak learner checkpoints.
- `curriculum-writer.agent.md`
  - Generate or revise training modules, slide decks, presenter notes, and lab documentation.
- `lab-validator.agent.md`
  - Review labs for observability, validation, failure modes, and learner success evidence.

## Source Repository
- `https://github.com/github/awesome-copilot`

## Notes
- This repository is broad. Many agents are software-engineering-oriented, so only a subset fits training and presentation work directly.
- The strongest pattern for this workspace is not one single agent, but a sequence of research, planning, writing, and evaluation.