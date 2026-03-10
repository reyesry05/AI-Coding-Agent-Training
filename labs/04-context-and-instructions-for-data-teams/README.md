# Lab: Context And Instructions For Data Teams

## Scenario Context
Your data team wants more reliable Copilot output in VS Code.
The goal is to compare weak context with strong context and identify one team rule that belongs in instructions.

## Learner Goal
By the end of this lab, you should be able to:
- improve an answer by adding better context
- choose when to use `#file` or `#codebase`
- identify one recurring team preference for instructions
- explain when to start a fresh chat

## Starter State
You begin with:
- a workspace containing at least one file that can be discussed safely
- Copilot Chat available in VS Code
- no assumption that current context is sufficient

## Target State
You finish with:
- one generic answer
- one improved answer using better context
- one instruction candidate for the team
- one short note about session hygiene

## Prerequisites And Setup
Goal of the step:
- Prepare a small and safe context comparison exercise.

Exact actions:
- Open a workspace with at least one README, notebook note, SQL file, or pipeline-related file.
- Open Chat.

What success looks like:
- You can describe the file you will reference and why it is relevant.

Common failure mode and fix:
- Failure: The file does not contain enough information to compare context quality.
- Fix: Choose a file with clear purpose or add a short description file.

## Lab Tasks

### Task 1. Ask Without Explicit Context
Goal of the step:
- Observe how generic a response can be without added context.

Exact action:
- Ask a question about the workspace without attaching a file.

What success looks like:
- You receive a response that is somewhat generic or uncertain.

Common failure mode and fix:
- Failure: The question is so broad that the answer is not useful.
- Fix: Keep the question focused enough to compare later.

### Task 2. Ask Again With Explicit Context
Goal of the step:
- Improve the response by attaching the right file or codebase context.

Exact action:
- Ask the same question using `#file` or `#codebase`.

What success looks like:
- The new answer is more specific and grounded.

Common failure mode and fix:
- Failure: You attach too much irrelevant context.
- Fix: Use the smallest context scope that fits the question.

### Task 3. Compare The Results
Goal of the step:
- Identify what changed because of the improved context.

Exact action:
- Record the main differences in relevance, specificity, and usefulness.

What success looks like:
- You can explain why the second answer is better.

Common failure mode and fix:
- Failure: You compare only sentence quality.
- Fix: Compare whether the answer actually uses workspace information.

### Task 4. Identify One Instruction Candidate
Goal of the step:
- Decide what recurring team guidance should be stored permanently.

Exact action:
- Write down one team rule that is repeated often, such as Windows-first commands or required validation sections.

What success looks like:
- You produce one instruction candidate that would improve repeated tasks.

Common failure mode and fix:
- Failure: The rule is too specific to one file.
- Fix: Choose a rule that applies to many tasks.

### Task 5. Decide Whether To Start A Fresh Chat
Goal of the step:
- Practice session hygiene.

Exact action:
- Decide whether your current task still belongs in the same conversation.

What success looks like:
- You can explain whether the current session still has relevant context.

Common failure mode and fix:
- Failure: You keep unrelated topics in one thread.
- Fix: Start a new chat for a different goal.

## Suggested Learner Prompts
- Explain this file for a new data team member.
- Explain #file for a new BI analyst.
- Using #codebase, identify where a validation checklist belongs.
- Summarize the context advice from #fetch https://code.visualstudio.com/docs/copilot/best-practices for a BI, DS, or DE team.

## Expected Observable Output
- One generic answer
- One improved answer using explicit context
- One written instruction candidate
- One decision about whether to continue or restart the session

## Validation Checklist
- I can improve an answer by adding explicit context.
- I can choose between `#file` and `#codebase`.
- I can name one rule that belongs in instructions.
- I can explain when a fresh chat is better than continuing.

## Reflection Tasks
- What type of context improved your result the most?
- What did the generic answer miss?
- What instruction would save your team the most repeated effort?

## Solution Guidance
A complete solution should show:
- one before-and-after context comparison
- one justified instruction candidate
- one clear explanation of session management
