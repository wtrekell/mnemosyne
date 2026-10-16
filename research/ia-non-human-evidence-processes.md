---
name: Non-human evidence processes for information architecture
topic: The processes and evidence sources an information architect uses to inform IA work without interacting with people (content, systems, logs, analytics, standards and existing artifacts), their methods, tools, outputs, limits, and how unvalidated findings should be labeled
type: general
created: 2026-10-12
updated: 2026-10-12
---

# Non-human evidence processes for information architecture

## Findings

Scope: these are processes that use evidence already in hand: content, systems, logs, analytics, standards and existing artifacts. They exclude interviews, card sorts, tree tests, surveys, workshops and contextual inquiry. Artifacts appear here only as outputs. A companion report covers the IA role and the artifact catalog.

Reading the labels: most practitioner sources (NN/g, Boxes and Arrows, AIIM blogs) are labeled **Unconfirmed** because this run did not complete the five-citation test for them. That is a gap in this run's checking, not a judgment that they are weak (see Appendix A, item 1). Standards bodies, tool vendors describing their own tools, and the field's recognized authors (Rosenfeld, Land, Covert on her own heuristics) are labeled **Official**.

### 1. The organizing frame: warrant

ANSI/NISO Z39.19-2005 names three sources of warrant for choosing terms. *Literary warrant* comes from the language used in the content. *User warrant* comes from the language of users. *Organizational warrant* comes from the organization's needs and priorities. The 1993 edition had only the first two [S12] [S13] [C12]. This frame sorts every process in this report. Content inventories, corpus analysis and standards reuse produce literary warrant. Mining org charts, CMS schemas and business terms produces organizational warrant. Search logs and analytics are the only non-interactive sources of indirect user warrant. Z39.19-2005 was reaffirmed in 2010. A 2016 review ballot asked for a revision to align it with ISO 25964 and SKOS, but this run found no newer edition [S14] [C13].

The two main IA texts frame research the same way. *Information Architecture: For the Web and Beyond* (4th ed., 2015) runs from research to strategy, design and implementation, and treats organization, labeling, navigation, search and metadata as the core components [S40] [C35]. Lambe's *Organising Knowledge* treats taxonomies as central to how organizations coordinate, not as a content-management sideline. It gives an overall methodology rather than a step-by-step manual (the publisher and a reviewer disagree on that; see Conflicts) [S38] [S39] [C34].

### 2. Content inventory (quantitative) and content audit (qualitative)

**What it is.** Paula Land separates the two. An inventory is a quantitative, usually spreadsheet-based catalog of all content assets across types and channels. An audit is the qualitative assessment layered on top of it [S1] [S41] [C1]. NN/g defines an inventory as "a list of every piece of digital content you currently have" and says an audit "examines, assesses, and evaluates the quality of the content listed in the inventory" [S2] [C1].

**Inputs and fields.** Typical inventory fields are the title, URL, owner or author (including whether the content is user-generated or imported), topic, format, created or modified date, metadata (page title, meta description, alt text) and where the source files live [S2] [C2].

**Automated collection.** Crawlers and CMS exports can fill in titles, dates, authors and metadata, and a CMS can keep the inventory current. NN/g still holds that people should do the audit assessment [S2] [C3].
- Screaming Frog finds orphan pages by crawling the XML sitemaps listed for a site and joining Google Analytics and Search Console data to the crawl. A URL that is never reached through internal links has no crawl-depth value, so a blank depth flags an orphan [S3] [C4].
- The sitemaps.org protocol requires `<loc>` and makes `<lastmod>` optional [S7] [C8]. Google says `lastmod` should mean the "last significant modification" and should track reality. So sitemap dates are a weak proxy for content freshness unless the publisher keeps them honest [S8] [C8].

**Audit method.** NN/g's sequence is as follows [S2] [C10] [C33]:
1. Set ownership.
2. Start with the most-visited content or the content behind top tasks.
3. Choose a scope: a whole site, a section or one journey.
4. Fill in details from the CMS, analytics and, when needed, user research. Flag uncertain items for the team instead of over-analyzing them.
5. Rate quality as high, mediocre or low against web-writing best practice and organizational standards.
6. Give each item a status of keep, update or remove, with an owner.
7. Maintain the inventory continuously.

NN/g suggests timeboxing the first pass to about six weeks [S2] [C10].

**ROT analysis.** ROT is Redundant, Outdated (or Obsolete), Trivial. Kevin Parker, writing on AIIM's forum, notes that "Outdated" is the usual word for web content and "Obsolete" for enterprise information [S9] [C9]. Richard Surber, also on AIIM's forum, defines ROT as information kept for no valid business, legal or common-practice purpose: duplicates of official records, material past its useful life, or material that is not a record [S10] [C9]. In an audit, ROT becomes the remove or merge side of the keep/update/remove decision [S2] [S9] [C10].

