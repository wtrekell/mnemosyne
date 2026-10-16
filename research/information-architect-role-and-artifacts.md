---
name: The Information Architect - Role, Responsibilities, and Artifact Catalog
topic: The role, practices, and responsibilities of an information architect, with emphasis on the breadth and depth of the artifacts and documentation an IA produces
type: general
created: 2026-10-12
updated: 2026-10-12
---

# The Information Architect - Role, Responsibilities, and Artifact Catalog

## Findings

Scope note: this report is one half of a two-part study. Processes and evidence sources that need no human participants (inventories as a method, analytics, search-log mining, crawls) belong to the companion report. They appear here only where needed to explain an artifact.

### 1. The role

**Definitions.** The field's standard text, the "Polar Bear book" by Rosenfeld, Morville and Arango, defines information architecture in three parts: "the structural design of shared information environments"; the synthesis of organization, labeling, search and navigation systems across digital, physical and cross-channel ecosystems; and the art and science of shaping information products to support usability, findability and understanding [S1] [C1]. Abby Covert gives a plainer version: IA is how we arrange the parts of something so the whole can be understood. Her book treats it as a set of concepts anyone can use on a "mess", meaning a situation where people's interactions with information are confusing or difficult [S2] [C3]. Jorge Arango, co-author of the 4th edition and former Information Architecture Institute president, frames IA as designing information environments as places, with responsibility for their long-term social effects [S24] [C11].

**Core systems.** The Polar Bear book arranges the discipline around four systems found in most interactive information environments: organization, labeling, navigation and search. Behind them sit "invisible" components: thesauri, controlled vocabularies and metadata [S1] [C2]. Most artifacts in Section 2 specify one of these systems.

**Principles.** Dan Brown's eight principles (2010) are widely repeated as design criteria. Objects: treat content as having a lifecycle and attributes. Choices: offer focused, meaningful options. Disclosure: show just enough to signal what lies deeper. Exemplars: describe categories by sample contents. Front doors: assume at least half of visitors arrive on an internal page. Multiple classification: offer several browsing schemes. Focused navigation: don't mix kinds of logic in one scheme. Growth: assume today's content is a small fraction of tomorrow's [S3] [S4] [C4]. The original Bulletin text could not be retrieved, so the wording here comes from consistent secondary summaries (see Conflicts).

**IA is a practice, not a deliverable.** NN/g stresses that IA is an ongoing process. Its activities include content inventories, content audits, taxonomy development, and card sorting and tree testing, and each produces its own deliverable [S12] [C5].

**Where IA meets neighboring roles.**
- *UX and interaction design.* The structure users see (menus, links, breadcrumbs) is navigation. Behind it sit three "backstage" maps: the IA structure, the taxonomy, and the content model. Navigation is built on them but is smaller than them [S11] [C6]. Garrett treats architecture as conceptual and wireframes as the place for concrete interface detail, so page layout tends to fall to UX design while structure falls to IA [S6] [C7].
- *Taxonomy, ontology and librarianship.* The standards for controlled vocabularies and thesauri (ANSI/NISO Z39.19, ISO 25964) come from the information-science and standards community (NISO, ISO TC46/SC9). IA borrows them for its invisible systems, so the overlap with library and taxonomy work sits mainly in vocabulary control [S7] [S8] [C8].
- *Content strategy.* The content model is shared ground. Rachel Lovinger presents it as a document that IAs, designers, developers and content authors all use, each at a different level of detail [S13] [C13].
- *Knowledge management.* No source retrieved in this run defines the IA/KM boundary (see Appendix A).

**Lifecycle position.** The Polar Bear book follows research with a strategy phase and then a design-and-documentation phase. Documentation (diagrams, sitemaps, wireframes, content mapping and models, controlled vocabularies, style guides) comes after strategy is set [S1] [C9]. Dan Brown's documentation book likewise spans project plans, usability reports, content maps, flow charts, site maps and wireframes. Each chapter pairs a checklist of contents with a presentation strategy and a maintenance strategy [S16] [C30].

