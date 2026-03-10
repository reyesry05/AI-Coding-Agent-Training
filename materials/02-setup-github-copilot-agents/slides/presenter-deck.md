# Presenter Deck: Set Up GitHub Copilot Agents In VS Code

## Slide 1. Title

On-screen content:

- Set Up GitHub Copilot Agents In VS Code
- Beginner setup module
- Technical staff familiar with VS Code, new to agents

Presenter notes:

- Open by clarifying that this session is about readiness and safe first use.
- The goal is not advanced prompting. The goal is to make sure learners can get into the product, confirm that agents are available, and use them without guessing.
- Assume learners already know the module 01 baseline: Ask, Edit, Plan, Agent, then review. This module turns that behavior model into actual product readiness and prepares them for module 03 prompt work.

## Slide 2. Learning Objectives

On-screen content:

- Explain the prerequisites for GitHub Copilot agents
- Verify Copilot, Chat, and agent availability
- Open a suitable workspace for agent context
- Start a first safe session using Ask, Edit, Plan, then Agent
- Review output before accepting it

Presenter notes:

- Tell learners that if they leave with only one behavior change, it should be this: start with lower-risk interaction modes and verify before accepting.

## Slide 3. What Learners Need Before Starting

On-screen content:

- Windows with Visual Studio Code installed
- GitHub account
- GitHub Copilot entitlement or Copilot Free
- GitHub Copilot and GitHub Copilot Chat extensions enabled
- Small practice workspace open in VS Code
- GitHub or Azure DevOps repository access when practicing in a team workflow

Presenter notes:

- Clarify the difference between having a GitHub account and having Copilot access.
- Mention that Copilot Free can be enough for first exposure, depending on current plan limits.
- Tie the examples back to BI, data science, and data engineering teams so the setup feels relevant.

## Slide 4. Common Setup Blockers

On-screen content:

- Wrong GitHub account signed in
- Missing or disabled extensions
- Agent picker not visible
- Organization policy disabling agent features
- Empty or irrelevant workspace causing generic answers

Presenter notes:

- Normalize these blockers. Beginners often assume they are doing something wrong when the real issue is licensing, policy, or missing extensions.

## Slide 5. Step 1: Confirm Account And Product Access

On-screen content:

- Sign in to GitHub in VS Code
- Check the Copilot status bar entry
- Confirm the correct account has Copilot access

Success check:

- Copilot shows as available instead of prompting for sign-in or purchase

Presenter notes:

- Demonstrate where learners can confirm identity inside VS Code.
- If your organization uses multiple GitHub identities, stress that this is the first thing to verify.

## Slide 6. Step 2: Verify Extensions

On-screen content:

- Open Extensions
- Confirm GitHub Copilot is installed and enabled
- Confirm GitHub Copilot Chat is installed and enabled
- Reload VS Code if needed

Success check:

- Chat entry point is visible

Presenter notes:

- Explain that chat availability and agent availability are related but not identical.
- If Chat exists but Agent does not, the environment still needs more investigation.

## Slide 7. Step 3: Verify Agents Are Available

On-screen content:

- Open Chat with Ctrl+Alt+I
- Look for Ask, Edit, Plan, and Agent
- If missing, update VS Code and extensions first

Recovery path:

- If still missing, check organization policy or tenant restrictions

Presenter notes:

- Show the agent picker if possible.
- State clearly that agent features can be admin-controlled.

## Slide 8. Step 4: Open A Good Workspace

On-screen content:

- Use a small, relevant practice folder
- Prefer a safe sample from GitHub or Azure DevOps if the team already works that way
- Keep only related files open
- If needed, create a simple README or starter file for context

Key teaching point:

- Better context improves agent output quality

Presenter notes:

- Explain why an empty workspace leads to vague answers.
- Connect this to the broader habit of supplying explicit context.

## Slide 9. Safe Beginner Progression

On-screen content:

- Ask for orientation or explanation
- Plan for structure and task breakdown
- Agent only after the goal and success criteria are clear

Presenter notes:

- This sequence prevents beginners from over-delegating too early.
- Reinforce that Agent is useful, but not the default first move.

## Slide 10. Demo Prompt Sequence

On-screen content:

- Ask: Explain what files are in this workspace and what kind of project it appears to be.
- Plan: Create a short plan for adding a beginner-friendly setup guide for GitHub Copilot agents to this workspace.
- Agent: Create a draft README section that lists the prerequisites for using GitHub Copilot agents in VS Code. Keep it beginner-friendly and Windows-first.

Presenter notes:

- Read each prompt slowly and point out why it is safe.
- Show that the prompts specify scope, tone, and expected output.

## Slide 11. Review Before Accepting

On-screen content:

- Read diffs
- Check proposed commands before running them
- Compare output to the original request
- Verify at least one visible detail before accepting

Minimum beginner rule:

- Never accept a change you cannot explain

Presenter notes:

- This is the core guardrail of the entire module.
- Give one example of a plausible-looking but incomplete result.

## Slide 12. Hands-On Lab

On-screen content:

- Sign in to the correct GitHub account
- Verify extensions
- Confirm Ask, Edit, Plan, and Agent availability
- Open a small practice workspace
- Run one Ask, one Plan, and one Agent prompt
- Record one thing you verified before accepting output

Presenter notes:

- Keep the lab observable.
- Encourage learners to capture screenshots or short notes of each success check.

## Slide 13. Validation Checklist

On-screen content:

- Learner can list prerequisites
- Learner can explain the difference between Chat and agent access
- Learner can identify Ask, Edit, Plan, and Agent or explain why unavailable
- Learner can write one specific low-risk starter prompt
- Learner can describe one verification step they performed

Presenter notes:

- Use this slide as the completion check for the session.
- If a learner cannot demonstrate one of these items, stop and resolve that gap before moving on.

## Slide 14. Reflection

On-screen content:

- What setup step caused the most friction?
- Why start with Ask or Plan before Agent?
- What makes a workspace useful to an agent?
- What review rule should every beginner follow?

Presenter notes:

- Use this as a debrief rather than a quiz.
- The reflection is intended to strengthen habits, not test memorization.

## Slide 15. References

On-screen content:

- VS Code Copilot overview
- VS Code chat overview
- VS Code agents tutorial
- VS Code AI best practices
- GitHub Copilot best practices
- Workspace reference: references/copilot-agent-beginner-best-practices.md

Presenter notes:

- Encourage learners to rely on first-party documentation when product behavior changes.
- Mention that internal training material should be updated when official UI or policies change.
