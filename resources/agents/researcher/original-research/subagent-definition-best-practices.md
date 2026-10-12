---
name: Best practices for defining subagents
topic: How to write subagent definition files and system prompts for delegated agents, from sources other than Anthropic's Claude Code subagents page
type: general
created: 2026-10-11
updated: 2026-10-11
---

# Best practices for defining subagents

Scope: sources other than Anthropic's Claude Code subagents documentation page. Anthropic engineering posts and prompting docs, other frameworks' docs (LangChain, OpenAI Agents SDK, CrewAI), and practitioner write-ups are used. Where the original source could not be read, that is stated.

## Findings

### Description and trigger writing

- A subagent's name and description are the main way a parent decides whether to call it. LangChain's docs say to use an action-oriented name and a description that is specific about what tasks the agent handles and when to use it, and they list vague descriptions as the first pitfall (misrouting or skipped calls) [S8]. The OpenAI Agents SDK has the same mechanism: `handoff_description` for handoffs, and `tool_name`/`tool_description` when an agent is wrapped as a tool [S9]. Anthropic's tool-writing guidance says descriptions are prompts and that small refinements can matter a lot [S3]. (C1)
- Tembo advises opening with "Use this agent when..." or including "use proactively", and being specific, because vague descriptions make automatic delegation unreliable [S11]. (C1)
- Models tend to over-delegate. Anthropic's prompting docs report that recent Claude models delegate proactively and can spawn subagents where a direct grep would do. They give a damping prompt: use subagents for parallel, isolated, or independent work, and work directly for simple tasks, sequential steps, or single-file edits [S5]. Anthropic's research-system post reports an early failure of "spawning 50 subagents for simple queries" [S1]. LangChain says a single agent is usually enough for a few tools with simple logic [S8]. Tembo notes that subagents add latency and small edits can be faster in the main conversation [S11]. A description should therefore say when not to delegate, not only when to. (C2)
- Simplicity first: add agents or workers only when they demonstrably improve outcomes [S2]. Cognition argues multi-agent setups are fragile because decisions are spread across agents [S7]. (C18)

### The brief the parent must give (inputs) and context isolation

- Anthropic found that each subagent needs "an objective, an output format, guidance on the tools and sources to use, and clear task boundaries." A one-line task such as "research the semiconductor shortage" led to one subagent covering the wrong year and two duplicating each other [S1]. (C3)
- By default a LangChain subagent receives only the task description and starts in a clean window. Passing more of the parent's history helps continuity but bloats the prompt and weakens isolation, and passing too little forces the subagent to redo work. Isolation can be the main reason to use a subagent at all [S8]. Anthropic's context-engineering post describes sub-agents as doing deep search in clean windows and returning a condensed summary [S4]. (C11)
- Cognition's counter-position: share full agent traces, not just messages, because subagents working from a task-only handoff make conflicting implicit decisions and misread nuance [S7]. This disagrees with the isolation-as-feature view of [S8] and [S4]. The two fit together as a trade-off: narrow, read-only lookups suit isolation, while interdependent work (such as parallel writing) is where [S7] says it breaks. (C11)
- Effort scaling belongs in the prompt because agents judge effort poorly. Anthropic gives rough budgets: one agent and about 3-10 tool calls for a simple fact, 2-4 subagents for comparisons, more for complex work [S1]. Stopping conditions such as a maximum iteration count are recommended in [S2], and CrewAI exposes `max_iter` (default 20), `max_execution_time` and retry limits [S10]. (C4)

### Tool scoping and least privilege

- Grant only the tools the role needs. Tembo describes `tools` as an allowlist, with read-only reviewers on Read/Grep/Glob and write tools only for fixers. It also says hooks can enforce rules the allowlist cannot, such as restricting where an agent may write [S11]. CrewAI's agent `tools` list defaults to empty and the docs say to give each agent only what its role needs. `allow_delegation` defaults to False [S10]. (C5)
- Fewer, distinct tools beat many overlapping ones. Each tool needs a distinct purpose and a clear description, since bad descriptions send agents down wrong paths [S1][S3]. If the prompt names several overlapping tools (for example web search and a docs-lookup tool), it should say which to use for what [S1][S3]. (C6)

### Prompt length, structure, and how much to specify