**Governance and maintenance.** The IA's job continues after launch. For taxonomies, NN/g lists ongoing governance as the final build step: regular reviews to add, rename, merge or remove terms, plus spot-checks that content is tagged consistently [S11] [C10]. ISO 25964-1 also sets requirements for thesaurus management software and makes maintenance part of the standard's scope [S7] [C19].

### 2. Artifact catalog

Each entry gives what the artifact is, its purpose, contents, fidelity, consumers, lifecycle timing and inputs, as far as the sources support. Entries marked *thin sourcing* rest mainly on the Polar Bear book's and Brown's lists of documentation types [S1] [S16] [C30], with no dedicated source retrieved.

**Content inventory and content audit (as artifacts).** A quantitative list of every content item, with a qualitative audit layered on it. These come first: NN/g puts the inventory and audit at the head of taxonomy work, and they feed taxonomy and structure decisions [S11] [S12] [C12]. Typical form: a spreadsheet, one row per item. Consumers: the IA, content strategists, migration teams. How the inventory is built is covered by the companion report.

**Content model and content types.** This documents every content type, each type's elements (attributes, including metadata) and the relationships between types. It can be a high-level diagram or a detailed spreadsheet that records each field's format and whether it is required [S13] [C13]. GOV.UK describes modeling content as smaller pieces rather than whole pages, which supports reuse, findability and consistency [S23] [C13]. Lovinger gives three reasons to make something its own type: it is reused (Author), it has a functional need (Video needs a player), or an organizational need (Press Release filtered into a Newsroom) [S13] [C14]. Consumers and fidelity: designers and IAs at high to medium detail, developers at full detail for CMS configuration, authors for entry guidance; stakeholders get extracted questions, not the full model. The model also includes an assembly model showing how items combine into pages [S13] [C13]. Inputs: inventory, business requirements, CMS constraints.

**Taxonomies (hierarchical, faceted, polyhierarchical).** A taxonomy is a closed, controlled list of approved terms, arranged hierarchically and used behind the scenes to classify content. A hierarchical taxonomy is a single parent-child tree. A faceted taxonomy is several independent hierarchies, each describing one attribute, which can be combined for filtering [S11] [C16]. Polyhierarchy, where a term has more than one broader term, is permitted under Z39.19 [S8] [C16]. NN/g notes that most digital "taxonomies" are really thesauri, because they carry synonym and related-term links [S11] [C16]. Build steps: inventory, look for an existing industry taxonomy to reuse, find core concepts (from content, metadata, SMEs, search logs), choose user-friendly preferred terms, build relationships, review with SMEs, apply with tagger training, then govern [S11] [C17]. Consumers: content authors and taggers, the search and CMS teams. Not usually shown to end users [S11] [C6].

**Controlled vocabularies and thesauri.** ANSI/NISO Z39.19-2005 (R2010) covers monolingual controlled vocabularies, from simple lists through synonym rings and taxonomies to thesauri. It defines three relationship types: equivalence (USE/UF), hierarchical (BT/NT) and associative (RT) [S8] [S9] [C18]. An associative link connects concepts that are related but not hierarchically, such as a disease and the virus that causes it [S10] [C18]. ISO 25964-1 (2011) replaces ISO 2788 and ISO 5964. It covers monolingual and multilingual thesauri and includes a data model and a free XML schema (v1.4) for exchange. SKOS is its counterpart for publishing on the Web, with a published correspondence between the two [S7] [S10] [C19]. Z39.19 has no data model and does not cover multilingual vocabularies or mapping [S10] [C19]. Form: a term record per concept (preferred term, non-preferred terms, BT/NT/RT, scope note), held in thesaurus software. Consumers: indexers, the search engine, CMS tagging.

**Synonym rings and labeling choices.** A synonym ring groups terms treated as equivalent for retrieval without naming a preferred term. It is one of the vocabulary types under Z39.19 and ISO 25964-2 [S7] [S8] [C18]. For labels, NN/g advises choosing user-friendly preferred terms and keeping jargon as non-preferred synonyms [S11] [C35]. A label inventory, listing every label in use with where it appears, is *thin sourcing* [S1] [C30].

