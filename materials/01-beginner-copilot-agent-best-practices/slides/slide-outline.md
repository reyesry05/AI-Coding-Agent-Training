# Slide Outline

## 1. Module Title

- Beginner Best Practices For GitHub Copilot Agents In VS Code
- Audience: BI, DS, and DE practitioners
- Outcome: safer, more effective beginner workflows

## 2. Why This Module Matters

- Many beginners start with prompts that are too broad.
- High-autonomy agent use without review creates avoidable errors.
- Small workflow changes improve quality and trust quickly.

## 3. What Copilot Modes Do

- Ask: explain, orient, answer questions
- Edit: targeted inline changes with diff review
- Plan: create a step-by-step approach before changes
- Agent: perform coordinated work with tools and edits

## 4. Choose The Right Mode

- Start with Ask for understanding
- Use Edit for targeted file changes
- Move to Plan for multi-step work
- Use Agent for clear, reviewable implementation tasks

## 5. Prompt Quality For Beginners

- State the goal
- Bound the scope
- Add constraints
- Name the expected output

## 6. Context Makes The Difference

- Use active file and selection
- Add `#file`, `#folder`, `#codebase`
- Use `#fetch` for current official docs

## 7. Demo: Improve A Weak Prompt

- Start from a vague request
- Refine it into a scoped, verifiable prompt
- Show one BI, DS, or DE example

## 8. Review Before Accepting

- Read diffs
- Check file placement
- Validate commands and claims
- Reject changes you cannot explain

## 9. BI Before And After -- SQL KPI View

- Before: basic `SELECT SUM(revenue) AS margin` view
- After: AI renames to `gross_margin`, adds `gross_margin_pct`
- Review: did the AI change the definition or just add clarity?
- Decision: Keep, Revise, or Reject?

## 10. DS Before And After -- Notebook Cell

- Before: churn-model cell with no seed or version info
- After: AI adds `random_state`, data version comment, shape check
- Review: are the seed and data version correct?
- Decision: Keep, Revise, or Reject?

## 11. DE Before And After -- Pipeline Task

- Before: bare `PythonOperator` with no retries
- After: AI adds retry logic, upstream dependency comment, escalation path
- Review: are retry count, delay, and escalation correct for your SLA?
- Decision: Keep, Revise, or Reject?

## 12. Reuse Instructions And Prompts

- Use workspace instructions for shared defaults
- Use prompt files for repeatable beginner tasks
- Keep rules concise and non-obvious

## 13. Common Beginner Mistakes

- Too much in one prompt
- Wrong mode for the task
- Missing context
- No review step
- Mixing unrelated tasks in one session

## 14. Validation And Reflection

- Can learners choose the right mode?
- Can they improve a prompt?
- Can they explain what they still need to verify?

## 15. References

- Point to the shared reference document
- Highlight the official GitHub and VS Code sources
