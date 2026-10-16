---
name: Website platforms for a Claude Code, Figma and GitHub workflow
topic: How well Webflow, Wix, Framer, Squarespace, WordPress, Builder.io, Plasmic and Duda support a Claude Code + Figma + GitHub loop, compared with a code-first Next.js/Astro baseline
type: general
created: 2026-10-13
updated: 2026-10-13
---

# Website platforms for a Claude Code, Figma and GitHub workflow

## Findings

### Summary

None of the hosted visual platforms gives a clean round trip of Figma → platform → GitHub → Claude Code → live site. Each one keeps the visual design in its own editor, and that state isn't in Git. Where Git exists, it covers only a code layer: Webflow code components and Webflow Cloud apps, Wix Velo code, WordPress themes and plugins, Squarespace 7.0 templates, and Plasmic codegen output. Agents can now edit the visual editor state directly through official MCP servers or agent bridges (Webflow, Wix, Framer, WordPress.com, Duda). That means Claude Code can be the "hands" for designer-owned sites. In that loop, GitHub drops out for design changes. [C41] [C42] [C43] [C44] [C45]

The code-first baseline is still the only setup where every change, designer-driven or not, ends up as a reviewable Git commit with preview deploys: the Figma MCP server, Claude Code, a GitHub repo and Next.js/Astro on Vercel or Netlify. Its cost is that designers never touch the live site directly. [C25]

On marketing: much of what the searches turned up was selling something. That included Webflow and Framer agency blogs, MCP directory listings, integration sellers (Composio), pricing aggregators, and Builder.io's own blog arguing against the Figma MCP round trip. I estimate more than half of the non-vendor results were in this group. I relied on vendor documentation for what each product does, and treated third-party material as Unconfirmed context or ignored it. Vendor docs also come from a seller with an interest, so they're used here only for capabilities and limits, not for claims about quality.

### Comparison table

