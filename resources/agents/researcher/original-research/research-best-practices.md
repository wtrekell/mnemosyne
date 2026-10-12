---
name: Best practices for research by an AI research agent
topic: General research practice (information science, evidence synthesis, intelligence analysis, journalism verification, LLM deep-research agents) as it applies to an agent that searches the web and writes a sourced report
type: general
created: 2026-10-11
updated: 2026-10-11
---

# Best practices for research by an AI research agent

## Findings

**Scope and limits of this report.** The strongest evidence here comes from Official sources on human practice: intelligence standards [S1], [S2], evidence-synthesis reporting [S3], [S4], verification methods [S5], and a newsroom handbook [S7]. The evidence on LLM research agents is thinner. Most of it is preprints or workshop papers that I could not show to pass the five-citation test, so those claims are marked weak in the claim map. Several PDFs were read through search summaries or truncated fetches; the Source list says which. Two fetches failed (BMJ PRISMA statement, AP news values) and are not used. Claim IDs (C1 and so on) point to the claim map in Appendix B.

### 1. Scoping the question

- Rapid-review guidance says to engage the requester early, narrow the work to a few priority questions, and write a protocol that records every change and why it was made [S4] (C1).
- Intelligence standards say analysis must be fitted to its purpose, source base, and timeline, and that analysts should find and address critical information gaps [S1] (C7).
- Anthropic's multi-agent research team found that agents cannot judge how much effort a question deserves, so the prompts carry explicit budgets. A simple fact check gets one agent and about 3 to 10 tool calls. A direct comparison gets 2 to 4 subagents. Complex research gets more than 10. Agents also defaulted to long, narrow queries, so the prompts say to start with short broad queries and then narrow [S8] (C13).
- Surveys describe deep research as a loop of query planning, information acquisition, memory management, and answer generation [S13] (C20).
- Heuer's point about unseen constraints applies to scoping too. The nine-dots puzzle is hard only because the solver adds a constraint the problem never stated [S2, pp. 82-84]. For an agent, this means stating the interpretation of the question and any assumed limits in the report.

### 2. Search strategy and documentation

- PRISMA 2020 asks reviewers to report, for each source searched, the date it was last searched, and to give the full search strategy with any limits (date, language) tied to the eligibility criteria. It names PRESS as a way to peer review a strategy [S3] (C2). PRISMA is built for reviews of studies, so applying it to web research is my adaptation, not its stated scope.
- Rapid reviews, the closest human analogue to an agent run, commonly search fewer databases, limit by date and language, and use one screener. One methods study found single screening missed about 5% of eligible studies on average. The authors suggest a second check on at least a 10% sample of extractions and say transparency is critical because it is unclear how much streamlining biases conclusions [S4] (C3).
- Anthropic's team wrote that early agents scoured the web "endlessly for nonexistent sources" and duplicated each other's searches when task descriptions were vague. Each delegated task needs an objective, an output format, tool and source guidance, and clear boundaries [S8] (C13).

### 3. Source evaluation

- SIFT gives four moves: stop, investigate the source, find better coverage, and trace claims and quotes to their original context [S5] (C10). Caulfield's page frames this as rebuilding the context the web strips away.
- In the Stanford study of 10 historians, 10 professional fact checkers, and 25 undergraduates, the fact checkers were fastest and most accurate. They left the page and read laterally. The others judged sites by surface cues such as professional logos, scholarly-looking references, or a nonprofit URL. Even readers who went lateral often searched poorly: they omitted quotation marks for exact phrases and clicked top-ranked results without considering search-engine optimization [S6] (C11). The sample is small and the tasks used social and political sites, so I treat the result as suggestive.
- Anthropic's testers found their agents "consistently chose SEO-optimized content farms over authoritative but less highly-ranked sources." The fix was source-quality heuristics added to the prompts [S8] (C13).
- ICD 203 says products must describe the quality and credibility of sources, including accuracy, completeness, age and currency, possible deception, and motivation or bias, and should explain which sources matter most to key judgments [S1] (C7).
- Reuters requires clear attribution of material it did not gather, naming the actual source, and separates reporting facts from reporting rumours [S7] (C12). That copy of the handbook is dated 2008; I could not confirm a newer edition.

### 4. Conflicting evidence and competing hypotheses

