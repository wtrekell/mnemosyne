---
name: Characteristics of a good research report template for an AI subagent
topic: Ideal characteristics of a research report template that an AI subagent fills in, useful to the parent agent or human reader and to later machine checking
type: general
created: 2026-10-11
updated: 2026-10-11
---

# Characteristics of a good research report template for an AI subagent

## Findings

### Answer

A good template makes the reader's first screen a short answer with an overall confidence, then states the question and method briefly, then gives findings that each carry their sources and a confidence tied to a stated basis, then shows conflicts, limitations and gaps in their own places. Intelligence standards require the main message up front [S1], and reporting guidelines require rationale, objectives, methods and limitations [S2]. Evidence-grading practice shows certainty per finding with reasons [S3]. LLM research suggests that a citation that resolves is not a citation that supports [S7], that stated confidence is unreliable [S10], and that rigid output formats can hurt reasoning [S8]. So the template should fix metadata and checkable fields and leave reasoning as prose. Overall confidence in this answer: moderate. The Official sources agree on the human-facing structure. The LLM-specific evidence is all Unconfirmed (see Limitations and gaps).

Confidence labels used below: High means an Official source states it directly. Moderate means an Official source supports it indirectly, or several Unconfirmed sources agree. Low means one Unconfirmed source, or an inference resting on one. "Inference" marks this report's own recommendations.

### Scope and method

Question: what characteristics make a report template, filled in by a subagent, useful to a human or parent agent and checkable by a machine. In scope: section set and order, summary placement, confidence, limitations, scope and method, conflicts, checkability, length, omissions. Out of scope: how to conduct research, and the choice of source labels in the repo, which is settled. Sources came from web searches and page fetches on 2026-10-11 and from the two repo files. Several sources were seen only as search summaries or abstracts; Appendix B and the Limitations section say which. Labels follow the researcher agent's rules. I could not verify five-citation counts, so no source is labeled Reputable or Trusted.

### Section set, order and summary placement