- Aim for the "Goldilocks" altitude: not brittle hardcoded logic, not vague guidance. Start with a minimal prompt, test it, then add instructions and a few canonical examples in response to observed failures, rather than listing every edge case [S4]. Tembo: keep the system prompt short, give one job and a clear definition of done [S11]. (C7)
- Explaining the reason behind an instruction helps the model generalize it [S5]. (C8)
- Leave method to the model but fix the things it cannot judge: effort budget, stopping, output shape, tool boundaries [S1][S4]. Anthropic's tool post and the research post both tell agents to start with short, broad queries and narrow afterwards, because long specific queries return little [S1][S3]. (C12)

### Output contract to the parent

- The parent typically sees only the subagent's final message. LangChain names as a common failure a subagent that does the work but leaves the results out of that message, and says to remind it that the supervisor only sees the final output [S8]. (C9)
- State the output format explicitly and ask for aggressive summarization, since verbose results still consume the parent's context [S11]. Anthropic describes condensed returns of about 1,000-2,000 tokens [S4]. The OpenAI SDK offers `output_type` to force a structured result [S9]. (C9)
- For large or structured outputs, have the subagent store results externally and return a lightweight reference, which avoids information loss and token overhead [S1]. (C10)

### Failure modes

- Looping after results suffice, endless searching for sources that do not exist, excessive status chatter, over-long queries, and wrong tool choice were observed in Anthropic's multi-agent system. Agents also favored SEO content farms over authoritative sources, which human testing caught [S1]. Mitigations were explicit prompt heuristics and guardrails against runaway behavior [S1]. (C12)
- Vague tasks, missing results in the final message, and too little or too much context are the LangChain pitfalls [S8]. (C9, C11)

### Hallucinated sources and self-verification

- Anthropic's hallucination guidance: give explicit permission to say "I don't know", ground answers in extracted word-for-word quotes, and have the model check each claim for a supporting quote and retract the claim if none is found. The page says these reduce but do not eliminate hallucination [S6]. Stopping the search instead of inventing a source is the matching behavior for agents [S1][S6]. (C13)
- Verification during the run: agents should get ground truth from the environment at each step [S2], and use interleaved thinking after each tool result to judge quality and spot gaps [S1]. Tembo suggests a verifier step for risky changes [S11]. (C14)

### Evaluation and testing of definitions

- Start with about 20 representative queries, because prompt-caused effects are large and easy to see on few cases. Judge outcomes rather than exact paths, use an LLM judge with a rubric (factual accuracy, citation accuracy, completeness, source quality, tool efficiency), and add human testing. Run the real prompt and tools and watch step by step [S1]. (C15)
- Read transcripts. Track accuracy, runtime, tool-call count, and tool errors; many redundant calls or invalid-parameter errors point to description or default problems. Use held-out tasks to avoid overfitting, and avoid verifiers so strict they reject correct answers [S3]. (C15, C17)
- Error analysis workflow: gather traces, note the first failure in each without preset categories, cluster into named failure modes, label and measure rates, then fix or add an evaluator [S12]. (C16)
- Tembo gives no formal test method, only to start with one specialist and measure how often it is invoked [S11].

### Comparison to the repo's researcher agent

File read: `/Users/trekell/repos/mnemosyne/.claude/agents/researcher.md`. Source-label scheme is not judged here. Only gaps likely to cause failure or worse reports are listed.

Strengths

- The prompt is short and ordered: one role line, a numbered procedure, then rules. It matches the short, single-job guidance, and the design keeps detail in the template file [S4][S11]. (C24)
- Tools are an explicit allowlist with no Bash, matching least privilege [S10][S11]. (C24)
- The output contract is strong. The report goes to a file via a template and the parent gets a location plus a short summary, as recommended for large outputs and condensed returns [S1][S4][S8]. (C25)
- "Search official sources first" counters the content-farm failure that Anthropic observed [S1]. (C12 applied)

Gaps

