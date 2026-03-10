# Advanced Skills, Agents, And Plugins

## Learning Objectives

By the end of this module, learners should be able to:

- explain the difference between a skill, an agent, and a plugin in this curriculum
- choose the right mechanism for a repeated workflow, an end-to-end task, or an external integration
- combine skills, agents, and plugins without creating unclear ownership
- identify governance checks before enabling advanced automation
- apply the model to realistic BI, DS, and DE scenarios

## Prerequisites And Setup

Audience:

- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:

- Modules 01 through 07 completed or equivalent knowledge
- Familiarity with Ask, Plan, and Agent workflows in VS Code
- One safe workspace with files that can be used for advanced workflow examples
- GitHub Copilot Chat available in VS Code

Success looks like:

- The learner can explain what each mechanism is for.
- The learner can defend a choice between skill, agent, and plugin.
- The learner can describe one safe advanced workflow for their team.

Common failure mode and fix:

- Failure: The learner treats every advanced capability as the same thing.
- Fix: Decide first whether the problem is about reusable guidance, multi-step execution, or external capability access.

## Walkthrough

### Step 1. Define The Three Terms Clearly

Goal of the step:

- Build a stable shared vocabulary before learners automate more work.

Exact action:

- Review the working definitions used in this workspace:
  - Skill: reusable domain or workflow guidance that teaches how to approach a class of tasks
  - Agent: an execution mode or specialized workflow that can reason across steps and carry a task forward
  - Plugin: an external capability provider, usually a VS Code extension, integration, MCP server, or tool source that gives the agent access it would not have from prompt text alone

What success looks like:

- The learner can explain each term in one sentence without overlap.

Common failure mode and fix:

- Failure: The learner says a plugin and an agent are interchangeable.
- Fix: Ask whether the item provides capability access or task execution behavior.

### Step 2. Choose The Right Mechanism For The Problem

Goal of the step:

- Match the mechanism to the actual need.

Exact action:

- Use a skill when the team repeats the same kind of task and needs consistent guidance.
- Use an agent when the task requires planning, iteration, and multi-step execution.
- Use a plugin when the workflow needs external capabilities, systems, data, or tools.

What success looks like:

- The learner can justify the choice before starting the task.

Common failure mode and fix:

- Failure: The learner creates an agent for a problem that only needs a reference or checklist.
- Fix: Start with the smallest mechanism that solves the problem safely.

### Step 3. Understand How They Work Together

Goal of the step:

- Show how advanced automation is usually composed, not isolated.

Exact action:

- Review a layered pattern:
  - A skill defines the method or standard.
  - An agent performs the task using that method.
  - A plugin provides access to systems or tools the task depends on.

What success looks like:

- The learner can sketch a simple flow from guidance to execution to capability access.

Common failure mode and fix:

- Failure: The learner adds multiple layers without assigning clear responsibility.
- Fix: State what each layer owns before combining them.

### Step 4. Apply The Pattern To BI, DS, And DE Examples

Goal of the step:

- Ground the distinctions in realistic work.

Exact action:

- BI example:
  - Skill: reusable report-review checklist
  - Agent: a reviewer agent that checks a Power BI README, KPI glossary, and release notes
  - Plugin: a Power BI or data-access integration that provides model or artifact access
- DS example:
  - Skill: notebook reproducibility checklist
  - Agent: an experiment-review agent that inspects notebook narrative, seed usage, and dependency notes
  - Plugin: an integration that exposes model registry or experiment metadata
- DE example:
  - Skill: pipeline incident triage checklist
  - Agent: an agent that investigates a failed pipeline run and prepares a summary
  - Plugin: an integration that exposes logs, orchestration state, or data-quality tooling

What success looks like:

- The learner can map each example to the three mechanisms.

Common failure mode and fix:

- Failure: The learner jumps straight to tooling without defining the method.
- Fix: Write the skill or standard first, then choose the execution and integration layers.

### Step 5. Add Governance And Review Rules

Goal of the step:

- Keep advanced automation reviewable and safe.

Exact action:

- Require explicit scope, expected outputs, validation steps, and escalation rules.
- Limit plugin access to the minimum needed capability.
- Review whether the agent should be allowed to edit, fetch, or execute.
- Document the skill source or reference so the workflow stays repeatable.

What success looks like:

- The learner can explain how the advanced workflow will be reviewed before rollout.

Common failure mode and fix:

- Failure: The learner enables broad access without a review plan.
- Fix: Add narrow scope, observable outputs, and human approval checkpoints.

## Hands-On Lab

Scenario context:

- Your team wants to move beyond beginner prompting and decide which advanced Copilot building block to use for repeated work.

Learner goal:

- Classify one realistic team scenario and propose the right mix of skill, agent, and plugin.

Tasks:

1. Pick one BI, DS, or DE workflow that your team repeats.
2. Write the workflow outcome in one sentence.
3. Decide whether the problem first needs a skill, an agent, a plugin, or a combination.
4. Write one reason for each chosen component.
5. Define one validation check and one human approval step.
6. Record one thing that should stay manual.

Suggested learner prompts:

- `For this reporting-review workflow, decide whether I need a skill, an agent, a plugin, or a combination. Explain why.`
- `Design a safe advanced Copilot workflow for a notebook reproducibility review.`
- `For a failed data pipeline investigation, separate what belongs in reusable guidance, what belongs in the agent, and what requires external integration.`

Expected observable output:

- One classified workflow diagram or note
- One written explanation of the chosen mechanism mix
- One validation check
- One human approval step
- One explicitly manual step

## Validation Checklist

- The learner can define skill, agent, and plugin without overlap.
- The learner can choose the smallest mechanism that fits the problem.
- The learner can explain how the three can work together.
- The learner can name one governance control for advanced automation.
- The learner can classify a BI, DS, or DE workflow correctly.

## Reflection Tasks

- Which mechanism does your team most overuse today?
- What task in your environment should stay a checklist instead of becoming an agent?
- What plugin access would require the strongest review before rollout?
- Where would a lightweight skill improve consistency without adding automation risk?

## References

- Workspace reference: `references/skills-agents-and-plugins-differences.md`
- GitHub Copilot coding agent guidance: <https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results>
- VS Code AI best practices: <https://code.visualstudio.com/docs/copilot/best-practices>
- VS Code custom instructions: <https://code.visualstudio.com/docs/copilot/customization/custom-instructions>
- VS Code extensions overview: <https://code.visualstudio.com/docs/editor/extension-marketplace>
