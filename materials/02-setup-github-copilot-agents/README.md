# Set Up GitHub Copilot Agents In VS Code

## Learning Objectives

By the end of this module, learners should be able to:

- explain the prerequisites for using GitHub Copilot agents in Visual Studio Code
- verify whether GitHub Copilot, Copilot Chat, and agent features are available in their environment
- configure a VS Code workspace so agent sessions have useful context
- start a first local agent session and review the result safely
- identify the most common setup failures and recover from them

## Prerequisites And Setup

Audience:

- Initial target audience: business intelligence teams, data science teams, and data engineering teams
- Technical staff familiar with VS Code but new to GitHub Copilot agents

Target duration:

- 15 to 20 minutes

Module type:

- Coding-focused setup module

Required tools and access:

- Visual Studio Code installed on Windows
- GitHub account
- GitHub Copilot entitlement or Copilot Free access
- GitHub Copilot and GitHub Copilot Chat enabled in VS Code
- A small local workspace or project folder open in VS Code
- Access to a representative GitHub repository or Azure DevOps repository is helpful if learners want to practice in a realistic team context

Nice to have:

- Git installed and signed in, especially if learners will later use background or cloud agent workflows
- Permission from the organization administrator if agent features are policy-controlled

Success looks like:

- The learner can open Chat in VS Code.
- The learner can see the agent picker in Chat.
- The learner can start a local agent session.
- The learner can review generated changes before accepting them.

Common failure mode and fix:

- Failure: The learner has Copilot Chat but does not see agents.
- Fix: Confirm the account has Copilot access, confirm the latest VS Code and extensions are installed, and check whether agents are disabled by organization policy.

## Walkthrough

### Step 1. Confirm account and product access

Goal of the step:

- Make sure the learner actually has access to GitHub Copilot features before troubleshooting VS Code.

Exact action:

- Sign in to GitHub in VS Code.
- Hover over the Copilot status bar icon and select the setup option if prompted.
- Confirm the account is the expected GitHub identity.

What success looks like:

- VS Code shows the learner as signed in.
- Copilot features appear enabled instead of showing a sign-in or purchase prompt.

Common failure mode and fix:

- Failure: The learner is signed into the wrong GitHub account.
- Fix: Sign out and sign back in with the account that has Copilot access.

### Step 2. Install or verify the required VS Code extensions

Goal of the step:

- Ensure the minimum extension set required for Copilot chat and agents is available.

Exact action:

- Open Extensions in VS Code.
- Verify that GitHub Copilot and GitHub Copilot Chat are installed and enabled.
- If they are missing, install them from the VS Code Marketplace.

What success looks like:

- Both extensions show as installed and enabled.
- The Chat entry point is visible in VS Code.

Common failure mode and fix:

- Failure: The extensions are installed but disabled for the current workspace.
- Fix: Re-enable the extensions and reload the window.

### Step 3. Verify agent availability

Goal of the step:

- Confirm that the environment supports agent sessions, not just basic chat.

Exact action:

- Open Chat with `Ctrl+Alt+I`.
- Check whether the Chat view shows the agent picker.
- Look for built-in options such as Ask, Edit, Plan, and Agent.

What success looks like:

- The learner can switch between Ask, Edit, Plan, and Agent in the Chat view.

Common failure mode and fix:

- Failure: The agent picker is missing.
- Fix: Update VS Code and extensions first. If the issue remains, check whether agent functionality is disabled by organizational policy.

### Step 4. Open a suitable workspace

Goal of the step:

- Give the agent enough local context to produce relevant results.

Exact action:

- Open a small practice folder or starter project in VS Code. If your team uses GitHub or Azure DevOps, open a safe working copy from that repository system when possible.
- Keep only relevant files open.
- If the folder is empty, create a simple `README.md` or small sample file so the agent has something concrete to work with.

What success looks like:

- The learner has a focused workspace open and can describe what the folder is for.
- The agent can refer to workspace files instead of answering in generic terms.

Common failure mode and fix:

- Failure: The learner starts in an empty or unrelated workspace and gets generic output.
- Fix: Open a small, task-relevant folder and reference files explicitly with `#file` or `#codebase`.

