# Presenter Deck: Advanced Skills, Agents, And Plugins

## Slide 1. Module Purpose

Presenter note:

- Introduce this as the first advanced module after the beginner core. Learners should leave with a decision model, not just more terminology.

Key points:

- Module 08 moves from safe beginner use into controlled advanced design.
- The main goal is to choose the right building block for the job.

## Slide 2. Why This Matters

Presenter note:

- Teams often create unnecessary automation because they skip the classification step.

Key points:

- A repeated checklist is not automatically an agent.
- An agent is not useful if it lacks the capability access it needs.
- A plugin does not provide judgment by itself.

## Slide 3. Core Definitions

Presenter note:

- Keep the definitions simple and repeat them exactly.

Key points:

- Skill: reusable guidance, method, checklist, or pattern for a type of work.
- Agent: task execution workflow that can reason across steps and carry a task forward.
- Plugin: external capability provider such as an extension, MCP server, or integration.

## Slide 4. Decision Rules

Presenter note:

- Encourage learners to ask one question first: what is actually missing?

Key points:

- Missing consistency: start with a skill.
- Missing multi-step execution: add an agent.
- Missing system access: add a plugin.

## Slide 5. How They Work Together

Presenter note:

- Show the layered pattern rather than teaching the parts in isolation.

Key points:

- Skill sets the method.
- Agent runs the workflow.
- Plugin provides external access.

Example flow:

- A notebook reproducibility skill defines the review checklist.
- A review agent executes the checklist across files.
- A plugin exposes experiment metadata or artifact access.

## Slide 6. BI Example

Presenter note:

- Use a concrete reporting example instead of generic automation language.

Key points:

- Skill: monthly KPI release checklist for gross margin, net sales, and YTD revenue.
- Agent: report review agent that compares README guidance, glossary terms, and release notes.
- Plugin: Power BI or metadata integration that exposes model context.

## Slide 7. DS Example

Presenter note:

- Keep the example grounded in reproducibility and experiment discipline.

Key points:

- Skill: notebook reproducibility standard covering seeds, package versions, and dataset snapshots.
- Agent: experiment review agent that inspects notebook notes and dependency files.
- Plugin: registry or experiment-tracking integration.

## Slide 8. DE Example

Presenter note:

- Focus on incident triage rather than promising automatic fixes.

Key points:

- Skill: failed-pipeline triage checklist.
- Agent: incident summary agent that reviews logs, runbooks, and validation notes.
- Plugin: orchestration or log integration for external state.

## Slide 9. Governance Checks

Presenter note:

- This slide is the control point. Do not rush through it.

Key points:

- Define scope before enabling the workflow.
- Keep plugin permissions narrow.
- Require observable validation output.
- Keep a human approval checkpoint for risky actions.

## Slide 10. Design Exercise

Presenter note:

- Ask learners to classify one workflow from their own team.

Exercise:

- Write the workflow outcome in one sentence.
- Label what belongs in a skill.
- Label what belongs in an agent.
- Label what requires plugin access.

## Slide 11. Validation Check

Presenter note:

- Learners should be able to justify the architecture, not just label the boxes.

Validation prompts:

- Why is this not only a checklist?
- Why is this not only a plugin?
- What stays manual?

## Slide 12. Reflection

Presenter note:

- Ask where the team should deliberately avoid more automation.

Discussion prompts:

- What task is over-automated today?
- Where would a reusable skill help immediately?
- Which plugin request would need the strongest review?

## Slide 13. References

Presenter note:

- Point learners to the local comparison reference so the terminology stays consistent across later modules.

References:

- `references/skills-agents-and-plugins-differences.md`
- `references/github-copilot-reimagine-overview.md`
- `references/copilot-agent-beginner-best-practices.md`
- `references/awesome-copilot-agents-for-presentation-improvement.md`
