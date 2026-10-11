# Proposal: The Researcher

Source: voice note `10-58-49.md`, recorded 2026-10-11. Revised the same day with your feedback.

## What it is

A researcher that finds information, judges how far to trust it, and writes a report that shows exactly where every part came from. It replaces the current researcher.

It does more than one kind of research, so it carries a separate set of instructions for each kind and picks the right one for the request.

## What it does

### 1. Topic research

Gathers what is known about a subject.

### 2. Build research

When asked "I need something that does X," it finds the existing tools and code libraries that could do it, that work in the programming language the project already uses.

### 3. Feeding later work

Its findings must be usable as the starting point for other work, such as writing a full build plan. That later work is not designed yet, so the researcher's output should be easy to hand off.

## How it judges sources

### The citation test

A source passes when **five or more other sources cite it**, and none of those five are Public talk or Ignore. This test separates Reputable and Trusted sources from Unconfirmed ones.

### Labels

| Label | Who | Bar | Example |
| --- | --- | --- | --- |
| **Official** | The owner of the subject. | Owns it. No test needed. | A product's documentation, published by the company that makes it. The recognized standards body or research group for a field. |
| **Reputable** | An organization. | Passes the citation test. | A research archive that other institutions cite on a subject. A company's guide that five other organizations cite. |
| **Trusted** | An individual. | Passes the citation test. | A blog post by an engineer at the company that makes a product, cited by five or more qualifying sources. |
| **Unconfirmed** | An organization or individual. | Has an audience but fails the citation test. | A blogger with a large following and active comments but fewer than five qualifying citations. |
| **Public talk** | Anyone speaking in public. | See the levels below. | A recorded talk, a blog post, a forum thread. |
| **Ignore** | A single source with no citations or responses. | Meets none of the bars above. | A blog with no followers, comments, or links to it. |

### Public talk levels

Public talk is ranked by the quality of the setting.

1. **Talks given on a selective stage.** Recorded talks and conference presentations where organizers chose the speaker. The selection step adds value.
2. **Blogs and articles.** Less value. They still go through the citation test, so a blog post can rise to Trusted or Reputable, or fall to Ignore.
3. **Social media and forums.** Not a reliable account of how things work, but a record of the problems, questions, and requests people raise. The researcher sorts this material with a set method that looks at a subject from several fixed viewpoints. The voice note names one such method; choosing the method is itself a research task.

### Age

On the same subject, newer counts for more.

| Age | Value |
| --- | --- |
| Under 3 months | High |
| 3 to 9 months | Moderate |
| Over 9 months | Low |

### Other rules

- A subject can have more than one official source.

## What the report contains

1. **Front matter.** Details to be decided (see open questions).
2. **Findings**, with quotes placed inside the text where they apply, not collected separately.
3. **Appendix A: Next searches.** Up to five suggested searches. Each one either goes deeper into the topic or covers a related topic worth knowing.
4. **Appendix B: Sources.** A report on the report:
   - Every source used, with its label, level (for public talk), and date.
   - Which source backs each paragraph.
   - How much of the report each label accounts for, for example "65% official, 25% reputable, 10% public talk."

Nothing that shaped the report should be hidden.

### Links between reports

When one of the Appendix A searches is carried out, the two reports must link to each other. The new report links back to the report that suggested it, and that report's Appendix A entry links forward to the new one.

### When to quote

Quote when the exact words matter. Summarize and cite when only the idea matters.

**Quote:**

- Definitions and official statements of how something works.
- Rules, limits, and requirements, where rewording could change the meaning.
- Commands, settings, file names, and code.
- Exact numbers and dates.
- A person's stated opinion, when the report credits that opinion to them.
- Claims that are surprising or disputed, so the reader can judge the original wording.

**Do not quote:**

- Background or general explanation that a summary covers.
- Promotional language and repeated content.
- Anything labeled Ignore.
- Social media posts used only to show a pattern. Summarize the pattern instead, with one short example post at most.
- Long passages. Keep a quote to the few sentences that matter and cite the rest.

## How to build it

The voice note is a starting point, not a full plan. Before building:

1. Answer the open questions below.
2. Clean up and organize the requirements.
3. Then build.

## Open questions

1. **Front matter.** Which fields should every report carry? Some likely options: date, topic, type of research, overall trust mix, and links to parent and child reports.
2. **Who sets the official sources?** A fixed list per subject that you keep, or does the researcher decide each time and show its reasoning?
3. **Do talks count toward the citation test?** A talk on a selective stage is Public talk, but at the highest level. Should stage talks count as one of the five?
4. **Age of official documents.** Official docs are often updated quietly. Should age be measured from when a page was first published or from when it was last updated? Should stable official docs lose value with age at all?
5. **Old official vs. new reputable.** When a year-old official source conflicts with last month's reputable source, which wins, or does the report show both?
6. **Measuring the percentages.** By word count, by number of claims, or by paragraph?
7. **Quote limits.** Should there be a cap on quote length, or on how much of a report can be quoted?
8. **Method for social media and forums.** Compare several viewpoint methods first, or start with the one named in the voice note and revisit later?
9. **Changing old reports.** Adding forward links means editing a finished report. Is that acceptable, or should links live in a separate index?
10. **The build-plan step.** Is it part of this researcher, or a separate tool that takes the researcher's output?
11. **Where reports go.** Which folder in this repository?
12. **Other kinds of research.** Are there more besides topic and build research to plan for now?