### Step 5. Start a first safe session

Goal of the step:

- Let the learner practice agent setup without taking on a large or risky task.

Exact action:

- In Chat, start with Ask and submit a low-risk prompt such as:

```text
Explain what files are in this workspace and what kind of project it appears to be.
```

- Next, switch to Plan and ask:

```text
Create a short plan for adding a beginner-friendly setup guide for GitHub Copilot agents to this workspace.
```

- Only after reviewing the plan, switch to Agent and ask:

```text
Create a draft README section that lists the prerequisites for using GitHub Copilot agents in VS Code. Keep it beginner-friendly and Windows-first.
```

What success looks like:

- The learner experiences Ask, Edit, Plan, and Agent in a controlled sequence.
- The learner can explain why Agent was not the first step.

Common failure mode and fix:

- Failure: The learner starts with a vague high-autonomy prompt and gets low-quality output.
- Fix: Reduce the scope, specify the desired output, and add validation criteria before rerunning the request.

### Step 6. Review before accepting

Goal of the step:

- Establish the correct beginner habit: inspect output before trusting it.

Exact action:

- Review diffs in the editor.
- Check any proposed commands before running them.
- Compare the generated result with the original request.

What success looks like:

- The learner can point to at least one thing they verified before accepting a result.

Common failure mode and fix:

- Failure: The learner accepts output because it sounds correct.
- Fix: Require one visible check before accepting any change, such as confirming file location, wording, or command accuracy.

## Hands-On Lab

Scenario context:

- You are preparing a workspace for a beginner pilot group from a BI, data science, or data engineering team. The team may keep its work in GitHub or Azure DevOps.

Learner goal:

- Verify prerequisites, confirm agent availability, and run one safe first session.

Tasks:

1. Sign in to the correct GitHub account in VS Code.
2. Verify that GitHub Copilot and GitHub Copilot Chat are installed and enabled.
3. Open Chat and confirm whether Ask, Edit, Plan, and Agent are available.
4. Open a small practice workspace.
5. Run one Ask prompt, one Plan prompt, and one Agent prompt.
6. Review the output and record one thing you verified before accepting it.

Suggested learner prompts:

- `Explain what prerequisites I need to use GitHub Copilot agents in VS Code on Windows.`
- `Create a short setup checklist for a beginner using GitHub Copilot agents for the first time.`
- `Using #codebase, identify whether this workspace has enough context for a useful agent session.`
- `Create a safe first-session checklist for a BI, DS, or DE team that stores work in GitHub or Azure DevOps.`
- `Before making changes, ask clarifying questions if anything about the setup task is ambiguous.`

Expected observable output:

- Chat is available in VS Code.
- The learner can identify whether the agent picker is present.
- A short setup checklist or prerequisite summary is generated.
- The learner can show one reviewed change, plan, or explanation from the session.

## Validation Checklist

- The learner can list the minimum prerequisites for GitHub Copilot agents.
- The learner can explain the difference between having Copilot Chat and having agent access.
- The learner can identify Ask, Edit, Plan, and Agent in VS Code, or explain why agents are unavailable in their environment.
- The learner can open a relevant workspace before starting an agent task.
- The learner can write one specific, low-risk starter prompt.
- The learner can describe one verification step they performed before accepting output.

## Reflection Tasks

- What was the most common point of failure in your setup, and how did you resolve it?
- Why is it useful to start with Ask or Plan before Agent?
- What makes a workspace more useful to an agent?
- What is one rule you would give beginners about reviewing AI output?

## References

- GitHub Copilot in VS Code: <https://code.visualstudio.com/docs/copilot/overview>
- Chat overview: <https://code.visualstudio.com/docs/copilot/chat/copilot-chat>
- Tutorial: Work with agents in VS Code: <https://code.visualstudio.com/docs/copilot/agents/agents-tutorial>
- Best practices for using AI in VS Code: <https://code.visualstudio.com/docs/copilot/best-practices>
- Best practices for using GitHub Copilot: <https://docs.github.com/en/copilot/get-started/best-practices>
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
