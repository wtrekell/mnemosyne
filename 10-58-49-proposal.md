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
| **Checks** (hooks) | Declared in the agent file; script in `scripts/` | Automatic checks on every report the agent writes. | Agent and skill instructions are guidance the model reads. Hooks are enforced. Anything that must always hold goes here. |
| **Rules** | `.claude/rules/` | Not used for now. | Rules are guidance for the main session, optionally scoped to file paths. Here they would repeat the agent's instructions. Revisit after the wiki review (section 12). |

## 3. Agent definition

| Field | Value | Notes |
| --- | --- | --- |
| `name` | `researcher` | |
| `description` | "Researches a topic and writes a sourced report with labeled sources, a claim map, and suggested next searches. Use for any research request." | Claude reads this to decide when to hand work to the agent, so it states the trigger plainly. |
| `tools` | Read, Grep, Glob, Write, Edit, WebSearch, WebFetch, Skill, documentation lookup (context7) | Only what research needs. No shell access. Write and Edit are for reports and the links between them. |
| `model` | Inherit from the session | Revisit after first use. |
| `skills` | None preloaded | Preloading puts the full text of every listed skill into context at start. Leaving this empty lets the agent load only the add-on it needs. |
| `hooks` | See section 10 | Run only while the agent is active. |

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

A source passes when **five or more other sources cite it**. Talks given on a selective stage count toward the five. Social media, forums, and sources labeled Ignore do not.

### Labels

| Label | Who | Bar | Example |
| --- | --- | --- | --- |
| **Official** | The owner of the subject. | Owns it. No test needed. | A product's documentation, published by the company that makes it. The recognized standards body or research group for a field. |
| **Reputable** | An organization. | Passes the citation test. | A research archive that other institutions cite on a subject. |
| **Trusted** | An individual. | Passes the citation test. | A blog post by an engineer at the company that makes a product, cited by five or more qualifying sources. |
| **Unconfirmed** | An organization or individual. | Has an audience but fails the citation test. | A blogger with a large following and active comments but fewer than five qualifying citations. |
| **Public talk** | Anyone speaking in public. | See levels below. | A recorded talk, a blog post, a forum thread. |
| **Ignore** | A single source with no citations or responses. | Meets none of the bars above. | A blog with no followers, comments, or links to it. |

The agent decides which sources are official, based on the topic and what it finds. A subject can have more than one.

### Public talk levels

1. **Talks on a selective stage.** Recorded talks and conference presentations where organizers chose the speaker.
2. **Blogs and articles.** They still go through the citation test, so a blog post can rise to Trusted or Reputable, or fall to Ignore.
3. **Social media and forums.** A record of the problems, questions, and requests people raise, not of how things work. Included only when highly relevant. When included, sorted by a method that looks at the subject from several fixed viewpoints (method to be chosen, section 12).

### Age

| Age | Value |
| --- | --- |
| Under 3 months | High |
| 3 to 9 months | Moderate |
| Over 9 months | Low |

Official sources are exempt. When older and newer versions of an official source are both found, the newest takes priority.

### Conflicts

When sources with different labels conflict and neither is clearly right, they are treated as equals and the report shows both.

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

1. **Findings**, with quotes placed in the text where they apply.
2. **Appendix A: Next searches.** Up to five. Each goes deeper into the topic or covers a related topic worth knowing.
3. **Appendix B: Sources.**
   - **Source list:** every source, with its label, public talk level (if any), date, and a brief reason for the label.
   - **Claim map** (below).

Add-ons may add sections but may not remove these.

### Claim map

Each claim the report makes gets one row.

| Column | Content |
| --- | --- |
| ID | C1, C2, and so on. |
| Claim | One sentence stating it. |
| Sources | Each source behind it, with its label. |
| Role | **Foundation:** other claims depend on it. **Support:** adds to a foundation claim. **Detail:** stands alone. |
| Depends on | IDs of the claims it builds on, directly or through another claim. |

A summary sits above the table, using counts:

| Line | Example |
| --- | --- |
| Foundation claims by strongest backing | 6 foundation claims: 4 official, 1 reputable, 1 unconfirmed. |
| Weak foundations, by name | "C3 rests only on an unconfirmed source." |
| Sources by label | 3 official, 2 reputable, 1 trusted, 2 unconfirmed, 1 public talk. |

A report is only as solid as its weakest foundation claim, so weak foundations are always named.

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

When a report follows up on an Appendix A suggestion, the new report links back to the report that suggested it, and the earlier report's Appendix A entry is edited to link forward. The earlier report's `updated` date changes.

## 10. Checks

A script runs after every report the agent saves (a `PostToolUse` hook on Write and Edit, limited to report files). If a check fails, the script exits with code 2 and its message goes back to the agent to fix.

| Check | Fails when |
| --- | --- |
| Front matter | Any of the five fields is missing or empty. |
| Sections | Findings, Appendix A, or Appendix B is missing. |
| Next searches | Appendix A has more than five entries. |
| Source list | A source has no label or no reason. |
| Claim map | A claim has no source, or a `Depends on` ID does not exist. |
| Weak foundations | A foundation claim backed only by Unconfirmed or Public talk sources is not named in the summary. |
| Quote limit | Quoted words exceed 10% of the report. |
| Ignore sources | A source labeled Ignore backs any claim. |

Judgments the script cannot make, such as whether a label or a quote is right, stay with the agent.

A `Stop` hook could also block the agent from finishing until the last report passes. Add it only if the `PostToolUse` check proves not enough.

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
| `research-build` | What would inform building something: existing tools, services, and code libraries that work in the project's programming language. Example: options for watching online discussion boards for keywords and saving matching threads. Its report feeds a separate tool that designs the build plan; it does not write the plan itself. |

## 12. Open items

1. **Wiki review.** Where reports are saved, how links are stored, and whether a path-scoped rule should guide other sessions that edit reports.
2. **Viewpoint method** for social media and forums. To be chosen through its own research.
3. **Model choice.** Confirm after first use.

## 13. References

**Agent design** (Claude Code documentation):

- Subagents: https://code.claude.com/docs/en/sub-agents
- Hooks: https://code.claude.com/docs/en/hooks
- Rules and memory: https://code.claude.com/docs/en/memory

**Quote rules** (majority view where sources disagreed):

- https://owl.purdue.edu/owl/research_and_citation/using_research/quoting_paraphrasing_and_summarizing/index.html
- https://writingcenter.unc.edu/tips-and-tools/quotations/
- https://guides.library.jhu.edu/avoidingplagiarism/quoting
- https://american.edu/provost/academic-access/upload/To-Quote-Paraphrase-or-Summarize.pdf
- https://www.citewrite.qut.edu.au/cite/examples/sources/sources_quote_quoting.html
- https://www.mediareform.org.uk/wp-content/uploads/2015/12/Reuters_Handbook_of_Journalism.pdf
