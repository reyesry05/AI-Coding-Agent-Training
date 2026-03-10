# Beginner Best Practices For GitHub Copilot Agents

This reference is for beginner-friendly training content about GitHub Copilot agents in Visual Studio Code.
It summarizes practical guidance from official Microsoft and GitHub documentation and is intended to help authors design safe, realistic, and repeatable learning experiences.

## What Beginners Should Learn First
Beginners should first understand that Copilot is an assistant, not an authority.
They should learn how to:
- choose the right Copilot interaction mode for the task
- write clear, constrained prompts
- provide the right context
- review every change before accepting it
- verify output with observable checks
- protect secrets and sensitive data

## Recommended Beginner Workflow
Use this progression when teaching new users:

1. Start with Ask mode for understanding and exploration.
2. Use Plan mode before larger or ambiguous tasks.
3. Use Agent mode only after the goal, constraints, and success criteria are clear.
4. Keep early tasks small and reversible.
5. Review diffs and checkpoints before accepting changes.
6. Validate results with commands, screenshots, expected files, or checklists.
7. Start a new chat when switching to a different task to avoid irrelevant context.

## Best Practices

### 1. Pick the right tool for the task
Beginners should not start with full autonomy for every task.
Use:
- Inline suggestions for quick completions
- Ask for explanation, brainstorming, and low-risk questions
- Inline chat for targeted edits in the current file
- Plan for multi-step work
- Agent for well-scoped tasks that may span files or tools

### 2. Prefer small, explicit prompts
Good beginner prompts are specific about:
- the goal
- the files or content in scope
- constraints
- expected output
- how success will be checked

Example:

```text
Create a beginner lab outline for GitHub Copilot agents in VS Code.
Include learning objectives, prerequisites, a 20-minute walkthrough, one hands-on exercise, a validation checklist, and two reflection questions.
Do not assume coding experience beyond basic VS Code use.
```

### 3. Give relevant context
Responses improve when learners provide context intentionally.
Recommend that beginners:
- open relevant files only
- reference files, folders, or symbols explicitly
- attach screenshots when the task is visual
- include sample input, output, or acceptance criteria
- avoid mixing unrelated tasks in one session

### 4. Ask for clarifying questions
When a task is ambiguous, beginners should explicitly tell the agent to ask questions before acting.
This reduces guessing and produces better first-pass results.

Example:

```text
Before making changes, ask clarifying questions if any requirement is ambiguous.
```

### 5. Review before accepting
Beginners must be taught to inspect generated edits, not just trust them.
They should:
- read the proposed changes
- check whether the output matches the request
- watch for invented facts, missing steps, or wrong assumptions
- use checkpoints or undo options if the session drifts off course

### 6. Verify outcomes, not just wording
A response that sounds correct can still be wrong.
For beginner training, every task should include a visible verification method such as:
- a file created in the expected location
- a checklist item completed
- a command with known output
- a screenshot or preview result
- a documented explanation that matches the prompt exactly

### 7. Use safe autonomy settings
For beginners, start with lower-risk workflows:
- prefer local sessions for immediate feedback
- prefer default approvals rather than full auto-approval
- use background or cloud agents later, once review habits are established

### 8. Protect data and credentials
Do not paste secrets, tokens, passwords, private keys, or sensitive business data into prompts.
Teach learners to redact sensitive values and use placeholders.

### 9. Keep expectations realistic
Copilot is strong at drafting, explaining, restructuring, and accelerating repetitive work.
It can still be wrong, incomplete, outdated, or overly confident.
Training should repeatedly reinforce human judgment and verification.

## Suggested Teaching Pattern
For beginner modules, prefer this sequence:
- explain the tool choice
- provide a model prompt
- show what good output looks like
- show how to review the output
- show how to validate the result
- include one common failure mode and how to recover

## Anti-Patterns To Avoid In Beginner Training
Avoid teaching beginners to:
- start with vague prompts like "make this better"
- let the agent act on broad tasks without success criteria
- keep piling unrelated requests into one long chat
- accept changes without review
- paste sensitive information into prompts
- use maximum autonomy before they understand approvals and rollback options

## Official References
These are the primary first-party sources used for this summary.

### VS Code Documentation
- GitHub Copilot in VS Code: https://code.visualstudio.com/docs/copilot/overview
- Chat overview: https://code.visualstudio.com/docs/copilot/chat/copilot-chat
- Best practices for using AI in VS Code: https://code.visualstudio.com/docs/copilot/best-practices
- Prompt engineering in VS Code: https://code.visualstudio.com/docs/copilot/guides/prompt-engineering-guide
- Tutorial: Work with agents in VS Code: https://code.visualstudio.com/docs/copilot/agents/agents-tutorial
- Review AI-generated edits: https://code.visualstudio.com/docs/copilot/chat/review-code-edits
- Chat checkpoints: https://code.visualstudio.com/docs/copilot/chat/chat-checkpoints
- Manage chat sessions: https://code.visualstudio.com/docs/copilot/chat/chat-sessions
- Custom instructions: https://code.visualstudio.com/docs/copilot/customization/custom-instructions
- Custom agents: https://code.visualstudio.com/docs/copilot/customization/custom-agents
- Agent tools and approvals: https://code.visualstudio.com/docs/copilot/agents/agent-tools
- GitHub Copilot security in VS Code: https://code.visualstudio.com/docs/copilot/security

### GitHub Documentation
- Best practices for using GitHub Copilot: https://docs.github.com/en/copilot/get-started/best-practices
- Prompt engineering for Copilot Chat: https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat
- Changing the AI model for Copilot Chat: https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat?tool=vscode
- Copilot Chat cookbook: https://docs.github.com/en/copilot/copilot-chat-cookbook

## Author Guidance For This Workspace
When creating beginner-facing materials in this repository:
- default to Ask, Plan, then Agent as the learning sequence
- require explicit validation steps in every lab
- favor short prompts with visible constraints
- include recovery guidance when the agent produces a weak result
- link back to the official references above when deeper explanation is needed