**Scoring rubric.** Fred Leise's eleven content-analysis heuristics give a ready-made qualitative rubric: collocation, differentiation, completeness, information scent, bounded horizons, accessibility, multiple access paths, appropriate structure, consistency, audience relevance and currency. Each can be scored on an optional five-point scale from 1 (strongly deviates) to 5 (strongly conforms). Leise says the results show general trends and are "not statistically valid in the strict sense." He suggests a second reviewer to validate them [S11] [C11].

**Outputs and the IA decisions they inform.** The outputs are an inventory spreadsheet, audit scores, and keep/update/remove lists. They inform migration scope, which content to consolidate, the content types and templates, and the raw material for the taxonomy [S2] [S16] [C1] [C15].

**Limits.** Automated fields describe content's form, not its quality [S2] [C3]. Sitemap dates can be wrong [S8] [C8]. Rubric scores are one evaluator's judgment [S11] [C11].

### 3. Structural analysis: link graph, depth, orphans, duplicates

**Method and tools (Screaming Frog as the documented example).**
- *Crawl depth* is the number of clicks from the start page, with redirects counted as a level. The tool flags high-depth pages at depth 4 or more by default [S4] [S5] [C5].
- *Unique inlinks* count each linking page once [S4] [C5].
- *Link Score* is a 0 to 100 internal-PageRank-style figure computed after the crawl. It takes account of redirects, canonicals and nofollow, and it weighs how important each linking page is, how many links that page has, and how far it is from the home page [S4] [C7].
- *Duplicate detection:* MD5 hashing finds exact duplicates. MinHash finds near-duplicates at a default 90% text-similarity threshold [S6] [C6].
- *Orphans:* as described in section 2 [S3] [C4].

**Decisions informed.** Flattening deep branches, deciding where to cross-link, consolidating duplicates, and rehoming or retiring orphans [S4] [S5] [S6] [C5] [C6] [C7].

**Limits.** Near-duplicate matching works on words, so it misses pages that say the same thing in different words [S6] [C6]. Link Score models how link equity flows, not whether people can find the page [S4] [C7].

### 4. Corpus and text analysis, and bottom-up taxonomy derivation

**What it is.** Heather Hedden presents content analysis and term extraction as the ways to fit a taxonomy to its content, and user interviews as the way to fit it to its users [S15] [C14]. This is literary warrant [S12] [C12].

