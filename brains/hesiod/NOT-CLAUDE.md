# Wiki install

This directory is an LLM-maintained wiki template that has just been dropped into a host repository. It is not set up yet: everything it needs is still inside this directory. If you are reading this, the human wants you, the host repository's agent, to install it by following the steps below in order, then hand the wiki to the agent the human names as its owner.

`<wiki>` below is this directory's path relative to the host root (the directory holding the host's `.claude/`; create `.claude/` there if it doesn't exist). `<agent>` is the owner's agent name: the `name:` field in its definition's frontmatter, which is what the fence matches (normally the same as the filename, `.claude/agents/<agent>.md`).

**Template check.** If this directory is inside the `solinari` repository (a directory named `solinari` is this directory or one above it), this is the template, being developed there. Don't install anything: skip every step below and follow "Template development" at the end of this file instead.

## How to run this

- **Order matters.** Steps 3–7 work inside `<wiki>` while it is still unregistered and open to you. Steps 8–9 register it and check the fence; step 10, turning the fence on, is the human's to do. Once the wiki is registered under a live fence you can no longer reach it, and the fence always blocks agents from changing the registry, the hook, the skill and settings files.
- **Merge, never replace.** Whenever a step adds to a file that already exists in the host (settings, registry, ignore files, formatter configs, agent definitions, the host's `CLAUDE.md`), add the new content alongside what is there and keep its formatting. If something already present conflicts, stop and ask.
- **Who decides.** Ask the human, and wait, wherever a step says "with the human's agreement". If the human already answered a question earlier in the conversation, use that answer and say so in the report. Anything else that blocks a step: report it and wait. Warnings (things that make the wiki less safe but don't stop the install, such as hooks being switched off) go in the report and don't block later steps.
- **No version-control actions.** Don't commit, stage, or run other version-control commands; the human handles that.
- **Expect permission prompts.** Claude Code asks before edits under `.claude/` and to some config files (pre-commit, for example), separately from the fence. Approving them is the human's call. In a non-interactive run where they can't be approved, put those edits on the human's to-do list in step 8 with the exact change.
- **Under a live fence, search narrowly.** Grep, Glob and recursive shell commands rooted at the host root are denied because they would sweep in other wikis. Search specific paths, and read the registry, hook, skill and settings files with the Read tool; shell commands that name them are denied.

## 1. Owner
1. The owner is the agent the human named when asking you to install this. If they didn't name one, ask.
2. Its definition must exist under the host's `.claude/agents/`. If it doesn't, ask whether to create it or use a different agent; don't create one on your own.
3. Its `tools:` line, if it has one, limits what it can use. The wiki needs `Skill`, `Read`, `Write`, `Edit`, `Grep`, `Glob` and `Bash`, plus `WebFetch` if `WIKI.md` will allow URL captures. If any are missing, propose adding them; add them with the human's agreement in step 8. No `tools:` line means all tools, which is fine.
4. If the host has `.claude/skills/wiki/registry.yaml`: `<agent>` must not already own a wiki, and `<wiki>` must not already be registered, contain a registered wiki, or sit inside one. Stop and ask if any of these is true.

## 2. Preflight (read-only)
Check each item and report what you find before changing anything. The only file this step creates is the wiki's derived search index (`<wiki>/.wiki.db`), built by `doctor`.

- **Is a fence already live?** It is live if the host's `.claude/settings.json` or `.claude/settings.local.json` has a `PreToolUse` hook whose command runs `.claude/hooks/wiki-fence.py`, and `disableAllHooks` is not `true` in either file or in user settings (`~/.claude/settings.json`). Live or not decides how steps 6, 8 and 10 go.
- **Hooks switched off.** `disableAllHooks: true` anywhere above means no fence will run. Don't change it; it's a warning for the report.
- **Wikis registered but not fenced.** If the registry already has entries but no fence hook is in settings, step 10 will start fencing those wikis too. Say so in the report.
- **Existing hooks.** List every hook in the host's settings files (every event, not just `PreToolUse`). Flag:
  - any that formats or rewrites files (Prettier, Black, gofmt, `sed`, `--fix`, `--write`), especially on `PostToolUse` for `Write|Edit`. These run on everything the owner writes, including raw captures, and an ignore file may not stop them;
  - any whose command points to a script that doesn't exist.

  Don't change hooks yourself. For a formatting hook, propose a change that skips `<wiki>/` (a narrower matcher, or a path check in its script) and make it only with the human's agreement.
- **Host tooling that rewrites files.** Look for formatters, linters and commit hooks that would touch `<wiki>/`: `.pre-commit-config.yaml`, lint-staged config, Prettier config and `.prettierignore`, markdownlint config and ignore files, `.editorconfig` (`trim_trailing_whitespace`, `insert_final_newline`), Biome, dprint, Vale, cspell, and anything similar. Any rewrite of a file in `<wiki>/raw/` breaks its write-once check. Step 4 adds the exclusions.
- **Ignore rules.** Read the host's ignore files (the root `.gitignore` and any in directories above `<wiki>`). Note any pattern that would exclude `<wiki>/raw-manifest.tsv`, `raw/`, `wiki/` or `*.md` under `<wiki>`, and whether it excludes a *directory* above `<wiki>` (for example `docs/`). That decides the fix in step 5.
- **Host instructions.** If the host's `CLAUDE.md` (or `AGENTS.md`) tells agents to format, lint or rewrite Markdown, note the line for step 4.
- **Python.** `python3 --version` must be 3.9 or newer, and `python3 <wiki>/tools/wiki.py doctor` must report 0 problems; it exits with a message if SQLite lacks FTS5.

## 3. Wiki purpose and capture criteria
`WIKI.md` holds this wiki's purpose, scope and capture criteria, and every placeholder must be replaced.
1. Gather the wiki's name, purpose, what is in and out of scope, where material may come from, and what must never be captured. Use answers the human already gave; ask for the rest.
2. Draft each section as short, checkable bullets. Don't add criteria the human didn't give; put suggestions in the report instead. Write the Examples from the human's answers (one or two items that qualify, one or two near-misses), and mark them as yours in the report.
3. Show the human the draft and write it once they agree. If the human said to proceed without reviewing it, write it and say in the report that it hasn't been reviewed.
4. Keep every section and the "When unsure" rule. Delete the HTML comment at the top of `WIKI.md` once every placeholder is replaced; it is the instruction for this step, and its `<placeholder>` text would otherwise count as one left behind.

## 4. Keep host tooling out of the wiki
For each tool found in step 2, add an exclusion for `<wiki>/` using that tool's own mechanism. Add, don't replace:
- **pre-commit:** a top-level `exclude:` regex `^<wiki>/`. If a top-level `exclude:` already exists, combine the two into one: `exclude: '(?:<existing regex>)|^<wiki>/'`. Check the file still parses.
- **Ignore files** (`.prettierignore`, `.markdownlintignore` and the like): add a `<wiki>/` line.
- **Config lists** (`ignorePaths`, `ignores`, `exclude` arrays): append `<wiki>/**`.
- **`.editorconfig`:** add two sections, `[<wiki>/raw/**]` and `[<wiki>/raw-manifest.tsv]`, each with `trim_trailing_whitespace = false` and `insert_final_newline = unset`.
- **Host instructions:** with the human's agreement, add this line directly under the conflicting rule in the host's `CLAUDE.md` (or `AGENTS.md`): `Exception: never format, lint or edit files under <wiki>/. That wiki is maintained by <agent> under its own rules, and its raw/ files are write-once.`
- **Hooks and anything you can't configure safely** (CI jobs that reformat, for example): leave as they are and report them, with the proposal from step 2.

## 5. Ignore rules
- Keep `<wiki>/.gitignore`. It excludes the derived search index (`.wiki.db`, `.wiki.db-wal`, `.wiki.db-shm`).
- `raw-manifest.tsv` is the durable record of every raw file's write-once baseline, and nothing under `<wiki>` except the index may be ignored.
  - If a host pattern matches files only (for example `*.tsv`), append negations to `<wiki>/.gitignore` for every file the pattern catches, then confirm with `git check-ignore -v`. For `*.tsv` that is `!raw-manifest.tsv` and `!tools/eval/questions.tsv` (the search eval set).
  - If a host pattern excludes a directory above or at `<wiki>` (for example `docs/`), a negation inside `<wiki>` can't work, because files under an excluded directory can't be re-included. Propose the change to the host's ignore file instead (for example `!docs/` followed by re-adding what should stay ignored) and make it only with the human's agreement.

## 6. Install the skill and hook into the host
| Source | Destination in the host |
| --- | --- |
| `<wiki>/.claude/skills/wiki/SKILL.md` | `.claude/skills/wiki/SKILL.md` |
| `<wiki>/.claude/hooks/wiki-fence.py` | `.claude/hooks/wiki-fence.py` |
| `<wiki>/.claude/skills/wiki/registry.yaml` | `.claude/skills/wiki/registry.yaml`, **only if the host has none** |

- If the destination doesn't exist, copy the file.
- If it exists and is identical, skip it.
- If it exists and differs (another wiki was installed from an older or newer template), show the human the difference and ask which to keep. Compare them with the Read tool.
- Never overwrite an existing `registry.yaml`.
- Note the `VERSION` line from `<wiki>/.claude/hooks/wiki-fence.py`; step 9 checks it after the source is gone.
- **If the fence is live** you can't change these files. For each copy that's needed, add it to the human's to-do list for step 8 as an exact `cp` command run from the host root, and leave `<wiki>/.claude/` in place for them.
- Don't install `<wiki>/.claude/agents/sqlite-fts5.md` or `<wiki>/.claude/settings.local.json`; they belong to template development.

## 7. Finish inside the wiki
This is the last step with access to `<wiki>`, and it rewrites this file. Make sure steps 8–10 are in front of you before starting.
1. Append to `<wiki>/wiki/log.md`:
   - the heading `## [YYYY-MM-DD] schema | Installed in <host>`, where `<host>` is the name of the host root directory;
   - one bullet naming the owner;
   - one bullet listing every change made outside `<wiki>`: exclusions, ignore-file and host `CLAUDE.md` edits, and hooks left unchanged.
2. Delete `<wiki>/.claude/` (unless step 6 left it for the human), plus any `.DS_Store` files and `<wiki>/tools/__pycache__/`.
3. Replace this file, `<wiki>/CLAUDE.md`, with exactly the text below, filling in the placeholders. From then on it is the owner's entry point.

````markdown
# <wiki name>

This directory is the wiki owned by the agent `<agent>`, registered in `.claude/skills/wiki/registry.yaml` at the repository root. Only that agent can read or write here; a hook blocks everyone else.

Before any work in this directory, read `SCHEMA.md` (how the wiki is built and maintained) and `WIKI.md` (its purpose, scope and capture criteria) in full. They govern everything here. The `wiki` skill maps tasks to their workflows.

Installed <YYYY-MM-DD>.
````

## 8. Register the owner
1. With the human's agreement from step 1, add any missing tools to the `tools:` line in the owner's agent definition.
2. Add this line to the end of the owner's agent definition, keeping everything already there:

   > Your wiki is `<wiki>`. Use the `wiki` skill for it; you are its only writer. Read `<wiki>/CLAUDE.md` before any work there.

3. Add an entry to the end of the host's `.claude/skills/wiki/registry.yaml`, in exactly this shape (two-space indent, under `wikis:`):

   ```yaml
     - agent: <agent>
       path: <wiki>
   ```

**If the fence is live,** you can't change the registry, so this entry joins the human's to-do list. Give the human that list now:
- the `cp` commands from step 6;
- the registry entry above;
- `rm -r <wiki>/.claude` if it is still there.

They run these in their own terminal or editor, which the fence doesn't govern. Wait until they confirm, then continue with step 9.

## 9. Verify the fence
From the host root, run exactly:

```
python3 .claude/hooks/wiki-fence.py --selftest
```

The fence always allows this one command. For every registered wiki it checks that the owner can read it, that a plain session and another agent can't, and that the owner can't edit the registry. Its first line names the hook version; it must match the `VERSION` you noted in step 6 whenever the template's hook was copied in. It must end with `0 failures` and exit 0. If it doesn't, stop, report the output, and don't go on to step 10.

## 10. Turn on the fence (the human does this; it locks you out)
Turning the fence on is the one step you don't do. It locks you out of every registered wiki, and the human should see and make that change, so there is a person in the loop before the lock closes. Don't edit the host's settings files for this, even if you can.

**If the fence is already live**, there's nothing to do. The new wiki was fenced the moment it was registered.

Otherwise, give the human this to-do item and stop until they confirm:
- Add the object below to `hooks.PreToolUse` in the host's `.claude/settings.json`, keeping the file's existing content and formatting. If `hooks` or `PreToolUse` don't exist, create them. Don't add a second copy if an identical object is already there.
- Say what it will do: after the next session start (or once Claude Code reloads its hook settings), only the owner reaches `<wiki>`, and every other registered wiki in the host is fenced the same way.

```json
{ "matcher": "*", "hooks": [ { "type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/wiki-fence.py\"" } ] }
```

The `*` matcher runs the fence for every tool, including plugin and MCP tools that take file paths. Tools without path inputs pass straight through.

When the human confirms, check the result with the Read tool: the object is present, exactly once, and the file is still valid JSON. Report anything off; don't fix it yourself.

## Report to the human
Cover steps 1–10: what you did, what you skipped, and anything waiting on them. Step 10 is always the human's, so say plainly whether they have done it yet; until they do, the wiki is registered but not fenced. Then add:
- **Warnings from step 2:** hooks switched off, formatting hooks left in place, broken hooks, wikis that step 10 will start fencing.
- **When the lock takes effect:** once step 10 is done, only `<agent>` can reach `<wiki>`, from the next session or once Claude Code reloads its hook settings. Hooks in project settings also need the host folder accepted in the workspace trust dialog.
- **Ownership changes:** made by hand in `registry.yaml`. The fence stops every agent from editing it, the hook, the skill and the settings files.
- **Their own access:** they can still drop files into `<wiki>/raw/` through Finder or an editor, because the fence governs only Claude's tools.
- **Capture tooling:** no faithful web-extraction tool is configured, so URL captures use `capture_method: webfetch`, which is a paraphrase risk. Choosing one means updating the Capture rules in `SCHEMA.md`.
- **Optional:** open `<wiki>/` as its own Obsidian vault, not the whole host repository.

## Template development (solinari only)
This section applies only inside the `solinari` repository. Step 7 replaces this whole file in an installed copy, so none of it reaches a host.

- **Rules.** Edit template files directly. Use `SCHEMA.md` as the rules for the seeded `wiki/` pages, and log template changes in `wiki/log.md` as `schema` entries.
- **Search tool.** Changes to `tools/wiki.py`, the index or the eval set go to the `sqlite-fts5` agent in `.claude/agents/`. That agent is for template development only; step 6 never installs it.
- **Fence hook.** Bump `VERSION` in `.claude/hooks/wiki-fence.py` on every change to that file. Installs compare it to tell an older host copy from the template's.
- **Re-testing the fence.** After changing the hook, test it in a throwaway host with at least two registered wikis. Run `--selftest`, then check by hand:
  - owner allowed;
  - plain session and other agents denied;
  - `..` escapes denied;
  - searches rooted above another wiki denied;
  - Bash `cd` and glob paths denied;
  - registry, hook and settings edits denied;
  - an MCP-style tool with a path field denied;
  - a garbled registry blocking everything;
  - no registry allowing everything.

  After changing these install steps, rehearse a full install, including into a host whose fence is already live.
- **Accepted limits of the fence.** Don't treat these as bugs to fix:
  - Bash commands that build paths at run time (`python3 -c`, variables) get past it.
  - A tool that puts a path in an input field without a path-like name (`path`, `file`, `dir`, `source`, `target`, ...) isn't caught.
  - Subagents an owner spawns are blocked from its wiki, by design.
- **Search baseline.** `python3 tools/wiki.py eval` scored hit@1 13/16 and hit@3 16/16 on 2026-10-10. Compare against this after any change to the tokenizer, weights or chunking.
- **Open item.** No faithful web-extraction tool is chosen, so URL captures use `capture_method: webfetch`. Choosing one means updating the Capture rules in `SCHEMA.md` and the matching line in the install report above.