1. Over-delegation trigger. The description says "Use proactively for any research request" and has no when-not-to-use. Proactive wording plus models' tendency to over-delegate means trivial lookups will spawn a full labeled, claim-mapped report [S1][S5][S8][S11]. Fix: narrow the description to multi-source research that yields a saved report, and say when the parent should answer directly. (C19)
2. No input and budget handling. The prompt never says what to do with a vague or underspecified request, and a fresh subagent sees only the brief [S8][S7]. It also has no effort budget, search heuristics (short broad queries first), or stopping condition, so it can search endlessly or over-research simple questions [S1][S2][S3][S10]. Fix: say how to proceed or return questions when scope is unclear, scale effort to the request, and set a stop rule. (C20)
3. No anti-fabrication rules. A sourced-report agent is judged on citation accuracy, yet the prompt does not say to cite only pages actually opened, to say "not found" instead of filling a gap, or to drop claims without support [S1][S6]. Search snippets alone can produce confident but wrong citations. Fix: add those three rules. (C21)
4. Write and Edit are unscoped. The agent can change any file, though it only needs to create reports and edit one earlier report's Appendix A. Anthropic and Tembo both recommend narrowing and enforcing it, with hooks for path limits [S5][S10][S11]. Fix: add a path-restricting hook or state the allowed paths. (C22)
5. Return contract omits problems, and step 6 is ambiguous. The return is "location and a short summary" with nothing about reporting what was not found, what stayed unverified, or failed checks, and the parent sees only that message [S8]. Step 6 says "Fix anything the checks report", but the file defines no checks and the agent has no Bash tool to run any. If a hook reports them, the prompt should say so, since otherwise the step is a no-op [S2][S8]. (C23)
6. No test set for the definition. There is no sign of a set of about 20 representative requests with a rubric, or transcript review, which is how definition problems such as the above would be found [S1][S3][S12]. This is a process gap rather than a file edit. (C26)

## Appendix A: Next searches

1. OpenAI "A practical guide to building agents" (PDF), read in full: instruction-writing, tool overlap, and when to split agents. Only secondary summaries were reachable in this run.
2. Anthropic "Prompting Claude Opus 5", section "Controlling subagent spawning", for a sample damping prompt and subagent-control specifics.
3. LangChain "How and when to build multi-agent systems" and the Deep Agents subagents page, for task-description and fork-versus-isolated context guidance.
4. Evaluation of prompts for citation accuracy in research agents: published rubrics and judge-calibration studies.
5. Hook patterns that restrict an agent's Write/Edit paths, and how they surface check results to the agent.

## Appendix B: Sources

### Source list

Dates for S1-S4 and S7 are the publication months as known to the researcher; the fetched text did not display them. Undated living docs show the access date.

| ID | Citation | Label | Setting | Reason for label |
| --- | --- | --- | --- | --- |
| S1 | Anthropic, "How we built our multi-agent research system," Anthropic Engineering, June 2025, https://www.anthropic.com/engineering/multi-agent-research-system | Official | Organized | Anthropic is the recognized authority on agent design for Claude and built this system. No test. |
| S2 | Anthropic, "Building effective agents," Anthropic Engineering, December 2024, https://www.anthropic.com/engineering/building-effective-agents | Official | Organized | Same authority as S1. Does not use the term subagent; orchestrator-workers pattern used. |
| S3 | Anthropic, "Writing effective tools for agents," Anthropic Engineering, September 2025, https://www.anthropic.com/engineering/writing-tools-for-agents | Official | Organized | Same authority as S1. |
| S4 | Anthropic, "Effective context engineering for AI agents," Anthropic Engineering, September 2025, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Official | Organized | Same authority as S1. |
| S5 | Anthropic, "Prompting best practices" (section "Subagent orchestration"), Claude Platform docs, accessed 2026-10-11, https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | Official | Organized | Newest version of the owner's prompting docs. Not the Claude Code subagents page. |
| S6 | Anthropic, "Reduce hallucinations," Claude Platform docs, accessed 2026-10-11, https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations | Official | Organized | Owner's docs. Written for prompts generally, not subagents specifically. |
| S7 | Walden Yan, "Don't Build Multi-Agents," Cognition, June 2025, https://cognition.com/blog/dont-build-multi-agents | Unconfirmed | Organized | Widely discussed, so it has an audience, but five qualifying citing sources were not checked in this run. It is a position piece from one team's experience. |
| S8 | LangChain, "Subagents" (multi-agent), LangChain docs, accessed 2026-10-11, https://docs.langchain.com/oss/python/langchain/multi-agent/subagents | Official | Organized | Owner's documentation for LangChain's subagent pattern. No test. |
| S9 | OpenAI, "Agents" (OpenAI Agents SDK), accessed 2026-10-11, https://openai.github.io/openai-agents-python/agents/ | Official | Organized | Owner's documentation for the SDK. |
| S10 | CrewAI, "Agents," CrewAI docs, accessed 2026-10-11, https://docs.crewai.com/en/concepts/agents | Official | Organized | Owner's documentation for CrewAI. |
| S11 | Tembo Team, "Claude Code Subagents: A 2026 Practical Guide," Tembo, 2026-05-15, https://tembo.io/blog/claude-code-subagents | Unconfirmed | Organized | Vendor practitioner guide with an audience; no qualifying citations checked. Opinions, not documented behavior. |
| S12 | Langfuse, "Error analysis to evaluate LLM applications," Langfuse blog, 2025-08-29 (date from search listing; page showed none), https://langfuse.com/blog/2025-08-29-error-analysis-to-evaluate-llm-applications | Unconfirmed | Organized | Vendor guide, stated to be adapted from Hamel Husain's Eval FAQ. Citation test not run. |