- The ICD 203 tradecraft standard on argumentation says a product presents a clear main analytic message up front. Where there are several judgments, the main message is drawn from them together [S1]. Confidence: High. [C1]
- Minto's Pyramid Principle, as summarized by secondary pages, puts one governing idea at the top. Each level beneath summarizes the group below it, and the executive summary expresses the document's single idea [S9]. Confidence: Low (secondary only, not Minto's book). [C1]
- PRISMA 2020 orders a review as title, abstract, rationale, objectives, methods, results, discussion, and other items such as registration and data availability [S2]. Methods come before results, and the abstract has its own checklist. Confidence: High. [C6]
- Models use information at the start or end of a long context better than information in the middle, per secondary write-ups of the "lost in the middle" work [S11]. A parent agent reading a long report is exposed to this. Confidence: Low. [C15]
- Inference: order the sections as answer, scope and method, findings, conflicts, limitations and gaps, then appendices. The answer needs to be short enough to hold the whole conclusion and its confidence. [C17] [C23]
- The Anthropic multi-agent write-up reports that subagents return condensed findings, that the lead tells each subagent the output format it wants, and that large outputs can be stored externally with a lightweight reference passed back [S5]. Confidence: Low (Unconfirmed source). [C14]

### Confidence, assumptions and certainty

- ICD 203 requires products to explain the basis for uncertainty in major judgments. It separates the likelihood of an event from the analyst's confidence in the judgment, and names causes of uncertainty such as knowledge gaps and the amount and currency of information. It also asks for indicators that would change the level of uncertainty, consistent terms, and no confidence level and likelihood in the same sentence [S1]. Confidence: High. [C2]
- ICD 203 also asks products to separate underlying information from assumptions and judgments, and to state assumptions that are the linchpin of an argument [S1]. Confidence: High. [C3]
- ICD 203 requires describing the quality and credibility of sources and addressing critical information gaps [S1]. Confidence: High. [C5]
- GRADE, as applied in Cochrane's Summary of findings tables, rates certainty for each important outcome as high, moderate, low or very low. It uses five downgrade domains: risk of bias, inconsistency, indirectness, imprecision and publication bias. Tables hold at most seven outcomes, with full judgments in separate evidence profiles [S3]. Confidence: Moderate (search summary of the Handbook, chapter not opened). The point for a template is that certainty belongs to each finding, comes with reasons, and sits in a compact table apart from the long judgments. [C9]
- Verbalized LLM confidence is often miscalibrated, clusters in a few values, and can be pushed up by training [S10]. Confidence: Low. [C10]
- Inference: record confidence as a small fixed scale per finding, with a one-phrase basis drawn from observable facts. Examples are the labels of the sources, whether independent sources agree, and whether the source was read in full or seen as a snippet. Do not ask the agent for a free percentage. This keeps source strength (what the claim map already records) apart from claim confidence (what the reader needs), which is the split ICD 203 draws between source quality and confidence [S1]. [C18]
- Toulmin's model adds a qualifier and a rebuttal to claim, grounds and warrant [S14]. Inference: a per-finding confidence with basis serves as the qualifier. Conflicts and gaps serve as the rebuttal. [C25]

### Scope, method and reporting items

- PRISMA 2020 asks for rationale and explicit objectives, eligibility criteria, every source searched with the date last searched, and the search strategy. It also asks for how selection and extraction were done, how certainty was assessed, and limitations of both the evidence and the review process [S2]. The Statement says it guides reporting, not conduct, and should not be used to judge a review's quality [S2]. Confidence: High. [C6] [C7]
- PRISMA-S adds sixteen items so that literature searches can be reproduced [S4]. Confidence: Moderate (summary only). [C8]
- Inference: a subagent report needs only a compact version. That means the question as asked, what is in and out of scope, which sources and tools were searched with dates, how sources were labeled, and what the agent could not read. This is the minimum for a reader to judge whether the report answers their question. [C23]

### Conflicts and alternatives

- ICD 203 asks products to assess plausible alternative hypotheses, especially under significant uncertainty, and to acknowledge significant supporting and contrary information [S1]. Confidence: High. [C4]
- GRADE treats inconsistency across evidence as a reason to lower certainty [S3]. Confidence: Moderate. [C9]
- Inference: give conflicts a fixed place. Each entry names the question in dispute, each position with its sources and labels, and a short note on how the disagreement affected confidence. A conflict buried in a finding is easy for a parent agent to miss. [C20]
- Two conflicts found in this research:
  - ICD 203 requires confidence statements [S1]. An ODNI research note says the community has rarely used confidence levels as intended and that they may give a false sense of precision [S13]. Both are Official; the second was seen as a search summary only. Resolution used here: keep confidence, but define it by a rule. [C27]
  - Strict output formats lowered reasoning performance and looser formats did better on reasoning tasks, while classification tasks tolerated or gained from strict formats [S8]. Human and machine readers both want structure. The paper also tested a two-step approach of free text first, then conversion [S8]. Inference: reason in prose, then fill the fixed fields. [C12] [C22]

### Limitations, gaps and what to leave out

- PRISMA requires discussing limitations of the evidence and of the review process [S2]. ICD 203 requires identifying information gaps [S1]. Confidence: High. [C5] [C6]
- Inference: a limitations and gaps section lists what was searched but not found, what was only partly read (snippet, abstract, secondary summary), what was not searched, and assumptions made. Without it, a reader reads silence as "checked and clean". [C19]
- Leave out, as inference from ICD 203's note that explaining change or consistency need not be lengthy or boilerplate [S1] and from the verbosity findings below: narrative of the search path, boilerplate disclaimers, restated background the reader already has, and repeated confirmation of consistency. The search path belongs in a log or the method line. Confidence: Low. [C19] [C22]

### Machine-checkability and faithfulness

- An evaluation of 14 LLMs found that citation links resolved over 94% of the time and were relevant over 80% of the time, but factual support was only 39 to 77%. Factual accuracy fell about 42% on average as tool calls went from 2 to 150 [S7]. Confidence: Low (Unconfirmed; abstract page only). The authors conclude that more retrieval does not produce more accurate citations. [C11]
- Anthropic's guidance for Claude lists three grounding steps: allow "I don't know", extract quotes before analysis, and have each claim checked against a supporting quote, retracting it if none is found [S6]. Confidence: High for Claude behavior, with the page's own note that these reduce but do not eliminate hallucination. [C13]
- Inference: a checker can verify structure cheaply and exactly. It can check required headings, that every cited ID exists in the source table, that every source is cited somewhere, that counts in the summary equal counts from the tables, that roles follow from the dependency column, that quote share is under the cap, and that no placeholder text remains. Support of a claim by its source is the hard part [S7]. A template can help by giving each claim row an anchor, such as a short locator or a verbatim snippet, that a verifier can find in the cited source. [C21]
- Inference: link each prose finding to its claim-map row with a claim ID, so a checker can compare the statement with the row's sources. [C21]
- Length: LLM judges, and humans in one study, preferred longer answers at equal quality [S12]. Confidence: Low. Template implication: length caps per section, and a summary that is a fixed small size, so a longer report does not look better only because it is longer. [C16] [C22]

### Comparison to the repo's template

Basis: [S15] and [S16]. The claim map, five-citation labels and Appendix A are settled and are judged only on what they lack. Gaps are limited to those likely to make the report worse for its reader or the agent. [C26]

Strengths

- Inline source IDs on every statement, a source table with date, label, setting and reason, and a claim map with dependencies and roles. These give a checker exact structure to test and give a reader provenance, which matches the claim-to-source practice above [S7] [S6].
- A quote cap and "summarize by default" help length and faithfulness [S12].
- Findings is free-form prose with subsections. This is consistent with the format-restriction result [S8].
- The template has a slot for the source's date and for each label's reason, which supports ICD 203's call to describe source quality [S1].

Gaps, most important first

1. No answer up front. The report opens at Findings, so the reader must assemble the conclusion. ICD 203 puts the main message first [S1], and position effects favor the top of a long document [S11]. Suggested fix: a short "Answer" block (a few sentences plus overall confidence) before Findings.
2. No question, scope or method statement. Front matter has `topic` only. A reader cannot tell the question as understood, what was excluded, which tools were used, or the search date. PRISMA items on objectives, information sources with dates and search strategy cover this [S2] [S4]. Suggested fix: a "Scope and method" block of about five lines, which the agent's source rules already imply.
3. No per-finding confidence. The claim map records which sources back a claim (source strength) but not how confident the agent is in the claim, which depends on agreement, directness and whether the source was fully read. ICD 203 and GRADE both keep these apart [S1] [S3]. Suggested fix: a Confidence column in the claim map and a tag in the prose, using a fixed three-level scale with a one-phrase basis, not a free number [S10].
4. No limitations and gaps section. Nothing prompts the agent to say which sources were seen only as snippets, what was not searched, or what was not found. PRISMA and ICD 203 both require this [S2] [S1]. This is the largest honesty risk, since the "Weak foundations" line covers only claims resting on Unconfirmed sources.
5. No place for conflicts. The agent definition says to report each position with its sources and labels [S16], but the template gives it no home, so it will be scattered through Findings. Suggested fix: a "Conflicts" subsection under Findings, or a single marked line per conflict.
6. Prose is not tied to claim rows. Findings cite source IDs but not claim IDs, and the claim map has one-sentence claims that may or may not match the prose. A checker cannot test whether each prose statement has a row. Suggested fix: tag each finding statement with its claim ID [S7].
7. Inference is not marked. Findings may mix what sources say with the agent's own conclusions. ICD 203 asks products to separate information from judgments [S1]. Suggested fix: one word tag (Sourced or Inference) on each finding, which also tells the claim map what a row's sources are.
8. No length guidance beyond quotes. Findings is unbounded, and there is a tendency toward longer output [S12]. Suggested fix: a soft cap on the Answer and per-subsection guidance in the placeholders. Confidence in this gap: Low, as the supporting evidence is Unconfirmed.

Not raised as gaps: the field order of the front matter, and the Related reports section.

## Conflicts

See the Conflicts and alternatives subsection of Findings.

## Limitations and gaps

- Read in full or large part: ICD 203 (PDF, as amended 2023) [S1]; the PRISMA 2020 paper (first 100,000 of 116,000 characters) [S2]; Anthropic's hallucination page [S6]; Anthropic's multi-agent article [S5]; the two repo files [S15] [S16].
- Seen only as search summaries or abstract pages: Cochrane chapter 14 [S3], PRISMA-S [S4], the citation-evaluation paper [S7], the format-restriction paper [S8], the confidence-calibration papers [S10], the verbosity papers [S12], the ODNI note [S13], the Minto summaries [S9], the lost-in-the-middle write-ups [S11], and the Toulmin pages [S14]. Claims resting on these carry the confidence shown.
- Five-citation counts were not verified, so every non-Official source is Unconfirmed, and these labels are provisional.
- Not found or not searched: published report schemas from deep-research products; consulting formats beyond Minto (such as SCQA); GRADE primary papers; claim-level attribution benchmarks other than [S7]; research-log practice beyond PRISMA-S; Claim-Evidence-Reasoning education sources (Toulmin was used instead).
- Almost all LLM-specific evidence comes from 2024 to 2026 preprints or papers on other tasks, not on report templates. How a template changes faithfulness or length was not found as a direct test. The section recommendations are therefore inference from human-facing standards plus indirect LLM evidence.
- Claim C26 and all Inference claims are this report's own judgments.

## Appendix A: Next searches

1. How deep-research products (OpenAI, Google, Perplexity) structure their reports and citations, from their documentation or system cards.
2. Claim-level attribution benchmarks (for example AIS and ALCE) and how a claim anchor or supporting snippet improves automated verification.
3. The GRADE primary papers (Core GRADE, BMJ 2024) and a minimal three-level certainty rubric derived from them for agent use.
4. Effect of required summary and per-section length caps on LLM report length and faithfulness, tested directly.
5. Rubric-based or evidence-derived confidence for LLM outputs, compared with verbalized confidence.

## Appendix B: Sources

### Source list

| ID | Citation | Label | Setting | Reason for label |
| --- | --- | --- | --- | --- |
| S1 | Office of the Director of National Intelligence, "Intelligence Community Directive 203: Analytic Standards," signed 2 Jan 2015, technical amendments 21 Jan 2022 and 12 Jun 2023, https://archive.dni.gov/files/documents/ICD/ICD-203.pdf | Official | Organized | Owns the intelligence analytic standards, newest version used. |
| S2 | Page et al., "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews," BMJ 372:n71, 29 Mar 2021, https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/ | Official | Organized | The field's recognized reporting guideline. |
| S3 | Cochrane, "Handbook for Systematic Reviews of Interventions, Chapter 14: Completing 'Summary of findings' tables and grading the certainty of the evidence," version 6.5, 2024, https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14 | Official | Organized | Recognized authority on applying GRADE in reviews. Seen via search summary. |
| S4 | Rethlefsen et al., "PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews," Systematic Reviews, 2021, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8270366/ | Official | Organized | Official extension of PRISMA. Seen via search summary. |
| S5 | Anthropic, "How we built our multi-agent research system," Anthropic Engineering, 2025, https://www.anthropic.com/engineering/multi-agent-research-system | Unconfirmed | Organized | Has an audience; I could not list five citing sources. Not the owner of the subject. |
| S6 | Anthropic, "Reduce hallucinations," Claude Docs, undated (accessed 2026-10-11), https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations | Official | Organized | Owner of the model the repo's agent runs on; used only for Claude behavior. |
| S7 | Onweller et al., "Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents," arXiv:2605.06635, 7 May 2026, https://arxiv.org/abs/2605.06635 | Unconfirmed | Organized | Recent preprint; no verified citations. Abstract page only. |
| S8 | Tam et al., "Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models," EMNLP 2024 Industry Track, https://arxiv.org/abs/2408.02442 | Unconfirmed | Organized | Selective venue and an audience; citation count not verified. Abstract page only. |
| S9 | Secondary summaries of Minto, "The Pyramid Principle," e.g. https://thinkinsights.net/strategy/pyramid-principle and a slide deck at https://www.slideshare.net/slideshow/the-pyramid-principle-by-barbara-minto/6099582, undated | Unconfirmed | Individual | Summaries of a widely used consulting book, not the book. Seen via search results only. |
| S10 | "On Verbalized Confidence Scores for LLMs," arXiv:2412.14737, Dec 2024; "Calibrating Verbalized Confidence with Self-Generated Distractors," arXiv:2509.25532, Sep 2025, https://arxiv.org/pdf/2509.25532 | Unconfirmed | Organized | Preprints with no verified citation count. Search summary only. |
| S11 | Secondary write-ups of "Lost in the Middle," e.g. Arize, https://arize.com/blog/lost-in-the-middle-how-language-models-use-long-contexts-paper-reading/, undated | Unconfirmed | Organized | Vendor blog about a well-known paper; original not read. |
| S12 | "MTalk-Bench," arXiv:2508.18240, Aug 2025, and "Do Chatbot LLMs Talk Too Much? The YapBench Benchmark," arXiv:2601.00624, Jan 2026, https://arxiv.org/pdf/2601.00624 | Unconfirmed | Organized | Preprints; MTalk-Bench is on speech models, not reports. Search summary only. |
| S13 | Office of the Director of National Intelligence, National Intelligence University research note on confidence levels, DF-2024-00001, https://www.dni.gov/files/documents/FOIA/DF-2024-00001-NIU_Research_Short.pdf | Official | Organized | ODNI-released research on its own standards; not a directive. Search summary only. |
| S14 | Verheij, "Evaluating arguments based on Toulmin's scheme," Argumentation 19:347-371, 2005, https://www.ai.rug.nl/~verheij/publications/pdf/toulmin2005.pdf, and Cal State open textbook, https://pressbooks.calstate.edu/writingargumentsinstem/chapter/toulmin-argument-model/ | Unconfirmed | Organized | Academic paper and teaching text; counts not verified. Search summary only. |
| S15 | Repo template, `_templates/research/general-research.md`, read 2026-10-11 | Official | Individual | The subject of the comparison. |
| S16 | Repo agent, `.claude/agents/researcher.md`, read 2026-10-11 | Official | Individual | The subject of the comparison. |

### Claim map

- **Foundation claims by strongest source:** 23 foundation claims: 9 backed by an Official source (C1, C2, C3, C4, C5, C6, C8, C9, C13), 0 by Reputable or Trusted at best, 6 by Unconfirmed only (C10, C11, C12, C15, C16, C24). The other 8 (C17, C18, C19, C20, C21, C22, C23, C25) are this report's inferences and have no source of their own; they rest on the claims they list.
- **Weak foundations:** C10, C11, C12, C15, C16 and C24 each rest only on Unconfirmed sources. Inferences that depend on them: C17 (C15), C18 (C10), C21 (C11), C22 (C12, C16), C25 (C24).
- **Sources by label:** 8 official, 0 reputable, 0 trusted, 8 unconfirmed, 0 ignored.

| ID | Claim | Sources | Role | Depends on |
| --- | --- | --- | --- | --- |
| C1 | Intelligence standards require a clear main message up front; consulting practice puts one governing idea at the top. | S1 (Official), S9 (Unconfirmed) | Foundation | none |
| C2 | ICD 203 requires explaining the basis of uncertainty, separating likelihood from confidence, naming causes of uncertainty and indicators that would change it. | S1 (Official) | Foundation | none |
| C3 | ICD 203 requires separating information from assumptions and judgments. | S1 (Official) | Foundation | none |
| C4 | ICD 203 requires assessing alternatives and acknowledging contrary information. | S1 (Official) | Foundation | none |
| C5 | ICD 203 requires describing source quality and addressing information gaps. | S1 (Official) | Foundation | none |
| C6 | PRISMA 2020 requires rationale, objectives, methods, search sources with dates, and limitations of evidence and process. | S2 (Official) | Foundation | none |
| C7 | PRISMA 2020 is for reporting, not conduct or quality judgment. | S2 (Official) | Detail | none |
| C8 | PRISMA-S sets sixteen items to make literature searches reproducible. | S4 (Official) | Foundation | none |
| C9 | GRADE-based tables give certainty per outcome on four levels with reasons, in a compact table separate from full judgments. | S3 (Official) | Foundation | none |
| C10 | Verbalized LLM confidence is often miscalibrated and clustered. | S10 (Unconfirmed) | Foundation | none |
| C11 | LLM citations usually resolve and are on topic, but factual support is weak and worsens with retrieval depth. | S7 (Unconfirmed) | Foundation | none |
| C12 | Strict output formats lower LLM reasoning performance; looser formats help reasoning. | S8 (Unconfirmed) | Foundation | none |
| C13 | Grounding steps for Claude: allow "I don't know", quote first, retract unsupported claims. | S6 (Official) | Foundation | none |
| C14 | Subagents are told the output format and return condensed findings or references to stored outputs. | S5 (Unconfirmed) | Detail | none |
| C15 | Models use information at the start and end of long context better than the middle. | S11 (Unconfirmed) | Foundation | none |
| C16 | LLM judges favor longer outputs at equal quality. | S12 (Unconfirmed) | Foundation | none |
| C17 | Inference: place a short answer with overall confidence first. | none (inference) | Foundation | C1, C15 |
| C18 | Inference: per-finding confidence on a fixed scale with an observable basis, separate from source strength. | none (inference) | Foundation | C2, C3, C9, C10 |
| C19 | Inference: include a limitations and gaps section, and leave out boilerplate and search-path narrative. | none (inference) | Foundation | C5, C6 |
| C20 | Inference: give conflicts a fixed place with positions, sources, labels and effect on confidence. | none (inference) | Foundation | C4, C9 |
| C21 | Inference: make structure exactly checkable, tag prose with claim IDs, and give each claim a verifiable anchor. | none (inference) | Foundation | C11, C13 |
| C22 | Inference: fixed fields for metadata, prose for reasoning, length caps per section. | none (inference) | Foundation | C12, C16 |
| C23 | Inference: a short scope and method block with question, scope, sources, dates, labeling, unread items. | none (inference) | Foundation | C6, C8 |
| C24 | Toulmin's model adds qualifier and rebuttal to claim, grounds and warrant. | S14 (Unconfirmed) | Foundation | none |
| C25 | Inference: per-finding confidence acts as the qualifier; conflicts and gaps act as the rebuttal. | none (inference) | Foundation | C24, C9 |
| C26 | The repo template lacks an up-front answer, scope and method, per-finding confidence, a limitations section, a conflicts slot, prose-to-claim links, an inference marker and length guidance; its provenance structure is a strength. | S15 (Official), S16 (Official) | Support | C17, C18, C19, C20, C21, C22, C23, C25 |
| C27 | An ODNI research note says confidence levels have rarely been used as intended and may give false precision. | S13 (Official) | Detail | none |
