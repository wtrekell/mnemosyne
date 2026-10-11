# Researcher: Agent Specification

Status: draft. Not yet built.

## 1. Purpose

The researcher finds information, judges how far to trust each source, and writes a report that shows where every part came from.

Its one job is research. What each kind of research covers lives in separate add-ons, so new kinds of research can be added without changing the researcher.

## 2. Parts

Claude Code offers four ways to shape an agent. This design uses three.

| Part | Location | Holds | Why this part |
| --- | --- | --- | --- |
| **Agent** | `.claude/agents/researcher.md` | The rules that apply to all research: source labels, report format, quoting. | An agent runs in its own context and returns only its result, which keeps long research out of the main session. |
| **Add-ons** (skills) | `.claude/skills/research-<kind>/SKILL.md` | What one kind of research covers and what its output adds. | Skills load only when needed. The agent finds and loads the one that fits the request, so adding a skill needs no change to the agent. |
| **Checks** (hooks) | `.claude/settings.json`; script in `scripts/` | A final check on the report that the researcher cannot skip. | Agent and skill instructions are guidance the model reads. Hooks are enforced. Hooks in project settings run in every session, including untrusted folders and non-interactive runs; hooks in an agent file do not. |
| **Rules** | `.claude/rules/` | Not used for now. | Rules load into every session in the project, including subagents such as this one. A rule without `paths` loads at start; a rule with `paths` loads when a matching file is read or edited. The researcher's instructions already live in its agent file, so a rule would repeat them and load them into sessions that don't need them. Revisit with the deferred report format (section 12). |

## 3. Agent definition

| Field | Value | Notes |
| --- | --- | --- |
| `name` | `researcher` | |
| `description` | "Researches a topic and writes a sourced report with labeled sources, a claim map, and suggested next searches. Use for any research request." | Claude reads this to decide when to hand work to the agent, so it states the trigger plainly. |
| `tools` | Read, Grep, Glob, Write, Edit, WebSearch, WebFetch, Skill, mcp__plugin_context7_context7__resolve-library-id, mcp__plugin_context7_context7__query-docs | Only what research needs. No shell access. Write and Edit are for reports and the links between them. The two context7 tools come from the context7 plugin and look up current library documentation. |
| `model` | Inherit from the session | Revisit after first use. |
| `skills` | None preloaded | Preloading puts the full text of every listed skill into context at start. Leaving this empty lets the agent load only the add-on it needs. |
| `hooks` | None | Checks live in project settings so they always run (section 10). |

The body of the agent file holds sections 4 to 9 of this specification, written as instructions.

## 4. Input

A short written prompt naming the subject. The agent picks the add-on that fits. If none fits, it uses topic research.

## 5. Process

1. Pick the add-on and load it.
2. Search, looking for official sources first, then reputable and trusted ones.
3. Label each source (section 6) and note why.
4. Write the findings, building the claim map along the way.
5. Fill in Appendix A and Appendix B.
6. Save the report. Fix anything the checks report.
7. If this report follows up on an earlier report's suggestion, link the two (section 9).
8. Return the report's location and a short summary.

## 6. Source rules

### Citation test

A source passes when **the agent finds five or more other sources that cite it**. The agent lists those citing sources in the source's reason. Talks on a selective stage count toward the five. Sources in a Community setting and sources labeled Ignore do not.

### Labels

A label says how far a source can be trusted on the subject of this report. It is given to the item used (a page, document, talk, or post), not to its publisher as a whole, and it is judged against the report's subject. The same publisher can be Official on one subject and Unconfirmed on another.

| Label | Who | Bar | Example |
| --- | --- | --- | --- |
| **Official** | The owner of the subject, or the recognized authority for a field. | Owns it, or is the field's recognized authority. No test needed. | A product's documentation, published by the company that makes it. The recognized standards body or research group for a field. |
| **Reputable** | An organization. | Passes the citation test. | A research archive that other institutions cite on a subject. |
| **Trusted** | An individual. | Passes the citation test. | A blog post by an engineer at the company that makes a product, cited by five or more qualifying sources. |
| **Unconfirmed** | An organization or individual. | Fails the citation test, but has an audience or at least one qualifying citation. | A blogger with a large following and active comments but fewer than five qualifying citations. |
| **Ignore** | Any source with no audience and no qualifying citations. | Meets none of the bars above. | A blog with no followers, comments, or links to it. |

The agent decides which sources are official, based on the topic and what it finds. A subject can have more than one.

### Setting

Every source also gets a setting. An organized setting is worth more than an individual one.

