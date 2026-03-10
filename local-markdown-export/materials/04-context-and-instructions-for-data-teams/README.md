# Context And Instructions For Data Teams

## Learning Objectives
By the end of this module, learners should be able to:
- explain why context quality strongly affects Copilot output
- choose when to use active file context, `#file`, `#codebase`, or web references
- identify which team preferences belong in workspace instructions
- avoid context overload in long chat sessions
- create repeatable behavior for BI, DS, and DE workflows

## Prerequisites And Setup
Audience:
- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:
- Modules 01 through 03 completed or equivalent knowledge
- One small workspace containing a README, notebook, SQL file, script, or pipeline file
- GitHub Copilot Chat available in VS Code

Success looks like:
- The learner can improve output by adding better context.
- The learner can name examples of useful permanent instructions.
- The learner can explain when to start a fresh chat.

Common failure mode and fix:
- Failure: The learner assumes Copilot already has all needed context.
- Fix: Explicitly attach files, reference the codebase, and remove irrelevant conversation history.

## Walkthrough

### Step 1. Understand context sources
Goal of the step:
- Learn the main types of context available in VS Code chat.

Exact action:
- Review implicit context from the active file and selection.
- Review explicit context from `#file`, `#folder`, `#codebase`, and `#fetch`.

What success looks like:
- The learner can explain the difference between implicit and explicit context.

Common failure mode and fix:
- Failure: The learner assumes the active file is enough.
- Fix: Add explicit references when the task spans multiple files or concepts.

### Step 2. Choose the right context for the task
Goal of the step:
- Match the context method to the problem.

Exact action:
- For a SQL explanation, use `#file`.
- For repository-wide discovery, use `#codebase`.
- For current product guidance, use `#fetch` against official docs.

What success looks like:
- The learner can justify why a particular context source was used.

Common failure mode and fix:
- Failure: The learner uses `#codebase` for a tiny single-file question.
- Fix: Start with the narrowest context that can answer the question.

### Step 3. Avoid context pollution
Goal of the step:
- Prevent irrelevant history from lowering response quality.

Exact action:
- Start a new chat for unrelated tasks.
- Compact or reset sessions when they accumulate too much unrelated history.

What success looks like:
- The learner can explain why a fresh session may improve results.

Common failure mode and fix:
- Failure: The learner keeps multiple unrelated topics in one conversation.
- Fix: Split topics into separate chats with clean context.

### Step 4. Decide what belongs in instructions
Goal of the step:
- Identify team preferences that should be remembered across tasks.

Exact action:
- Review examples such as:
  - Windows-first command expectations
  - BI/DS/DE audience assumptions
  - preferred module structure
  - validation checklist requirements
  - repo assumptions for GitHub or Azure DevOps

What success looks like:
- The learner can tell the difference between one-time prompt details and recurring instructions.

Common failure mode and fix:
- Failure: The learner repeats the same rules in every chat.
- Fix: Move repeated guidance into instructions.

### Step 5. Apply context in realistic data scenarios
Goal of the step:
- Practice adding the right context for data-team work.

Exact action:
- BI example: ask for a plain-language explanation of a reporting README using `#file`.
- DS example: attach a notebook and ask for a reproducibility checklist.
- DE example: use `#codebase` to find where pipeline validation belongs.

What success looks like:
- The learner sees more targeted and less generic output.

Common failure mode and fix:
- Failure: The learner attaches too much irrelevant context.
- Fix: Limit context to the files, symbols, or docs directly needed for the task.

## Hands-On Lab
Scenario context:
- Your team wants more consistent Copilot results for documentation, notebooks, SQL, and pipeline work.

Learner goal:
- Improve one response by adding better context and identify one instruction that should be stored permanently.

Tasks:
1. Select one safe file or small set of files.
2. Ask a question without explicit context.
3. Ask the same question again with `#file` or `#codebase`.
4. Compare the outputs.
5. Identify one team rule that should go into instructions.
6. Record what changed when context was improved.

Suggested learner prompts:
- `Explain this file for a new data team member.`
- `Explain #file for a new BI analyst.`
- `Using #codebase, identify where a data quality checklist should live.`
- `Using #fetch https://code.visualstudio.com/docs/copilot/best-practices, summarize the context advice most relevant to data teams.`

Expected observable output:
- Two versions of an answer: one generic and one improved by context
- A short note describing the improvement
- One candidate instruction that should be reused across future tasks

## Validation Checklist
- The learner can explain the difference between implicit and explicit context.
- The learner can choose between `#file` and `#codebase` for a realistic task.
- The learner can explain why unrelated sessions should be separated.
- The learner can name one recurring team preference that belongs in instructions.
- The learner can show how better context improved output quality.

## Reflection Tasks
- What type of context improved your result the most?
- When is `#codebase` helpful, and when is it excessive?
- What rule does your team repeat often enough to move into instructions?
- What would make you start a fresh chat instead of continuing the old one?

## References
- VS Code chat context: https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context
- VS Code custom instructions: https://code.visualstudio.com/docs/copilot/customization/custom-instructions
- VS Code AI best practices: https://code.visualstudio.com/docs/copilot/best-practices
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
