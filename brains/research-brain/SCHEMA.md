# Wiki Schema

This directory is an LLM-maintained wiki (see `llm-wiki.md` for the pattern). It belongs to exactly one agent, the owner registered for it in the host repository's `.claude/skills/wiki/registry.yaml`. If you are reading this, you are that owner: you do all writing, cross-referencing, and bookkeeping. The human drops sources into `raw/` and asks questions through you; your own tasks may also capture material that meets this wiki's criteria. No other agent or session can reach this directory, so nobody else will fix what you leave broken.

`WIKI.md` says what this wiki is for and what may be captured into it. Read it before capturing anything.

All paths here are relative to the wiki root (the directory holding this file). Commands are written as `python3 tools/wiki.py ...`; from anywhere else, prefix the wiki path (`python3 <wiki>/tools/wiki.py ...`). The tool finds its own root, but path arguments such as `status <path>` are resolved from your working directory.

## Layers

| Path | Owner | Rule |
| --- | --- | --- |
| `WIKI.md` | human | This wiki's purpose, scope, and capture criteria. Follow it; propose changes, don't make them. |
| `SCHEMA.md` | human | This file. Propose changes when a workflow isn't working. |
| `CLAUDE.md` | human | Entry point: who owns this wiki and what to read first. Before install it holds the install steps instead. |
| `llm-wiki.md` | human | The pattern this wiki implements. Read-only reference; summarized in `wiki/sources/llm-wiki.md`. |
| `raw/` | both | Write-once sources. You may add new captures under the Capture rules below; never modify or delete an existing file. Images live in `raw/assets/`. |
| `wiki/` | you | All pages live here. You create and edit freely. |
| `tools/wiki.py` | template | Helper CLI: `search`, `lint`, `new`, `backlinks`, `status`, `captured`, `provenance`, `log`, `digest`, `eval`, `reindex`, `doctor`. Backed by a SQLite/FTS5 index in `.wiki.db` (derived, not versioned), synced on every command. Safe to delete; `reindex --full` rebuilds it. `raw/` baselines are loaded from `raw-manifest.tsv`, so a rebuild never accepts raw changes. Don't edit the tool; report problems to the human. |
| `raw-manifest.tsv` | tool | Write-once baselines for `raw/` (path, size, sha256, source, captured, capture_method), maintained by `tools/wiki.py`. Never hand-edit it. A changed or missing raw file is a `lint` error until restored or accepted with `wiki.py reindex --accept-raw <path>`, which needs the human's agreement. |

## Wiki layout

- `wiki/index.md` — catalog of every page: `- [[page]] — one-line summary`, grouped by category. Update on every ingest and every filed answer.
- `wiki/log.md` — append-only chronology. Entry heading format: `## [YYYY-MM-DD] <op> | <title>` where op is `ingest`, `query`, `lint`, or `schema`. Body: bullets of pages created/updated.
- `wiki/overview.md` — the evolving top-level synthesis/thesis. Revise when new sources shift it.
- `wiki/sources/` — one summary page per raw source (`<slug>.md`), linking back to the file in `raw/`.
- `wiki/entities/` — people, orgs, products, places, characters.
- `wiki/concepts/` — ideas, themes, methods, topics.
- `wiki/analyses/` — filed answers: comparisons, syntheses, explorations worth keeping.

The wiki ships seeded with one ingested source, `llm-wiki.md`, and the pages built from it. Keep them; they document the pattern you are running.

## Page conventions

- Filenames: lowercase-kebab-case, unique across the whole wiki (links resolve by filename, not path).
- Links: Obsidian wikilinks `[[page-name]]` or `[[page-name|label]]`. Link generously; every page should have inbound links. Links resolve only within this wiki.
- Every page starts with YAML frontmatter:

  ```yaml
  ---
  title: Human Readable Title
  type: source | entity | concept | analysis | overview
  description: What this page covers and when to consult it.
  aliases: [alt name, synonym]              # optional; searched with extra weight
  tags: [tag1, tag2]
  sources: [source-slug-1, source-slug-2]   # source pages supporting claims here
  updated: YYYY-MM-DD
  ---
  ```

- `description` is required: one or two sentences, written like a skill description, saying what the page covers and when to consult it. It is what search returns so a query can decide "open or skip" without reading the page. Write it at creation; revise it when the page's scope shifts. `aliases` (optional, inline or block list) lists alternate names and synonyms; they are indexed and searchable.
- Cite claims to source pages via `[[source-slug]]`. Mark uncertain claims and record contradictions explicitly (`> [!warning] Contradiction: ...` with links to both sides) rather than silently overwriting.
- Source pages additionally carry `raw: <path>` (normally `raw/<filename>`; it may point to another file in the wiki root, such as `llm-wiki.md`, which is treated as not a capture) and `ingested: YYYY-MM-DD` in frontmatter.