**Method (from NN/g's taxonomy process).** [S16] [C15]
1. Inventory and audit the content first.
2. Look for an existing standard taxonomy for the domain, for example through BARTOC.org, and check the licensing.
3. Mine the keywords and topics already in the CMS.
4. Draw concepts from the content, from subject-matter experts and from key business terms.
5. For each concept, record its variant terms and **where the concept came from**.
6. Drop concepts that cover only one piece of content.
7. Choose a preferred term and record nonpreferred variants.
8. Build the hierarchy and related-term links.
9. Review the draft with stakeholders.
10. Apply it to content, and check AI-generated tags by hand.
11. Set up governance.

**Automated and LLM-assisted pipelines.** Microsoft's TnT-LLM has an LLM generate and refine a label taxonomy directly. Its baselines embed the documents, cluster them, and have an LLM name the clusters. Evaluation covers coverage (measured through an "Other" bucket), label accuracy, and agreement between human and LLM raters (kappa) [S17] [C16]. Zhu et al. (2025) report that plain clustering and direct LLM prompting often lack coherence and the right granularity. They generate aspect-specific summaries with an LLM and cluster those instead. They score the result with NMI, ARI and purity, plus human ratings of coverage, relevance, structure, validity and adequacy [S18] [C16] [C17]. A poster on Portuguese news found that an LLM merging topics from keywords alone sometimes merged clusters that sat far apart in embedding space [S19] [C17].

**Outputs and decisions informed.** The outputs are candidate term lists, concept clusters and draft hierarchies, each concept traceable to its source. They inform facets, category labels, tagging vocabularies and auto-classification rules [S16] [S17] [C15] [C16].

**Limits.** These methods find what the content talks about, not what users want. NN/g therefore makes "user relevance" an explicit filter, and asks for a user-friendly preferred term, with jargon kept as a nonpreferred synonym [S16] [C15]. Model output needs human review, especially for ambiguous or high-impact branches [S17] [S18] [C16] [C17].

### 5. Search log analysis

**What it is.** Lou Rosenfeld presents site search analytics, the analysis of query data from a site's own search engine, as a user research tool. The core log fields are the query, how often it was searched, and how many results it returned [S21] [C18]. His workshop splits the work into pattern analysis, failure analysis (zero and low results) and session analysis. The minimum fields are IP address, timestamp, query and result count [S22] [C20].

**Method (Susan Farrell, NN/g, 2017).** [S20] [C18]
1. Take several months of logs.
2. Rank roughly the top 1,000 queries and review the top 300, grouping synonyms by meaning or task.
3. Pull out frequent zero-result queries, which are usually misspellings or missing content.
4. Read the longest queries for stated needs.
5. Sort by user and time to see query sequences. Repeated, related queries mean the earlier ones failed.
6. Note blank, numeric and non-ASCII queries.
7. Rerun the top queries and check whether the first results page holds the right content.

On tooling: plain Google Analytics site-search reports do not separate zero-result searches, so tracking them takes a custom event [S23] [C21].

**Decisions informed.** Navigation labels, cross-links and groupings; synonyms and best bets; content gaps; and matching brand terms to generic terms [S20] [C18].

**Limits.** Logs show *what* people searched for, not *why*. Shared IP addresses and bots distort counts, sessions can only be approximated, and logs hold personal data that should be de-identified, encrypted, access-limited and deleted after use [S20] [C19]. Follow-up research is needed to confirm what the patterns mean [S20] [C19].

### 6. Analytics and behavioral data (existing data only)

**Method.** Whitenton and Sherwin (NN/g, 2016) list five IA warning signs in existing analytics [S24] [C22]:
- low traffic to a category (use unique views);
- low conversions;
- high bounce rates on category landing pages;
- low entrance rates;
- heavy search volume for terms that already have a category.

**Limits they name.** Placement and repeated listings inflate traffic, so categories with very different prominence should not be compared. Conversions that span sessions or devices may be missed. Analytics cannot show visibility problems. Niche categories can serve real goals despite poor numbers [S24] [C22].

### 7. Heuristic and expert evaluation, competitive analysis, benchmarking

**Abby Covert's ten IA heuristics** are Findable, Accessible, Clear, Communicative, Useful, Credible, Controllable, Valuable, Learnable and Delightful. Each comes with a one-line definition, and they were drawn from a survey of academic work in human-centered design and information science. The page gives no scoring method; a separate workbook is sold for running evaluations [S25] [C23]. Leise's heuristics (section 2) are the content-focused counterpart and come with a five-point scale [S11] [C11].

**Rosenfeld's heuristics.** This run did not find a primary source for a Rosenfeld IA heuristics list. It is recorded as a gap (Appendix A).

**Competitive and comparative analysis.** Boxes and Arrows advises a high-level inventory of competitor sites, recording page or feature names and a short summary, rather than an exhaustive inventory [S26] [C24].

**Limits.** Heuristic scores are expert judgments with no inter-rater reliability built in [S11] [C11].

### 8. Standards and reference-vocabulary reuse; crosswalking

**Standards.** ISO 25964-1 (2011) covers building thesauri and replaced ISO 2788 and ISO 5964. ISO 25964-2 (2013) covers interoperability between thesauri and classification schemes, taxonomies and ontologies, including how to set up and maintain mappings. ISO last reviewed and confirmed Part 2 in 2023 [S27] [S28] [C25].

**Crosswalk mechanics.** SKOS defines five mapping properties: `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch` and `skos:relatedMatch`. `closeMatch` is symmetric and deliberately not transitive, so that similarity does not spread across contexts. `exactMatch` is transitive [S29] [S30] [C26].

**Reference vocabularies.**
- schema.org is a type tree rooted at `Thing`. Types rarely have more than one supertype, properties have no unified hierarchy, and terms removed from the core sit in an "attic" that publishers should not use. At the snapshot read, it listed 826 types and 1,540 properties [S31] [C27].
- NN/g advises checking for an industry-standard taxonomy before building one [S16] [C15].
- This run did not find primary material on reusing LCSH or industry classification schemes (Appendix A).

**Decisions informed.** The starting hierarchy, preferred terms, interoperability with outside systems, and structured-data markup [S16] [S27] [S31] [C15] [C25] [C27].

### 9. Mining existing organizational artifacts

The sources found describe this mainly as organizational warrant [S12] [C12]. NN/g lists existing CMS metadata, subject-matter experts and "key internal business terms" as concept sources [S16] [C15]. This run found no dedicated method sources for mining database schemas, APIs, support-ticket categories or regulatory requirements. Treat any such process as practitioner practice not documented here (Appendix A).

The main documented danger is copying the org chart. A Berkeley course summary of Rosenfeld and Morville cites Edward Tufte's observation that most sites mirror the organization's structure rather than users' information needs [S36] [C31]. An agency audit found sub-navigation that followed internal product names while users thought in terms of outcomes [S37] [C31]. Rosenfeld and Morville separate exact organization schemes (alphabetical, chronological, geographical) from ambiguous ones (topical, task, audience) [S36] [C32].

### 10. Metadata analysis and quality assessment

Bruce and Hillmann's 2004 framework has seven dimensions: completeness, accuracy, provenance, conformance to expectations, logical consistency and coherence, timeliness, and accessibility. Completeness, accuracy and consistency are the ones most used in later work [S32] [C28]. Applied to a CMS export, each field can be profiled for fill rate (completeness), allowed values (conformance) and consistent use across content types (consistency). That application is this report's synthesis of S32 and S2 [S32] [S2] [C28] [C33].

### 11. Validation proxies that avoid people

- **Retrieval evaluation with test query sets.** This uses the information-retrieval test-collection method: a document collection, a set of queries, and a relevance judgment for each query-document pair. Use at least about 50 information needs, measure precision and recall at rank cutoffs, and average across queries [S33] [S34] [C29]. For IA, the top queries from the search logs make a natural test set [S20] [C18].
- **Structural checks.** Crawl depth, orphan, near-duplicate and link-score reports can be rerun against a proposed structure (sections 2 and 3) [S3] [S4] [S6] [C4] [C5].
- **Findability simulation with AI.** NN/g reports that ChatGPT was not an acceptable stand-in for real users in tree testing, because it vastly outperformed most real people. It judges synthetic users useful for desk research and hypotheses but not for decisions [S35] [C30].
- **Governance metrics.** NN/g treats the inventory as continuously maintained, and Leise's currency heuristic calls for expiry dates and review schedules [S2] [S11] [C10] [C11].

### 12. Risks of IA built only from non-human evidence, and how to flag findings

**Known risks:**
- inside-out structure that mirrors the org chart [S36] [S37] [C31];
- internal jargon used as labels [S16] [S37] [C15] [C31];
- analytics artifacts read as user intent [S24] [C22];
- logs that show what users did but not why [S20] [C19];
- AI simulations that overstate how findable things are [S35] [C30].

**Mitigations the sources recommend:**
- record where each concept came from [S16] [C15];
- prefer user-friendly preferred terms and keep jargon as nonpreferred terms [S16] [C15];
- compare categories only when their prominence is similar [S24] [C22];
- treat log and analytics findings as hypotheses that need follow-up research [S20] [S24] [C19] [C22].

**Labeling recommendation (this report's synthesis).** Tag each finding with its warrant type and its validation status, using Z39.19's categories [S12] [C12]:
- *literary* (from content or standards);
- *organizational* (from internal artifacts);
- *indirect user* (from logs or analytics).

Mark it "not user-validated" until it is tested with people, and never count AI-simulated tests as user validation [S12] [S20] [S24] [S35] [C36].

## Conflicts

1. **Can automation do the audit assessment?** NN/g (Unconfirmed) says crawlers and CMS exports may fill the inventory, but people should do the qualitative audit [S2]. The TnT-LLM work (Unconfirmed) reports usable agreement between LLM and human raters on taxonomy labels and uses LLMs as evaluators [S17]. Zhu et al. (Unconfirmed) still use human reviewers alongside LLM reviewers [S18]. Effect: the findings treat LLM output as draft material that needs human review, not as a finished audit [C3] [C16].
2. **ROT wording.** Parker (Unconfirmed) prefers "Obsolete" for enterprise information and notes that "Outdated" is common for web content [S9]. Surber (Unconfirmed) uses "Obsolete" [S10]. Effect: the meaning is the same; this report uses "Outdated (or Obsolete)" [C9].
3. **Is Lambe's book a how-to guide?** The publisher's description (Unconfirmed) calls it a step-by-step guide [S38]. The Step Two review (Unconfirmed) says the methodology is not detailed enough to follow unaided [S39]. Effect: Lambe is cited only for framing, not for method steps [C34].

## Appendix A: Next searches

1. Run the citation test for the NN/g articles, Boxes and Arrows (Leise), AIIM's ROT posts and Bruce and Hillmann, to settle whether they are Reputable or Trusted. Many foundation claims currently rest on Unconfirmed labels for that reason alone.
2. Primary sources for mining organizational artifacts: support-ticket taxonomies, database and API schemas as IA input, and regulatory-requirement mapping.
3. Lou Rosenfeld's IA heuristics and Peter Morville's findability heuristics, from primary sources (louisrosenfeld.com, semanticstudios.com, *Ambient Findability*).
4. Reusing LCSH, NAICS/UNSPSC and other industry classification schemes as IA starting points, with licensing and adaptation guidance (Hedden's *The Accidental Taxonomist*, 3rd ed.).
5. Retrieval-evaluation practice applied to site search and IA: building test query sets from logs, and known-item findability metrics.

## Appendix B: Sources

### Source list

| ID | Citation | Label | Setting | Reason for label |
| --- | --- | --- | --- | --- |
| S1 | Paula Land, interviewed in "Content Inventory – Learn to Love Them," Content Marketing Institute, n.d., https://contentmarketinginstitute.com/articles/content-inventories-audits/ | Official | Organized | Land wrote the standard handbook on content audits and inventories (XML Press). The item gives her own definitions. |
| S2 | Anna Kaley, "Content Inventory and Auditing 101," Nielsen Norman Group, 2020-09, https://www.nngroup.com/articles/content-audits/ | Unconfirmed | Organized | Large audience. UXPin and HubSpot guides found in this run cite NN/g's approach (2 citations); the five-citation test was not completed. |
| S3 | Screaming Frog, "How to Find Orphan Pages," n.d., https://screamingfrog.co.uk/find-orphan-pages/ | Official | Organized | The vendor documenting its own tool's behavior. |
| S4 | Screaming Frog, "SEO Spider Tabs" user guide, n.d., https://www.screamingfrog.co.uk/seo-spider/user-guide/tabs/ | Official | Organized | The vendor documenting its own tool's metrics. |
| S5 | Screaming Frog, "Issues – Links: Pages With High Crawl Depth," n.d., https://www.screamingfrog.co.uk/seo-spider/issues/links/pages-with-high-crawl-depth/ | Official | Organized | The vendor documenting its own tool. |
| S6 | Screaming Frog, "Issues – Content: Near Duplicates," n.d., https://www.screamingfrog.co.uk/seo-spider/issues/content/near-duplicates/ ; "How To Check For Duplicate Content," https://www.screamingfrog.co.uk/how-to-check-for-duplicate-content/ | Official | Organized | The vendor documenting its own tool. |
| S7 | sitemaps.org, "Sitemaps XML format," n.d., https://sitemaps.org/protocol.html | Official | Organized | Owns the sitemap protocol. |
| S8 | Google Search Central, "Sitemaps ping endpoint is going away," 2023-06, https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping | Official | Organized | Owns how Google reads `lastmod`. |
| S9 | Kevin Parker, "Defining information ROT," AIIM Community, 2016-05-05, https://community.aiim.org/blogs/kevin-parker/2016/05/05/defining-information-rot | Unconfirmed | Individual | Personal post on the AIIM community forum, so not organizationally edited. It has an audience through AIIM; citations were not counted. |
| S10 | Richard Surber, "ROT: introduction and prevention tips," AIIM Community, 2017-09-05, https://community.aiim.org/blogs/richard-surber/2017/09/05/rot-introduction-prevention-tips | Unconfirmed | Individual | Same as S9. |
| S11 | Fred Leise, "Content Analysis Heuristics," Boxes and Arrows, 2007-03-12, https://boxesandarrows.com/content-analysis-heuristics/ | Unconfirmed | Organized | Edited IA magazine with an audience; citations not counted in this run. |
| S12 | ISKO Encyclopedia of Knowledge Organization, "Literary warrant," n.d., https://www.isko.org/cyclo/literary_warrant | Official | Organized | ISKO is the field's recognized scholarly authority for knowledge organization. Used for the Z39.19-2005 warrant definitions it reports. |
| S13 | NISO, "NISO releases new standard for vocabulary control" (Z39.19-2005), 2005-11, https://www.niso.org/press-releases/2005/11/niso-releases-new-standard-vocabulary-control | Official | Organized | The standards body that owns Z39.19. |
| S14 | ASIS&T standards mailing list, "Z39.19 Re: Upcoming vote," 2016-01, https://asist-archive.ischool.illinois.edu/asis-standards/2016-January/000555.html | Unconfirmed | Community | A professional standards mailing list discussing this standard's review ballot. Used only for the review status (reaffirmed 2010, revision proposed). |
| S15 | Rutgers Business School / WIAA, "Custom Taxonomy Creation" (Heather Hedden talk), 2023, https://mbs.rutgers.edu/events/custom-taxonomy-creation | Unconfirmed | Organized | An event listing summarizing Hedden's talk; the listing itself was not tested for citations. |
| S16 | Page Laubheimer, "Taxonomy 101," Nielsen Norman Group, 2022-07-03, https://www.nngroup.com/articles/taxonomy-101/ | Unconfirmed | Organized | Large audience; citation test not completed. |
| S17 | Wan et al. (Microsoft), "TnT-LLM for Automated Taxonomy Generation," HackerNoon mirror, n.d., https://hackernoon.com/tnt-llm-for-automated-taxonomy-generation-outperforming-clustering-baselines | Unconfirmed | Organized | A mirror of a research paper. Cited as a comparison point by the TaxCE and Zhu et al. papers found in this run (2 citations seen). |
| S18 | Zhu et al., "Context-Aware Hierarchical Taxonomy Generation for Scientific Papers via LLM-Guided Multi-Aspect Clustering," arXiv, 2025, https://arxiv.org/pdf/2509.19125 | Unconfirmed | Organized | A preprint; citations not counted. |
| S19 | "TaxonomAI: Leveraging LLM for Automated Taxonomy Construction" (poster), Universidade NOVA de Lisboa, n.d., https://run.unl.pt/bitstream/10362/175558/1/TaxonomAI_Leveraging_LLM_for_Automated_Taxonomy_Construction_poster_.pdf | Unconfirmed | Organized | A university repository poster; small audience. |
| S20 | Susan Farrell, "Search-Log Analysis: The Most Overlooked Opportunity in Web UX Research," Nielsen Norman Group, 2017-07-30, https://www.nngroup.com/articles/search-log-analysis/ | Unconfirmed | Organized | Large audience; citation test not completed. |
| S21 | Rosenfeld Media, "Now on sale: Search Analytics for Your Site" (Louis Rosenfeld), 2011, https://rosenfeldmedia.com/?p=183965 | Official | Organized | Rosenfeld co-wrote the field's foundational IA text and co-founded the IA Institute (see S42). This is his book on the subject. |
| S22 | Louis Rosenfeld, "Site Search Analytics" workshop slides, SlideShare, 2010, https://www.slideshare.net/slideshow/site-search-analytics-workshop-presentation/323514 | Official | Individual | The same authority's own material on the subject. |
| S23 | Fulcrum Technologies, "Using Google Analytics to Track 'Zero Results Found' for Site Searches," n.d., https://fulcrumtech.net/blog/using-google-analytics-to-track-zero-results-found-for-site-searches/ | Unconfirmed | Organized | A vendor tutorial with a small audience. |
| S24 | Kathryn Whitenton and Katie Sherwin, "5 Information Architecture Warning Signs in Your Analytics Reports," Nielsen Norman Group, 2016-09-25, https://www.nngroup.com/articles/ia-warning-signs-analytics/ | Unconfirmed | Organized | Large audience; citation test not completed. |
| S25 | Abby Covert, "Information Architecture Heuristics," abbycovert.com, n.d., https://abbycovert.com/ia-tools/ia-heuristics/ | Official | Individual | Owns this heuristic set; former president of the IA Institute. |
| S26 | Boxes and Arrows, "Competitive Analysis: Understanding the Market Context," n.d., https://boxesandarrows.com/competitive-analysis-understanding-the-market-context/ | Unconfirmed | Organized | Edited IA magazine; citations not counted. |
| S27 | NISO, "ISO 25964 – the international standard for thesauri and interoperability with other vocabularies," n.d., https://niso.org/schemas/iso25964 | Official | Organized | Hosts the ISO 25964 committee pages. |
| S28 | ISO, "ISO 25964-2:2013," n.d., https://www.iso.org/standard/53658.html?browse=tc | Official | Organized | Owns the standard. |
| S29 | W3C, SKOS Core vocabulary, namespace document, https://www.w3.org/2004/02/skos/core.html | Official | Organized | Owns SKOS. This namespace file serves the current (2009 Recommendation) vocabulary; the normative SKOS Reference text itself was not opened. |
| S30 | Baker et al., "Key Choices in the Design of Simple Knowledge Organization System (SKOS)," arXiv, 2013, https://arxiv.org/pdf/1302.1224 | Unconfirmed | Organized | Written by the SKOS designers but not normative; citations not counted. |
| S31 | schema.org, "Schemas" and "Full schema hierarchy," n.d., https://schema.org/docs/schemas.html ; https://schema.org/docs/full.html | Official | Organized | Owns the vocabulary. |
| S32 | Thomas R. Bruce and Diane I. Hillmann, "The Continuum of Metadata Quality," in *Metadata in Practice*, ALA Editions, 2004 (as described in search results; chapter not opened) | Unconfirmed | Organized | Search results described several papers using it as a benchmark (UNT, FSU, FBK and others), but they were not opened, so the five-citation test is unverified. |
| S33 | M. Beigy, "Lecture 8: Evaluation" (after Manning, Raghavan and Schütze), Sharif University, n.d., https://sharif.edu/~beigy/courses/14032/40324/Lect-8.pdf | Unconfirmed | Organized | Course slides restating a standard textbook. |
| S34 | CUHK SEEM5680, "Evaluation" lecture, 2022, https://www1.se.cuhk.edu.hk/~seem5680/lecture/evaluation-2022spring.pdf | Unconfirmed | Organized | Course slides. |
| S35 | Nielsen Norman Group, "Synthetic Users: If, When, and How to Use AI-Generated 'Research'," n.d., https://www.nngroup.com/articles/synthetic-users/ | Unconfirmed | Organized | Large audience; citation test not completed. |
| S36 | UC Berkeley SIMS 290-2, "Information Design" course notes (summarizing Rosenfeld and Morville), 1998, https://courses.ischool.berkeley.edu/i290-2/f98/InfoDesign | Unconfirmed | Organized | A course page that summarizes the primary text and cites Tufte second-hand. |
| S37 | Axelerant, "Navigation reflects org chart, not customer," n.d., https://www.axelerant.com/blog/navigation-reflects-org-chart-not-customer | Unconfirmed | Organized | An agency blog with a small audience. |
| S38 | Elsevier/Chandos, *Organising Knowledge* (Patrick Lambe) product page, 2007, https://shop.elsevier.com/books/organising-knowledge/lambe/978-1-84334-227-4 | Unconfirmed | Organized | A publisher blurb, not the text. |
| S39 | Step Two Designs, review of *Organising Knowledge*, n.d., https://steptwo.com.au/?p=2394 | Unconfirmed | Organized | A consultancy review; citations not counted. |
| S40 | Rosenfeld, Morville and Arango, *Information Architecture: For the Web and Beyond*, 4th ed., O'Reilly, 2015, https://www.oreilly.com/library/view/-/9781491913529 | Official | Organized | The field's foundational text, newest edition. |
| S41 | XML Press, "Content Audits and Inventories" (Paula Land), n.d., https://xmlpress.net/content-strategy/audits-and-inventories/ | Official | Organized | The publisher page for the recognized handbook on the subject. |
| S42 | Wikipedia, "Louis Rosenfeld," n.d., https://en.wikipedia.org/wiki/Louis_Rosenfeld | Unconfirmed | Community | Used only to support the authority judgment for S21, S22 and S40; backs no claim. |

### Claim map

- **Foundation claims by strongest source:** 12 foundation claims: 5 backed by an Official source (C1, C4, C12, C18, C25), 0 by Reputable or Trusted at best, 7 by Unconfirmed only.
- **Weak foundations:** C9 rests only on Unconfirmed sources (AIIM forum posts). C15 rests only on an Unconfirmed source (NN/g taxonomy article). C16 rests only on Unconfirmed sources (preprints and a mirror). C19 rests only on an Unconfirmed source (NN/g). C22 rests only on an Unconfirmed source (NN/g). C30 rests only on an Unconfirmed source (NN/g). C31 rests only on Unconfirmed sources (a course page and an agency blog).
- **Sources by label:** 18 official, 0 reputable, 0 trusted, 24 unconfirmed, 0 ignored.

| ID | Claim | Sources | Role | Depends on |
| --- | --- | --- | --- | --- |
| C1 | An inventory is a quantitative catalog of content assets; an audit is the qualitative assessment of that content. | S1 (Official), S41 (Official), S2 (Unconfirmed) | Foundation | none |
| C2 | Typical inventory fields are title, URL, owner, topic, format, date, metadata and source location. | S2 (Unconfirmed) | Support | C1 |
| C3 | Crawlers and CMS exports can fill the inventory, but people should do the audit assessment. | S2 (Unconfirmed) | Support | C1 |
| C4 | Screaming Frog finds orphans by joining sitemap, analytics and Search Console URLs to the crawl; orphans have no crawl depth. | S3 (Official) | Foundation | none |
| C5 | Crawl depth counts clicks from the start page (redirects count as a level), high-depth pages are flagged at 4 or more, and unique inlinks count each linking page once. | S4 (Official), S5 (Official) | Support | C4 |
| C6 | MD5 finds exact duplicates and MinHash finds near-duplicates at a 90% default threshold; word-based matching misses pages that are similar in meaning but worded differently. | S6 (Official) | Detail | none |
| C7 | Link Score is a 0 to 100 internal-PageRank-style figure that accounts for redirects, canonicals and nofollow. | S4 (Official) | Detail | none |
| C8 | Sitemaps require `loc` and make `lastmod` optional; Google reads `lastmod` as the last significant modification. | S7 (Official), S8 (Official) | Detail | none |
| C9 | ROT means Redundant, Outdated or Obsolete, Trivial: content kept for no valid business, legal or common-practice purpose. | S9 (Unconfirmed), S10 (Unconfirmed) | Foundation | none |
| C10 | NN/g's audit rates quality high/mediocre/low, assigns keep/update/remove with owners, timeboxes the first pass, and maintains the inventory continuously. | S2 (Unconfirmed), S9 (Unconfirmed) | Support | C1, C9 |
| C11 | Leise's eleven content-analysis heuristics can be scored on a five-point scale and give qualitative, not statistically valid, results. | S11 (Unconfirmed) | Detail | none |
| C12 | Z39.19-2005 defines literary, user and organizational warrant as the bases for selecting terms. | S12 (Official), S13 (Official) | Foundation | none |
| C13 | Z39.19-2005 was reaffirmed in 2010, a revision was proposed in 2016, and no newer edition was confirmed. | S14 (Unconfirmed) | Detail | none |
| C14 | Content analysis and term extraction fit a taxonomy to its content; interviews fit it to its users. | S15 (Unconfirmed) | Support | C12 |
| C15 | NN/g's taxonomy process starts from the inventory, existing standards and CMS metadata, records each concept's origin, drops single-item concepts, and keeps jargon as nonpreferred terms. | S16 (Unconfirmed) | Foundation | C1, C12 |
| C16 | LLM and clustering pipelines can generate candidate taxonomies, evaluated by coverage, label accuracy and agreement between human and LLM raters. | S17 (Unconfirmed), S18 (Unconfirmed) | Foundation | none |
| C17 | Plain clustering and LLM prompting can lack coherence and granularity, and LLMs can merge clusters that are far apart. | S18 (Unconfirmed), S19 (Unconfirmed) | Support | C16 |
| C18 | Site search log analysis (top queries, zero results, sessions, rerunning top queries) is a user research tool for IA. | S21 (Official), S20 (Unconfirmed) | Foundation | none |
| C19 | Search logs show what people searched for, not why; they are distorted by shared IPs and bots and hold personal data. | S20 (Unconfirmed) | Foundation | C18 |
| C20 | Rosenfeld splits log analysis into pattern, failure and session analysis, using IP, timestamp, query and result count. | S22 (Official) | Support | C18 |
| C21 | Plain Google Analytics site-search reports do not separate zero-result searches without a custom event. | S23 (Unconfirmed) | Detail | none |
| C22 | Five analytics warning signs flag IA problems, but prominence, incomplete conversion data and invisible layout issues can mislead. | S24 (Unconfirmed) | Foundation | none |
| C23 | Covert's ten IA heuristics come from a survey of academic work and have no scoring method on the page. | S25 (Official) | Detail | none |
| C24 | Competitive analysis should use a high-level inventory of competitor sites rather than an exhaustive one. | S26 (Unconfirmed) | Detail | none |
| C25 | ISO 25964-2 (confirmed 2023) covers mappings between thesauri and other vocabularies. | S27 (Official), S28 (Official) | Foundation | none |
| C26 | SKOS defines five mapping properties; closeMatch is not transitive and exactMatch is transitive. | S29 (Official), S30 (Unconfirmed) | Support | C25 |
| C27 | schema.org is a `Thing`-rooted type tree in which multiple supertypes are rare and removed terms move to the attic. | S31 (Official) | Detail | none |
| C28 | Bruce and Hillmann's seven metadata quality dimensions; completeness, accuracy and consistency are the most used. | S32 (Unconfirmed), S2 (Unconfirmed) | Detail | none |
| C29 | Retrieval evaluation needs a collection, a query set and relevance judgments, uses about 50 or more needs, and measures precision and recall at rank cutoffs. | S33 (Unconfirmed), S34 (Unconfirmed) | Detail | none |
| C30 | AI-simulated users vastly outperformed real people in tree testing and are fit only for hypotheses. | S35 (Unconfirmed) | Foundation | none |
| C31 | IA drawn from internal structure tends to mirror the org chart and internal naming rather than user needs. | S36 (Unconfirmed), S37 (Unconfirmed) | Foundation | none |
| C32 | Rosenfeld and Morville separate exact organization schemes from ambiguous ones (topic, task, audience). | S36 (Unconfirmed) | Support | C31 |
| C33 | NN/g fills audit details from the CMS, analytics and, when needed, user research, and flags uncertain items. | S2 (Unconfirmed) | Support | C1 |
| C34 | Lambe treats taxonomies as central to organizational coordination and gives a methodology rather than a manual. | S38 (Unconfirmed), S39 (Unconfirmed) | Detail | none |
| C35 | The 4th edition of the IA text runs from research to strategy, design and implementation across organization, labeling, navigation, search and metadata. | S40 (Official) | Detail | none |
| C36 | Non-human IA findings should be tagged by warrant type and marked not user-validated, and AI simulations should not count as validation. | S12 (Official), S20 (Unconfirmed), S24 (Unconfirmed), S35 (Unconfirmed) | Support | C12, C15, C19, C22, C30, C31 |