### Claim map

- **Foundation claims by strongest source:** 14 foundation claims: 14 backed by an Official source, 0 by Reputable or Trusted at best, 0 by Unconfirmed only.
- **Weak foundations:** None.
- **Sources by label:** 9 official, 0 reputable, 0 trusted, 3 unconfirmed, 0 ignored.

| ID | Claim | Sources | Role | Depends on |
| --- | --- | --- | --- | --- |
| C1 | Name and description are the primary routing lever, and vague descriptions cause misrouting. | S8 (Official), S9 (Official), S3 (Official), S11 (Unconfirmed) | Foundation | none |
| C2 | Models over-delegate, so definitions should say when not to delegate. | S1 (Official), S5 (Official), S8 (Official), S11 (Unconfirmed) | Foundation | none |
| C3 | A subagent brief needs objective, output format, tool/source guidance, and boundaries. | S1 (Official) | Foundation | none |
| C4 | Effort scaling and stopping conditions must be written into the prompt. | S1 (Official), S2 (Official), S10 (Official) | Foundation | none |
| C5 | Tools should be an explicit least-privilege allowlist, enforced by hooks where needed. | S10 (Official), S11 (Unconfirmed) | Foundation | none |
| C6 | Tools need distinct purposes and descriptions, and overlapping ones need usage guidance. | S1 (Official), S3 (Official) | Detail | none |
| C7 | Keep prompts short at the right altitude; start minimal and add from observed failures. | S4 (Official), S11 (Unconfirmed) | Foundation | none |
| C8 | Giving the reason for an instruction helps the model apply it. | S5 (Official) | Detail | none |
| C9 | The parent sees only the final message, so results and format must be stated and condensed there. | S8 (Official), S4 (Official), S9 (Official), S11 (Unconfirmed) | Foundation | none |
| C10 | Large outputs should be stored externally and returned as a reference. | S1 (Official) | Foundation | C9 |
| C11 | Context isolation helps focus but starves subagents of context; Cognition argues for sharing full traces. | S8 (Official), S4 (Official), S7 (Unconfirmed) | Foundation | none |
| C12 | Observed failures include endless searching, content-farm sources, and long queries; short broad queries first. | S1 (Official), S3 (Official) | Foundation | C4 |
| C13 | Allow "I don't know", ground in quotes, and retract unsupported claims. | S6 (Official), S1 (Official) | Foundation | none |
| C14 | Verify during the run using environment ground truth and reflection after tool results. | S2 (Official), S1 (Official), S11 (Unconfirmed) | Foundation | C13 |
| C15 | Evaluate with about 20 representative tasks, outcome-based rubric judging, tool metrics, and human review. | S1 (Official), S3 (Official) | Foundation | none |
| C16 | Error analysis from traces drives fixes to prompts and evaluators. | S12 (Unconfirmed), S3 (Official) | Foundation | C15 |
| C17 | Redundant calls and invalid-parameter errors signal description or default problems. | S3 (Official) | Detail | none |
| C18 | Prefer the simplest design; multi-agent adds fragility. | S2 (Official), S7 (Unconfirmed), S8 (Official) | Support | C2 |
| C19 | Researcher: "proactively for any research request" invites over-delegation. | S1, S5, S8, S11 | Support | C1, C2 |
| C20 | Researcher: no handling of vague briefs, effort budget, or stop rule. | S1, S2, S3, S7, S8, S10 | Support | C3, C4, C11, C12 |
| C21 | Researcher: no rule to cite only opened sources, say not found, or retract. | S1, S6 | Support | C12, C13, C14 |
| C22 | Researcher: Write and Edit are not scoped to report paths. | S5, S10, S11 | Support | C5 |
| C23 | Researcher: return omits caveats, and step 6 "checks" are undefined. | S2, S8 | Support | C9, C14 |
| C24 | Researcher strength: short ordered prompt and explicit allowlist without Bash. | S4, S10, S11 | Support | C5, C7 |
| C25 | Researcher strength: file-based report with a short return to the parent. | S1, S4, S8 | Support | C9, C10 |
| C26 | Researcher: no evaluation set or transcript review for the definition. | S1, S3, S12 | Support | C15, C16 |
