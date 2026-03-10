---
name: "Refine Beginner Prompt"
description: "Rewrite a vague Copilot prompt into a specific, bounded prompt for a beginner"
argument-hint: "Paste the rough prompt and optional file scope"
agent: "ask"
---

Rewrite the user's rough prompt so it is safer and easier for a beginner to review.

Requirements:

- preserve the original goal,
- make the scope explicit,
- include constraints,
- name the expected output,
- prefer reviewable changes over broad edits.

Return:

1. an improved prompt,
2. a short explanation of what changed,
3. one optional follow-up prompt to validate the result.