1. **Organized:** an organization chose, edited, or published it. Examples: a product's documentation, a journal, a talk on a selective stage where organizers chose the speaker, an edited publication.
2. **Individual:** a person published it on their own. Examples: a personal blog, newsletter, or channel. It still goes through the citation test, so it can be Trusted, Unconfirmed, or Ignore.
3. **Community:** social media and forums. A record of the problems, questions, and requests people raise, not of how things work. Included only when highly relevant: the discussion is about the subject, and it is active compared with other topics in the same forum. When included, sorted by a method that looks at the subject from several fixed viewpoints, such as Six Thinking Hats (method to be confirmed, section 12).

### Value rubric (proposed)

Proposed. Confirm the multipliers before building (section 12).

Each source is scored on three dimensions. 1.0 is the average for each dimension. Each step above or below the average moves the multiplier by 0.2.

| Dimension | 1.4 | 1.2 | 1.0 | 0.8 |
| --- | --- | --- | --- | --- |
| Trust (label) | Official | Reputable, Trusted | Unconfirmed | — |
| Setting | — | Organized | Individual | Community |
| Age | — | Under 3 months | 3 to 9 months | Over 9 months |

- Score = Trust × Setting × Age.
- Age is measured from the date in the source's citation (section 7).
- Ignore sources get no score and back no claim.
- Official sources are exempt from age and always take 1.0 for it. When older and newer versions of an official source are both found, only the newest is used.
- Reputable and Trusted pass the same test, so they share a multiplier. The difference between an organization and an individual is carried by Setting.
- A claim's backing is the highest score among its sources.

### Conflicts

When sources conflict, the source whose score is higher by 0.4 or more is preferred, and the report notes the other. Otherwise the report shows both.

## 7. Report format

### Front matter

| Field | Content |
| --- | --- |
| `name` | Report title. |
| `topic` | The subject researched. |
| `type` | The add-on used, for example `research-build`. |
| `created` | Date first written. |
| `updated` | Date last changed. |

### Body

1. **Findings**, with quotes placed in the text where they apply. Each statement cites every source that informs it, in the text. The exact citation syntax is part of the deferred report format (section 12).
2. **Appendix A: Next searches.** Up to five. Each goes deeper into the topic or covers a related topic worth knowing.
3. **Appendix B: Sources.**
   - **Source list:** every source, as a standard citation that includes its date, with its label, setting, a brief reason for the label, its three multipliers, and its score.
   - **Claim map** (below).

Add-ons may add sections but may not remove these.

### Claim map

Each claim the report makes gets one row.

| Column | Content |
| --- | --- |
| ID | C1, C2, and so on. |
| Claim | One sentence stating it. |
| Sources | Each source behind it, with its label. |
| Role | Follows from the Depends on column. **Foundation:** at least one other claim lists it. **Support:** it lists another claim, and no claim lists it. **Detail:** it lists no claim, and no claim lists it. |
| Depends on | IDs of the claims it builds on, directly or through another claim. |

A summary sits above the table, using counts:

| Line | Example |
| --- | --- |
| Foundation claims by strongest backing | 6 foundation claims: 4 scoring 1.4 or more, 1 from 1.0 to 1.4, 1 below 1.0. |
| Weak foundations, by name | "C3 rests only on an unconfirmed source." |
| Sources by label | 3 official, 2 reputable, 1 trusted, 2 unconfirmed. |

A foundation claim is weak when its backing scores below 1.0, or when all its sources are Unconfirmed. A report is only as solid as its weakest foundation claim, so weak foundations are always named.

## 8. Quote rules

Summarize and cite by default. A quote has to earn its place.

| Quote when | Why |
| --- | --- |
| The passage carries weight: it drives a large part of its source, and that source shapes a large part of the report. | Foundation claims are the likeliest candidates. |
| The wording is the meaning: definitions, rules, limits, requirements, specifications. | Rewording can change what they say. |
| Exact text is needed: commands, settings, file names, code. | Copied exactly and set apart as code. |
| The report credits an opinion, first-hand account, or disputed claim to its owner. | The reader sees who said it and how. |
| The report examines or challenges the passage. | The reader needs the original wording to judge the response. |

| Summarize when | Why |
| --- | --- |
| The passage states plain facts or numbers. | The fact matters, not the wording. |
| It is long or wordy. | Quote only the few words that matter, or none. |
| Its only appeal is how it is written. | Style alone is not a reason. |
| It is common knowledge found across many sources. | No one source owns it. |
| It is unclear, poorly worded, or translated. | A summary states it more clearly. |
| It would make the report's point for it. | The report states its own findings; quotes back them up. |
| It comes from a source labeled Ignore, or is a social media post used only to show a pattern. | Summarize the pattern, with one short example post at most. |

