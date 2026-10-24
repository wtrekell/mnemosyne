# Claude in UX: documented practice

**Research date: October 23, 2026**  
**Prepared for: UX Design Engineer**  
**Export note:** This is the full report previously delivered in the conversation, with source citations linked for use outside the chat. It preserves the report’s evidence limitations and does not represent additional research or verification.

## Executive summary

The clearest documented use in the evidence reviewed is **turning a designer’s interaction ideas into low-fidelity, clickable prototypes for team discussion**—with the designer directing the work and evaluating the result.[cite:443] Firsthand accounts also describe research synthesis, reusable project context, and transcript-based follow-up, but the accessible supporting evidence does not establish five independent, artifact-backed conversational UX workflows.[cite:349][cite:424][cite:405][cite:459]

**This report therefore does not claim to meet the requested five-practitioner threshold.** It presents one bounded historical case, compares five independent practitioners’ accounts, and makes the admission failures visible rather than promoting unverified accounts into substantive cases.

The most consequential distinction is between **evidence that someone uses Claude** and **evidence that a particular workflow produces dependable UX work**. The accounts reviewed establish the former more readily than the latter: they do not provide a reproducible comparison demonstrating better research conclusions, improved usability, or measured product outcomes attributable specifically to conversational Claude.[cite:443][cite:349][cite:424][cite:405][cite:459]

The practical lesson is correspondingly narrow: use Claude to produce something a practitioner can inspect—an interaction alternative, a source-linked extraction, or a context handoff—not to certify an interpretation, validate an experience, or manufacture evidence about users.

## Scope and method

### Admission criteria

The requested scope was treated as requiring all of the following:

- A public, firsthand account from a practitioner with an explicit UX connection.
- Explicit identification of Claude’s contribution.
- Use through Claude’s conversational interface, rather than Claude Code, Claude Design, or an API-built application.
- A concrete task and workflow, not merely a proposed use.
- Supporting artifacts or a session recording.
- Sufficient information to distinguish outputs from human checking and subsequent use.

Searches covered practitioner publications, UX editorial sites, recorded-workflow leads, substantive interviews, and public professional posts. Search results were followed to original accounts where accessible; five practitioners were retained for comparison, but only one account supplied enough task-level detail and supporting illustrations for a bounded case analysis.

This is a **qualitative evidence review, not a prevalence study**. Search visibility, public sharing, and willingness to disclose work all affect the available sample.

### Product boundaries

A conversational interface is no longer enough to identify the underlying product. Current official documentation describes Claude Design as usable inside conversations and the Artifacts tab; consequently, an example being “in Claude chat” does not automatically put it within this report’s scope.[cite:494][cite:496]

Historical Artifacts use remains distinguishable: Anthropic’s June 25, 2024 announcement described generated documents, diagrams, code, and website designs appearing beside a Claude conversation.[cite:484] The case below explicitly separates that earlier chat-prototyping practice from the practitioner’s later move to Claude Design.[cite:443]

Cowork was not counted as ordinary conversational use here. Anthropic describes it as an agentic environment for executing multi-step tasks, and current documentation distinguishes Chat, Cowork, and Code as different working surfaces.[cite:467][cite:468] This conservative boundary excludes an otherwise relevant design-leadership example rather than silently expanding the user’s clarification.

### Evidence labels

| Label | Meaning |
|---|---|
| **Strong** | Detailed firsthand workflow plus inspectable artifacts or recorded execution |
| **Moderate** | Substantive firsthand account with limited supporting artifacts |
| **Limited** | Confirmed use, but insufficient detail to assess the workflow or result |

These labels describe support for an account—not proof that the workflow is effective.

## Evidence map

Five independent practitioners are compared below. **Only the first row is developed as a bounded case; the others are screened evidence, not additional qualifying cases.**