- Heuer describes the default human method as satisficing: pick the likeliest answer, collect support, stop. The danger is that most of the supporting evidence is also consistent with other explanations that were never refuted [S2, ch. 8, p. 96] (C9).
- His ACH procedure has eight steps. List all reasonable hypotheses. List evidence and arguments, including your own assumptions. Build a matrix and judge each item's diagnosticity. Delete non-diagnostic evidence. Try to disprove rather than prove. Test sensitivity to the few critical items. Report all hypotheses, not just the leader. Name milestones that would signal a different course [S2, pp. 97-102] (C9).
- Items consistent with every hypothesis have no diagnostic value. Absence of evidence matters: ask what you should see if a hypothesis were true. A hypothesis that is only unproven should be kept alive until it is disproved. Heuer says ACH suits controversial issues where an audit trail is wanted, and that more than about seven hypotheses is unmanageable [S2, pp. 95-99] (C9).
- ICD 203 requires products to assess plausible alternative hypotheses where major judgments face significant uncertainty, and to acknowledge significant contrary information [S1] (C7).
- Reuters tells reporters doing initiative reporting to "try to disprove as well as prove your story," and to tell all sides; it also warns that verbs like "claimed" or "refuted" can imply an editorial judgment [S7] (C12).
- Rapid reviews usually use a descriptive or narrative synthesis rather than a meta-analysis, and GRADE works best with trials and a meta-analysis, so it is of limited use there [S4] (C3). For a web-research agent, evidence synthesis offers reporting discipline more than a ready-made certainty scale.

### 5. Fact versus inference, and calibrated confidence

- ICD 203 requires products to separate underlying information from assumptions and judgments. Assumptions that are the linchpin of an argument must be stated, along with what follows if they are wrong, and indicators that would change the judgment [S1] (C7).
- It requires the basis for uncertainty to be explained. For likelihood it requires one fixed set of terms, set out here as written [S1] (C8):

| almost no chance | very unlikely | unlikely | roughly even chance | likely | very likely | almost certain(ly) |
| --- | --- | --- | --- | --- | --- | --- |
| 01-05% | 05-20% | 20-45% | 45-55% | 55-80% | 80-95% | 95-99% |

  Analysts are strongly encouraged not to mix terms from different rows. A "confidence level" such as "high confidence" must not be combined with a likelihood term in the same sentence, because the first describes the analyst's basis and the second describes the event [S1] (C8).
- Models are poor self-reporters. An evaluation of GPT-4, GPT-3.5, LLaMA-2, PaLM 2 and vision-language models found them overconfident most of the time [S16]. A 2026 benchmark of 15 frontier models reports the most accurate model was not the best calibrated [S17] (C19). Both are Unconfirmed. They point the same way, so an agent's confidence is better tied to stated criteria (how many independent sources, what label, how direct) than to its own sense of certainty. That conclusion is my inference.

### 6. Recency, bias, and selection

- PRISMA wants a last-searched date per source [S3] (C2). ICD 203 lists the age and continued currency of information among the factors that affect source quality [S1] (C7). Reuters has formal correction procedures for stories, which implies published claims should be rechecked for later correction [S7] (C12).
- Selection bias has two named sources in the evidence: search ranking, which favors SEO-optimized pages [S8] (C13), and fixed search limits, which rapid reviews accept but ask to be disclosed [S4] (C3). Anthropic found human testers caught source-selection bias that automated evaluations missed [S8] (C13).

### 7. Stopping rules

- Sources differ on how to stop. Anthropic uses effort budgets set by question complexity, and reports agents kept going after they had enough [S8] (C13, C18). A 2026 industry-track paper argues for evidence-based termination, where the agent continues until stated sufficiency conditions are met, because enterprise research suffers from uneven coverage, context explosion, and premature stopping [S15] (C18).
- DeepSearchQA (900 prompts, 17 fields) names deciding when to stop as a core skill. Its two failure modes are premature stopping, which leaves answers out, and hedging, which pads the answer with low-confidence items [S14] (C18).
- ACH adds a human-analysis version: stop when the hypotheses are narrowed and the sensitivity check is done, and record milestones for future observation [S2] (C9).
- The two approaches fit together: a budget bounds cost, and a sufficiency condition prevents stopping early. No source gives a validated numeric threshold.

