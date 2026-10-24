# Claude Design in UX practice

**Evidence-led research report · Research cutoff: October 23, 2026**

*Export of the report prepared for UX Design Engineer. This download preserves the report's findings and limitations; it is not a new research pass. Source citations are linked so they remain usable outside the conversation.*

## Executive summary

**The evidence reviewed does not support six to ten substantive, independently auditable professional case studies.** It establishes a named product designer's commercial-team use through a vendor-hosted testimonial, an agency's announcement of professional adoption, and a much more detailed practitioner demonstration—but these offer very different levels of evidence. [Anthropic, April 17, 2026](https://www.anthropic.com/news/claude-design-anthropic-labs)[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

The clearest documented workflow is **requirements clarification → alternative onboarding wireflows → practitioner selection → interactive prototype → transfer to Claude Code**. However, that example is published as an instructional walkthrough, not an independently documented client engagement or evaluated product release.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)[cite:357](https://www.youtube.com/watch?v=xwzXSegBJbo)

The strongest professional-use lead is **turning existing static designs into prototypes of complex interactions**, followed by a reported handoff to implementation. Its public documentation does not expose the prototype, prompts, revision history, implementation changes, or user evaluation. [Anthropic, April 17, 2026](https://www.anthropic.com/news/claude-design-anthropic-labs)

The defensible finding is therefore narrower than an adoption narrative: **Claude Design is being reported as a prototyping and communication tool, but the reviewed evidence is considerably better at establishing artifact creation than improved UX outcomes.** None of the retained accounts establishes a measured improvement in task success, comprehension, accessibility, error recovery, or another user outcome. [Anthropic, April 17, 2026](https://www.anthropic.com/news/claude-design-anthropic-labs)[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

## Product and research scope

### Product identity

The official product name is **Claude Design**, introduced by **Anthropic Labs on April 17, 2026**. The launch announcement describes a visual-work product supporting designs, prototypes, presentations, and other artifacts—not simply a name for any design work performed with Claude. [Anthropic launch announcement](https://www.anthropic.com/news/claude-design-anthropic-labs)

At launch, it was a **research preview for Claude Pro, Max, Team, and Enterprise subscribers**, with a gradual rollout; Enterprise administrators had to enable it. The announcement also documented a separate handoff from Claude Design to Claude Code. [Anthropic launch announcement](https://www.anthropic.com/news/claude-design-anthropic-labs)

**Availability limitation:** those launch facts are verified, but this review did not establish a complete authoritative release chronology through October 23. It should not be read as confirmation that the April preview status, model, access arrangements, or interface remained unchanged in October.

### Attribution boundaries

For this report, the following were treated as separate attribution categories:

| Category | Inclusion rule |
|---|---|
| Claude Design | Requires explicit identification of the product in the practitioner account or execution record |
| Claude chat | A conversation producing design advice or code does not establish Claude Design use |
| Claude Artifacts | A shared interactive artifact does not, by itself, identify the authoring product |
| Claude Code | Coding, local implementation, or a repository contribution does not establish prior Claude Design involvement |
| Claude API | A custom application using Claude models does not establish use of Claude Design |
| Other design tools | Their contribution must remain separately attributed |

These are **research rules**, not claims that the tools cannot overlap. In particular, the launch announcement explicitly separates Claude Design's design work from a subsequent Claude Code handoff. [Anthropic launch announcement](https://www.anthropic.com/news/claude-design-anthropic-labs)

### Inclusion and verification

The review prioritized identifiable UX practitioners or design teams, explicit product attribution, a recoverable workflow, and evidence of subsequent use. Multiple publications about the same project were treated as one account.

“Verified” here means **publicly attributable**, not independently replicated. A named testimonial can establish that a designer publicly reported using the product; it cannot independently establish the effectiveness of that use.

The requested professional-case target was not met. Rather than reconstruct missing steps or substitute other Claude products, the report retains **two bounded professional-use accounts** and separates **one detailed demonstration**.

## Evidence map

The labels below describe support for the account—not proof that the design was effective.

- **Strong:** substantive firsthand account plus an inspectable artifact or recorded execution.
- **Moderate:** substantive firsthand account with limited supporting artifacts.
- **Limited:** confirmed attribution but insufficient detail to assess the workflow or result.

| Practitioner or team | UX activity | Claude Design contribution | Work classification |
|---|---|---|---|
| **Olivia Xu, Brilliant** | Prototyping intricate interactions and animations | Reportedly converted static designs into interactive prototypes; supplied design intent for a Claude Code handoff. [Primary source](https://www.anthropic.com/news/claude-design-anthropic-labs) | Professional team use, documented through a vendor-selected launch testimonial |
| **Webdorks** | Early website/MVP exploration and stakeholder review | Agency reports using prototypes to discuss structures, selected interactions, journeys, and requirements.[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/) | Professional adoption announcement; agency-authored newswire material |
| **Elizabeth Alli, DesignerUp** | Onboarding alternatives, wireflows, interactive prototyping, implementation preparation | Generated alternatives, supported clarification and revision, produced a prototype, and supplied a handoff to Claude Code.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/) | Instructional demonstration using a self-described real project; commercial project status not established |

| Account | Available artifact | Outcome supported | Strength and primary evidence |
|---|---|---|---|
| **Brilliant** | No project-specific prototype, source files, or execution record supplied in the testimonial | Named practitioner reports useful prototyping and implementation handoff; performance claims remain unverified. [Source](https://www.anthropic.com/news/claude-design-anthropic-labs) | **Limited** |
| **Webdorks** | No project-specific artifact identified in the retrieved release | Agency reports adoption since May 2026; no completed-project or user-outcome evidence established.[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/) | **Limited** |
| **DesignerUp** | Public video and illustrated firsthand article; no independently assessed production repository.[cite:357](https://www.youtube.com/watch?v=xwzXSegBJbo)[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/) | A documented prototype-to-Claude-Code demonstration; no user evaluation or shipped-product outcome established.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/) | **Strong for the demonstration**, not for professional effectiveness |

## Detailed cases

### Complex interaction prototyping

**Practitioner and context.** Anthropic's April 17 launch announcement identifies **Olivia Xu as Senior Product Designer at Brilliant** and attributes a firsthand account to Xu. This establishes the UX connection and explicit Claude Design attribution, but the vendor selected and published the account; the underlying work dates are not disclosed. [Primary source](https://www.anthropic.com/news/claude-design-anthropic-labs)

**UX problem.** The account concerns the difficulty of prototyping Brilliant's intricate interactivity and animations. It does not identify a particular learner problem, task, lesson, or design decision. [Primary source](https://www.anthropic.com/news/claude-design-anthropic-labs)

**Actual workflow**

| Stage | What the source establishes |
|---|---|
| Inputs | Existing static designs; their format and accompanying requirements are unspecified |
| Claude Design actions | Conversion into interactive prototypes; the designer reports that complex pages required two prompts |
| Artifact | Interactive prototypes are reported, but not exposed for inspection |
| Human evaluation | A senior designer endorses the result; specific critique, acceptance criteria, and revisions are not described |
| Subsequent use | A Claude Code handoff incorporating design intent is reported; the resulting implementation is not inspectable |

All stages above come from the named launch testimonial, not from a published project log. [Primary source](https://www.anthropic.com/news/claude-design-anthropic-labs)

**Tool contribution.** Claude Design is explicitly credited with prototype generation. Claude Code is separately associated with the subsequent implementation handoff; the source does not justify attributing production engineering to Claude Design itself. [Primary source](https://www.anthropic.com/news/claude-design-anthropic-labs)

**Outcome.** Xu reports two prompts for pages that required more than twenty prompts in other tools, and describes the prototype-to-production transition positively. The comparator tools, equivalent task conditions, elapsed time, correction effort, and measurement method are not supplied; this is an **unverified practitioner comparison**, not a controlled productivity result. [Primary source](https://www.anthropic.com/news/claude-design-anthropic-labs)

**Limitations.** The public account does not establish usability testing, accessibility evaluation, production acceptance, or measured learner benefit. It also does not show whether fewer prompts reduced total work or merely shifted work into preparation and review. [Primary source](https://www.anthropic.com/news/claude-design-anthropic-labs)

**Transferable lesson—interpretation.** Existing static designs may be a useful starting point when the uncertainty concerns behavior rather than appearance. A practitioner borrowing this approach would still need to specify timing, interaction rules, invalid states, and acceptance criteria—and inspect the resulting behavior rather than judge screenshot fidelity.

### Stakeholder review before development

**Practitioner and context.** A Webdorks newswire announcement, dated **June 3, 2026 in its body**, identifies the organization as a web design and development agency and states that it had used Claude Design in selected website and MVP projects since May. This verifies the agency's public claim, not the completion or quality of individual engagements.[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)

**UX problem.** The stated purpose is to make concepts and user journeys tangible enough for stakeholders to refine requirements before full UI/UX design and development.[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)

**Actual workflow**

| Stage | What the source establishes |
|---|---|
| Inputs | Project ideas and requirements are discussed, but actual briefs and uploaded materials are not disclosed |
| Claude Design actions | Initial prototyping within selected engagements |
| Artifact | Selected screens, structures, feature concepts, interactions, or journeys may be represented; no particular deliverable is identified |
| Human evaluation | Stakeholder discussion is described as the intended use |
| Subsequent use | The process is positioned before fuller design and development; no specific transition is documented |

This is a **process description**, not a recoverable execution trace for a named project.[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)

**Tool contribution.** Claude Design is explicitly placed in the initial prototyping phase. The announcement does not expose which activities remain in other design tools, how prototypes are revised, or whether generated code is retained.[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)

**Outcome.** The announcement describes clearer discussion and earlier requirements refinement as benefits of the approach, but supplies no decision log, client example, comparison, or measured result.[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)

**Limitations.** No individual designer, project artifact, research protocol, or implementation record is available in the retrieved release. It therefore cannot support a substantive case study of how a professional UX decision actually changed.[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)

**Transferable lesson—interpretation.** A prototype can be used as a discussion object before development commitment. That is a plausible starting workflow, but this announcement does not establish whether it improved decisions, reduced rework, or simply made meetings more visual.

### Onboarding exploration demonstration

**Practitioner and context.** **Elizabeth Alli**, a designer and mentor publishing through DesignerUp, documented the workflow in an **April 21, 2026 video** and **April 22 article**. Alli calls it a real UX/UI project, but the public material is instructional; no client, paid engagement, or deployed product is established.[cite:357](https://www.youtube.com/watch?v=xwzXSegBJbo)[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

**UX problem.** The project combines a curated news feed with a private journal, encouraging users to formulate a position on topics. The demonstrated task centers on onboarding, including topic interests, a short introduction, and the relationship between the feed and journaling.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

**Actual workflow**

| Stage | Documented sequence |
|---|---|
| Inputs | Existing project assets and code-related files; a description of the app, onboarding requirements, and requested alternative directions |
| Clarification | Claude Design asks questions; Alli supplies decisions about privacy, interests, onboarding length, and the desired experience |
| Alternatives | Three onboarding wireframe directions: editorial, gallery, and notebook |
| Human selection | Alli reviews the alternatives and favors the editorial direction |
| Prototype | The earlier wireframes are referenced in a high-fidelity project, producing a mobile-app prototype |
| Subsequent use | Alli copies a Claude Code handoff instruction, downloads a ZIP, and transfers the work into Claude Code |

The article documents these steps, and the accompanying recording provides an execution record; this report does not claim independent hands-on replication.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)[cite:357](https://www.youtube.com/watch?v=xwzXSegBJbo)

**Tool contribution.** Claude Design performs clarification, alternative generation, wireflow/prototype creation, and handoff preparation. Alli controls the problem framing, answers, requested alternatives, selection, and review; Claude Code handles the subsequent implementation stage.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

**Human evaluation.** The documented review is the designer's own inspection and preference. The material does not establish participant testing, a formal critique, or evidence that users understood the proposed onboarding.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

**Outcome.** The walkthrough supports the creation of a prototype and its transfer into a Claude Code workspace. Although the article describes the result as implemented, it also identifies journal-entry work as a future flow; the evidence should not be stretched into a complete, tested application.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

**Limitations.** No public production repository, deployment evaluation, user-study results, or measured time comparison is established. The author's favorable assessment of the interface remains a practitioner judgment, not evidence of usability.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

**Transferable lesson—interpretation.** The borrowable pattern is **clarify requirements before generating alternatives, then select a direction before increasing fidelity**. Its value depends on whether the alternatives differ in task structure and interaction—not merely visual treatment.

### Leads not promoted

Several attractive-looking leads were deliberately not used to increase the professional-case count:

| Lead | Reason for exclusion or reservation |
|---|---|
| **Tra Nguyen's family-storytelling portfolio project** | The account explicitly names Claude Design and describes research-led interaction exploration, but the retrieved page does not establish publication/work dates, commercial context, or an inspectable execution record. It remains a promising follow-up lead, not a verified professional case here. [Original account](https://www.tra-nguyen.com/cnt) |
| **Vezert agency field notes** | The account reports real briefs, but does not expose project-level artifacts or measurements supporting its substantial speed claims. Its stated component-reuse figure invokes unrelated coding-tool research, which cannot validate Claude Design performance.[cite:374](https://vezert.com/blog/claude-design-web-agency) |
| **Enso Labs' own website** | The account explicitly separates Claude chat, Claude Design, and Claude Code, but the named practitioner's stated role is AI transformation advisor rather than an established UX role; it also centers on the studio's own site. [Original account](https://ensolabs.ai/built-with-ai) |
| **Anthropic's internal design/research workflows** | The broader case material includes generic Claude use and a precursor to Claude Design. Those accounts cannot automatically be counted as use of the released product. [Original case](https://stateofaidesign.com/cases/anthropic) |

## Cross-case findings

### Outcomes versus implementation

| Outcome level | Brilliant | Webdorks | DesignerUp |
|---|---|---|---|
| Artifact generated | Practitioner-reported | General agency adoption claim | Documented demonstration |
| Practitioner found it useful | Explicit endorsement | Agency endorsement | Explicit author assessment |
| Supported a design decision | Not documented | Intended use; no decision trace | Designer selects a direction |
| Evaluated with users | Not established | Not established | Not established |
| Entered implementation | Reported handoff; implementation not inspectable | Not established | Transfer into Claude Code demonstrated/described |
| Measured user improvement | Not established | Not established | Not established |

The distinctions above follow the available accounts; “not established” means **not supported by the reviewed documentation**, not that the activity never happened. [Brilliant source](https://www.anthropic.com/news/claude-design-anthropic-labs)[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

### Recurring and isolated patterns

**Prototyping is the recurring activity.** Brilliant reports converting existing designs into interactive behavior, Webdorks describes early project prototypes, and DesignerUp documents onboarding exploration and prototype generation. The evidence does not establish how prevalent these practices are across the profession. [Brilliant source](https://www.anthropic.com/news/claude-design-anthropic-labs)[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

**Implementation remains a separate evidentiary step.** Brilliant reports a Claude Code handoff, while DesignerUp documents a transfer; neither supports treating the generated prototype itself as proof of a production-ready experience. [Brilliant source](https://www.anthropic.com/news/claude-design-anthropic-labs)[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

**Decision-making evidence is thinner than generation evidence.** DesignerUp exposes an individual designer's selection; Webdorks describes stakeholder decision support without showing a decision; Brilliant's testimonial does not disclose which design question the prototype resolved.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)[Brilliant source](https://www.anthropic.com/news/claude-design-anthropic-labs)

### Control, revision, and rework

The most detailed account keeps the practitioner involved through requirements answers, alternative selection, and inspection before handoff. However, it does not provide a longitudinal revision history showing how the prototype behaves after repeated changes.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

Consequently, **net time savings remain unresolved**. The accounts do not measure combined preparation, generation, review, correction, regression checking, and implementation work; fewer prompts or a faster first draft cannot settle that question. [Brilliant source](https://www.anthropic.com/news/claude-design-anthropic-labs)[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

## Practical implications

The following are **recommendations derived from the bounded evidence**, not additional observed cases.

| Starting workflow | Suits | Required inputs | Review criteria | Risks and reasons not to use |
|---|---|---|---|---|
| **Static design → behavior prototype** | Interaction designers exploring an already-defined flow | Authorized mockups, behavior rules, realistic states, a specific question | State transitions, timing, keyboard behavior, errors, recovery | Avoid when the problem is unresolved or when visual similarity could conceal invented behavior |
| **Requirements → alternative wireflows** | Product designers comparing onboarding or task structures | User goal, constraints, content, known research findings, meaningful alternatives | Task sequence, assumptions, cognitive load, terminology, unnecessary steps | Avoid treating stylistic variations as alternative solutions or designer preference as validation |
| **Prototype → implementation discussion** | Designers and engineers reviewing a selected direction | Reviewed prototype, behavior notes, unresolved questions, acceptance criteria | Differences between prototype behavior and production requirements | Avoid assuming that successful transfer means integration, security, accessibility, or maintainability are solved |

The first recommendation follows the Brilliant account; the second follows the DesignerUp demonstration; the third reflects the handoff activity described in both. [Brilliant source](https://www.anthropic.com/news/claude-design-anthropic-labs)[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

For a useful local experiment, record five things separately: **preparation time, generation time, review time, correction time, and implementation effort**. Also record the design decision supported. This would produce more meaningful evidence than prompt counts alone.

## Privacy and research integrity

### Documented safeguards

The launch announcement documents private documents and organization-scoped sharing options. These are product capabilities—not evidence that a particular case used appropriate access controls, obtained permission for uploaded materials, or protected research participants. [Anthropic launch announcement](https://www.anthropic.com/news/claude-design-anthropic-labs)

The retained accounts do not document participant consent, customer-data handling, upload authorization, retention decisions, or confidentiality review. The review also did not verify the current contractual, retention, or model-training arrangements applicable to each account type. [Brilliant source](https://www.anthropic.com/news/claude-design-anthropic-labs)[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

### Recommended safeguards

Before adopting any workflow:

- **Confirm organizational permission:** check approved products, account arrangements, contracts, and restrictions before uploading work.
- **Minimize data:** use synthetic task data rather than participant identities, transcripts, support records, or customer information.
- **Sanitize screens:** inspect screenshots for names, account details, internal URLs, confidential metrics, and distinctive product information.
- **Check material rights:** permission to view a file does not necessarily authorize uploading it to another service.
- **Separate generated content from findings:** fabricated examples, personas, or feedback must never enter a research record as participant evidence.
- **Control prototype access:** inspect sharing settings and exported files before distribution.
- **Disclose prototype limitations:** tell participants which interactions and data are simulated.
- **Preserve traceability:** retain the source requirement, generated version, human changes, evaluation findings, and decision rationale.

These are recommended controls; they should not be attributed to the practitioners without further evidence.

## What remains unestablished

### Coverage gaps

| UX activity | What this review establishes |
|---|---|
| Alternative solution exploration | A detailed onboarding demonstration, but no independently evaluated professional comparison.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/) |
| Multi-step interactions | An onboarding wireflow demonstration and a professional claim about complex interactivity.[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)[Brilliant source](https://www.anthropic.com/news/claude-design-anthropic-labs) |
| Preparing usability tests | Prototyping capability and intended feedback use, but no retained professional test protocol or results. [Anthropic source](https://www.anthropic.com/news/claude-design-anthropic-labs) |
| Research-driven revision | No retained professional case with a traceable finding → design change → reevaluation sequence |
| Information architecture | Agency process claims, but no retained project showing an evaluated navigation decision.[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/) |
| Content design | No retained professional case showing interface-language alternatives and comprehension evidence |
| Errors and recovery | No retained professional case exposing systematic state coverage |
| Accessibility | No retained professional case establishing an accessibility audit or disabled-participant evaluation |
| Improving an existing experience | No retained professional before/after evaluation |
| Production outcomes | Reported or demonstrated handoff activity, but no measured user improvement attributable to Claude Design |

The empty areas are **findings about this review's evidence**, not assertions that practitioners are not doing the work.

### Reporting and selection bias

The professional evidence includes vendor-selected testimony and an agency announcement; the most detailed independent practitioner material is instructional. These formats make successful generation visible but offer little access to abandoned directions, integration failures, sustained maintenance, or unfavorable results. [Brilliant source](https://www.anthropic.com/news/claude-design-anthropic-labs)[cite:349](https://thebruneian.news/2026/06/03/webdorks-launches-claude-design-assisted-prototyping-for-website-and-mvp-development/)[cite:361](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/)

The report therefore cannot establish prevalence, comparative effectiveness, total productivity improvement, or replacement of existing UX methods. It also cannot establish that the public evidence available elsewhere is exhausted.

### Publication quality check

| Requirement | Assessment |
|---|---|
| Explicit Claude Design involvement | Established for retained accounts |
| Verified UX connection | Named product designer at Brilliant; self-described design agency; identified designer/educator for the demonstration |
| No design-system-centered main case | Met |
| Professional work separated from demonstrations | Met |
| Visual polish separated from UX quality | Met |
| Reported benefits separated from measured outcomes | Met |
| Recommendations distinguished from observations | Met |
| Six to ten substantive professional cases | **Not met; not padded** |
| Current authoritative release chronology | **Incomplete beyond launch** |

**Editorial next step:** publish this, if useful, as an **evidence-gap report**, not a mature-adoption survey. A stronger professional feature requires project-level originals showing the brief, Claude Design execution, human revisions, the decision supported, and what happened during testing or implementation.