## Capture rules (writing to `raw/`)

You capture when the human gives you a URL or asks you to save something, or when your own work turns up material that meets the criteria in `WIKI.md`. The human may also drop files in directly.

- **Criteria first.** Check the material against `WIKI.md`. Every "Capture when" item must hold and no "Never capture" item may apply. If it is borderline, don't capture; mention it to the human instead.
- **Write-once.** Create a new file; never edit, overwrite, or delete an existing one. Corrections or re-captures become a new file (e.g. `-v2`) and the source page notes the relationship.
- **Faithful, not distilled.** A capture is the source as retrieved (converted to markdown). Summarizing belongs in `wiki/sources/`, not `raw/`.
- **Filenames:** `YYYY-MM-DD-<slug>.md`, lowercase-kebab-case slug. Before capturing, run `python3 tools/wiki.py captured <url-or-path>`: exit 0 lists existing captures and their source page; exit 1 means not captured. Scheme/host case and a trailing slash are normalized; http vs https and `www.` are not.
- **Frontmatter on every capture:**

  ```yaml
  ---
  source: <original URL or path>
  captured: YYYY-MM-DD
  capture_method: webfetch | manual | human
  ---
  ```

  `webfetch` means the page passed through a model's reading, so it is a paraphrase risk; say so when capturing. `manual` means you copied the text verbatim (for example from a file in the host repository; use its repo-relative path as `source`). Files without `capture_method` have unknown provenance, not clean provenance; do not backfill them. Human-dropped files are not stamped by you.
- Don't copy `capture_method` onto wiki pages; it lives only in the raw capture. `python3 tools/wiki.py provenance <page>` resolves each supporting source's method (`unknown` = none recorded, `not-a-capture` = `raw:` outside `raw/`). `provenance --all --method webfetch` finds pages resting on paraphrase-risk captures; treat those as lower-confidence when claims conflict.
- Do not capture anything containing secrets or credentials. Everything here is committed with the host repository and visible to everyone who can read it.

## Workflows

Do all wiki work yourself. Don't hand it to subagents: they run under their own names and are blocked from this directory.

### Ingest (strictly one source at a time)
1. Queue: `python3 tools/wiki.py status [path]` lists raw files with no source page (all of `raw/`, a directory, or one file). Empty queue: say so and stop.
2. For each source, in order:
   1. Read it from `raw/`. If the human is in the conversation, discuss key takeaways briefly.
   2. `python3 tools/wiki.py new source <slug>` and fill in the page (summary, key claims, quotes worth keeping; set `raw:` to the real path).
   3. Find related pages with `search <key terms>` and `backlinks <page>`. Update existing entity/concept pages before creating new ones (`new entity|concept <slug>`); expect 5–15 touched pages. Flag contradictions with existing claims; revise stale statements.
   4. Update `wiki/overview.md` if the synthesis shifts; add every new page to `wiki/index.md`; append a `## [YYYY-MM-DD] ingest | <title>` entry to `wiki/log.md`.
   5. Run `python3 tools/wiki.py lint` and fix anything you introduced.
3. Finish with a short report: sources ingested, pages created and updated, contradictions found, open questions.

### Query
1. Read `wiki/index.md` first; use `python3 tools/wiki.py search "<terms>"` if the index isn't enough. Search returns `path:start-end  heading  description` lines: decide open-or-skip from the description, then `Read` just that line range (offset/limit) rather than the whole page.
2. Read the relevant sections, then answer with `[[wikilink]]` citations.
3. If the answer is reusable (comparison, synthesis, connection), file it as `wiki/analyses/<slug>.md` (offer first if the human is present), then update index and log (`query` op).

### Health (read-only)
Run `python3 tools/wiki.py digest [--days N]` and report it compactly, most actionable first, naming one next step per "Attention" item. Numbers come from the tool output, never estimated. Don't fix anything as part of a health check; fixing is a Lint run.

### Lint (periodic, or on request)
Run `python3 tools/wiki.py lint`, then also check by reading: contradictions, stale claims superseded by newer sources, concepts mentioned repeatedly without a page, missing cross-references, gaps worth a web search. Report findings, suggest new questions/sources, fix what's clearly safe, log a `lint` entry. Add questions to `tools/eval/questions.tsv` as pages are added, and run `python3 tools/wiki.py eval` after large changes to see whether search still finds the right pages.

## Rules
- Never edit or delete an existing file under `raw/`; new captures follow the Capture rules. If `lint` reports a write-once violation, restore the file; re-baseline (`reindex --accept-raw <path>`) only with the human's agreement.
- Never leave a page out of `index.md`.
- Don't delete pages without asking; mark them superseded and link to the replacement.
- Prefer updating an existing page over creating a near-duplicate.
- Stay inside this directory for wiki work. Other wikis in the host repository belong to other agents and are blocked to you.
