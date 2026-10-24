# Claude Code in UX practice

## Evidence beyond design systems

**Research date: October 23, 2026**  
**Requested coverage: 2023–2026; retained cases: 2025–2026**  
**Editorial context: UX Design Engineer**

> **Export note:** This document contains the full report previously presented in the conversation, not a shortened summary. Source references have been made into clickable links for use outside the conversation. This export is not an additional round of research or independent validation. Where the earlier report relied on a recording transcript or practitioner account, that inspection boundary still applies. Publication dates are reproduced as reported; date discrepancies are noted where visible in the research record.

## Executive summary

UX professionals are demonstrably using Claude Code to develop and critique working interactions, make changes in existing repositories, build personally owned products, and process research materials through file-based analysis workflows. The clearest public evidence concerns **how work is performed**, not whether it produces better UX outcomes or sustained productivity gains. [Research account](https://aicustomerresearch.substack.com/p/october25) · [Shopify walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Repository-based design demonstration](https://www.youtube.com/watch?v=hKeDfupbA4U)

Seven practitioner cases meet the report’s inclusion threshold. The most informative include a recorded Shopify prototyping session, an Anthropic designer’s demonstration of repository-based design work, a researcher’s documented parallel-analysis workflow, and an interaction-design experiment supported by a public repository. [Shopify walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Anthropic designer presentation](https://www.youtube.com/watch?v=hKeDfupbA4U) · [Research account](https://aicustomerresearch.substack.com/p/october25) · [Interaction-design project](https://thoughtwax.com/2025/07/2027-race-to-agi/)

Three findings deserve particular attention:

- **Working software becomes a material for design judgment.** Practitioners inspect behavior, discover incomplete interactions, and revise the implementation—not merely generate an initial interface. [Shopify walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Epilogue account](https://permissionless.krispuckett.com/)
- **Research workflows extend beyond chat-based summarization.** Claude Code reads organized source files, runs separate analysis tasks, and writes persistent outputs; however, the retained evidence does not independently validate the resulting interpretations. [Research account](https://aicustomerresearch.substack.com/p/october25) · [Research lesson](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do)
- **Automation introduces additional review obligations.** Documented problems include nonfunctional controls, conflicting parallel changes, difficult debugging, and an automated design-review workflow whose outward notifications were disabled after poor results. [Shopify walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Epilogue account](https://permissionless.krispuckett.com/) · [Anthropic designer presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

The largest gaps concern dedicated information architecture, content operations, accessibility remediation, and prototypes evaluated through documented usability studies. No retained case establishes a complete chain from participant testing through revision to measured improvement. This is a limitation of the evidence collected—not proof that these practices are absent.

## Research method

### Inclusion and verification

A case was retained only when public evidence established a UX-related practitioner role, explicitly named **Claude Code**, and described completed work rather than proposed applications. Design-system construction, generic capability demonstrations, and repositories containing instructions without evidence of use were excluded.

The report prioritizes firsthand posts and accounts, recorded practitioner explanations, and publicly inspectable artifacts. Source dates below are publication dates unless stated otherwise; an account’s publication date should not be mistaken for the date every described activity occurred.

**Inspection boundary:** Public pages, repository documentation, and available recording transcripts were examined. Applications were not installed or tested; private repositories, participant data, internal tools, and complete session histories were not accessed. A recording transcript establishes what was described or demonstrated in that recording, not an independent replication.

### Evidence-strength labels

- **Strong:** Detailed firsthand workflow plus an inspectable artifact or recorded execution.
- **Moderate:** Explicit, substantive firsthand account, but limited supporting artifacts or evaluation.
- **Limited:** Confirmed use with insufficient detail to assess the workflow or result.

These labels describe support for the account—not proof of effectiveness. A strong demonstration can still have no usability evaluation.

### Technical terms

Claude Code is an agentic tool that can read project files, edit them, execute commands, and operate through development environments; it is distinct from an ordinary Claude chat conversation. [Claude Code overview](https://code.claude.com/docs/en/overview)

A **repository** is a version-controlled project folder. A **pull request**, or PR, proposes changes for review. A **worktree** provides an isolated working copy so parallel tasks do not overwrite one another; that distinction matters in the recorded Anthropic workflow. [Anthropic designer presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

A **subagent** handles a delegated task with separate working context. In the research case below, subagents perform different analyses rather than independently establish that an interpretation is correct. [Research account](https://aicustomerresearch.substack.com/p/october25)

## Evidence map

| Practitioner or team | UX activity | Claude Code’s role | Work context and maturity | Available artifact | Reported or demonstrated outcome | Evidence strength | Primary source |
|---|---|---|---|---|---|---|---|
| **Caitlin Sullivan** | Research analysis and evidence documentation | Parallel analysis of surveys, calls, and bias; later demonstration of segment analysis | Self-reported working practice, plus a synthetic-data teaching demonstration. [Account](https://aicustomerresearch.substack.com/p/october25) · [Lesson](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do) | Detailed post, screenshots/video links, and a recording page with timestamped chapters; no underlying real dataset inspected. [Account](https://aicustomerresearch.substack.com/p/october25) · [Lesson](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do) | Persistent analysis outputs; substantial time reduction claimed, not independently validated. [Account](https://aicustomerresearch.substack.com/p/october25) | **Moderate** | [October 2025 account](https://aicustomerresearch.substack.com/p/october25); [February 2026 lesson](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do) |
| **Kazden Cattapan, Shopify** | Interaction exploration and functional prototyping | Builds and revises a merchant content-generation flow, including storage and model integration | Recorded exploration within an established internal prototyping environment; not evidence that this feature shipped. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg) | Hour-long recording and transcript; internal project not publicly available. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg) | Working upload behavior and successive interaction revisions; defects remain visible during the session. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg) | **Strong** | [March 2026 walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg) |
| **Michael Angeles** | Sketch-led structural exploration | Converts photographed sketches into browser-rendered HTML/CSS | Personal workflow experiment, discussed in relation to own products and client conversations. [Account](https://konigi.com/articles/sketch2claude/) | Public sketch-paper downloads and linked demonstration; generated implementation not independently audited. [Account](https://konigi.com/articles/sketch2claude/) | A runnable starting point for inspecting structure in a real viewport; no measured usability result. [Account](https://konigi.com/articles/sketch2claude/) | **Moderate** | [August 24, 2026 account](https://konigi.com/articles/sketch2claude/) |
| **Meaghan Choi, Anthropic** | Feature exploration, implementation review, and UX polish | Generates alternatives, modifies a repository, verifies in-browser, prepares PRs; also monitors changes internally | Recorded open-source demonstration, plus reported internal workflows and a failed automation experiment. [Presentation](https://www.youtube.com/watch?v=hKeDfupbA4U) | Recorded execution against Excalidraw; internal routines and their outputs are not public. [Presentation](https://www.youtube.com/watch?v=hKeDfupbA4U) | Alternative implementations and browser verification shown; automated design-review notifications were curtailed after poor results. [Presentation](https://www.youtube.com/watch?v=hKeDfupbA4U) | **Strong** for the demo; **Moderate** for internal practice | [June 4, 2026 presentation](https://www.youtube.com/watch?v=hKeDfupbA4U) |
| **Martin Rariga, Equals** | Interactive product explanation and implementation | Handles larger changes, refactoring, and animated HTML/CSS product mockups | Firsthand account of a launched website, using multiple tools. [Account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai) | Published account and identified public website; no repository or launch-version snapshot inspected. [Account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai) | Static feature imagery replaced with interactive demonstrations; combined-tool time savings claimed without a measurement method. [Account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai) | **Moderate** | [March 4, 2026 account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai) |
| **Emmet Connolly** | Interaction design and playtesting | Principal coding tool for a decision game | Completed personal learning project, not employer product work. [Account](https://thoughtwax.com/2025/07/2027-race-to-agi/) | Public repository, requirements document and original prototype identified in repository documentation. [Repository](https://github.com/thoughtwax/2027-race-to-agi) | Completed game; practitioner reports extensive playtesting and UI-performance repair. [Account](https://thoughtwax.com/2025/07/2027-race-to-agi/) | **Strong**, with limited process granularity | [July 14, 2025 account](https://thoughtwax.com/2025/07/2027-race-to-agi/); [repository](https://github.com/thoughtwax/2027-race-to-agi) |
| **Kris Puckett** | Native interaction design and product implementation | Implements layouts and behavior through iterative direction and feedback | Personally owned iOS product reported as shipped; separate from employer adoption. [Announcement](https://x.com/krispuckett/status/1963315419957403970) · [Interview](https://pod.wave.co/podcast/dive-club-1/kris-puckett-becoming-an-ai-native-designer) | Detailed essay, interview, and publicly linked App Store listing; source code not inspected. [Essay](https://permissionless.krispuckett.com/) · [App listing](https://apps.apple.com/us/app/epilogue-ambient-reading/id6751764862) | Shipped reading companion; difficult debugging and repeated human correction reported. [Essay](https://permissionless.krispuckett.com/) | **Moderate** | [September 2025 announcement](https://x.com/krispuckett/status/1963315419957403970); [firsthand essay](https://permissionless.krispuckett.com/) |

**Date qualification:** The earlier report used October 31, 2025 for Sullivan’s post, March 5, 2026 for the Shopify recording, and September 3, 2025 for Puckett’s announcement. Search metadata in the research record shows October 30, March 4, and September 2 respectively. These one-day discrepancies were not resolved; the evidence map therefore uses the month where appropriate. This qualification does not establish the dates on which the described work occurred.

## Detailed cases

### Research analysis and documentation

#### Caitlin Sullivan

**Practitioner and context.** Sullivan’s research connection is explicit: the lesson biography identifies a former head-of-user-research role and current work advising on customer insights. The main firsthand account was published in October 2025; a February 4, 2026 lesson provides a separate, synthetic-data demonstration. [Research account](https://aicustomerresearch.substack.com/p/october25) · [Lesson and biography](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do)

**UX problem.** The account addresses two operational problems: analyzing lengthy feedback within context limits, and preserving the evidence and reasoning behind product decisions. [Research account](https://aicustomerresearch.substack.com/p/october25)

**Actual workflow — inputs → actions → outputs → review.** The working-practice example uses survey results and customer calls as inputs. Sullivan reports delegating survey analysis, call analysis, and examination of bias to three parallel agents; the workflow produces analysis and documentation files. [Research account](https://aicustomerresearch.substack.com/p/october25) The later lesson uses synthetic premium, free, and churned-user material, with separate segment analyses, a human-feedback stage, cross-segment synthesis, and saved outputs. [Research lesson](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do)

**Claude Code’s specific role.** Claude Code operates over folders and writes persistent documents rather than requiring each exchange to remain inside a chat. Separate subagents organize the work; the researcher supplies project context and reviews the analysis. [Research account](https://aicustomerresearch.substack.com/p/october25) · [Research lesson](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do) The two sources should not be treated as evidence of an identical, unchanged implementation.

**Evidence and artifacts.** The [2025 post](https://aicustomerresearch.substack.com/p/october25) establishes explicit use and describes a concrete parallel workflow. The [2026 recording page](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do) identifies its synthetic dataset and provides timestamped stages for feedback, synthesis, output inspection, and evaluation discussion; the underlying analysis files were not inspected.

**Outcome.** Sullivan reports that a workflow representing more than four hours of analysis ran in 14 minutes, and states that manual and AI work were timed. No task-matching protocol, full timing record, independent quality assessment, or accounting for setup and review is supplied in the retrieved account; the comparison remains an **unverified practitioner-reported benefit**. [Research account](https://aicustomerresearch.substack.com/p/october25)

**Limitations and failure modes.** The public demonstration does not establish validity on real participant data. A bias-review agent is a documented workflow element, not evidence that bias was detected reliably; similarly, persistent documentation does not establish faithful interpretation. [Research account](https://aicustomerresearch.substack.com/p/october25) · [Research lesson](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do)

**Transferable lesson — interpretation.** Researchers can reasonably borrow the separation between source material, task-specific analysis, and saved outputs. The prerequisite is an approved, organized corpus and a human review process capable of checking interpretations against original evidence—not merely reviewing the final prose.

### Interaction exploration and prototyping

#### Kazden Cattapan, Shopify

**Practitioner and context.** The March 2026 recording identifies Cattapan as a staff product designer at Shopify. It shows a live exploration using internal infrastructure, not a retrospective claim based only on finished screens. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg)

**UX problem.** The exploration concerns how merchants might create AI-generated marketing imagery from their existing files: controls, previews, reference-image selection, saved results, and generation feedback. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg)

**Actual workflow — inputs → actions → outputs → review.** Inputs include merchant pain points recorded in Markdown, FigJam diagrams, selectively annotated reference screenshots, and a rough HTML prototype. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg) Claude Code builds an initial interface, transfers the exploration into Shopify’s Playground, and adds storage and model integration through the internal Quick platform; Cattapan repeatedly uses the result and redirects its behavior. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg)

The review loop is unusually concrete: an overlay fails to cover the intended area; a gallery control reaches a dead end; image selection becomes cramped; and generation exposes streaming text where the designer wants a different loading treatment. These observations lead to further implementation changes. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg)

**Claude Code’s specific role.** Claude Code plans and edits the implementation. FigJam and Mobbin support visual thinking, Quick supplies hosting and service infrastructure, and Playground supplies the surrounding product environment; the existing design system is incidental rather than the activity being studied. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg) Cattapan controls scope, conceptual grouping, interaction direction, and acceptance of changes. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg)

**Evidence and artifacts.** The [recording and transcript](https://www.youtube.com/watch?v=aVDAhJ3PtLg) expose inputs, prompts, intermediate states, errors, and revisions. Useful sections include initial context at approximately 02:26–09:25, backend work around 21:14, and interaction inspection around 31:37–36:00; the repository and internal review links are not public. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg)

**Outcome.** The session documents functioning upload behavior and several revised interactions. It does **not** demonstrate a finished image-generation product: Cattapan supplies mock imagery for part of the exploration, and incomplete behavior remains visible. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg)

**Limitations and failure modes.** Reproduction depends heavily on internal infrastructure. Parallel sessions can collide when editing the same code, and Cattapan warns against overlapping work; broad initial scope also makes precise correction harder. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg) Claims that projects became dramatically shorter are self-reports without a disclosed comparison method. [Recording](https://www.youtube.com/watch?v=aVDAhJ3PtLg)

**Transferable lesson — interpretation.** The useful starting point is a deliberately narrow, behaviorally meaningful flow. Another designer can borrow the cycle of contextual input, running interaction, direct inspection, and bounded correction without assuming access to Shopify’s tooling.

#### Michael Angeles

**Practitioner and context.** Angeles identifies as a product designer in the August 24, 2026 account. The post documents experimentation with a sketch-to-Claude-Code workflow and offers the input materials publicly. [Firsthand account](https://konigi.com/articles/sketch2claude/)

**UX problem.** The activity supports early structural judgment: whether a page’s hierarchy and arrangement hold up in a browser before investing in a polished static composition. [Firsthand account](https://konigi.com/articles/sketch2claude/)

**Actual workflow — inputs → actions → outputs → review.** Angeles draws on a numbered grid with screen metadata and callouts, scans the sheet into a project folder, and provides the image to Claude Code. Claude Code interprets the layout and produces static HTML/CSS; the resulting page becomes a starting point for browser inspection and further sketching or coding. [Firsthand account](https://konigi.com/articles/sketch2claude/)

**Claude Code’s specific role.** It translates the designer’s spatial decisions into a browser-rendered implementation. The sketch supplies structure and intent; Angeles retains the decision about whether the implementation expresses that intent. [Firsthand account](https://konigi.com/articles/sketch2claude/)

**Evidence and artifacts.** The [firsthand post](https://konigi.com/articles/sketch2claude/) links to printable PDFs and a demonstration. Those sheets are inspectable **input artifacts**, not evidence that a resulting interface is usable; no generated repository or evaluated prototype was inspected.

**Outcome.** Angeles reports successful interpretation of sketch boundaries and callouts, followed by a static browser prototype. No controlled comparison, client outcome, or participant study is documented. [Firsthand account](https://konigi.com/articles/sketch2claude/)

**Limitations and failure modes.** The account principally establishes translation of a sketch, not complex interaction behavior. Angeles also distinguishes situations where skipping high-fidelity mockups is useful from team settings that still need a shared design artifact. [Firsthand account](https://konigi.com/articles/sketch2claude/)

**Transferable lesson — interpretation.** A sketch can constrain generation without specifying every pixel. This suits an early structural question; it is a poor substitute for a behavioral specification when important states, errors, or transitions are absent from the drawing.

### Existing-product implementation and review

#### Meaghan Choi, Anthropic

**Practitioner and context.** The June 4, 2026 presentation identifies Choi as Claude Code’s lead designer. It combines recorded work on the open-source Excalidraw project with descriptions of internal Anthropic practice; the latter is a vendor-employee self-report, not independent adoption evidence. [Presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

**UX problem.** Three related activities appear: exploring an autocomplete interaction, addressing small interface-quality issues, and identifying frontend changes that may have bypassed design involvement. [Presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

**Actual workflow — inputs → actions → outputs → review.** In the public demonstration, an existing repository and feature request feed a reusable prototyping instruction. Claude Code produces alternative implementations, an option is selected, and the agent proceeds toward implementation, browser verification, and a PR containing visual evidence. [Presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

Separately, Choi describes a scheduled internal routine that inspects frontend changes and checks connected discussions for design involvement. It drafts alternative designs and originally contacted engineers; after poor design output, the outward messaging was disabled and Choi retained the material for personal review. [Presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

**Claude Code’s specific role.** Claude Code coordinates repository changes and review artifacts. Browser integration supplies a way to exercise and record the interface; internal integrations supply organizational context. [Presentation](https://www.youtube.com/watch?v=hKeDfupbA4U) Choi explicitly retains responsibility for product and craft decisions despite allowing the agent to propose an option. [Presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

**Evidence and artifacts.** The [presentation](https://www.youtube.com/watch?v=hKeDfupbA4U) records the public feature workflow. Excalidraw is an inspectable starting repository, but this research did not identify and audit the resulting contribution; the internal monitoring routine and its evidence remain private.

**Outcome.** The recording shows alternative generation and browser verification progressing toward a reviewable change. The internal monitoring experiment supplies a significant negative result: automated design judgment was inadequate for the original outward-facing workflow. [Presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

**Limitations and failure modes.** Choi’s setup includes extensive internal integrations and access to comparatively generous model settings. Frequent small fixes also created review overhead for engineers, prompting consolidation into fewer PRs. [Presentation](https://www.youtube.com/watch?v=hKeDfupbA4U) The account does not establish that automated verification catches UX or accessibility problems reliably.

**Transferable lesson — interpretation.** The transferable unit is **a small proposed change with inspectable evidence**, not autonomous design approval. Repository access, isolated working copies, engineering conventions, and an agreed review boundary are prerequisites.

#### Martin Rariga, Equals

**Practitioner and context.** The March 4, 2026 publication identifies Rariga as Equals’ founding product designer and reproduces a substantive first-person account of rebuilding the company website. [Firsthand account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai)

**UX problem.** The relevant work is interactive product communication: replacing static feature images with demonstrations that explain behavior and can vary by audience. Brand restyling forms part of the surrounding project but is not the qualifying activity here. [Firsthand account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai)

**Actual workflow — inputs → actions → outputs → review.** Inputs include completed visual direction, Figma material, and an existing website implementation. Rariga uses Claude Code for larger changes and animated mockups, then refines the work through precise edits and manual inspection; the account describes interactive example prompts added shortly before launch. [Firsthand account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai)

**Claude Code’s specific role.** The allocation is explicit: Claude Code handles larger changes, refactoring, and animated mockups; Cursor handles smaller edits; Figma supplies design references; GitHub Desktop provides checkpoints and a convenient way to discard experiments. [Firsthand account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai) Reported benefits belong to this combined workflow, not Claude Code alone.

**Evidence and artifacts.** The [published account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai) establishes the tool allocation and launched-work context. It identifies the public website, but no repository, session trace, or preserved launch version was inspected.

**Outcome.** Rariga reports replacing feature imagery with HTML/CSS mockups and introducing animated responses to example prompts. A claim that Claude and Cursor saved at least a month is not accompanied by a baseline or measurement method and remains unverified. [Firsthand account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai)

**Limitations and failure modes.** The account describes favorable starting conditions: an existing, well-structured implementation and prior experience making smaller code changes. It supplies no comprehension test, conversion analysis, accessibility evaluation, or maintenance assessment. [Firsthand account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai)

**Transferable lesson — interpretation.** An interactive demonstration may be worth trying when motion or state change is essential to explaining a product. The hypothesis to test is improved understanding—not whether an animation can be generated quickly.

### Personally owned interaction projects

#### Emmet Connolly

**Practitioner and context.** Connolly’s public biography establishes a product-design leadership role. The July 14, 2025 account describes *2027: Race to AGI!* as a completed personal learning project, separate from employer work. [Public biography](https://thoughtwax.com/about/) · [Project account](https://thoughtwax.com/2025/07/2027-race-to-agi/)

**UX problem.** The project explores how a decision game communicates trade-offs through choices, resource changes, consequences, difficulty, and endings. [Project account](https://thoughtwax.com/2025/07/2027-race-to-agi/)

**Actual workflow — inputs → actions → outputs → review.** Connolly reports designing and coding the game primarily with Claude Code and Midjourney, then spending much of the effort on playtesting and small UI repairs. [Project account](https://thoughtwax.com/2025/07/2027-race-to-agi/) Repository documentation identifies a requirements document, an original prototype, structured decision-card content, state-management code, and responsive styling. [Repository](https://github.com/thoughtwax/2027-race-to-agi)

This is a **coarse documented sequence**, not a reconstructed prompt history. The sources do not establish which individual changes Claude Code made or the exact order of each iteration.

**Claude Code’s specific role.** Claude Code is explicitly named as the principal coding tool. Midjourney is also named, but the account does not provide a complete division of labor between generated imagery, implementation, and manual changes. [Project account](https://thoughtwax.com/2025/07/2027-race-to-agi/)

**Evidence and artifacts.** The [firsthand post](https://thoughtwax.com/2025/07/2027-race-to-agi/) links to the [public repository](https://github.com/thoughtwax/2027-race-to-agi). Repository documentation was examined; implementation correctness, commit history, and runtime behavior were not audited.

**Outcome.** Connolly completed the game and reports approximately 20 hours of work. This is a self-reported project duration, not a measured saving against a comparable non-AI project. [Project account](https://thoughtwax.com/2025/07/2027-race-to-agi/) Playtesting influenced the interpretation of difficulty: the author considered rebalancing it, then largely retained it because the difficulty supported the intended cautionary experience. [Project account](https://thoughtwax.com/2025/07/2027-race-to-agi/)

**Limitations and failure modes.** Web-interface jank and performance expectations made the final stage difficult. The account describes the author’s playtesting, not a recruited usability study or independently measured player outcomes. [Project account](https://thoughtwax.com/2025/07/2027-race-to-agi/)

**Transferable lesson — interpretation.** The strongest lesson is about completing an interaction loop: implement, play, notice consequences, and decide what should change. An operational game demonstrates execution; whether its interaction communicates the intended idea remains a separate evaluative question.

#### Kris Puckett

**Practitioner and context.** A March 2026 practitioner interview establishes Puckett’s design-management role. A September 2025 announcement explicitly attributes the Epilogue reading app largely to Claude Code; a detailed firsthand essay documents development and debugging but displays no publication date in the retrieved page. [Interview](https://pod.wave.co/podcast/dive-club-1/kris-puckett-becoming-an-ai-native-designer) · [Announcement](https://x.com/krispuckett/status/1963315419957403970) · [Essay](https://permissionless.krispuckett.com/)

**UX problem.** Epilogue supports physical-book reading through a native companion experience, including book management, quote capture, and book-specific visual treatment. [Essay](https://permissionless.krispuckett.com/)

**Actual workflow — inputs → actions → outputs → review.** Puckett describes specifying hierarchy and layout in language, reviewing implementations, and repeatedly correcting them. The interview explicitly ties that loop to Claude Code rather than a canvas-based design process. [Interview](https://pod.wave.co/podcast/dive-club-1/kris-puckett-becoming-an-ai-native-designer) The essay adds examples of inspecting cover-derived colors and diagnosing discrepancies between expected and actual presentation. [Essay](https://permissionless.krispuckett.com/)

**Claude Code’s specific role.** Claude Code implements the directed interface and behavior. Xcode and the simulator appear in the broader development account, while the launch announcement identifies other models as runtime product services rather than coding tools. [Essay](https://permissionless.krispuckett.com/) · [Announcement](https://x.com/krispuckett/status/1963315419957403970) The essay’s earliest references to “Claude” do not establish that every early step used Claude Code; those steps should not be attributed to it automatically.

**Evidence and artifacts.** The [launch announcement](https://x.com/krispuckett/status/1963315419957403970) confirms Claude Code involvement. The [essay](https://permissionless.krispuckett.com/) supplies detailed failures and decision-making, and the [interview transcript](https://pod.wave.co/podcast/dive-club-1/kris-puckett-becoming-an-ai-native-designer) adds explicit process detail; a [public App Store listing](https://apps.apple.com/us/app/epilogue-ambient-reading/id6751764862) was identified, but the application and source were not independently inspected.

**Outcome.** Puckett reports shipping the application. The more informative process evidence is the sustained correction required to reach an acceptable implementation—not a demonstrated improvement in reading behavior or user satisfaction. [Essay](https://permissionless.krispuckett.com/) · [Interview](https://pod.wave.co/podcast/dive-club-1/kris-puckett-becoming-an-ai-native-designer)

**Limitations and failure modes.** The essay describes several days of unsuccessful color-pipeline debugging, attempted rewrites, and regressions before a more precise diagnosis. It also acknowledges uncertainty about implementation details; no independent security, accessibility, or maintainability audit is supplied. [Essay](https://permissionless.krispuckett.com/)

**Transferable lesson — interpretation.** Precise articulation of an expected interaction can help direct implementation, but it does not eliminate technical diagnosis. Personally owning the product also means owning unresolved engineering and maintenance risks.

## Cross-case findings

### Recurring workflows

Within this selected sample—not the UX profession generally—three practices recur across independent accounts:

| Observed pattern | Supporting cases | What the evidence supports |
|---|---|---|
| **Externalize intent before implementation** | Cattapan’s context files and references; Angeles’ annotated sketches; Rariga’s existing design material. [Shopify](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Angeles](https://konigi.com/articles/sketch2claude/) · [Rariga](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai) | Inputs constrain implementation and make the practitioner’s intention available for inspection. They do not prove the intention is correct. |
| **Inspect the running result** | Cattapan’s flow corrections; Connolly’s playtesting; Puckett’s visual and behavioral debugging. [Shopify](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Connolly](https://thoughtwax.com/2025/07/2027-race-to-agi/) · [Puckett](https://permissionless.krispuckett.com/) | Generation is followed by direct use and revision, rather than accepted as a finished UX solution. |
| **Produce persistent work artifacts** | Sullivan’s saved analysis; Choi’s PRs; Connolly’s repository. [Sullivan](https://aicustomerresearch.substack.com/p/october25) · [Choi](https://www.youtube.com/watch?v=hKeDfupbA4U) · [Connolly](https://github.com/thoughtwax/2027-race-to-agi) | Outputs can survive the conversation and enter another review process. Persistence alone does not guarantee traceability or quality. |

Research synthesis is credible but less independently corroborated within the retained sample than interaction implementation. Sullivan supplies a substantive account and a synthetic-data teaching example, not multiple independent demonstrations of validated research outcomes. [Research account](https://aicustomerresearch.substack.com/p/october25) · [Research lesson](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do)

### Changes to the work

**Interpretation:** The clearest change is not simply faster output. Designers can move into an implementation, encounter actual state and data dependencies, and revise the experience there. Cattapan’s gallery and loading-state corrections illustrate this more convincingly than the existence of the initial generated screen. [Shopify walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg)

For research, the structural change is the ability to operate over an organized collection of files and leave durable intermediate outputs. The evidence supports that operational difference; it does not establish superior synthesis. [Research account](https://aicustomerresearch.substack.com/p/october25) · [Research lesson](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do)

### Judgments that remain human

The retained cases leave important decisions with practitioners: what problem matters, which structure or interaction to pursue, whether the implementation expresses the intended experience, and whether a proposed change should ship. [Shopify walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Puckett interview](https://pod.wave.co/podcast/dive-club-1/kris-puckett-becoming-an-ai-native-designer) · [Choi presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

Choi’s failed notification experiment is especially instructive. Automating detection, critique, redesign, and communication in one chain did not remove the need to judge the quality of the redesign before involving colleagues. [Choi presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

### Technical and organizational prerequisites

Access requirements vary substantially. Angeles’ static experiment has a comparatively small technical surface; Cattapan depends on internal hosting, storage, and model-access infrastructure; Choi’s internal workflows depend on repositories and connected organizational information. [Angeles account](https://konigi.com/articles/sketch2claude/) · [Shopify walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Choi presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

Limited coding experience does not make setup and maintenance disappear. Puckett’s debugging and Rariga’s checkpointing illustrate different ways practitioners encounter and manage implementation risk. [Puckett essay](https://permissionless.krispuckett.com/) · [Rariga account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai)

### Additional work created

The evidence contains concrete counterweights to speed claims: broken controls require diagnosis, parallel sessions require coordination, polished native behavior requires technical debugging, and many small changes can overwhelm review capacity. [Shopify walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Puckett essay](https://permissionless.krispuckett.com/) · [Choi presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

Consequently, elapsed generation time should not be reported as end-to-end time saved. None of the retained numerical claims provides a complete, independently assessed accounting of setup, review, correction, and maintenance.

## Practical adoption implications

The following are **recommendations derived from the cases**, not additional observed workflows. No undocumented prompts, commands, or configurations are supplied.

### Start with a bounded interaction

- **Who it suits:** Product and interaction designers investigating a specific behavior, such as selection, upload, loading, or return navigation.
- **Required inputs and access:** A clear task, intended states, sanitized examples, and an approved local or hosted prototype environment.
- **Inspect before trusting:** Exercise every control; distinguish mocked services from real ones; check empty, error, loading, and return states.
- **Risks and reasons not to use:** Avoid unnecessary backend work when a simpler prototype can answer the question. Do not introduce real customer data merely to increase realism.
- **Supporting evidence:** Cattapan’s session shows useful discoveries through running interactions; Angeles demonstrates a simpler route from a visual structure to browser inspection. [Shopify walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Angeles account](https://konigi.com/articles/sketch2claude/)

### Trial evidence-linked research processing

- **Who it suits:** Researchers who already understand the corpus and can audit the output.
- **Required inputs and access:** Approved, consistently organized source files; explicit research questions; an agreed place for intermediate and final outputs.
- **Inspect before trusting:** Check cited passages in context, investigate contradictory evidence, distinguish participant statements from interpretation, and review whether files were omitted.
- **Risks and reasons not to use:** Do not use sensitive data without authorization. Avoid treating polished synthesis or a second agent’s agreement as independent validation.
- **Supporting evidence:** Sullivan documents parallel analysis and persistent outputs; the public synthetic demonstration supports trying the mechanics, not trusting substantive findings without review. [Research account](https://aicustomerresearch.substack.com/p/october25) · [Research lesson](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do)

### Propose one repository change

- **Who it suits:** Design engineers and product designers with engineering support.
- **Required inputs and access:** Permission to work in a repository, an isolated branch or worktree, a reproducible issue, and team review conventions.
- **Inspect before trusting:** Review the code difference, exercise the affected flow, examine visual evidence, and check for unrelated changes.
- **Risks and reasons not to use:** Avoid autonomous merging when review responsibilities are unclear. Small visual changes can still affect behavior or accessibility.
- **Supporting evidence:** Choi demonstrates reviewable implementation work; Rariga explicitly uses checkpoints to keep exploration reversible. [Choi presentation](https://www.youtube.com/watch?v=hKeDfupbA4U) · [Rariga account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai)

### Make product behavior explainable

- **Who it suits:** Designers responsible for product education, onboarding, or interactive demonstrations.
- **Required inputs and access:** A specific comprehension question, accurate product behavior, and a maintainable implementation environment.
- **Inspect before trusting:** Verify that the demonstration reflects the actual product and test whether intended readers understand it.
- **Risks and reasons not to use:** Animation can imply capabilities or responsiveness the product does not possess. Maintenance may outweigh the communication benefit.
- **Supporting evidence:** Rariga documents replacing static feature imagery with interactive mockups, but supplies no evidence that comprehension improved. [Rariga account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai)

## Privacy, permissions, and integrity

### Safeguards described by practitioners

Several accounts document partial controls: Cattapan approves plans and file-access requests; Rariga checkpoints work before larger experiments; Choi uses isolated worktrees and later limits the audience for unreliable automated critique. [Shopify walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Rariga account](https://www.dive.club/ideas/how-martin-built-the-new-equals-website-with-ai) · [Choi presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

Sullivan’s teaching example uses synthetic data, which allows workflow mechanics to be demonstrated without establishing permission to process real participant material. [Research lesson](https://maven.com/p/70d474/claude-code-for-user-insights-what-agents-can-do)

These are bounded safeguards. They do not establish comprehensive consent, privacy, security, or research-governance compliance.

### Safeguards recommended here

The following are editorial recommendations, not claims about what every practitioner did:

- **Verify authorization before processing.** Check organizational policy, participant consent, customer agreements, repository permissions, and any restrictions on third-party processing.
- **Do not confuse file location with processing location.** A source file being on a laptop is not sufficient assurance of local-only handling; verify what leaves the device and which account terms apply.
- **Minimize access and data.** Use approved, de-identified material where possible, restrict connected folders and tools, and keep identity keys separate.
- **Preserve originals.** Keep raw research material unchanged and distinguish generated analysis from source evidence.
- **Maintain traceability.** Require stable source identifiers and enough location information to verify quotations and interpretations.
- **Separate checking from validation.** Confirming that a quotation exists does not establish that it supports a theme, represents the sample, or warrants a product decision.
- **Keep external actions gated.** Generated critique should not automatically message participants, colleagues, or customers, or publish findings.
- **Sanitize demonstrations.** Remove customer records, credentials, internal URLs, private names, and identifying metadata before sharing recordings or artifacts.

Choi’s experience provides a concrete reason for the communication boundary: a technically functioning chain can still distribute poor design judgment. [Choi presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)

## What the evidence does not establish

### Adoption prevalence

This is a purposive collection of public accounts, not a representative survey. It cannot establish how many UX professionals use Claude Code, which activities dominate across the profession, or whether the retained practitioners are typical.

The retained cases cluster in 2025–2026. No verified 2023–2024 case is presented, and no retrospective use of ordinary Claude is relabeled as Claude Code adoption.

### Outcome quality

The report does not establish:

- That generated prototypes improve usability
- That AI-assisted synthesis preserves all important evidence
- That a shipped product is accessible, secure, or maintainable
- That agent-based review can approve an experience without a practitioner
- That reported speed gains survive complete accounting for review and maintenance

The sources establish completed activities and reported experiences. They do not provide controlled outcome studies.

### Thinly evidenced activities

No retained case supplies a sufficiently documented, dedicated workflow for content inventories, taxonomy or navigation analysis, content operations, or accessibility remediation. Nor does a retained case document a full participant-testing cycle with recruitment, task observations, revisions, and subsequent measured improvement.

Public instruction repositories were found for several such activities, but an available skill is not evidence that a verified UX practitioner used it successfully on a real project. [Design-skills repository](https://github.com/richhemsley3/claude-design-skills) · [Accessibility-audit repository](https://github.com/humbleteam/accessibility-audit) · [Designer-skills repository](https://github.com/sidelineprojects/designer-skills)

### Important exclusions

| Candidate evidence | Why it was not counted |
|---|---|
| **Ben Shih’s LennyRPG account** | The Miro-hosted account verifies a product-design role and names Claude Code, but attributes implementation jointly to Claude Code and Cursor without enough action-level allocation. It remains a useful vendor-hosted lead, not a main case here. [Account](https://miro.com/blog/miro-designer-vibe-coding-process-lennyrpg/) |
| **Else van der Berg’s interview-library workflow** | The firsthand excerpt explicitly names Claude Code, but the retrieved material did not establish the required UX-role connection. A secondary page’s description of the author as a UX researcher was not accepted as sufficient verification. [Firsthand post](https://elsevanderberg.substack.com/p/claude-code-for-interview-synthesis) · [Secondary guide](https://ccforeveryone.com/guides/claude-code-for-researchers) |
| **Qualitative-analysis tutorials without verified UX roles** | Explicit Claude Code use and detailed output formats are insufficient when the practitioner’s connection to UX research has not been established. [Kristi Zuhlke account](https://aiforinsightsleaders.substack.com/p/watch-me-build-a-qual-analysis-agent) · [Andrea Chiarelli account](https://andreachiarelli.substack.com/p/i-automated-the-most-time-consuming) |
| **Accessibility and IA skill repositories** | Inspectable instructions establish that someone published a workflow specification—not that an actual engagement, evaluation, or remediation occurred. [Design-skills repository](https://github.com/richhemsley3/claude-design-skills) · [Accessibility-audit repository](https://github.com/humbleteam/accessibility-audit) · [Designer-skills repository](https://github.com/sidelineprojects/designer-skills) |

### Selection and survivorship bias

Public accounts disproportionately expose work that practitioners are willing and able to show. Confidential research and product work may be underrepresented, while demos, personal products, and commercially promoted teaching material are easier to discover.

The most useful negative evidence in this collection is therefore worth preserving: incomplete prototype behavior, difficult debugging, review overload, and curtailed automation. Those details help practitioners identify review boundaries without turning a documented experiment into a universal recommendation. [Shopify walkthrough](https://www.youtube.com/watch?v=aVDAhJ3PtLg) · [Puckett essay](https://permissionless.krispuckett.com/) · [Choi presentation](https://www.youtube.com/watch?v=hKeDfupbA4U)