### 8. Verification of claims against sources

- Fluent cited answers are not necessarily supported ones. In a human audit of four generative search engines (Bing Chat, NeevaAI, perplexity.ai, YouChat), on average 51.5% of sentences were fully supported by their citations (citation recall) and 74.5% of citations supported their sentence (citation precision). Perceived utility averaged 4.5 on a 5-point scale. Precision correlated inversely with perceived utility (r = -0.96); the authors attribute this to close paraphrase of sources [S10] (C14). These are 2023 systems.
- DeepResearch Bench (100 PhD-level tasks, 22 fields) scores reports on quality against a reference (RACE) and checks each statement-URL pair for whether the cited page supports the statement (FACT). Reported citation accuracy ranged from 77.96% to 90.24% across four commercial agents, and effective citations per task from 8.15 to 111.21. The agent with the highest accuracy (Perplexity, 90.24%) gave far fewer effective citations (31.26) than Gemini Deep Research (81.44%, 111.21) [S9] (C15). Accuracy and volume trade off. These results date from mid-2025.
- Fabricated sources are real but declining. Walters and Wilder found 55% of GPT-3.5 and 18% of GPT-4 citations in generated literature reviews were fabricated, and 43% and 24% of the real ones had substantive errors [S12] (C17). A 2026 study of ten models and agents found 3 to 13% of citation URLs hallucinated and 5 to 18% non-resolving, with deep research agents producing more citations per query but hallucinating URLs at higher rates than search-augmented LLMs. Letting models use a URL-health tool cut non-resolving URLs to under 1% [S11] (C16).
- Anthropic added a separate citation step after research, which assigns each claim to a location in a source [S8], and grades with a rubric covering factual accuracy, citation accuracy, completeness, source quality, and tool efficiency, plus human review [S8] (C13).
- Reuters treats quotes as unalterable and prefers paraphrase when a quote cannot be run verbatim; it asks reporters to consider how they would withstand a challenge before publishing [S7] (C12).
- Observation from this research run (not a cited source): the fetch tool summarizes pages with a smaller model. It returned a binary PDF with no text for four PDFs and sometimes said a rule was absent that was present. I read ICD 203, Heuer, and the Reuters handbook by opening the saved PDFs with the Read tool. A claim should be checked against the actual passage, not a fetch summary.

### 9. Where sources disagree

- **Stopping:** fixed budgets by complexity (S8, Reputable) versus evidence-sufficiency conditions (S15, Unconfirmed). Treated above as complementary; neither is validated against the other.
- **Rigor versus speed:** ACH asks for exhaustive alternatives and warns against early rejection of unproven hypotheses [S2, Official]. Rapid-review guidance accepts shortcuts if disclosed [S4, Official], and ICD 203 itself says the standards are applied "in a manner appropriate to" purpose and timeline [S1, Official]. The sources do not conflict on disclosure; they differ on how much to do. The common rule is to state what was skipped.
- **Citation quality versus quantity:** high-accuracy agents gave fewer citations [S9, Unconfirmed]; precision tracked lower perceived utility [S10, Unconfirmed]. No source says which to prefer.

### 10. Comparison to the repo's researcher agent

Compared: `.claude/agents/researcher.md` [S18] and its design notes [S19]. I judged what exists and did not revisit the label scheme. Gaps are limited to ones that would plausibly make the agent fail or produce worse research.

**Strengths**

- **Every claim needs a source, and weak foundations are surfaced.** The claim map with Role and Depends on, the "no source" check, and the weak-foundation summary give an audit trail of the kind Heuer wants [S2] and ICD 203's explanation of which sources carry key judgments [S1]. They address citation recall, the weakest measured metric in [S10] (C29).
- **Judging the item, not the publisher, plus a citation test.** Both match lateral reading: check what others say about a source rather than trusting its self-presentation [S5], [S6]. Official-first ordering also counters the SEO-farm failure [S8] (C30).
- **Conflicts report each position with sources and labels, and Appendix A carries next searches.** These meet the ICD 203 requirements to acknowledge contrary information and identify gaps and indicators [S1] and Reuters' tell-all-sides rule [S7] (C31).
- **A deterministic SubagentStop check** enforces structure the model cannot skip (C32). That matches the lesson that agents need guardrails [S8].