**Ontologies and knowledge graphs.** Noy and McGuinness define an ontology as "a formal explicit description of concepts in a domain of discourse": classes, slots (properties) and facets (restrictions on slots). Classes plus instances make a knowledge base, which is the core of a knowledge graph [S15] [C20]. Build steps: set domain and scope with competency questions, reuse existing ontologies, list terms, define the class hierarchy, add slots and facets, create instances [S15] [C20]. Consumers: developers, data and search engineers, reasoners.

**Metadata schemas and application profiles.** A Dublin Core Application Profile (DCAP) "specifies and describes the metadata used in a particular application". It has five components: functional requirements, a domain model, a Description Set Profile (terms with constraints such as repeatability, value types and obligation), usage guidelines, and syntax guidelines [S14] [C22]. Schema.org is a shared vocabulary of types and properties for structured data on web pages, and can supply the terms an application profile constrains [S22] [C23]. Consumers: metadata creators, developers, partner systems.

**Sitemaps and structure diagrams.** A visual diagram, usually boxes joined by lines, showing how pages and sections fit together. Annotations can mark whether a box is a category label or a real page. It is an internal planning and reference tool for spotting content gaps, and rarely shown to users [S12] [C24]. NN/g insists that "A sitemap is only one part of the site's information architecture". The sitemap leaves out navigation labels, local and contextual links, and UI components such as breadcrumbs and search placement [S12] [C25]. Timing: after the IA structure is decided, as its visual expression [S12] [C25].

**Annotation conventions: Garrett's Visual Vocabulary.** A notation released in October 2000 (v1.1b, 2002) for site architecture and interaction diagrams. It uses a small set of shapes (pages, page stacks, files, decision points and conditional logic, connectors, areas), is tool-independent, fits on a letter-sized page, has been widely adopted (an OmniGraffle template, seven translations), and has been called the de facto standard for site diagrams [S5] [S6] [C26]. Garrett acknowledges its main limit: it "treats the page as something of a black box", so it can show conditional navigation but not page-level logic such as dynamically assembled content [S6] [C27].

**Navigation system specifications.** Global navigation is stable and represents the top level. Local navigation varies by category and acts as a "you are here" cue. Utility navigation reaches site functions (help, search, account). Contextual navigation offers embedded and related links [S18] [S19] [C28]. A navigation spec lists each system, its items and labels, where it appears, and the rules for when it changes. The spec's format is *thin sourcing* [S1] [C30].

**Search system specifications.** A spec can cover what is indexed, facets (drawn from a faceted taxonomy) [S11] [C16], best bets, synonym handling and zero-result handling. Best bets are hand-picked results tied to specific queries and shown above automated results, typically chosen by studying search logs. Query-log analysis flags frequent zero-result queries as dead ends that need help [S17] [C29]. The log mining itself is in the companion report.

**Wireframes and page-level blueprints.** These are part of the IA documentation set in both the Polar Bear book and Brown [S1] [S16] [C30]. Garrett puts concrete interface detail in wireframes rather than the architecture diagram, which explains shared or contested ownership: IA decides what goes on the page and how it is ordered and labeled, while UX or visual design decides presentation [S6] [C7]. Annotation conventions for IA wireframes are *thin sourcing*.

**User flows and task flows.** Brown lists flow charts as a standard deliverable [S16] [C30]. The Visual Vocabulary's decision points and connectors are used to draw flows between page classes [S5] [S6] [C26]. *Thin sourcing* beyond that.

**Concept maps and system models.** These diagram the concepts in a domain and how they relate, before any page structure exists. They fit Covert's aim of making the whole of a mess understandable [S2] [C3]. The Polar Bear book counts diagrams among its documentation types [S1] [C9]. *Thin sourcing* on specific formats.

