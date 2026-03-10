# First Safe Prompts For Ask, Plan, And Agent

## Learning Objectives
By the end of this module, learners should be able to:
- explain when to use Ask, Plan, and Agent in VS Code
- write safer first prompts for BI, data science, and data engineering work
- add constraints, expected outputs, and validation steps to prompts
- recognize when a prompt is too vague for autonomous execution
- improve weak prompts into specific, reviewable requests

## Prerequisites And Setup
Audience:
- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:
- Module 01 completed or equivalent knowledge of beginner guardrails
- Module 02 completed or equivalent environment setup
- GitHub Copilot Chat available in VS Code
- A small workspace with one or more files that are safe to inspect

Success looks like:
- The learner can explain why Ask is lower risk than Agent.
- The learner can rewrite a vague prompt into a safer one.
- The learner can add expected outputs and validation criteria.

Common failure mode and fix:
- Failure: The learner jumps directly to Agent with a broad request.
- Fix: Restate the task as Ask or Plan first, define output boundaries, then hand off to Agent only if the scope is clear.

## Walkthrough

### Step 1. Understand the three modes
Goal of the step:
- Distinguish the safest starting point for a task.

Exact action:
- Review the roles of Ask, Plan, and Agent in the Chat view.
- Match each mode to a realistic BI, DS, or DE scenario.

What success looks like:
- The learner can choose Ask for explanation, Plan for structure, and Agent for well-scoped implementation.

Common failure mode and fix:
- Failure: The learner treats all modes as interchangeable.
- Fix: Use one concrete example per mode and explain the risk difference.

### Step 2. Spot weak prompts
Goal of the step:
- Learn to identify prompts that are too broad or underspecified.

Exact action:
- Compare prompts such as `make this better` with more specific alternatives.
- Identify what is missing: scope, audience, output, or validation.

What success looks like:
- The learner can name at least three missing prompt elements.

Common failure mode and fix:
- Failure: The learner focuses only on wording style.
- Fix: Check for missing constraints and expected results, not just tone.

### Step 3. Add prompt structure
Goal of the step:
- Turn a broad request into a safe, reviewable prompt.

Exact action:
- Add these elements to a sample request:
  - goal
  - scope
  - audience
  - expected output
  - validation method

What success looks like:
- The rewritten prompt is specific enough that another person could review the result.

Common failure mode and fix:
- Failure: The prompt still leaves too many choices to the model.
- Fix: Constrain the number of files, type of output, and review expectations.

### Step 4. Practice Ask prompts
Goal of the step:
- Use Ask for low-risk orientation and understanding.

Exact action:
- Run Ask prompts such as:
  - `Explain what this SQL file does and summarize the business purpose in plain language.`
  - `Review this notebook and list the major steps without changing anything.`
  - `Describe the likely purpose of this data pipeline README.`

What success looks like:
- The learner gets a useful answer without triggering risky changes.

Common failure mode and fix:
- Failure: The learner asks Ask mode to perform implementation.
- Fix: Move implementation requests to Plan or Agent only after understanding the task.

### Step 5. Practice Plan prompts
Goal of the step:
- Use Plan to structure work before any edits happen.

Exact action:
- Run Plan prompts such as:
  - `Create a step-by-step plan to improve this Power BI data dictionary README for new analysts.`
  - `Create a plan to add validation notes to this notebook workflow for reproducibility.`
  - `Create a plan to document deployment checks for this data pipeline.`

What success looks like:
- The learner receives a sequence that can be reviewed before execution.

Common failure mode and fix:
- Failure: The plan is too generic to evaluate.
- Fix: Ask for phases, deliverables, and validation checks in the plan.

### Step 6. Practice Agent prompts safely
Goal of the step:
- Use Agent only after the task is bounded and reviewable.

Exact action:
- Run Agent prompts such as:
  - `Create a draft validation checklist for this BI lab README. Do not edit more than one file.`
  - `Add a beginner-friendly prerequisites section to this notebook lab README. Keep the existing structure.`
  - `Update this pipeline lab to include one troubleshooting section and one validation checklist.`

What success looks like:
- The learner gets a focused change set they can review easily.

Common failure mode and fix:
- Failure: The agent changes more than expected.
- Fix: Reduce the prompt scope and specify file limits before rerunning.

## Hands-On Lab
Scenario context:
- You are helping a BI, DS, or DE team write better first prompts so they can use Copilot without over-delegating.

Learner goal:
- Compare Ask, Plan, and Agent prompts and produce one safe prompt for each mode.

Tasks:
1. Find one file in the workspace that is safe to inspect.
2. Write one Ask prompt for explanation only.
3. Write one Plan prompt for a structured improvement.
4. Write one Agent prompt with clear scope and validation.
5. Run the prompts and compare the results.
6. Record which prompt felt safest and why.

Suggested learner prompts:
- `Explain this README in plain language for a first-time BI analyst.`
- `Create a plan to improve this notebook README for reproducibility and onboarding.`
- `Add a short validation checklist to this data pipeline lab README. Do not change any other file.`
- `Before making changes, ask clarifying questions if the file purpose is ambiguous.`

Expected observable output:
- One Ask response
- One Plan response
- One constrained Agent result or draft
- A short note explaining why the Agent prompt was safe enough to run

## Validation Checklist
- The learner can explain the difference between Ask, Plan, and Agent.
- The learner can identify at least three elements of a strong first prompt.
- The learner can rewrite a vague request into a safer one.
- The learner can create one low-risk prompt for each mode.
- The learner can describe one validation check before accepting Agent output.

## Reflection Tasks
- Which mode felt most appropriate for your first task, and why?
- What changed most when you added constraints to the prompt?
- What is one sign that a prompt is too vague for Agent mode?
- Which kind of work in your team should usually start with Plan instead of Agent?

## References
- VS Code chat overview: https://code.visualstudio.com/docs/copilot/chat/copilot-chat
- VS Code prompt engineering guide: https://code.visualstudio.com/docs/copilot/guides/prompt-engineering-guide
- VS Code AI best practices: https://code.visualstudio.com/docs/copilot/best-practices
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
