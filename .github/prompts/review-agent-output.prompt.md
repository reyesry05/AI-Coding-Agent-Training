---
name: "Review Agent Output"
description: "Help a beginner review Copilot output before accepting it"
argument-hint: "Describe the answer, diff, or command you want reviewed"
agent: "ask"
---

Help the user review GitHub Copilot output before accepting it.

Provide:

- a quick summary of what the output appears to do,
- a checklist of what to verify,
- one sign that the output may be off-target,
- one follow-up prompt the user can ask to tighten or validate the result.

Assume the user is a beginner and needs plain, direct guidance.
