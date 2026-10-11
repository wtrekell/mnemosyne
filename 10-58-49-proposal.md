# Proposal: The Researcher

Source: voice note `10-58-49.md`, recorded 2026-10-11.

## What it is

A researcher that finds information, judges how far to trust it, and writes a report that shows exactly where every part came from. It replaces the current researcher.

It does more than one kind of research, so it carries a separate set of instructions for each kind and picks the right one for the request.

## What it does

### 1. Topic research

Gathers what is known about a subject.

### 2. Build research

When asked "I need something that does X," it finds the existing tools and code libraries that could do it, in the language the project already uses. A Python project gets Python options; a TypeScript project gets TypeScript or Node options.

### 3. Feeding later work

Its findings must be usable as the starting point for other work, such as writing a full build plan. That later work is not designed yet, so the researcher's output should be easy to hand off.

## How it judges sources

Every source gets one of five labels.

| Label | Meaning | Example |
| --- | --- | --- |
| **Official** | The owner of the subject. | Anthropic's docs for Claude Code. Google's docs for Antigravity. Nielsen Norman Group for UX research. |
| **Trusted** | Widely cited by other organizations (not individuals or social posts). Rough test: five or more such references. | arXiv for how AI agents behave in general. An Anthropic employee's blog post that many people comment on and link to. |
| **Unconfirmed** | A single voice with a real audience. Worth reading, not worth relying on alone. | A blogger with a good following and active comments. |
| **Public talk** | Social media and forums. Not proof of how things work, but good evidence of what people struggle with, ask about, and want. | Posts asking how to use agents or complaining about them. |
| **Ignore** | A single voice no one cites or responds to. | A blog with no followers or links, including the user's own blog for now. |

Rules that go with the labels:

- **Newer wins.** On the same subject, something written yesterday counts for more than something written a year ago.
- **A subject can have more than one official source.**
- **Public talk needs a method.** Social media covers a subject from many angles (problems, questions, uses). The researcher should sort these with a set method. Six Thinking Hats is one candidate; picking the method is itself a research task.

## What the report contains

1. **The findings.**
2. **Quotes where they matter.** Some material is best given word for word, and there will be a lot of it. The researcher must also avoid padding the report with long copied passages. It quotes when the exact wording matters and summarizes, with a citation, when it doesn't.
3. **A source appendix**, a report on the report:
   - Every source used, with its label and date.
   - Which source backs each paragraph.
   - How much of the report each label accounts for, for example "65% official, 25% trusted, 10% public talk."

Nothing that shaped the report should be hidden.

## How to build it

The voice note is a starting point, not a full plan. Before building:

1. Answer the open questions below.
2. Clean up and organize the requirements.
3. Then build.

## Open questions

1. **The five-citation test.** Is five the right number? Does it change by subject?
2. **Who sets the official sources?** A fixed list per subject that you keep, or does the researcher decide each time and show its reasoning?
3. **How much newer is "newer"?** Is there a cutoff after which a source is too old to use, or does age only lower its weight?
4. **Old official vs. new trusted.** When a year-old official source conflicts with last week's trusted source, which wins?
5. **Measuring the percentages.** By word count, by number of claims, or by paragraph?
6. **Method for public talk.** Research Six Thinking Hats and alternatives first, or start with Six Thinking Hats and revisit?
7. **The build-plan step.** Is it part of this researcher, or a separate tool that takes the researcher's output?
8. **Where reports go.** Which folder in this repository, and in what format?
9. **Other kinds of research.** Are there more besides topic and build research to plan for now?