**URL and naming conventions; style and labeling guides; IA style guides; governance documents.** The Polar Bear book lists style guides and pattern libraries among the documentation that keeps an IA consistent after launch [S1] [C9]. Brown attaches a maintenance strategy to every deliverable type [S16] [C30]. Taxonomy governance (review schedule, change rules, tagging QA) is the best-documented governance artifact [S11] [C10]. A dedicated URL-convention source is *thin sourcing*. Redirect-map practice (next entry) shows that stable URL paths cut migration cost [S21] [C33].

**IA strategy documents and IA requirements.** In the Polar Bear book, strategy follows research and comes before design documentation [S1] [C9]. Ontology competency questions and DCAP functional requirements are two formal versions of "IA requirements" [S15] [S14] [C20] [C22].

**Crosswalks and mapping tables.** ISO 25964-2 covers mappings between vocabularies (thesauri, classification schemes, taxonomies, subject headings, ontologies, name authorities, synonym rings), with equivalence (exact, inexact, partial), hierarchical and associative mapping types [S7] [C34]. A metadata crosswalk is the same idea applied to schema elements. Form: a table, one row per source element or term, with the target and the mapping type.

**Migration maps.** This maps every old URL or content item to its destination and redirect type. Usually a spreadsheet, treated as the source of truth, and finished before launch rather than as post-launch cleanup [S21] [C33]. Inputs: the inventory and the new sitemap.

**Card-sort and tree-test output artifacts.** Card-sort output usually includes a similarity matrix (how often each pair of cards was grouped together) and a dendrogram (clusters by percentage agreement). One tool suggests treating agreement above 70% as strong, but that is a practitioner convention, not a standard [S20] [C32]. Tree-test output formats (success, directness, first click) were not confirmed from a source in this run.

### 3. Depth: excellent versus mediocre artifacts

- **Content models.** A strong model breaks sortable or reusable data into typed fields with set formats. A weak one buries data in one body field, stores markup with content, splits content into fields for no functional reason, ignores CMS limits, or leaves developers to invent the details [S13] [C15]. The model should be kept as a living working document [S13] [C31].
- **Ontologies (and taxonomies).** Common faults include separate classes for synonyms, a singular class under its plural, cycles, a class with only one child or with more than a dozen, changeable states modeled as classes, domains and ranges set too broad, modeling beyond what the application needs, inconsistent naming, and undocumented decisions [S15] [C21].
- **Taxonomies.** A strong taxonomy starts from an existing standard where one exists, prunes isolated terms with little content behind them, uses user language for preferred terms, and has governance in place [S11] [C17] [C10].
- **Sitemaps.** A sitemap that stands in for the whole IA is the classic failure. A good one is labeled as a planning view and paired with navigation and labeling specs [S12] [C25].
- **Diagrams.** Use a shared notation (the Visual Vocabulary) so readers don't need a new legend. Don't stretch it to page-level logic it cannot express [S6] [C26] [C27].
- **All deliverables.** Brown's per-deliverable checklist, presentation strategy and maintenance strategy amount to a quality rubric: is it complete, is it shaped for its audience, does someone own its upkeep? [S16] [C31]

## Conflicts

1. **Title and venue of Dan Brown's principles.** Secondary sources attribute the eight principles to a 2010 *Bulletin of ASIS&T* article, "Eight Principles of Information Architecture" [S3, Trusted] [S4, Unconfirmed]. Wikipedia's "Social information architecture" entry cites a paper titled "8 Principles of Social Information Architecture" (seen in search results, not used as a source). The publisher page returned HTTP 403. The principles' names and meanings agree across all summaries, so the findings use them, but the exact original wording is unverified.
2. **Z39.19 edition and scope.** The 1993 edition is titled for "Monolingual Thesauri". The current 2005 (R2010) edition covers "Monolingual Controlled Vocabularies" [S8, Official] [S9, Unconfirmed]. Following the newest-version rule, the findings use the 2005 (R2010) scope.
3. **How navigation types are grouped.** Kalbach treats local navigation as a subtype of structural navigation [S19, Unconfirmed]. NN/g and practitioner guides treat global, local, utility and contextual navigation as peers [S18, Unconfirmed]. The catalog lists all four and notes that either grouping works in a spec.
4. **ISO 25964-2 status.** The NISO page still says Part 2 is "to be published in 2013" [S7, Official], while Wikipedia describes both parts as published [S10, Unconfirmed]. This doesn't affect the mapping-type findings, which come from the standard's own description.