| Practitioner | UX activity | Claude’s contribution | Input material |
|---|---|---|---|
| **Maya Brennan** | Historical interaction prototyping | Generated clickable HTML wireframes and smaller interface alternatives in Claude chat.[cite:443] | Designer-supplied interaction direction; complete prompts and source inputs are unavailable.[cite:443] |
| **Debbie Levitt** | Qualitative analysis and reporting | Reports using Claude for analysis, synthesis, outlier exploration, and locating quotations.[cite:349] | Research transcripts; a separate recording announcement identifies anonymized qualitative transcripts.[cite:349][cite:353] |
| **Paul Boag** | Research context and product thinking | Describes research projects spanning Claude and ChatGPT; Claude-specific attribution is incomplete.[cite:424] | Prior research, transcripts, survey results, documentation, and website material.[cite:424] |
| **Ryan Rumsey** | Maintaining working context | Describes Claude Projects, instructions, chat logs, and handoff documents across iterations.[cite:405] | Previous conversations, a README, and a next-step checklist.[cite:405] |
| **Femke van Schoonhoven** | Transcript-based follow-up | Used Claude with a Granola connector to retrieve a quotation and prepare testimonial follow-up.[cite:459] | Transcript of a mentoring conversation captured by Granola.[cite:459] |

| Practitioner | Human validation | Outcome | Strength and admission |
|---|---|---|---|
| **Brennan** | Reports team feedback and repeated iteration; no documented usability evaluation of the prototypes.[cite:443] | Reports being able to influence a rapidly changing product more promptly; no controlled timing or user-outcome measurement.[cite:443] | **Moderate.** Bounded historical case; article includes prototype illustrations, but no inspected executable artifact or complete session log.[cite:443] |
| **Levitt** | Says outputs are checked against notes and recollection of sessions.[cite:349] | Perceived usefulness; no independently demonstrated analysis-quality improvement in the accessed material.[cite:349] | **Moderate account; artifact requirement unresolved.** A recording is announced, but its execution was not inspected.[cite:353] |
| **Boag** | Describes checking sources and transcript quotations, but across a mixed-tool account.[cite:424] | Reports substantial AI-related efficiency gains without isolating Claude’s contribution.[cite:424] | **Limited for Claude-specific assessment.** Not admitted as a main case. |
| **Rumsey** | Uses stable-version handoffs, but the post does not expose a complete tested conversation.[cite:405] | Reports reduced frustration and improved continuity; no measured comparison.[cite:405] | **Limited.** No inspected supporting chat log; associated Cowork material is outside the conservative scope. |
| **Van Schoonhoven** | Reports obtaining the speaker’s approval before publication.[cite:459] | Reports that the testimonial was approved and published.[cite:459] | **Limited for this question.** A narrated video transcript supports the account, but the task concerns design-education operations rather than a UX product decision. |

## Detailed case

### Interaction exploration: Maya Brennan

**Practitioner and context.** Brennan’s August 2026 article identifies the author as a lead designer working on an analytics product. It describes professional work, not a hypothetical prompt exercise, and distinguishes early Claude-chat prototyping from later Claude Design and production-coding practices.[cite:443]

**UX problem.** The team’s product was changing too quickly for detailed design files to remain current. Brennan needed a way to discuss evolving interactions and influence implementation without maintaining polished representations of every change.[cite:443]

**Actual workflow.**

| Stage | Documented practice | Evidence boundary |
|---|---|---|
| Source material | Brennan supplied design direction based on the intended interface and interactions.[cite:443] | The full brief, original screenshots, and complete input set are not published in the retrieved account. |
| Claude interaction | Requested clickable HTML prototypes; for smaller questions, requested several interface alternatives rather than a whole screen.[cite:443] | Complete prompts, model version, subscription, and settings are unspecified. |
| Output | Low-fidelity wireframes and smaller interface explorations, illustrated in the article.[cite:443] | No executable prototype or full generation history was inspected for this report. |
| Human checking | Shared work with the team, received feedback, and iterated.[cite:443] | The account does not expose the feedback record or specific rejected recommendations. |
| Subsequent use | Used prototypes to help shape what engineers built.[cite:443] | No traceable chain connects a particular generated alternative to a measured user outcome. |

