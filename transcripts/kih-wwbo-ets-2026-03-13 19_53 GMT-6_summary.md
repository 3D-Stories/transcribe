# ChoreStory Working Session — Homepage & Game Brainstorm

**Source:** kih-wwbo-ets-2026-03-13 19_53 GMT-6.mp4
**Duration:** 42 minutes 36 seconds
**Speakers:** 2 (Speaker A — Aug, Speaker B — Rocky)
**Confidence:** 88.2%
**Language:** English (US)

## Summary

This working session covers two major threads: the ChoreStory homepage buildout and early-stage brainstorming for the companion video game.

Rocky demonstrates a live workflow using Claude Code with the Rawgentic "create issue" skill to generate a GitHub epic for the homepage migration. The plan moves the main app from chorestory.com to app.chorestory.com, with a new Astro-based marketing homepage taking over the root domain. The architecture includes Traefik for routing, Astro + Tailwind for the static site, and subdomain separation for the app, headless display, and dev environments.

Aug introduces BMAD (a brainstorming/project management agent framework) and begins ideating on the game concept. The conversation evolves into a rich discussion about building an MMO where kids earn in-game currency by completing real-world chores. They explore survival/base-building mechanics (inspired by Minecraft, Valheim, Sons of the Forest), AI-driven NPCs, age-appropriate content tiers, and family safety architecture. A key design tension emerges: making the game compelling as a standalone experience while keeping it tied to the chore ecosystem.

The session ends with collaboration logistics: adding Aug to the 3D Stories GitHub org, setting up a WhatsApp group, and planning to reach out to Amanda about joining the project.

## Key Decisions

- The homepage will use **Astro + Tailwind**, not React — better for SEO and static marketing content
- App moves to **app.chorestory.com**; headless stays at **headless.chorestory.com**
- Old chorestory.com URLs should get **proper route rebuilding**, not just 301 redirects (Rocky overruled Claude's lazy suggestion)
- The game should be a **companion app**, not standalone — keeps the demographic closed and family-safe
- Parent participation in the game must be **fully optional** — requiring parents to log in would lose users
- **BMAD** will be used for game brainstorming; **Rawgentic** for implementation workflows

## Ideas & Concepts

- **AI NPCs**: Non-scripted AI characters in the game that players can interact with naturally — both agreed this is a compelling differentiator that hasn't been done well yet
- **Educational gameplay**: Kids could get homework help from AI characters in-game
- **Age-tiered game sections**: 6-8 and 8-10 year olds enjoy different types of gameplay; the game needs maturity tiers within a single world
- **Family server / world segregation**: Each family gets their own isolated piece of the game world; connecting to other families requires mutual permission
- **Chore-to-game rewards**: Completing a load of laundry could yield "100 magic fibers" that buff your base walls for a month
- **Exclusive cosmetic items**: Items only obtainable through chores, but with non-chore alternatives for the same functionality (different cosmetics)
- **Developer blog + bi-weekly vlog**: To document the build process, especially once game development ramps up

## Action Items

- Aug to message Amanda on Saturday morning about joining the project
- Aug to continue BMAD game brainstorming and share the resulting MD file
- Rocky to finish reviewing the homepage epic specs and start implementing via Rawgentic
- Set up a WhatsApp group for ongoing communication; add Amanda once she's on board
- Aug needs to accept the 3D Stories GitHub org invite (username: jamiros)
- Rocky to draft and send NDA before sharing code access

## Discussion Points

- **Fabric vs Snowflake**: Aug's morning started with a broken Fabric pipeline; Rocky shared that switching to Snowflake eliminated nearly all such incidents
- **Rawgentic vs BMAD**: Rocky initially evaluated BMAD as a replacement for Rawgentic but realized they serve complementary purposes — BMAD for ideation/brainstorming, Rawgentic for structured implementation workflows
- **Family safety in gaming**: Both emphasized this as a critical design requirement; Rocky wants to explore novel approaches to family security that go beyond simple access controls
- **Roblox as a platform option**: Aug suggested building on Roblox for younger kids, but Rocky preferred owning the platform to avoid revenue sharing — though not ruling it out at the ideation stage
- **Rocky's new homelab server**: Dual Xeon, 128GB RAM, 12 hot swap bays (Intel/McAfee chassis), plus a Tesla P40 (24GB VRAM, 3840 CUDA cores) for running local AI models via Ollama
- **Claude Opus 1M context**: Both noted the new million-token context window; Aug manages context manually with BMAD saves at 60%, while Rocky has similar functionality built into Rawgentic

## Questions Raised

- What feeling should players have when they put down the controller?
- How do you make the game matter to the whole family, not just the kid?
- Can the game work as both a standalone and a companion app?
- How do you prevent bad actors from using the chore app sign-up as a vector to access kids in-game?
- What's the right game genre for spanning the 6-14 age range?

## Participants

- **Speaker A (Aug)** — Co-founder, data scientist/engineer. Works with Fabric/data pipelines at his day job. Using BMAD for brainstorming. ~35% talk time.
- **Speaker B (Rocky)** — ChoreStory creator/lead developer. Runs the homelab infrastructure, uses Claude Code + Rawgentic for development. Driving the homepage buildout. ~65% talk time.

## Timeline

- **[00:00 - 01:37]** Setup — Screen sharing, Rocky demos the create-issue workflow for the homepage epic
- **[01:37 - 02:20]** Sidebar — Aug's DoorDash delivery fiasco
- **[02:20 - 04:35]** Homepage architecture — Astro framework, subdomain routing, SEO strategy
- **[04:35 - 06:35]** Work discussion — Aug's Fabric pipeline incident, Fabric vs Snowflake comparison
- **[06:35 - 11:15]** Homepage deep dive — Astro documentation, routing corrections, architecture review
- **[11:15 - 12:50]** BMAD introduction — Aug starts game brainstorming with BMAD agents
- **[12:50 - 17:50]** Homepage specs review — Rocky reviews generated specs, discusses NotebookLM assets, Traefik routing, repo organization
- **[17:50 - 23:10]** Homepage live build — Reviewing generated pages, design critique, smooth scroll demo; aside about Opus 1M context
- **[23:10 - 25:10]** Game concept framing — ChoreStory elevator pitch refinement, AI NPC idea emerges
- **[25:10 - 28:00]** Game design brainstorm — Survival/base-building mechanics, family virtual spaces, chore-to-game reward mapping
- **[28:00 - 33:30]** Game architecture discussion — Age tiers, Roblox option, standalone vs companion, family safety
- **[33:30 - 36:10]** Multiplayer safety — Segregated family worlds, permission-based connections, preventing bad actors
- **[36:10 - 38:30]** Collaboration tools — Notion, Obsidian, GitHub discussion; decide on GitHub repo
- **[38:30 - 42:00]** GitHub setup — Adding Aug to 3D Stories org, seat management, NDA mention
- **[42:00 - 42:36]** Wrap-up — WhatsApp group plan, Amanda outreach, goodbye
