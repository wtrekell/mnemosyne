# CLAUDE.md

## Session start

At the start of each session, read `brains/notes.md`. If its "To do (yours)" section has open tasks, remind the user to resolve them in the solinari repository before other work, and list the open ones. If none are open, say nothing.

## The researcher agent

- Keep `.claude/agents/researcher.md` generic: no scoring rules (they vary by research type), no file references, nothing specific to this repo. Type-specific detail goes in skills.
- Do only the actions the owner names for `brains/research-brain` and `hesiod`; don't act on their contents.
