# Wiki: Research Brain

Items marked **(provisional)** were filled in at install without the human's input. The human may update them in the future.

## Purpose
The long-term reference bank of the `researcher` agent: the sourced reports it writes over time, plus research the human chooses to add. It should answer what has already been found on a topic, from which sources, and how far those sources can be trusted.

## In scope
- Reports written by the `researcher` agent (sourced, with labeled sources and a claim map).
- Research material the human adds to `raw/`.
- (provisional) Any research topic the researcher or the human has investigated; no topic is excluded yet.

## Out of scope
- (provisional) Work that is not research: code, project notes, drafts, scratch work. Where these belong is not yet decided.

## Capture when (all must hold)
- The material is about something listed under In scope.
- It is a `researcher` report, or the human supplied it (a file dropped in `raw/`, or a URL or file the human gave).
- It holds something not already in the wiki: a finding, a source judgment, a conflict between sources, or a reference.
- It is likely to be needed again, not a one-off detail.

## Never capture
- Secrets, credentials, tokens, keys, or personal data.
- Anything already captured (check with `wiki.py captured`).
- (provisional) Generated files, logs, search logs, build output, vendored code.
- (provisional) Material the human has not supplied and that is not a `researcher` report.

## Examples
These examples were written by the installer, not supplied by the human. (provisional)
- Capture: a `researcher` report on a topic with a claim map and labeled sources — in scope, from an allowed source, new, reusable.
- Capture: a PDF the human drops into `raw/` for the researcher to draw on — in scope, supplied by the human.
- Skip: a search log from a research run — a log, and the report it belongs to is the item to capture.
- Skip: a report whose copy is already in `raw/` — already captured.

## When unsure
Don't capture. Mention the item and the condition in doubt to the human, and record it in `wiki/log.md` under a `query` entry if no human is present.