**Gaps**

1. **No scoping step.** The process starts at "search official sources" [S18]. Rapid-review guidance puts scope and a protocol first [S4], and Anthropic found that agents mis-size effort and duplicate work without it [S8]. A subagent also cannot ask the requester a question. Suggested fix: restate the question, list sub-questions and assumptions in the report, and set an effort budget by question type (C21).
2. **No stopping rule.** Nothing says when to stop searching. The sources name both failures: stopping too early and hedging with padding [S14], [S15], and continuing past sufficiency [S8]. Suggested fix: one short rule combining a budget with a sufficiency check, such as every sub-question having a claim backed by an Official or Reputable/Trusted source or an explicit "not found" (C22).
3. **No step that checks claims against the source text.** The checks in [S19] section 4 test structure: labels exist, IDs resolve, quote percentage. None tests whether the cited page supports the claim, which is the failure measured in [S10], [S9] and [S11]. The agent has WebFetch and Read, and the design keeps the script offline, so the step belongs in the agent file: read the passage before citing, never cite from a search snippet, and record sources known only from snippets or fetch summaries. My own run shows why, given the weak fetch summaries (section 8) (C23).
4. **The "five citing sources" reason is unchecked.** The label reason must list the citing sources [S18], but nothing requires the agent to have seen each one cite the source, and the script cannot check it. Given fabricated and non-resolving references [S11], [S12], an unseen list is a likely fabrication point. The test also does not ask whether the citing sources are independent of each other, which SIFT's "trace to the original" addresses [S5]. Suggested fix: list only citing sources actually opened, and count sources that derive from one origin once (C27).
5. **No search log, access dates, or limits.** The format is deferred, with "search log and rejected sources" listed as undecided [S19] section 7. Without them a reader cannot judge selection bias or repeat the search [S3], [S4]. The agent also has no "as of" date or recheck-for-updates rule beyond "newest official version" (C24, C28). Suggested fix: record queries run, date searched, and limits applied, and a short list of rejected sources, as soon as the format is settled.
6. **No active search for disconfirming evidence.** Conflicts are reported only when sources happen to disagree, and the process ranks sources before testing the answer. That invites the satisficing Heuer describes [S2] and the one-sided sourcing Reuters warns against [S7]. Suggested fix: for each foundation claim, run at least one search aimed at contrary evidence or a competing explanation, and record "none found" with the query (C25).
7. **No fact versus inference marker and no confidence language.** The claim map records source and role but not whether a claim is reported, inferred, or a judgment, nor how sure the report is. ICD 203 requires both distinctions and a fixed likelihood vocabulary [S1]. Model self-reported confidence is unreliable [S16], [S17], so the rubric should rest on source count, label, and directness. Suggested fix: add a claim type to the map and use ICD 203 terms for any judgment (C26).
8. **No evaluation plan.** The checks cannot tell whether the agent does good research. Anthropic started with about 20 real queries, outcome-based grading, and human review that caught source-selection bias [S8]; DeepResearch Bench's claim-support method is a template [S9]. This is a repo-level suggestion, not a defect in the agent file (C32).

## Appendix A: Next searches