- **Limit:** quotes make up no more than 10% of a report's words. Going past this triggers a review: each quote is checked against the tables above, and the weakest become summaries.
- **Length:** use the fewest words that work. A phrase beats a sentence; a sentence beats a paragraph.
- **Accuracy:** word for word, with no corrections. Trimming must not change the meaning.
- **Fairness:** a quote keeps its context and represents the source's actual position.

## 9. Links between reports

When a report follows up on an Appendix A suggestion, the new report links back to the report that suggested it, and the earlier report's Appendix A entry is edited to link forward. The earlier report's `updated` date changes. How links are stored is part of the deferred report format (section 12).

## 10. Checks

Checks are enforced by hooks declared in project settings (`.claude/settings.json`), not in the agent file. The script is referenced as `${CLAUDE_PROJECT_DIR}/scripts/...`.

1. A `SubagentStop` hook with matcher `researcher` runs the script when the researcher tries to finish. The script checks the report the agent is returning (step 8) and blocks finishing with `decision: "block"` and a `reason` until the report passes. The reason is delivered to the agent as its next instruction.
2. The script is deterministic: the same file always gives the same result. It uses no network and no model calls.
3. Claude Code overrides a block after eight consecutive continuations. The count resets each time the agent calls a tool, so fixing work does not hit it.
4. The checks run unless the person running Claude Code switches hooks off for that run. That is outside this spec.

| Check | Fails when |
| --- | --- |
| Front matter | Any of the five fields is missing or empty. |
| Sections | Findings, Appendix A, or Appendix B is missing. |
| Next searches | Appendix A has more than five entries. |
| Source list | A source has no label or no reason. |
| Claim map | A claim has no source, a `Depends on` ID does not exist, or a Role does not follow from the `Depends on` column. |
| Weak foundations | A weak foundation claim (section 7) is not named in the summary. |
| Quote limit | Quoted words exceed 10% of the report. |
| Ignore sources | A source labeled Ignore backs any claim. |

Judgments the script cannot make, such as whether a label or a quote is right, stay with the agent.

## 11. Add-on requirements

Each add-on is a skill named `research-<kind>`. Its file must state:

| Item | Content |
| --- | --- |
| `description` | When to use it, written so the agent can match it to a request. |
| Scope | What this kind of research covers and leaves out. |
| Where to look | Source types to favor, beyond the general rules. |
| Added sections | Any report sections it adds to the standard format. |

Add-ons may tighten the source rules but may not loosen them.

Starting add-ons:

| Add-on | Covers |
| --- | --- |
| `research-topic` | What is known about a subject. |
| `research-build` | What would inform building something: existing tools, services, and code libraries that work in the project's programming language. Example: options for watching online discussion boards for keywords and saving matching threads. Like all research, it ends in a report; it does not write a build plan. |

## 12. Open items

1. **Report format, destination, and storage (deferred).** Deferred until the rest of the spec is settled. It covers:
   - where reports are saved
   - the file template: headings, date format, table layouts, label words in table cells, inline citation syntax
   - source IDs
   - how quoted words and report words are counted for the quote limit
   - what Appendix B adds beyond sources and claims, such as a search log and rejected sources
   - how links between reports are stored
   - how a follow-up request names the report it follows
   - how the check script finds the report the agent is returning
   - whether a path-scoped rule should guide other sessions that edit reports
2. **Viewpoint method** for social media and forums. Six Thinking Hats is the starting candidate. Confirm it through its own research.
3. **Model choice.** Confirm after first use.
4. **Rubric multipliers.** Confirm the proposed values in section 6 after first use.

## 13. References

**Agent design** (Claude Code documentation):

- Subagents: https://code.claude.com/docs/en/sub-agents
- Hooks: https://code.claude.com/docs/en/hooks
- Rules and memory: https://code.claude.com/docs/en/memory
- Permissions (what runs before a folder is trusted): https://code.claude.com/docs/en/permissions
- Skills: https://code.claude.com/docs/en/skills

**Quote rules** (majority view where sources disagreed):

- https://owl.purdue.edu/owl/research_and_citation/using_research/quoting_paraphrasing_and_summarizing/index.html
- https://writingcenter.unc.edu/tips-and-tools/quotations/
- https://guides.library.jhu.edu/avoidingplagiarism/quoting
- https://american.edu/provost/academic-access/upload/To-Quote-Paraphrase-or-Summarize.pdf
- https://www.citewrite.qut.edu.au/cite/examples/sources/sources_quote_quoting.html
- https://www.mediareform.org.uk/wp-content/uploads/2015/12/Reuters_Handbook_of_Journalism.pdf
