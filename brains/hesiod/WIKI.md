# Wiki: <name>

<!-- Written at install with the human (CLAUDE.md step 3). The owning agent reads this before capturing and follows it; it proposes changes but doesn't make them. Replace every <placeholder>. Keep each bullet to one checkable condition. -->

## Purpose
<One or two sentences: what this wiki is for and what questions it should be able to answer.>

## In scope
- <topic, system, or question area>
- <...>

## Out of scope
- <near-miss topics that belong elsewhere, and where they belong if known>

## Capture when (all must hold)
- The material is about something listed under In scope.
- <it comes from an allowed source, e.g. "files under src/ or docs/ in the host repo", "URLs the human provides", "official vendor documentation">
- <it holds something not already in the wiki: a decision, a fact, a rationale, a reference>
- <it is likely to be needed again, not a one-off detail>

## Never capture
- Secrets, credentials, tokens, keys, or personal data.
- Anything already captured (check with `wiki.py captured`).
- <generated files, logs, build output, vendored code>
- <other exclusions>

## Examples
- Capture: <a concrete item that qualifies> — <which conditions it meets>
- Skip: <a concrete near-miss> — <which condition fails>

## When unsure
Don't capture. Mention the item and the condition in doubt to the human, and record it in `wiki/log.md` under a `query` entry if no human is present.