1. How to detect that several sources trace to one origin (citation cascades, duplicate publication) and how evidence synthesis handles dependent evidence; tied to gap 4.
2. Cheap per-claim support checks an agent can run without a shell or model-judge (entailment-style checks such as ALCE and FActScore, quote-anchoring); tied to gap 3.
3. Cochrane Rapid Reviews Methods Group's updated guidance and GRADE-style certainty rating, adapted to web evidence.
4. Structured analytic techniques beyond ACH (key assumptions check, devil's advocacy) and evidence on whether they improve accuracy.
5. Confidence rubrics for agent reports: evidence on words of estimative probability and whether rubric-based confidence beats self-reported confidence.

## Appendix B: Sources

### Source list

| ID | Citation | Label | Setting | Reason for label |
| --- | --- | --- | --- | --- |
| S1 | Office of the Director of National Intelligence, "Intelligence Community Directive 203: Analytic Standards," signed 2 Jan 2015, technical amendments 21 Jan 2022 and 12 Jun 2023, https://archive.dni.gov/files/documents/ICD/ICD-203.pdf | Official | Organized | Owns the US intelligence analytic standards. Official for those standards only. Read pp. 1-8 in full. |
| S2 | Richards J. Heuer Jr., "Psychology of Intelligence Analysis," CIA Center for the Study of Intelligence, 1999, https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf (read ch. 7 opening and ch. 8, pp. 95-102) | Official | Organized | Heuer developed ACH and this is the CIA's own publication of it. Only the first eight pages of chapter 8 were read. |
| S3 | Page MJ et al., "PRISMA 2020 explanation and elaboration," BMJ 2021;372:n160, https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/ | Official | Organized | The PRISMA group's own reporting guidance. First 100,000 of about 351,000 characters read (to item 13c). I identified it as n160 from its content; the n71 statement page returned HTTP 403 and was not used. |
| S4 | King VJ, Stevens A, Nussbaumer-Streit B, Kamel C, Garritty C, "Paper 2: Performing rapid reviews," Systematic Reviews 11:151, 30 Jul 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC9338520 | Official | Organized | Written by Cochrane Rapid Reviews Methods Group members as part of its guidance series, the recognized authority on rapid-review methods. |
| S5 | Mike Caulfield, "SIFT (The Four Moves)," Hapgood, 19 Jun 2019, https://hapgood.us/2019/06/19/sift-the-four-moves/ | Official | Individual | Caulfield created SIFT. First 100,000 of about 279,000 characters read. |
| S6 | Sam Wineburg and Sarah McGrew, "Lateral Reading and the Nature of Expertise," Stanford History Education Group, 2017, https://purl.stanford.edu/yk133ht8603; read through the summary in Stanford Daily, 26 Oct 2017, https://stanforddaily.com/2017/10/26/fact-checkers-more-likely-than-peer-expert-groups-to-identify-credible-information-determine-gse-researchers/ | Reputable | Organized | Cited by Stanford Daily, Stanford News, SSRC MediaWell, The Chronicle of Higher Education, and bespacific (5 seen in search results). The full study text was not read, only coverage. |
| S7 | Reuters, "Handbook of Journalism" (copy hosted by Media Reform Coalition, 2015; pages dated 2008), https://www.mediareform.org.uk/wp-content/uploads/2015/12/Reuters_Handbook_of_Journalism.pdf | Official | Organized | Owns Reuters' newsroom standards. Possibly not the newest edition; I could not confirm a later one. Read the Accuracy and Freedom from bias sections. |
| S8 | Anthropic Engineering, "How we built our multi-agent research system," Jun 2025, https://www.anthropic.com/engineering/multi-agent-research-system | Reputable | Organized | First-hand account. Cited by ByteByteGo, aktagon signals, Pat McGuinness's Substack, ZenML LLMOps database, and beri.net (5 seen in search results). Not all citing items are strictly independent organizations. |
| S9 | Du M, Xu B, Zhu C, Wang X, Mao Z, "DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents," arXiv:2506.11763, 13 Jun 2025 (ICLR 2026), https://arxiv.org/abs/2506.11763 | Unconfirmed | Organized | Accepted at ICLR 2026. Citing sources I verified: S11 and S15, which both use it, 2 of 5. Results read from the HTML version, first 100,000 of about 120,000 characters. |
| S10 | Liu NF, Zhang T, Liang P, "Evaluating Verifiability in Generative Search Engines," Findings of EMNLP 2023, https://arxiv.org/abs/2304.09848 | Unconfirmed | Organized | Peer-reviewed venue and widely visible, but I did not verify five citing sources. Table read from the arXiv HTML version. |
| S11 | Rao D, Wong E, Callison-Burch C, "Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents," arXiv:2604.03173, 3 Apr 2026, https://arxiv.org/abs/2604.03173 | Unconfirmed | Individual | Recent preprint, no citing sources verified. Abstract read. |
| S12 | Walters WH, Wilder EI, "Fabrication and errors in the bibliographic citations generated by ChatGPT," Scientific Reports 13:14045, 2023, https://doaj.org/article/fc88ea07ec994a7c8a144f8516c48cbf | Unconfirmed | Organized | Figures taken from a search summary, not the paper. Appears in several result lists but five citing sources not verified. Models tested are outdated. |
| S13 | "Deep Research" systematic survey (title as shown on a mirror page; authors not captured), arXiv:2512.02038, Dec 2025, https://arxiv.org/abs/2512.02038 | Unconfirmed | Individual | Abstract only. No citing sources verified. |
| S14 | "DeepSearchQA: Bridging the Comprehensiveness Gap for Deep Research Agents," arXiv:2601.20975, Jan 2026, https://arxiv.org/abs/2601.20975 | Unconfirmed | Individual | Abstract only. No citing sources verified. |
| S15 | "Don't Stop Early: Scalable Enterprise Deep Research with Controlled Information Flow and Evidence-Aware Termination," ACL 2026 Industry Track, arXiv:2604.24978, https://arxiv.org/abs/2604.24978 | Unconfirmed | Organized | Abstract only. Its results are the authors' own claims. |
| S16 | Groot T, Valdenegro-Toro M, "Overconfidence is Key: Verbalized Uncertainty Evaluation in Large Language and Vision-Language Models," TrustNLP 2024, https://arxiv.org/html/2405.02917v1 | Unconfirmed | Organized | Workshop paper. Read through a search summary only. |
| S17 | "ConfidenceBench: Evaluating Confidence Calibration in Large Language Models," arXiv:2607.20526, 2026, https://arxiv.org/pdf/2607.20526 | Unconfirmed | Individual | Recent preprint. Read through a search summary only. |
| S18 | Repo file `.claude/agents/researcher.md` (repo commit 312258d), /Users/trekell/repos/mnemosyne/.claude/agents/researcher.md | Official | Individual | Owns the agent under comparison. |
| S19 | Repo file `resources/agents/researcher/10-58-49-design.md` (status: draft, repo commit 312258d), /Users/trekell/repos/mnemosyne/resources/agents/researcher/10-58-49-design.md | Official | Individual | Owns the design notes for the agent under comparison. Reference material only; the agent does not read it. |

### Claim map

- **Foundation claims by strongest source:** 16 foundation claims: 8 backed by an Official source (C1, C2, C3, C7, C8, C9, C10, C12), 3 by Reputable or Trusted at best (C11, C13, C18), 5 by Unconfirmed only (C14, C15, C16, C17, C19).
- **Weak foundations:** C14 rests only on an unconfirmed source (S10). C15 rests only on an unconfirmed source (S9). C16 rests only on an unconfirmed source (S11). C17 rests only on an unconfirmed source (S12). C19 rests only on unconfirmed sources (S16, S17).
- **Sources by label:** 8 official, 2 reputable, 0 trusted, 9 unconfirmed, 0 ignored.

| ID | Claim | Sources | Role | Depends on |
| --- | --- | --- | --- | --- |
| C1 | Rapid-review guidance says to engage the requester, narrow to a few priority questions, and keep a protocol recording changes and reasons. | S4 (Official) | Foundation | none |
| C2 | PRISMA 2020 requires a last-searched date per source and the full search strategy with limits tied to eligibility criteria. | S3 (Official) | Foundation | none |
| C3 | Rapid reviews accept shortcuts (fewer databases, limits, single screening), single screening missed about 5% of eligible studies in one study, and transparency about the shortcuts is critical. | S4 (Official) | Foundation | none |
| C7 | ICD 203 requires source credibility description, uncertainty explanation, separation of information from assumptions and judgments, alternatives analysis, contrary information, and consideration of source currency, applied to fit purpose and timeline. | S1 (Official) | Foundation | none |
| C8 | ICD 203 fixes likelihood terms to probability ranges, discourages mixing term sets, and bars combining a confidence level with a likelihood term in one sentence. | S1 (Official) | Foundation | none |
| C9 | Heuer's ACH counters satisficing by listing alternatives, judging diagnosticity, seeking disproof, keeping unproven hypotheses alive, noting absent evidence, and reporting all hypotheses. | S2 (Official) | Foundation | none |
| C10 | SIFT is four moves: stop, investigate the source, find better coverage, trace claims to the original. | S5 (Official) | Foundation | none |
| C11 | In a Stanford study, fact checkers who read laterally outperformed historians and students who judged sites by surface cues. | S6 (Reputable) | Foundation | none |
| C12 | Reuters requires attribution of sourced material, separates fact from rumour, treats quotes as unalterable, and says to try to disprove as well as prove a story. | S7 (Official) | Foundation | none |
| C13 | Anthropic's research agents needed effort budgets, detailed delegation, source-quality heuristics against SEO farms, a citation step, and human review that caught source-selection bias. | S8 (Reputable) | Foundation | none |
| C14 | In a 2023 audit of four generative search engines, average citation recall was 51.5% and precision 74.5% while perceived utility was high. | S10 (Unconfirmed) | Foundation | none |
| C15 | DeepResearch Bench measures statement-level citation accuracy and effective citations; four commercial agents scored 77.96% to 90.24% accuracy, with accuracy and volume trading off. | S9 (Unconfirmed) | Foundation | none |
| C16 | In 2026 testing, 3 to 13% of agent citation URLs were hallucinated, deep research agents more than search-augmented LLMs, and a URL-health tool cut non-resolving URLs below 1%. | S11 (Unconfirmed) | Foundation | none |
| C17 | In 2023, 55% of GPT-3.5 and 18% of GPT-4 generated citations were fabricated, and many real ones had substantive errors. | S12 (Unconfirmed) | Foundation | none |
| C18 | Agents stop too early or hedge with padding; remedies are effort budgets and evidence-sufficiency conditions, neither validated against the other. | S14 (Unconfirmed), S15 (Unconfirmed), S8 (Reputable) | Foundation | none |
| C19 | Verbalized LLM confidence is often overconfident and accuracy does not imply calibration. | S16 (Unconfirmed), S17 (Unconfirmed) | Foundation | none |
| C20 | Surveys describe deep research as query planning, information acquisition, memory management, and answer generation. | S13 (Unconfirmed) | Detail | none |
| C21 | Gap: the agent has no scoping, sub-question, assumption-recording, or effort-budget step. | S18 (Official), S19 (Official), S4 (Official), S8 (Reputable) | Support | C1, C13 |
| C22 | Gap: the agent has no stopping rule. | S18 (Official), S14 (Unconfirmed), S15 (Unconfirmed), S8 (Reputable) | Support | C18 |
| C23 | Gap: the checks verify structure only and nothing makes the agent confirm that a cited page supports each claim. | S19 (Official), S10 (Unconfirmed), S9 (Unconfirmed), S11 (Unconfirmed) | Support | C14, C15, C16 |
| C24 | Gap: the report has no search log, search dates, or limits (format deferred). | S19 (Official), S3 (Official), S4 (Official) | Support | C2, C3 |
| C25 | Gap: the agent does not search for disconfirming evidence or competing explanations; conflicts are reported only if found. | S18 (Official), S2 (Official), S7 (Official) | Support | C9, C12 |
| C26 | Gap: the claim map has no fact/inference marker and no confidence vocabulary. | S18 (Official), S1 (Official), S16 (Unconfirmed), S17 (Unconfirmed) | Support | C7, C8, C19 |
| C27 | Gap: the five-citing-sources reason is not required to be seen by the agent or checked for independence. | S18 (Official), S5 (Official), S6 (Reputable), S11 (Unconfirmed), S12 (Unconfirmed) | Support | C10, C11, C16, C17 |
| C28 | Gap: the agent file has no as-of date or recheck rule for recency beyond newest-official-version. | S18 (Official), S3 (Official), S1 (Official) | Support | C2, C7 |
| C29 | Strength: the claim map, source reasons, and weak-foundation reporting give an audit trail aimed at citation recall. | S18 (Official), S2 (Official), S1 (Official), S10 (Unconfirmed) | Support | C9, C7, C14 |
| C30 | Strength: judging the item, the citation test, and Official-first ordering fit lateral reading and counter SEO-driven source choice. | S18 (Official), S5 (Official), S6 (Reputable), S8 (Reputable) | Support | C10, C11, C13 |
| C31 | Strength: conflict reporting with positions and labels, plus next searches, meet contrary-information and gap requirements. | S18 (Official), S1 (Official), S7 (Official) | Support | C7, C12 |
| C32 | Strength and gap: the deterministic hook enforces structure, but the agent has no evaluation set of the kind used for research agents. | S19 (Official), S8 (Reputable), S9 (Unconfirmed) | Support | C13, C15 |
