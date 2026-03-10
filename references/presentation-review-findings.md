# Presentation Review Findings

This review applies the presenter-oriented rubric captured in [references/awesome-copilot-agents-for-presentation-improvement.md](./awesome-copilot-agents-for-presentation-improvement.md).

Scope:
- reviewed `materials/**/slides/presenter-deck.md`
- reviewed `materials/**/slides/slide-outline.md`
- excluded `local-markdown-export/**`

## Findings

### High

#### 1. Cross-module handoff is mostly missing after module 01
Why it matters:
- Learners and presenters are not consistently told what prior context is assumed or what module follows next.
- This increases presenter improvisation and weakens the training sequence.

Evidence:
- `materials/01-beginner-copilot-agent-best-practices/slides/presenter-deck.md:122`
- `materials/03-first-safe-prompts-ask-plan-agent/slides/presenter-deck.md:21`
- `materials/04-context-and-instructions-for-data-teams/slides/presenter-deck.md:21`
- `materials/05-notebooks-sql-and-pipelines-with-copilot/slides/presenter-deck.md:21`
- `materials/06-review-and-verify-ai-output-for-data-work/slides/presenter-deck.md:21`
- `materials/07-repo-workflows-github-and-azure-devops/slides/presenter-deck.md:21`

#### 2. BI, DS, and DE examples are still too generic in several decks
Why it matters:
- The current examples often mention broad artifacts instead of realistic practitioner tasks.
- This makes the material safer but less credible and less transferable to real work.

Evidence:
- `materials/01-beginner-copilot-agent-best-practices/slides/presenter-deck.md:73`
- `materials/01-beginner-copilot-agent-best-practices/slides/presenter-deck.md:81`
- `materials/01-beginner-copilot-agent-best-practices/slides/presenter-deck.md:89`
- `materials/03-first-safe-prompts-ask-plan-agent/slides/presenter-deck.md:72`
- `materials/03-first-safe-prompts-ask-plan-agent/slides/presenter-deck.md:81`
- `materials/04-context-and-instructions-for-data-teams/slides/presenter-deck.md:52`
- `materials/07-repo-workflows-github-and-azure-devops/slides/presenter-deck.md:53`

### Medium

#### 3. Module 02 has outline-to-deck drift
Why it matters:
- Useful material was added to the presenter deck but not reflected in the outline.
- That makes review and facilitation planning less reliable.

Evidence:
- `materials/02-setup-github-copilot-agents/slides/slide-outline.md:21`
- `materials/02-setup-github-copilot-agents/slides/slide-outline.md:25`
- `materials/02-setup-github-copilot-agents/slides/slide-outline.md:26`
- `materials/02-setup-github-copilot-agents/slides/presenter-deck.md:31`
- `materials/02-setup-github-copilot-agents/slides/slide-outline.md:66`
- `materials/02-setup-github-copilot-agents/slides/slide-outline.md:67`
- `materials/02-setup-github-copilot-agents/slides/slide-outline.md:68`
- `materials/02-setup-github-copilot-agents/slides/slide-outline.md:69`
- `materials/02-setup-github-copilot-agents/slides/presenter-deck.md:92`

#### 4. Repetition across modules weakens the sense of progression
Why it matters:
- Shared structure is good, but recurring phrasing and repeated slide slots make later modules feel less distinct.
- The curriculum risks reading as repeated templates rather than cumulative skill-building.

Evidence:
- `materials/01-beginner-copilot-agent-best-practices/slides/presenter-deck.md:103`
- `materials/02-setup-github-copilot-agents/slides/presenter-deck.md:131`
- `materials/03-first-safe-prompts-ask-plan-agent/slides/presenter-deck.md:105`
- `materials/01-beginner-copilot-agent-best-practices/slides/slide-outline.md:61`
- `materials/03-first-safe-prompts-ask-plan-agent/slides/slide-outline.md:63`
- `materials/04-context-and-instructions-for-data-teams/slides/slide-outline.md:61`
- `materials/05-notebooks-sql-and-pipelines-with-copilot/slides/slide-outline.md:60`
- `materials/06-review-and-verify-ai-output-for-data-work/slides/slide-outline.md:60`
- `materials/07-repo-workflows-github-and-azure-devops/slides/slide-outline.md:57`

### Low

#### 5. Reference slides are not consistently anchored to workspace-specific materials
Why it matters:
- Presenters may know what the references mean, but learners and other instructors may not.
- Specific reference paths would make facilitation more reliable.

Evidence:
- `materials/07-repo-workflows-github-and-azure-devops/slides/presenter-deck.md:129`
- `materials/07-repo-workflows-github-and-azure-devops/slides/presenter-deck.md:130`
- `materials/07-repo-workflows-github-and-azure-devops/slides/presenter-deck.md:131`
- `materials/05-notebooks-sql-and-pipelines-with-copilot/slides/presenter-deck.md:133`
- `materials/05-notebooks-sql-and-pipelines-with-copilot/slides/presenter-deck.md:134`
- `materials/05-notebooks-sql-and-pipelines-with-copilot/slides/presenter-deck.md:135`

#### 6. Module 01 presenter notes are thinner than later modules
Why it matters:
- The first module sets teaching tone, so sparse presenter notes create early facilitation risk.
- Later modules have better prompts for what to demo and what to verify.

Evidence:
- `materials/01-beginner-copilot-agent-best-practices/slides/presenter-deck.md:19`
- `materials/01-beginner-copilot-agent-best-practices/slides/presenter-deck.md:28`
- `materials/02-setup-github-copilot-agents/slides/presenter-deck.md:58`
- `materials/02-setup-github-copilot-agents/slides/presenter-deck.md:85`
- `materials/02-setup-github-copilot-agents/slides/presenter-deck.md:99`
- `materials/02-setup-github-copilot-agents/slides/presenter-deck.md:158`

## Strong Areas

- `materials/02-setup-github-copilot-agents/slides/presenter-deck.md` and its matching outline are currently the strongest on prerequisite clarity, success checks, and recovery guidance.
- `materials/05-notebooks-sql-and-pipelines-with-copilot/slides/presenter-deck.md` and its matching outline are internally well aligned and do a good job framing data-artifact risk.
- Overall alignment between outlines and presenter decks is generally good in modules 03 through 07.

## Recommended Next Edits

1. Add a short module handoff note near the opening of modules 02 through 07.
2. Replace at least one generic example in each module with a more concrete BI, DS, or DE task.
3. Bring module 02 outline content back into sync with its presenter deck.
4. Vary repeated section phrasing so later modules feel cumulative rather than templated.
5. Strengthen module 01 presenter notes with clearer demo and facilitation cues.