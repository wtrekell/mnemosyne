---
name: <Report title>
topic: <The subject researched>
type: <general, or the skill used, for example research-build>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# <Report title>

## Findings

<Statements of what was found, organized in whatever subsections the subject needs. Each statement cites every source that informs it, in the text, using the source's ID, and carries its claim ID from the claim map, for example [S1] [S3] [C2]. Summarize by default; quote only when a quote earns its place. Quotes make up no more than 10% of the report's words.>

## Conflicts

<One entry per conflict: the question in dispute, each position with its source IDs and labels, and how the disagreement affected the findings. Write "None" if there are no conflicts.>

## Appendix A: Next searches

<Up to five, as many as are worth doing. Each goes deeper into the topic or covers a related topic worth knowing.>

1. <Search>

## Appendix B: Sources

### Source list

<Every source, as a standard citation that includes its date. Add columns when the loaded skill calls for them.>

| ID | Citation | Label | Setting | Reason for label |
| --- | --- | --- | --- | --- |
| S1 | <Author, "Title," Publisher, date, URL> | <Official / Reputable / Trusted / Unconfirmed / Ignore> | <Organized / Individual / Community> | <Why; for Reputable and Trusted, list the five or more citing sources> |

### Claim map

<Summary, using counts.>

- **Foundation claims by strongest source:** <N foundation claims: N backed by an Official source, N by Reputable or Trusted at best, N by Unconfirmed only.>
- **Weak foundations:** <Name each, for example "C3 rests only on an unconfirmed source." A foundation claim is weak when all its sources are Unconfirmed. Write "None" if there are none.>
- **Sources by label:** <N official, N reputable, N trusted, N unconfirmed, N ignored.>

<One row per claim. Every claim ID appears in Findings, and every claim ID in Findings has a row. Role follows from Depends on: Foundation = at least one other claim lists it; Support = it lists another claim and no claim lists it; Detail = it lists no claim and no claim lists it.>

| ID | Claim | Sources | Role | Depends on |
| --- | --- | --- | --- | --- |
| C1 | <One sentence.> | <S1 (Official)> | <Foundation / Support / Detail> | <Claim IDs, or none> |

## Related reports

<Include only when this report follows up on an earlier report's Appendix A suggestion; otherwise delete this section. Link back to that report, and edit its Appendix A entry to link forward to this one. Change its `updated` date.>

- Follows: <link to earlier report>