| Platform | Claude Code access | Figma path | GitHub path | Where the round trip breaks | Plan gating (verified) |
| --- | --- | --- | --- | --- | --- |
| **Webflow** | Official remote MCP server (Data + Designer via Bridge App); Webflow CLI with `--json` for agents | Official Figma to Webflow plugin + app (auto-layout layers, components, variables, styles) | Code components pushed from a repo via `webflow devlink import` (CI-capable); DevLink Export to React; Webflow Cloud deploys from GitHub | Designer canvas edits have no Git history; page branches are Enterprise-only; ZIP export drops CMS and code components | MCP on all Site plans; code components and DevLink need a paid Workspace plan or a CMS/Business(/Enterprise or Ecommerce) Site plan; ZIP export needs a paid Workspace plan |
| **Wix / Wix Studio** | Official Wix MCP (`claude mcp add` documented); Wix CLI | Official Figma to Wix Studio plugin (frames, styles; one-way, manual re-import) | Git Integration & Wix CLI for Sites (Velo code only); Wix-managed headless (Astro) via Wix CLI | Only code goes to Git; the editor becomes read-only for code once connected; design stays in Studio | Not stated in docs reviewed |
| **Framer** | No MCP by design; official "External Agents" bridge (`npx @framer/agent setup`) for Claude Code, Cursor, Codex; Server API (beta) | Official copy-paste plugin (fonts don't transfer) | None native; third-party plugins only | Framer branches aren't Git; code components live in Framer | Branching and staging on Pro ($30/mo); External Agents free in preview on Basic/Pro |
| **WordPress.com / block themes** | Official WordPress.com MCP (read and write groups, incl. Site Editing); official agent skills (`wp-block-themes`); Studio Code (beta) | No official Figma importer found | GitHub Deployments for themes/plugins (Business/Commerce); Create Block Theme writes Site Editor changes to theme files | Site Editor changes live in the database until saved to theme files; content is never in Git | MCP on all paid plans; GitHub Deployments on Business/Commerce |
| **Squarespace** | No official MCP found; community servers on Commerce APIs | No official Figma path found | Developer Mode Git/SFTP template repo + local dev server (7.0 only) | 7.1 sites have no file access; no public page-content API | Not verified |
| **Builder.io (Fusion)** | Works on your repo; MCP as prompt context; built-in MCP servers on Pro | Official Figma plugin as input | Connects GitHub/GitLab/Bitbucket; commits as PRs | Lives in your repo, so the break is the AI quality, not the platform | Free tier includes git connections and Figma plugin; Pro $24/user/mo |
| **Plasmic** | CLI (`plasmic sync`/`watch`); no MCP found | Official Figma importer (a "starting point") | Codegen writes React into your repo | One-way: local edits to generated code aren't synced back to Studio | Starter $39, Pro $103/mo (yearly); feature tiers not readable |
| **Duda** | Official MCP (beta) for content and stats; Claude Code not named | None found | None found; widget code edited only in Widget Builder or hosted externally | No Git path at all | Widget Builder on Agency plans and up |
| **Code-first baseline** | Claude Code edits the repo directly; Figma MCP server for design context | Figma MCP (`get_design_context`, variables); Code Connect maps components to code | Native: PR previews and production on merge (Vercel) | Designers can't edit the live site except through Figma → agent → PR | Code Connect needs Figma Organization/Enterprise; Figma MCP rate limits by seat |

### Webflow

**Claude Code integration.** Webflow publishes an official MCP server that lists Claude Code, Claude Desktop, ChatGPT, Codex and Cursor as clients. Agents act within the user's existing Webflow roles, and each authorization covers one workspace [C1]. Webflow's help center says the server is available on every Site plan, including the free Starter plan [C1]. Most tools work without the Designer open. Visual snapshots and changes to the current selection, page, breakpoint or canvas need the Designer open with the Bridge App connected; the changelog still says element snapshots depend "on a live Designer session via the Webflow MCP Bridge App" [C2]. Documented limits include no classic interactions (GSAP interactions only), Cloud deployments through MCP only for GitHub-connected apps, no secret environment variables through MCP, and no creation of new localized CMS items [C3]. The Webflow CLI's `webflow apps` namespace adds `--json` output and `--dry-run` for "CI jobs and AI agents" [C6].

**Figma integration.** The official Figma to Webflow plugin and app sync layers, variables and styles. Layers must use auto layout, and import is a separate step in the Webflow app [C8]. A practitioner thread reports that Claude, driving both the Figma and Webflow MCP servers, matches variables well. Nobody in that thread had recreated full sections in production, and the stated main risk was "trusting that it did it right" [C10].

**GitHub integration.** Three code paths exist, and none of them covers Designer state:
- *Code components (DevLink import):* React components written in a repo are bundled and uploaded with `webflow devlink import`. They are not pulled from GitHub, but the CLI can run in CI with a Workspace token. Prerequisites are Node.js 22.13+ and a paid Workspace plan or a CMS, Business or Enterprise Site plan [C4].
- *DevLink Export:* Webflow-built components, styles and variables become React components for your own app or a Webflow Cloud app. CMS and Ecommerce elements aren't supported [C5].
- *Webflow Cloud:* deploys Next.js, Astro and static apps from GitHub or `webflow cloud deploy`. Limits are a 10 MB bundle, 30 s CPU per request, 128 MB memory, and 5/15/50 projects per site by plan [C6].
- *ZIP code export:* needs a paid Workspace plan and leaves out CMS, ecommerce, user accounts, code components and localized content [C7].

**Round trip.** It breaks at the Designer. Canvas edits made by designers or by an agent through MCP don't produce Git commits. Page branching exists but requires Enterprise [C9]. Webflow works well when design lives in Webflow and Claude Code edits it through MCP, and when developer code (components, Cloud apps) lives in GitHub. The two halves stay separate. [C41]

### Wix and Wix Studio

**Claude Code integration.** The official Wix MCP documents a Claude Code command (`claude mcp add --transport http wix-mcp-remote https://mcp.wix.com/mcp`). Its tools search Wix docs, generate Wix code, call REST APIs on sites, and create, update and publish sites [C11]. For headless builds, the Wix CLI scaffolds Astro projects, and `npx wix release` uploads other frameworks' builds [C15].

**Figma integration.** The Figma to Wix Studio plugin imports frames and styles (colors, typography). Menus, forms, galleries and inputs aren't recognized, and nothing exports back to Figma. Re-sync is manual; in Wix's words, "your changes won't automatically update" [C14].

**GitHub integration.** Git Integration & Wix CLI for Sites puts the site's *code* in a GitHub repo. Once connected, the editor's code goes read-only, and Velo Packages block the connection [C12]. `wix publish` can publish local code that isn't committed, which leaves the live site and the repo out of sync [C13].

**Round trip.** Code round-trips through Git; design does not. Figma import is one-way and manual. [C43]

### Framer

**Claude Code integration.** Framer has no separate MCP server. Instead, its official External Agents bridge (`npx @framer/agent setup` plus a `/framer` skill) gives Claude Code, Cursor and Codex access to canvas, components, CMS and project context. Agent changes go on a branch for review and don't touch the live site until you publish [C16]. Framer 3.0 (16 June 2026) added built-in Agents that can write code components, plus Branching [C17]. The Server API (open beta) lets server-side scripts sync CMS data and publish [C19].

**Figma integration.** Framer's plugin copies Figma layers so you can paste them as editable Framer elements. Fonts don't transfer [C20].

**GitHub integration.** Framer has no native Git integration. Third-party Marketplace plugins claim two-way sync of code components with GitHub [C21].

**Pricing.** Branching and staging are Pro features ($30/mo). External Agents are free during preview on Basic and Pro [C18].

**Round trip.** Framer has the most complete agent loop without GitHub: Claude Code edits the canvas on a branch, a person reviews and merges, then publishes. The weak points are that Framer branches aren't Git and code components aren't versioned in a repo. [C42]

### WordPress.com and WordPress block themes

The WordPress.com MCP has Read and Write tool groups, including "Site Editing" and "Site Editor Context". Write actions require confirmation. It's available on all paid plans, uses OAuth 2.1, and serves generic MCP clients at `https://public-api.wordpress.com/wpcom/v2/mcp/v1` [C26]. The page doesn't say how far Site Editing reaches into templates. GitHub Deployments push themes and plugins from a branch, either as a simple copy or through a `wpcom.yml` workflow in GitHub Actions syntax, on Business and Commerce plans [C27]. The Create Block Theme plugin saves Site Editor changes back to the theme's files (theme.json, templates), so they can be committed [C28]. WordPress publishes official agent skills, including `wp-block-themes` [C29]. WordPress.com's Studio Code beta, a WordPress-specific terminal agent reported to use Claude Code technology, is covered only in secondary sources [C30]. I found no official Figma importer.

**Round trip.** Of the hosted CMSes, WordPress block themes come closest to Git: theme.json and template files are plain text in a repo. Designer edits in the Site Editor have to be saved to the theme explicitly first. Content stays in the database. [C44]

### Squarespace and Duda

Squarespace Developer Mode provides a Git/SFTP copy of the template plus a local development server. It doesn't support server-side code and stops template updates [C31]. It's limited to version 7.0 sites; Squarespace's own 7.1 upgrade guide says to disable it first [C32]. I found no official Squarespace MCP, and a user report says there's no public API for page content [C33]. Duda's official MCP (beta) handles content, site management and stats at `mcp.duda.co`, but its docs don't name Claude Code [C38]. Duda widget code can be edited only in its Widget Builder or hosted outside Duda, and Widget Builder requires an Agency plan or higher [C39]. Neither platform suits a Git-centered loop. [C47]

### Builder.io and Plasmic (visual layers over your repo)

Builder.io Fusion connects GitHub, GitLab or Bitbucket repos, commits as pull requests, and takes Figma designs as context [C34]. Its Free plan includes git connections and the Figma plugin with 60 credits a month; Pro is $24/user/month with 500 credits [C35]. Plasmic codegen writes React into your repo through `plasmic sync` or `plasmic watch` [C36]. Forum users report that the CLI doesn't sync local edits back into Studio, and that republishing can overwrite custom edits [C36]. Plasmic's Figma importer gives "a starting point" and can map to registered code components [C37]. Both tools keep the code in your repo, so Claude Code and GitHub fit naturally. The trade-off is a second source of truth (Builder's or Plasmic's visual model) alongside your code.

### Figma side and the code-first baseline

Figma's remote MCP server, which Figma recommends, provides design context, variables and component data. Its write-to-canvas works only for some clients [C22]. Rate limits depend on seat: View/Collab seats get 20 calls a month on every plan, and Dev/Full seats on Professional get 200 a day [C22]. Code Connect, which maps Figma components to repo components, requires an Organization or Enterprise plan with a Full or Dev seat; connecting GitHub is optional [C23]. Vercel builds a preview for every pushed branch and PR and a production deployment on merge. Hobby teams can't deploy private repos owned by a GitHub organization [C24]. Taken together, every change becomes a PR with a preview URL, and Claude Code works on the source of truth directly [C25]. Figma's Code Layers for Figma Sites, which reportedly can clone and sync a GitHub repo onto the canvas, was in early access after Config 2026 [C40].

### Ranked verdict by use case

1. **Marketing site run by designers:** (1) **Framer**, for agent edits on reviewable branches, a Figma paste path and low cost; (2) **Webflow**, for the most mature official MCP, a real Figma plugin with variables, and code components for developers; (3) **Wix Studio**, which has an MCP and Figma import, but import is one-way and the editor is less agent-addressable. In all three, GitHub doesn't hold the design. [C45]
2. **Developer-owned site:** (1) **Code-first baseline**; (2) **Builder.io** or **Plasmic** when non-developers need a visual layer over the repo; (3) **WordPress block themes** with GitHub Deployments when a CMS is needed. [C45]
3. **Hybrid (designers edit pages, developers own components and logic):** (1) **Webflow**, where designers own the canvas, developers ship code components from GitHub through CI with `webflow devlink import`, and app routes go to Webflow Cloud from GitHub; (2) **WordPress block themes**, where designers use the Site Editor and developers commit theme files, with Create Block Theme bridging the two; (3) **Framer**, if code components can live outside Git. [C45]
4. **Not recommended for this loop:** Squarespace and Duda. [C47]

### Claims not verified from primary sources

- The Webflow MCP command `claude mcp add --transport http webflow https://mcp.webflow.com/mcp` came from search results for Webflow's Claude Code install page, which I didn't open directly (see Conflicts) [C1].
- The Figma to Webflow plugin details come from a search summary of Webflow's help article; the page returned HTTP 403 when fetched [C8].
- That Webflow MCP is on all Site plans comes from a search summary of Webflow's help center; that page also returned 403 [C1].
- Squarespace Developer Mode being 7.0-only rests on third-party guides plus an indirect official statement [C32].
- WordPress Studio Code's features and its Claude Code basis come only from news coverage [C30].
- Third-party Framer GitHub plugins: listings only, untested [C21].
- Figma Code Layers GitHub sync and its access terms: news only [C40].
- Webflow, WordPress.com and Figma Organization plan prices weren't verified on official pricing pages.

## Conflicts

1. **Webflow MCP endpoint.** Webflow's Claude Code install page, seen only through search results, gives `https://mcp.webflow.com/mcp` [S2] (Official). Webflow's MCP overview names `https://developers.webflow.com/_mcp/server` [S1] (Official). The second may be the documentation MCP rather than the site-editing server. The findings cite the first as the command and flag it unverified.
2. **Framer Branching availability.** Framer's 3.0 announcement says Branching is "available to everyone today" [S18] (Official). The pricing page lists Branching as a Pro feature [S19] (Official). The findings treat it as Pro-gated, since the pricing page decides billing.
3. **Webflow code-component plan requirements.** The official quickstart lists paid Workspace plans or CMS, Business or Enterprise Site plans, with Node 22.13+ [S4] (Official). A 2026 practitioner blog lists only CMS and Business Site plans [S49] (Unconfirmed). The findings use the official list.
4. **Whether Framer has an official agent integration.** Older third-party guides say it has none [S48] (Unconfirmed). Framer's External Agents page documents one [S17] (Official). The findings use the official source.
5. **Figma Code Layers access.** News reports early access for Full seats [S50] (Unconfirmed); per that same coverage, the Figma help center says all paid plans. This is treated as unresolved and kept as a detail only.

## Appendix A: Next searches

1. Run an end-to-end test of Webflow code components in GitHub Actions: `webflow devlink import` with a Workspace token, plus Webflow MCP edits to the canvas. Measure what breaks.
2. Find out what Framer External Agents can actually do with code components: can Claude Code read and write component source files, and can those be mirrored to Git?
3. Find the official WordPress.com Studio Code post and docs, Studio sync to WordPress.com, and how far the MCP "Site Editing" tools reach into templates and theme.json.
4. Track Figma Code Layers and Figma Sites GitHub sync toward general availability, since that could become a Figma-native round trip.
5. Verify current official prices for Webflow Site and Workspace plans, the WordPress.com Business plan, Figma Organization seats and Vercel Pro, and confirm the Wix plan requirement for Git Integration.

## Appendix B: Sources

### Source list

| ID | Citation | Label | Setting | Reason for label |
| --- | --- | --- | --- | --- |
| S1 | Webflow, "Webflow MCP server," developers.webflow.com, n.d. (accessed 2026-10-13), https://developers.webflow.com/data/v2.0.0-beta/docs/ai-tools | Official | Organized | Webflow owns the product. |
| S2 | Webflow, "Claude Code" (MCP install), developers.webflow.com, n.d. (seen in search results 2026-10-13), https://developers.webflow.com/mcp/installing/claude-code.md | Official | Organized | Webflow owns the product; content seen only through search results. |
| S3 | Webflow, "Developer changelog (MCP filter)," developers.webflow.com, 2026 (accessed 2026-10-13), https://developers.webflow.com/home/changelog?filter=MCP | Official | Organized | Webflow's own changelog. |
| S4 | Webflow, "Quick start: Importing code components," developers.webflow.com, n.d. (accessed 2026-10-13), https://developers.webflow.com/code-components/importing/quick-start | Official | Organized | Webflow owns the product. |
| S5 | Webflow, "DevLink component export," developers.webflow.com, n.d. (accessed 2026-10-13), https://developers.webflow.com/devlink/docs/component-export.md | Official | Organized | Webflow owns the product. |
| S6 | Webflow, "Export components with DevLink Export," help.webflow.com, n.d. (seen in search results 2026-10-13), https://help.webflow.com/hc/en-us/articles/44746282129427-Component-export-using-DevLink | Official | Organized | Webflow help center. |
| S7 | Webflow, "Webflow Cloud limits," developers.webflow.com, n.d. (seen in search results 2026-10-13), https://developers.webflow.com/webflow-cloud/limits | Official | Organized | Webflow owns the product. |
| S8 | Webflow, "How do I export my Webflow site code?," help.webflow.com, n.d. (seen in search results 2026-10-13), https://help.webflow.com/hc/en-us/articles/33961386739347 | Official | Organized | Webflow help center. |
| S9 | Webflow, "Figma to Webflow plugin and app," help.webflow.com, n.d. (seen in search results 2026-10-13; direct fetch returned 403), https://help.webflow.com/hc/en-us/articles/33961219609875 | Official | Organized | Webflow help center. |
| S10 | Webflow, "Webflow MCP server overview," help.webflow.com, n.d. (seen in search results 2026-10-13; direct fetch returned 403), https://help.webflow.com/hc/en-us/articles/52536562285203-Webflow-MCP-server-overview | Official | Organized | Webflow help center. |
| S11 | Webflow (guest freelance author), "Import a Figma design into Webflow with one prompt," webflow.com blog, 2026 (seen in search results), https://webflow.com/blog/import-figma-to-webflow-mcp | Unconfirmed | Organized | Seller's own blog promoting its MCP; a demo with no disclosed method. Fewer than five citing sources found. Used only alongside S46. |
| S12 | Wix, "About the Wix MCP," dev.wix.com, n.d. (accessed 2026-10-13), https://dev.wix.com/docs/api-reference/articles/wix-mcp/about-the-wix-mcp | Official | Organized | Wix owns the product. |
| S13 | Wix, "Set Up Git Integration & Wix CLI for Sites," dev.wix.com, n.d. (accessed 2026-10-13), https://dev.wix.com/docs/develop-websites/articles/workspace-tools/developer-tools/git-integration-wix-cli-for-sites/setting-up-git-integration-wix-cli-for-sites | Official | Organized | Wix owns the product. |
| S14 | Wix, "Studio Editor: Exporting your designs from Figma," support.wix.com, n.d. (accessed 2026-10-13), https://support.wix.com/en/article/studio-editor-exporting-your-designs-from-figma | Official | Organized | Wix help center. |
| S15 | Wix, "About the Wix CLI" (headless) and "Deploy Your Own Frontend with the CLI," dev.wix.com, n.d. (seen in search results 2026-10-13), https://dev.wix.com/docs/go-headless/wix-managed-headless/full-integration-astro/development/about-the-wix-cli | Official | Organized | Wix owns the product. |
| S16 | Wix, "Velo: Working with the Wix CLI," support.wix.com, n.d. (seen in search results 2026-10-13), https://support.wix.com/en/article/velo-working-with-the-wix-cli | Official | Organized | Wix help center. |
| S17 | Framer, "Connect Claude, Cursor, Codex, Grok, and more to Framer," framer.com, n.d. (accessed 2026-10-13), https://www.framer.com/agents/external/ | Official | Organized | Framer owns the product. |
| S18 | Framer, "Introducing Framer 3.0 with Agents, Branching, and a new Community," framer.com blog, 2026-06-16, https://www.framer.com/blog/framer-3/ | Official | Organized | Framer's launch post. |
| S19 | Framer, "Pricing," framer.com, n.d. (accessed 2026-10-13), https://www.framer.com/pricing | Official | Organized | Framer's pricing page. |
| S20 | Framer, "Server API," framer.com/developers, n.d. (accessed 2026-10-13), https://www.framer.com/developers/server-api-introduction | Official | Organized | Framer owns the product. |
| S21 | Framer, "Import from Figma," Framer Academy, n.d. (seen in search results 2026-10-13), https://framer.com/academy/lessons/import-from-figma | Official | Organized | Framer's own lesson. |
| S22 | Third-party developer, "GitHub Link" plugin listing, Framer Marketplace, n.d. (seen in search results 2026-10-13), https://www.framer.com/marketplace/plugins/github-link/ | Unconfirmed | Individual | Plugin's own listing; no citing sources found. |
| S23 | Figma, "Figma MCP server," developers.figma.com, n.d. (accessed 2026-10-13), https://developers.figma.com/docs/figma-mcp-server/ | Official | Organized | Figma owns the product. |
| S24 | Figma, "Rate limits & access," developers.figma.com, n.d. (accessed 2026-10-13), https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/ | Official | Organized | Figma owns the product. |
| S25 | Figma, "Code Connect," help.figma.com, n.d. (accessed 2026-10-13), https://help.figma.com/hc/en-us/articles/23920389749655 | Official | Organized | Figma help center. |
| S26 | Figma, "Guide to the Figma MCP server," help.figma.com, n.d. (seen in search results 2026-10-13), https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server | Official | Organized | Figma help center. |
| S27 | WordPress.com, "GitHub Deployments," wordpress.com/support, last reviewed 2026-08-11, https://wordpress.com/support/github-deployments/ | Official | Organized | WordPress.com owns the product. |
| S28 | WordPress.com, "Model Context Protocol (MCP) settings," wordpress.com/support, last reviewed 2026-10-07, https://wordpress.com/support/model-context-protocol-mcp-settings/ | Official | Organized | WordPress.com owns the product. |
| S29 | WordPress.org, "Create Block Theme" plugin, wordpress.org, n.d. (seen in search results 2026-10-13), https://wordpress.org/plugins/create-block-theme/ | Official | Organized | Official WordPress plugin. |
| S30 | WordPress, "agent-skills" repository, GitHub, n.d. (seen in search results 2026-10-13), https://github.com/WordPress/agent-skills | Official | Organized | Published under the WordPress GitHub organization. |
| S31 | Gigazine, "WordPress.com releases Studio Code," gigazine.net, 2026-04-28, https://www.gigazine.net/gsc_news/en/20260428-wordpress-studio-code | Unconfirmed | Organized | News outlet with an audience; fewer than five citing sources found; the primary post wasn't retrieved. |
| S32 | Squarespace, "Local development," developers.squarespace.com, n.d. (seen in search results 2026-10-13), https://developers.squarespace.com/local-development | Official | Organized | Squarespace owns the product. |
| S33 | Squarespace, "Updating to version 7.1," support.squarespace.com, n.d. (seen in search results 2026-10-13), https://support.squarespace.com/hc/articles/360038270572 | Official | Organized | Squarespace help center; states the 7.0-only limit only indirectly. |
| S34 | SparkPlugin, "Squarespace Developer Mode (2025): The Ultimate Guide," sparkplugin.com, 2025, https://www.sparkplugin.com/blog/squarespace-developer-mode | Unconfirmed | Organized | Sells Squarespace plugins, but the claim used doesn't lead to its product; no citing sources found. |
| S35 | GitHub user, "Problem Statement" (Squarespace connector request), anthropics/claude-ai-mcp issue #372, n.d., https://github.com/anthropics/claude-ai-mcp/issues/372 | Unconfirmed | Community | Issue tracker post; a single first-hand report. Sorting: facts hat only (states a missing API); no other viewpoints present. |
| S36 | Builder.io, "Get started with Fusion" / Code Projects, builder.io/c/docs, 2026 (accessed 2026-10-13), https://www.builder.io/c/docs/get-started-fusion | Official | Organized | Builder.io owns the product. |
| S37 | Builder.io, "Pricing," builder.io, 2026 (accessed 2026-10-13), https://www.builder.io/pricing | Official | Organized | Builder.io's pricing page. |
| S38 | Plasmic, "Codegen overview," docs.plasmic.app, n.d. (accessed 2026-10-13), https://docs.plasmic.app/learn/codegen-guide/ | Official | Organized | Plasmic owns the product. |
| S39 | Plasmic, "Importing from Figma," docs.plasmic.app, n.d. (seen in search results 2026-10-13), https://docs.plasmic.app/learn/importing-from-figma/ | Official | Organized | Plasmic owns the product. |
| S40 | Plasmic forum, "Syncing custom changes into Plasmic" and "Using GitHub repo with Plasmic Studio," forum.plasmic.app, n.d., https://forum.plasmic.app/t/syncing-custom-changes-into-plasmic/5760 | Unconfirmed | Community | Vendor-hosted user forum; on-topic and active for this product. Sorting: black hat (overwritten edits, missing commits) and white hat (codegen required for commits). |
| S41 | Plasmic, "Pricing," plasmic.app, 2026 (accessed 2026-10-13), https://www.plasmic.app/pricing | Official | Organized | Plasmic's pricing page. |
| S42 | Duda, "Set up Duda's MCP Server," developer.duda.co, n.d. (accessed 2026-10-13), https://developer.duda.co/docs/duda-mcp-server | Official | Organized | Duda owns the product. |
| S43 | Duda, "Widget Builder Overview," support.duda.co, n.d. (seen in search results 2026-10-13), https://support.duda.co/hc/en-us/articles/34158215243927-Widget-Builder-Overview | Official | Organized | Duda help center. |
| S44 | Duda, "How to use external apps to power custom widgets in Duda," blog.duda.co, n.d., https://blog.duda.co/how-to-use-external-apps-to-power-custom-widgets-in-duda | Official | Organized | Duda describing its own product. |
| S45 | Vercel, "Deploying Git Repositories with Vercel," vercel.com/docs, updated 2026-09-18, https://vercel.com/docs/git | Official | Organized | Vercel owns the product. |
| S46 | Relume community, "Optimizing MCP workflow for Figma, Relume, Webflow," community.relume.io, 2026-08-03, https://community.relume.io/x/general/msg_dRbrpjGu4Eei/optimizing-mcp-workflow-for-figma-relume-webflow-a | Unconfirmed | Community | On-topic practitioner thread. Sorting: white hat (variables match well), black hat (verification risk), yellow hat (planned trial). |
| S47 | Composio, "How to integrate Wix MCP with Claude Code," composio.dev, n.d., https://composio.dev/toolkits/wix/framework/claude-code | Ignore | Organized | Leads to Composio's paid intermediary MCP service. |
| S48 | Usecarly, "Claude + Framer: What the Integration Can (and Can't) Do in 2026," usecarly.com, 2026, https://www.usecarly.com/blog/claude-framer-integration/ | Unconfirmed | Organized | Third-party blog; superseded by S17; no citing sources found. |
| S49 | Pravin Kumar, "Webflow code components, React and DevLink (2026)," pravinkumar.co, 2026-04, https://www.pravinkumar.co/blog/webflow-code-components-react-devlink-2026 | Unconfirmed | Individual | Webflow freelancer's blog (sells services); no citing sources found. |
| S50 | The Next Web, "Figma adds code layers to the canvas…at Config 2026," thenextweb.com, 2026, https://thenextweb.com/news/figma-config-code-layers-ai-skills-plugins-animations | Unconfirmed | Organized | News coverage; fewer than five citing sources found. |
| S51 | Builder.io, "Claude Code to Figma," builder.io blog, 2026, https://www.builder.io/blog/claude-code-to-figma | Ignore | Organized | Argues against the Figma MCP round trip to sell Builder.io Fusion. |

### Claim map

- **Foundation claims by strongest source:** 38 foundation claims: 35 backed by an Official source, 0 by Reputable or Trusted at best, 3 by Unconfirmed only.
- **Weak foundations:** C10 rests only on Unconfirmed sources (S11, S46). C21 rests only on an Unconfirmed source (S22). C33 rests only on an Unconfirmed source (S35).
- **Sources by label:** 39 official, 0 reputable, 0 trusted, 10 unconfirmed, 2 ignored.

| ID | Claim | Sources | Role | Depends on |
| --- | --- | --- | --- | --- |
| C1 | Webflow has an official MCP server for Claude Code and other clients, scoped to the user's roles, on every Site plan. | S1 (Official), S2 (Official), S10 (Official) | Foundation | none |
| C2 | Webflow canvas-level MCP actions need the Designer open with the Bridge App; data actions don't. | S1 (Official), S3 (Official) | Foundation | none |
| C3 | Webflow MCP can't handle classic interactions, secret env vars or new localized CMS items, and deploys only GitHub-connected Cloud apps. | S1 (Official), S3 (Official) | Foundation | none |
| C4 | Webflow code components are uploaded from a repo with `webflow devlink import` (CI-capable) and need a paid Workspace plan or a CMS/Business/Enterprise Site plan and Node 22.13+. | S4 (Official) | Foundation | none |
| C5 | DevLink Export turns Webflow components, styles and variables into React, without CMS or Ecommerce elements, on paid Workspace or CMS/Business/Ecommerce Site plans. | S5 (Official), S6 (Official) | Foundation | none |
| C6 | Webflow Cloud deploys Next.js, Astro and static apps from GitHub or the CLI within published runtime and project limits, and the CLI offers JSON output for agents. | S7 (Official), S3 (Official) | Foundation | none |
| C7 | Webflow ZIP export needs a paid Workspace plan and leaves out CMS, ecommerce, user accounts, code components and localization. | S8 (Official) | Foundation | none |
| C8 | The Figma to Webflow plugin and app sync auto-layout layers, components, variables and styles through a separate import step. | S9 (Official) | Foundation | none |
| C9 | Webflow page branches require Enterprise, and none of the Webflow docs reviewed sync Designer changes to Git. | S1 (Official) | Foundation | none |
| C10 | Practitioners report that Claude with the Figma and Webflow MCPs matches variables well but has no confirmed production section recreation. | S46 (Unconfirmed), S11 (Unconfirmed) | Foundation | none |
| C11 | Wix's official MCP documents a Claude Code command and tools for docs, code generation, site API calls and site publishing. | S12 (Official) | Foundation | none |
| C12 | Wix Git Integration puts site code (not design) in GitHub, makes the editor's code read-only, and is blocked by Velo Packages. | S13 (Official) | Foundation | none |
| C13 | `wix publish` of local code can leave the live site and the repo out of sync. | S16 (Official) | Foundation | none |
| C14 | The Figma to Wix Studio plugin imports frames and styles one-way, with manual re-import and unrecognized menus and forms. | S14 (Official) | Foundation | none |
| C15 | The Wix CLI scaffolds Astro headless projects and releases other frameworks' builds with `npx wix release`. | S15 (Official) | Detail | none |
| C16 | Framer connects Claude Code, Cursor and Codex through an official External Agents bridge rather than an MCP server, and agent changes go on a branch. | S17 (Official) | Foundation | none |
| C17 | Framer 3.0 (16 June 2026) added Agents that can write code components, plus Branching. | S18 (Official) | Foundation | none |
| C18 | Framer Branching and staging are Pro features ($30/mo), and External Agents are free in preview on Basic and Pro. | S19 (Official) | Foundation | none |
| C19 | Framer's Server API lets server scripts sync CMS data and publish sites. | S20 (Official) | Foundation | none |
| C20 | Framer imports Figma by copy-paste through a plugin, and fonts don't transfer. | S21 (Official) | Foundation | none |
| C21 | Framer has no native Git integration; third-party plugins offer GitHub sync for code components. | S22 (Unconfirmed) | Foundation | none |
| C22 | Figma's recommended remote MCP server provides design context and variables, and its rate limits depend on seat. | S23 (Official), S24 (Official), S26 (Official) | Foundation | none |
| C23 | Figma Code Connect requires an Organization or Enterprise plan with a Full or Dev seat, and connecting GitHub is optional. | S25 (Official) | Foundation | none |
| C24 | Vercel deploys a preview per branch or PR and production on merge; Hobby can't deploy private org repos. | S45 (Official) | Foundation | none |
| C25 | The code-first baseline turns every change into a reviewable Git commit with preview deploys. | S23 (Official), S25 (Official), S45 (Official) | Foundation | C22, C23, C24 |
| C26 | The WordPress.com MCP has read and write tool groups, including Site Editing, on all paid plans over OAuth 2.1. | S28 (Official) | Foundation | none |
| C27 | WordPress.com GitHub Deployments push themes and plugins, with optional Actions-style workflows, on Business and Commerce plans. | S27 (Official) | Foundation | none |
| C28 | Create Block Theme saves Site Editor changes back to theme files that can be committed. | S29 (Official) | Foundation | none |
| C29 | WordPress publishes official agent skills, including `wp-block-themes`. | S30 (Official) | Detail | none |
| C30 | WordPress.com's Studio Code is a beta WordPress-specific terminal agent reported to use Claude Code technology. | S31 (Unconfirmed) | Detail | none |
| C31 | Squarespace Developer Mode gives a Git/SFTP template repo and a local dev server, without server-side code. | S32 (Official) | Foundation | none |
| C32 | Squarespace Developer Mode is limited to version 7.0 sites. | S33 (Official), S34 (Unconfirmed) | Foundation | none |
| C33 | Squarespace has no official MCP and no public page-content API. | S35 (Unconfirmed) | Foundation | none |
| C34 | Builder.io Fusion connects git repos, commits as PRs and takes Figma designs as context. | S36 (Official) | Foundation | none |
| C35 | Builder.io's Free plan includes git connections and the Figma plugin; Pro is $24/user/month with 500 credits. | S37 (Official) | Detail | none |
| C36 | Plasmic codegen writes React into your repo through `plasmic sync`/`watch`, and local edits aren't synced back. | S38 (Official), S40 (Unconfirmed) | Foundation | none |
| C37 | Plasmic's Figma importer gives a starting point and can map to code components. | S39 (Official) | Detail | none |
| C38 | Duda's official MCP (beta) covers content, site management and stats, and doesn't name Claude Code. | S42 (Official) | Foundation | none |
| C39 | Duda widget code is edited only in the Widget Builder or hosted externally, on Agency plans and up. | S43 (Official), S44 (Official) | Foundation | none |
| C40 | Figma Code Layers for Figma Sites, with reported GitHub cloning, was in early access after Config 2026. | S50 (Unconfirmed) | Detail | none |
| C41 | Webflow's round trip breaks at the Designer: canvas state isn't in Git, while code components and Cloud apps are. | S1 (Official), S4 (Official), S5 (Official), S8 (Official), S9 (Official) | Foundation | C1, C2, C3, C4, C5, C6, C7, C8, C9, C10 |
| C42 | Framer gives the most complete agent loop without Git, through branch-reviewed agent edits, but has no repo versioning. | S17 (Official), S18 (Official), S19 (Official) | Foundation | C16, C17, C18, C19, C20, C21 |
| C43 | Wix round-trips code through Git but not design, and its Figma import is one-way. | S12 (Official), S13 (Official), S14 (Official), S16 (Official) | Foundation | C11, C12, C13, C14 |
| C44 | Of the hosted CMSes, WordPress block themes are closest to Git, once Site Editor changes are saved to theme files. | S27 (Official), S28 (Official), S29 (Official) | Foundation | C26, C27, C28 |
| C45 | Ranked verdict: Framer, then Webflow for designer-run sites; code-first for developer-owned sites; Webflow, then WordPress for hybrid. | S1 (Official), S17 (Official), S23 (Official), S36 (Official), S38 (Official) | Support | C25, C34, C36, C41, C42, C43, C44 |
| C47 | Squarespace and Duda aren't suited to a Git-centered Claude Code loop. | S32 (Official), S42 (Official) | Support | C31, C32, C33, C38, C39 |