**Claude’s specific contribution.** Claude produced reviewable representations of interaction ideas; Brennan retained responsibility for direction and selection.[cite:443] The article separately assigns later production coding to Cursor and later prototyping to Claude Design, so those outcomes cannot be credited to the historical conversational workflow.[cite:443]

**Validation and traceability.** Team critique is documented, but validation against user evidence is not. The source does not establish participant testing, accessibility testing, task-completion measurement, or a comparison with an independently produced design.[cite:443]

**Evidence and artifacts.** The [original article](https://uxdesign.cc/how-to-become-an-ai-designer-ff8ee8aed205) provides the practitioner’s account, role statement, prototype illustrations, and an explicit separation between Claude Chat, Claude Design, Cursor, ChatGPT, and other tools.[cite:443] It supports the existence and structure of the workflow more strongly than its effectiveness.

**Outcome.** Brennan reports faster participation in product development and an improved ability to influence implementation. These are practitioner-reported working benefits, not measured evidence of better usability or product performance.[cite:443]

**Limitations and failures.** The account identifies visual refinement as disproportionately frustrating and advises keeping early prototypes simple and deliberately separate from the product’s visual system.[cite:443] Broader reflections about context switching and reduced connection to craft concern the later mixed-tool workflow and should not be attributed solely to Claude chat.[cite:443]

**Transferable lesson — interpretation.** The useful unit is a **bounded interaction question**, not an entire product. A practitioner could reasonably borrow the practice of generating a rough, clickable alternative for critique, provided the team understands that the artifact expresses a proposal rather than a validated design.

## Screened firsthand accounts

### Research analysis: Debbie Levitt

Levitt’s UX role is explicitly identified in a substantive practitioner interview. The account describes using Claude for portions of analysis, synthesis, and reporting while retaining human responsibility for research questions, sessions, follow-up, and interpretation.[cite:349]

The documented sequence is transcripts → Claude-assisted analysis or quotation retrieval → checking against notes and session knowledge → reporting.[cite:349] The interview names Claude 3.7 as a historical preference and expresses dissatisfaction with version 4; that preference should not be converted into a current model recommendation.[cite:349]

A separate firsthand listing points to an October 2025 live demonstration using anonymized qualitative transcripts.[cite:353] However, the accessible listing does not itself expose the prompts, output, corrections, or recording execution, so it cannot satisfy the stricter artifact-backed admission requirement.

**What can be learned:** retaining firsthand knowledge of the sessions gives a researcher something against which to challenge generated interpretations. **What remains unestablished:** whether quotation retrieval was exact, whether themes were complete, and whether the assistance improved analysis after checking time was included.

A statement that Claude “admitted” a transcription-accuracy figure appears in the interview, but a model’s self-description is not a benchmark and is not treated as performance evidence here.[cite:349]

### Reusable context: Paul Boag

Boag’s October 17, 2025 account verifies the author’s UX connection and describes using AI across client research, design, and content work.[cite:424] It also describes Projects in both ChatGPT and Claude, populated with existing research and business context.[cite:424]

The attribution problem is material: spreadsheet work and a detailed copywriting sequence are explicitly assigned to ChatGPT, while other research passages discuss AI generally.[cite:424] Neither those outputs nor the article’s overall productivity claims can responsibly be reassigned to Claude.

The account includes instructions, illustrations, and checking practices, but does not connect a specific, inspectable Claude session to a specific research decision.[cite:424] It therefore supplies a useful lead about reusable context—not a qualifying Claude research-analysis case.

**Critical boundary:** the article also discusses generated personas and simulated advisers.[cite:424] Such representations do not become evidence about real users merely because research documents were included in the project; claim-level grounding would still need to be demonstrated.

### Working continuity: Ryan Rumsey

Rumsey describes maintaining paired Claude and v0 projects, with Claude providing development guidance and v0 handling implementation.[cite:405] At stable milestones, project instructions request a README and priorities for the next conversation; the practitioner also saves the previous conversation and supplies it to a fresh chat.[cite:405]

That is a concrete conversational use, but the accessible post does not expose the resulting handoff files or complete chat logs.[cite:405] It cannot establish whether the handoff preserved decisions accurately or whether a later session introduced errors.

Rumsey’s separate design-leadership work is better supported by a detailed account of converting existing teaching material into a reusable communication skill and linking a repository.[cite:407] However, that account explicitly uses Cowork, so it is not counted toward the conversational-only comparison.[cite:407]

**What can be learned:** context handoffs are a distinct task worth examining. **What remains unestablished:** whether generated handoffs are more reliable than a concise practitioner-written decision log.

### Follow-up operations: Femke van Schoonhoven

Van Schoonhoven’s firsthand post and accompanying video transcript describe a specific chain: Granola captures a mentoring call; Claude retrieves a quotation through the connector; the conversation then supports a testimonial draft and an approval-email draft.[cite:459]

Granola performed capture and transcription—not Claude.[cite:459] The practitioner reports that the speaker approved the quotation before publication, providing a meaningful human review point for this particular use.[cite:459]

The public material establishes a real follow-up activity more clearly than a UX research workflow. It concerns a course testimonial, not research synthesis or an interface decision, and the narrated transcript does not establish a complete recorded execution of every integration.[cite:459]

**What can be learned:** extracting an identifiable passage and routing it for approval creates a more inspectable task than asking for an unconstrained summary. Approval for testimonial publication does not, however, establish consent for research-data processing.

## Cross-case findings

### Representation versus evidence

The accounts illustrate two different jobs: **representing possibilities** and **organizing existing material**. Brennan’s prototypes belong to the former; Levitt’s transcript work and van Schoonhoven’s quotation retrieval belong to the latter.[cite:443][cite:349][cite:459]

Those jobs need different evaluation. A prototype should be judged against the intended interaction question; a quotation or research interpretation should be checked against its source. Neither a functioning prototype nor a coherent summary establishes that a product decision is sound.

### Recurring practices, limited prevalence

Reusable context appears independently in Boag’s Projects account and Rumsey’s conversation-handoff method.[cite:424][cite:405] Source checking appears in Levitt’s research account and Boag’s broader AI practice, while van Schoonhoven describes approval by the quoted speaker.[cite:349][cite:424][cite:459]

These are recurring practices **within this small, heterogeneous set**. The evidence does not establish that they are widespread among UX professionals, nor that the implementations are equivalent.

### Traceability remains incomplete

The accounts describe useful checking intentions, but do not expose a complete research chain from participant passage through code, theme, contradiction, recommendation, and product decision.[cite:349][cite:424] Participant-level identifiers, source locations, negative cases, and revisions would be needed to inspect that chain.

Retrieving a quotation is narrower than validating a theme. Even a verbatim quotation can be misleading if its surrounding context, contradictory statements, or the researcher’s selection process are missing.

### Checking costs are unmeasured

Brennan documents repeated iteration and visual-refinement frustration; Boag describes continued checking and challenging of AI output.[cite:443][cite:424] Neither supplies a Claude-specific, task-level measurement that includes preparation, prompting, correction, and review.

Accordingly, this review cannot calculate net time savings. Faster generation and faster completion are different claims.

### Expertise remains a prerequisite

Brennan’s account depends on being able to articulate interaction patterns and judge alternatives, while Levitt’s checking depends partly on knowledge of the research sessions.[cite:443][cite:349] These are not workflows in which an inexperienced operator can accept the output simply because it is well presented.

The documented boundary is not “Claude does the thinking.” It is that a practitioner can delegate parts of representation or organization while retaining the knowledge needed to reject the result.

## Practical adoption implications

The following are **recommendations derived from the accounts**, not additional observed cases or validated methods.

### Explore one interaction

**Suitable for:** product and interaction designers who already understand the task and constraints.

**Required inputs:** the intended task, known requirements, relevant states, and a specific uncertainty—for example, whether an interruption should preserve or discard a draft.

**Boundary:** request a rough representation of alternatives, not a production interface or a declaration of usability. Brennan’s experience supports keeping the work low fidelity rather than spending the exploration budget on visual matching.[cite:443]

**Inspection:** walk through the interaction manually; check transitions, recovery, persistence, keyboard behavior, and whether the artifact actually represents the intended question.

**Stop or reject when:** the generated structure changes the problem, hides missing states behind polish, or needs repeated repair before it can support a useful discussion.

**Reasons not to use it:** the team may mistake a working demonstration for validated behavior, or the proposed output may now route through excluded Claude Design functionality.

### Extract before interpreting

**Suitable for:** researchers who conducted or closely reviewed the sessions and have permission to process the material.

**Required inputs:** a minimized transcript set, stable participant identifiers, source locations, and a narrow extraction question.

**Boundary:** retrieve candidate evidence before asking for themes or recommendations. Levitt’s account supports the value of retaining session knowledge for checking, but does not establish a fully auditable extraction procedure.[cite:349]

**Inspection:** compare every retained quotation with its source; inspect surrounding context; deliberately search for contradictory passages and cases that do not fit.

**Stop or reject when:** quotations cannot be located, wording changes, speakers are merged, absence is interpreted as disagreement, or a theme lacks supporting passages.

**Reasons not to use it:** sensitive data, unavailable source records, or review costs that exceed the benefit. This is a controlled starting experiment, not a demonstrated replacement for analysis.

### Preserve a decision handoff

**Suitable for:** practitioners whose work spans several conversations and who can maintain a separate authoritative record.

**Required inputs:** decisions, constraints, rejected options, unresolved questions, and links to authoritative sources.

**Boundary:** ask for a draft handoff, not automatic memory. Rumsey’s account supplies a concrete example of moving README and conversation context into a new chat, but not an accuracy evaluation.[cite:405]

**Inspection:** compare the handoff with the decision record; correct lost qualifications and distinguish decisions from suggestions.

**Stop or reject when:** an unresolved possibility becomes a settled decision, provenance disappears, or old context is presented as current.

**Reasons not to use it:** a short human-written log may be clearer, safer, and cheaper to maintain.

## Privacy and research integrity

### Documented safeguards

Levitt’s recording announcement identifies anonymized transcripts, and the interview describes checking against notes and session knowledge.[cite:353][cite:349] Van Schoonhoven reports approval before testimonial publication.[cite:459]

These are bounded safeguards. Neither account establishes the full consent language, organizational authorization, contractual controls, retention configuration, or de-identification assessment.

### Recommended safeguards

Before uploading participant or organizational material:

- Confirm that the research agreement, participant consent, organizational policy, and applicable contract permit the proposed processing.
- Use only the material required for the task.
- Remove identifiers and assess whether combinations of contextual details could still identify someone.
- Keep an authoritative source copy outside the generated output.
- Record which product surface and workspace received the material.
- Separate permission to record, permission to process with an external service, and permission to publish.
- Require approval before externally sharing quotations or generated deliverables.

These are recommendations, not safeguards demonstrated across the reviewed cases.

### Product-specific limits

Current official documentation says Cowork tasks run on Anthropic’s servers and that sessions and files are saved with the Claude account.[cite:467] Consequently, access to local files must not be described as proof of local-only processing.

Official documentation also describes plan-dependent artifact-sharing controls.[cite:489] A shareable artifact is therefore an additional disclosure surface, not merely another way to view a private draft.

**Training use, retention periods, deletion behavior, and contractual processing terms were not sufficiently verified for this report.** No assurance about those matters should be inferred from the feature documentation cited here; they remain a pre-adoption verification requirement.

### Research integrity

Generated personas, imagined participants, and simulated advisers must remain labeled representations or speculation—not participant evidence. Boag’s account demonstrates why the distinction matters: the same broad workflow discussion includes both research-grounded material and simulated advisory perspectives.[cite:424]

For transcript work, the recommended acceptance test is source recoverability: can another researcher locate the passage, inspect its context, and understand how the interpretation was reached?

For interface work, generated critique should be treated as a list of hypotheses to examine. It does not establish usability, accessibility compliance, or suitability for a particular population.

## What remains unestablished

### Five qualifying practitioners

Five independent practitioners supplied relevant firsthand material, but **five artifact-backed, in-scope UX workflows were not established**. The unresolved issues are different: incomplete recording access, mixed-tool attribution, absent inspectable handoff files, an excluded agentic surface, and an adjacent rather than core UX task.[cite:353][cite:424][cite:405][cite:407][cite:459]

### Research quality improvements

The reviewed sources do not provide an inspectable comparison showing that Claude-assisted analysis preserves minority viewpoints, finds more consequential contradictions, or improves recommendations relative to an appropriate human baseline.[cite:349][cite:424]

### User and product outcomes

Brennan reports workflow benefits, but the accessed account does not connect a specific conversational prototype to measured user or product outcomes.[cite:443] Van Schoonhoven’s reported publication outcome is concrete, but is not evidence of improved UX research or design.[cite:459]

### Reproducibility

Missing prompts, model versions, complete inputs, output histories, and rejection records limit reproduction of the accounts.[cite:443][cite:349][cite:405] Historical methods also cannot be assumed to reproduce unchanged when current product surfaces have incorporated new Design and agentic functionality.[cite:494][cite:467]

### Selection and commercial influence

Several accounts are connected to educational products, workshops, or promotional offers.[cite:354][cite:407][cite:459] That does not invalidate the firsthand evidence, but it increases the importance of inspecting artifacts rather than relying on favorable outcome language.

### Failures and net effort

The public accounts include some frustrations, but not systematic failure logs or complete measurements of preparation and correction effort.[cite:443][cite:424][cite:405] The available evidence therefore supports **bounded experimentation**, not a general claim that conversational Claude makes UX work faster or better.

## Publication readiness

This material is suitable as an **evidence-constrained research memo**, not yet as the requested five-practitioner case-study feature.

Before expanding it into that feature, the remaining evidence should include:

- The actual Levitt recording, with identifiable examples of checking and correction.
- At least four additional independent, in-scope workflows with inspectable inputs and outputs or recorded execution.
- Explicit Claude attribution wherever several assistants are involved.
- A visible distinction between professional work, experiments, and teaching demonstrations.
- Claim-level source traceability for any research-analysis case.
- Outcome language limited to what was actually observed or measured.

The defensible editorial position is not that Claude has demonstrated a general transformation of UX practice. It is that practitioners have documented specific uses worth investigating—and that the strongest next step is to inspect the work closely enough to distinguish useful assistance from persuasive output.

[cite:443]: https://uxdesign.cc/how-to-become-an-ai-designer-ff8ee8aed205
[cite:349]: https://blog.uxtweak.com/ai-in-uxr-in-2025-expert-answers/
[cite:424]: https://www.smashingmagazine.com/2025/10/ai-ux-achieve-more-with-less/
[cite:405]: https://www.linkedin.com/posts/ryanrumsey_ive-been-building-small-web-apps-for-myself-activity-7353540242420686848-5lJD
[cite:459]: https://www.linkedin.com/posts/femkesvs_a-designer-i-was-mentoring-recently-told-activity-7460732702791483393-Y1pV
[cite:494]: https://support.claude.com/fr/articles/14604416-commencer-avec-claude-design
[cite:496]: https://support.claude.com/en/articles/14604406-claude-design-admin-guide-for-team-and-enterprise-plans
[cite:484]: https://www.anthropic.com/news/projects
[cite:467]: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
[cite:468]: https://claude.com/resources/guides/deploying-claude-across-your-organization/introducing-claude-cowork
[cite:353]: https://maven.com/deltacx/o/31bacf
[cite:407]: https://thecdo.school/articles/i-made-claude-skill-to-help-you-read-the-room/
[cite:489]: https://claude.com/features/artifacts
[cite:354]: https://maven.com/deltacx/ai-research-pmf