## Appendix A: Next searches

1. The IA versus knowledge-management and content-strategy boundary, from primary authors (Halvorson's *Content Strategy for the Web*, KM standards such as ISO 30401).
2. Tree-test and card-sort result report formats from NN/g and Optimal Workshop (success rate, directness, first-click), as artifacts.
3. IA documentation chapter of the Polar Bear book (4th ed., ch. 13): full list of deliverables and the authors' quality criteria, read in full.
4. URL design and naming-convention guidance (W3C "Cool URIs don't change", GOV.UK URL standards) as an IA artifact.
5. Taxonomy and IA governance documents in practice (Heather Hedden, *The Accidental Taxonomist*; Earley; enterprise taxonomy governance templates).

## Appendix B: Sources

### Source list

| ID | Citation | Label | Setting | Reason for label |
| --- | --- | --- | --- | --- |
| S1 | Louis Rosenfeld, Peter Morville, Jorge Arango, *Information Architecture: For the Web and Beyond*, 4th ed., O'Reilly, October 2015, https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ | Official | Organized | The field's standard text ("Polar Bear book"), written by the discipline's founders. The 4th edition is the newest. Contents seen through the O'Reilly overview and Part II description, plus reviewer knowledge of the text. |
| S2 | Abby Covert, *How to Make Sense of Any Mess*, CreateSpace, 2014 (book site © 2022, accessed 2026-10-12), https://www.howtomakesenseofanymess.com/ | Unconfirmed | Individual | Book site fetched 2026-10-12 confirms title and author; it shows chapter headings only, so the definition comes from the reviews listed here. Has a large audience and is reviewed or cited by Simon Whatley's reading notes, UX Booth and UX London 2016 (selected speaker). Five qualifying citations were not confirmed in this run. |
| S3 | Dan Brown, "Eight Principles of Information Architecture," *Bulletin of the American Society for Information Science and Technology* 36(6), Aug/Sep 2010, as linked by Cameron Moll, "Eight Principles of Information Architecture (PDF)," 13 August 2010, https://www.goodreads.com/author_blog_posts/593761-eight-principles-of-information-architecture-pdf | Trusted | Organized | Individual author whose principles are cited by principles.design, UX Planet, CareerFoundry, Uxcel, Revelry, University of Arkansas WebFirst toolkit, and Wikipedia ("Social information architecture"). Moll's post confirms the title, the Bulletin Aug/Sep 2010 issue and the PDF link. The Wiley DOI page returned 403, and the old asis.org PDF link now redirects to an unrelated domain, so the principles' content comes through these summaries. |
| S4 | principles.design, "Eight principles of information architecture," n.d. (accessed 2026-10-12), https://principles.design/examples/eight-principles-of-information-architecture | Unconfirmed | Organized | Secondary summary with an audience. Citing sources not verified. |
| S5 | Jesse James Garrett, "A Visual Vocabulary for Describing Information Architecture and Interaction Design," v1.1b, jjg.net, March 2002, https://www.jjg.net/ia/visvocab/ | Official | Individual | The notation's owner and its authoritative specification. The page refused the connection, so contents were confirmed through S6, the Web Style Guide 3rd ed. and Wikipedia. |
| S6 | Boxes and Arrows, "The Visual Vocabulary Three Years Later: An Interview with Jesse James Garrett," 11 December 2003, https://boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett/ | Official | Organized | First-hand account by the notation's owner of its scope and limits. |
| S7 | NISO (ISO TC46/SC9 Secretariat), "ISO 25964 - the international standard for thesauri and interoperability with other vocabularies," n.d. (accessed 2026-10-12), https://www.niso.org/schemas/iso25964 | Official | Organized | The standards body's own page for the standard. |
| S8 | NISO, ANSI/NISO Z39.19-2005 (R2010), *Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies*, 2005, reaffirmed 2010, https://www.niso.org/publications/ansiniso-z3919-2005-r2010 | Official | Organized | US national standard for controlled vocabularies, newest edition. The NISO page (fetched 2026-10-12) confirms its title, the 2010 reaffirmation, its scope and the four vocabulary types (lists, synonym rings, taxonomies, thesauri). Relationship types come through S9 and S10. |
| S9 | CASRAI Dictionary, "ANSI/NISO Z39.19 Controlled Vocabularies & Thesauri," n.d. (accessed 2026-10-12), https://www.casrai.org/dictionary/term/ansi-niso-z39-19-controlled-vocabularies-thesauri | Unconfirmed | Organized | Reference entry with an audience. Citations not verified. |
| S10 | Wikipedia, "ISO 25964," accessed 2026-10-12, https://en.wikipedia.org/wiki/ISO_25964 | Unconfirmed | Organized | Community-edited encyclopedia entry with an audience. Not tested for citations. |
| S11 | Page Laubheimer, "Taxonomy 101," Nielsen Norman Group, 3 July 2022, https://www.nngroup.com/articles/taxonomy-101/ | Unconfirmed | Organized | Large audience. Five citing sources for this article were not verified in this run. |
| S12 | Samhita Tankala, "Information Architecture vs. Sitemaps," Nielsen Norman Group, 3 September 2023 (reviewed 7 August 2026), https://www.nngroup.com/articles/information-architecture-sitemaps/ | Unconfirmed | Organized | Large audience. Citing sources not verified. |
| S13 | Rachel Lovinger, "Content Modelling: A Master Skill," *A List Apart*, 24 April 2012, https://alistapart.com/article/content-modelling-a-master-skill/ | Unconfirmed | Organized | Edited publication with an audience. Citing sources not verified. |
| S14 | Karen Coyle, Tom Baker, "Guidelines for Dublin Core Application Profiles," DCMI, 18 May 2009, https://www.dublincore.org/specifications/dublin-core/profile-guidelines/ | Official | Organized | DCMI owns Dublin Core and the DCAP concept. |
| S15 | Natalya F. Noy, Deborah L. McGuinness, "Ontology Development 101: A Guide to Creating Your First Ontology," Stanford University, c. 2001, https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html | Unconfirmed | Organized | Widely used tutorial with an audience. Five citing sources not listed in this run. |
| S16 | Dan Brown, *Communicating Design: Developing Web Site Documentation for Design and Planning*, 2nd ed., New Riders, 2010, https://www.peachpit.com/articles/article.aspx?p=1659710 | Unconfirmed | Organized | Book with an audience. Contents seen through publisher and Goodreads descriptions. Citations not verified. |
| S17 | Louis Rosenfeld, *Search Analytics for Your Site*, Rosenfeld Media, 2011, via BCS IRSG review https://archive-irsg.bcs.org/informer/?p=467, and Rich Wiggins and Louis Rosenfeld, "Using Search Analytics to Diagnose What's Ailing your Information Architecture," ASIS&T IA Summit, 24 March 2007, https://www.slideshare.net/lrosenfeld/using-search-analytics-to-diagnose-whats-ailing-your-information-architecture | Unconfirmed | Individual | Practitioner work with an audience. Citations not verified. |
| S18 | Nielsen Norman Group, "Local Navigation," n.d. (accessed 2026-10-12), https://www.nngroup.com/articles/local-navigation/ | Unconfirmed | Organized | Audience. Citations not verified. |
| S19 | James Kalbach, *Designing Web Navigation*, O'Reilly, 2007, ch. 4, https://www.oreilly.com/library/view/designing-web-navigation/9780596528102/ch04.html | Unconfirmed | Organized | Book with an audience. Citations not verified. |
| S20 | UXtweak, "What is a Similarity Matrix?," n.d. (accessed 2026-10-12), https://blog.uxtweak.com/similarity-matrix/ | Unconfirmed | Organized | Vendor blog with an audience. |
| S21 | urllo, "Complete redirect mapping guide for website migrations," n.d. (accessed 2026-10-12), https://www.urllo.com/resources/learn/redirect-mapping-guide-migrations | Unconfirmed | Organized | Vendor guide with an audience. |
| S22 | Schema.org, home page, accessed 2026-10-12, https://schema.org/ | Official | Organized | Owner of the schema.org vocabulary. Its home page (fetched 2026-10-12) describes a collaborative effort, founded by Google, Microsoft, Yahoo and Yandex, to create and maintain schemas for structured data on the Internet. |
| S23 | GOV.UK Service Manual / Design Guide, "Content model" glossary entry, n.d. (accessed 2026-10-12), https://design-guide.publishing.service.gov.uk/glossary/content-model/ | Unconfirmed | Organized | Government design guide with an audience. Not the owner of the general subject. |
| S24 | Jorge Arango, *Living in Information: Responsible Design for Digital Places*, Two Waves Books, 2018, via UXmatters review https://uxmatters.com/mt/archives/2018/09/book-review-living-in-information.php | Unconfirmed | Individual | Book with an audience. Citations not verified. |

### Claim map

- **Foundation claims by strongest source:** 12 foundation claims: 7 backed by an Official source, 0 by Reputable or Trusted at best, 5 by Unconfirmed only.
- **Weak foundations:** C5 rests only on an unconfirmed source (S12). C6 rests only on an unconfirmed source (S11). C13 rests only on unconfirmed sources (S13, S23). C20 rests only on an unconfirmed source (S15). C24 rests only on an unconfirmed source (S12).
- **Sources by label:** 7 official, 0 reputable, 1 trusted, 16 unconfirmed, 0 ignored.

| ID | Claim | Sources | Role | Depends on |
| --- | --- | --- | --- | --- |
| C1 | IA is the structural design of shared information environments, synthesizing organization, labeling, search and navigation to support findability and understanding. | S1 (Official), S2 (Unconfirmed) | Foundation | none |
| C2 | IA comprises four core systems (organization, labeling, navigation, search) plus invisible components (thesauri, controlled vocabularies, metadata). | S1 (Official) | Foundation | none |
| C3 | Covert defines IA as arranging parts so the whole is understandable, applicable by anyone to any "mess". | S2 (Unconfirmed) | Support | C1 |
| C4 | Dan Brown's eight principles are objects, choices, disclosure, exemplars, front doors, multiple classification, focused navigation and growth. | S3 (Trusted), S4 (Unconfirmed) | Support | C1 |
| C5 | IA is an ongoing process whose activities each produce their own deliverable, not a single deliverable. | S12 (Unconfirmed) | Foundation | none |
| C6 | Navigation is the frontstage; IA structure, taxonomy and content model are backstage maps, not usually shown to users. | S11 (Unconfirmed) | Foundation | none |
| C7 | Architecture is conceptual and wireframes hold concrete interface detail, so page layout shades into UX ownership. | S6 (Official) | Support | C6 |
| C8 | IA's overlap with librarianship and taxonomy work centers on vocabulary control standards from NISO and ISO. | S7 (Official), S8 (Official) | Support | C2 |
| C9 | In the Polar Bear book, strategy follows research and comes before design documentation, which includes diagrams, sitemaps, wireframes, content models, vocabularies and style guides. | S1 (Official) | Support | C5 |
| C10 | IA governance includes regular taxonomy review (add, rename, merge, remove terms) and spot-checks of tagging consistency. | S11 (Unconfirmed) | Support | C5 |
| C11 | Arango frames IA as designing information environments as places, with long-term social responsibility. | S24 (Unconfirmed) | Detail | none |
| C12 | Content inventories and audits are early artifacts that feed taxonomy and structure work. | S11 (Unconfirmed), S12 (Unconfirmed) | Support | C5 |
| C13 | A content model documents content types, their attributes and relationships, at diagram or spreadsheet fidelity, for designers, developers and authors. | S13 (Unconfirmed), S23 (Unconfirmed) | Foundation | none |
| C14 | Something becomes its own content type for reuse, functional or organizational reasons. | S13 (Unconfirmed) | Support | C13 |
| C15 | Content-model failure modes include data buried in body fields, markup stored with content, needless fields, ignored CMS limits and gaps left to developers. | S13 (Unconfirmed) | Support | C13 |
| C16 | A taxonomy is a closed hierarchical controlled vocabulary; it may be hierarchical, faceted or polyhierarchical, and most digital taxonomies are really thesauri. | S11 (Unconfirmed), S8 (Official) | Foundation | none |
| C17 | Taxonomy construction runs from inventory through reuse, concept finding, preferred terms, relationships, SME review, application and governance. | S11 (Unconfirmed) | Support | C16 |
| C18 | Z39.19 covers lists, synonym rings, taxonomies and thesauri, with equivalence (USE/UF), hierarchical (BT/NT) and associative (RT) relationships. | S8 (Official), S9 (Unconfirmed), S10 (Unconfirmed) | Foundation | none |
| C19 | ISO 25964-1 covers mono- and multilingual thesauri with a data model, XML schema and management-software requirements, and aligns with SKOS. | S7 (Official), S10 (Unconfirmed) | Foundation | C18 |
| C20 | An ontology is a formal explicit description of domain concepts (classes, slots, facets), built from scope and competency questions through instances. | S15 (Unconfirmed) | Foundation | none |
| C21 | Common ontology pitfalls include synonym classes, cycles, unbalanced hierarchies, states as classes, over-modeling and undocumented decisions. | S15 (Unconfirmed) | Support | C20 |
| C22 | A Dublin Core Application Profile has functional requirements, a domain model, a description set profile, usage guidelines and syntax guidelines. | S14 (Official) | Detail | none |
| C23 | Schema.org is a shared vocabulary of types and properties for structured data on web pages. | S22 (Official) | Detail | none |
| C24 | A sitemap is a visual diagram of how pages and sections fit together, used internally for planning and gap-spotting. | S12 (Unconfirmed) | Foundation | none |
| C25 | A sitemap is only one part of the IA, comes after the structure is decided, and leaves out navigation and UI detail. | S12 (Unconfirmed) | Support | C24 |
| C26 | Garrett's Visual Vocabulary (2000, v1.1b 2002) is a small, tool-independent, widely adopted notation for site architecture and flows. | S5 (Official), S6 (Official) | Foundation | none |
| C27 | The Visual Vocabulary treats the page as a black box and cannot express page-level logic. | S6 (Official) | Support | C26 |
| C28 | Navigation systems include global, local, utility and contextual navigation. | S18 (Unconfirmed), S19 (Unconfirmed) | Detail | none |
| C29 | Best bets are hand-picked, log-informed results for specific queries, and frequent zero-result queries mark dead ends to address. | S17 (Unconfirmed) | Detail | none |
| C30 | Standard IA documentation includes content maps, flow charts, site maps, wireframes and plans, each with a checklist, a presentation strategy and a maintenance strategy. | S16 (Unconfirmed), S1 (Official) | Foundation | none |
| C31 | Good IA deliverables are complete, fitted to their audience and maintained as living documents. | S16 (Unconfirmed), S13 (Unconfirmed) | Support | C30, C13 |
| C32 | Card-sort output artifacts include similarity matrices and dendrograms, and agreement thresholds are conventions, not standards. | S20 (Unconfirmed) | Detail | none |
| C33 | A migration or redirect map is a spreadsheet mapping each old URL to its destination and redirect type, finished before launch. | S21 (Unconfirmed) | Detail | none |
| C34 | ISO 25964-2 defines vocabulary mappings (exact, inexact and partial equivalence; hierarchical; associative) across many vocabulary types, which is the basis of crosswalks. | S7 (Official) | Support | C19 |
| C35 | Labels should use user-friendly preferred terms, with jargon kept as non-preferred synonyms. | S11 (Unconfirmed) | Support | C16, C18 |
