# Slide Outline: Set Up GitHub Copilot Agents In VS Code

## Slide 1. Title
- Set Up GitHub Copilot Agents In VS Code
- Beginner setup module
- Technical staff familiar with VS Code, new to agents

Speaker note:
- Set expectations: this is a setup and safe-first-use module, not an advanced productivity session.

## Slide 2. Learning Objectives
- Explain the prerequisites for GitHub Copilot agents
- Verify Copilot, Chat, and agent availability
- Open a suitable workspace for agent context
- Start a first safe session using Ask, Plan, then Agent
- Review output before accepting it

Speaker note:
- Emphasize that setup and review habits matter more than speed for first-time users.

## Slide 3. What Learners Need Before Starting
- Windows with Visual Studio Code installed
- GitHub account
- GitHub Copilot entitlement or Copilot Free
- GitHub Copilot and GitHub Copilot Chat extensions enabled
- Small practice workspace open in VS Code

Speaker note:
- Clarify that background and cloud workflows may also require Git and GitHub repository access later, but not for the first local session.

## Slide 4. Common Setup Blockers
- Wrong GitHub account signed in
- Missing or disabled extensions
- Agent picker not visible
- Organization policy disabling agent features
- Empty or irrelevant workspace causing generic answers

Speaker note:
- Position these as normal setup issues, not learner mistakes.

## Slide 5. Step 1: Confirm Account And Product Access
- Sign in to GitHub in VS Code
- Check the Copilot status bar entry
- Confirm the correct account has Copilot access

Success check:
- Copilot shows as available instead of prompting for sign-in or purchase

## Slide 6. Step 2: Verify Extensions
- Open Extensions
- Confirm GitHub Copilot is installed and enabled
- Confirm GitHub Copilot Chat is installed and enabled
- Reload VS Code if needed

Success check:
- Chat entry point is visible

## Slide 7. Step 3: Verify Agents Are Available
- Open Chat with `Ctrl+Alt+I`
- Look for Ask, Plan, and Agent
- If missing, update VS Code and extensions first

Recovery path:
- If still missing, check organization policy or tenant restrictions

## Slide 8. Step 4: Open A Good Workspace
- Use a small, relevant practice folder
- Keep only related files open
- If needed, create a simple README or starter file for context

Key teaching point:
- Better context improves agent output quality

## Slide 9. Safe Beginner Progression
- Ask for orientation or explanation
- Plan for structure and task breakdown
- Agent only after the goal and success criteria are clear

Speaker note:
- This is the most important behavioral habit in the module.

## Slide 10. Demo Prompt Sequence
- Ask: `Explain what files are in this workspace and what kind of project it appears to be.`
- Plan: `Create a short plan for adding a beginner-friendly setup guide for GitHub Copilot agents to this workspace.`
- Agent: `Create a draft README section that lists the prerequisites for using GitHub Copilot agents in VS Code. Keep it beginner-friendly and Windows-first.`

Speaker note:
- Show the difference in risk and output across the three modes.

## Slide 11. Review Before Accepting
- Read diffs
- Check proposed commands before running them
- Compare output to the original request
- Verify at least one visible detail before accepting

Minimum beginner rule:
- Never accept a change you cannot explain

## Slide 12. Hands-On Lab
- Sign in to the correct GitHub account
- Verify extensions
- Confirm Ask, Plan, and Agent availability
- Open a small practice workspace
- Run one Ask, one Plan, and one Agent prompt
- Record one thing you verified before accepting output

Speaker note:
- Keep this lab short and observable. The goal is correct setup behavior, not complex output.

## Slide 13. Validation Checklist
- Learner can list prerequisites
- Learner can explain the difference between Chat and agent access
- Learner can identify Ask, Plan, and Agent or explain why unavailable
- Learner can write one specific low-risk starter prompt
- Learner can describe one verification step they performed

## Slide 14. Reflection
- What setup step caused the most friction?
- Why start with Ask or Plan before Agent?
- What makes a workspace useful to an agent?
- What review rule should every beginner follow?

## Slide 15. References
- VS Code Copilot overview
- VS Code chat overview
- VS Code agents tutorial
- VS Code AI best practices
- GitHub Copilot best practices
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`

Speaker note:
- Encourage learners to use first-party docs when product behavior changes.