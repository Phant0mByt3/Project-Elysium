# 0003 — Roadmap

**Project:** Elysium MMORPG
**Category:** Project
**Status:** Living Document
**Related:** [0004-Version-History.md](0004-Version-History.md) · [0005-Future-Plans.md](0005-Future-Plans.md)

---

This roadmap tracks Project Elysium's development phases at a high level. Detailed completed work is logged per-version in [0004-Version-History.md](0004-Version-History.md); long-term ideas beyond this roadmap live in [0005-Future-Plans.md](0005-Future-Plans.md).

Phases are sequential in intent but overlap in practice — art and narrative work on Phase 3 content often begins during Phase 2, for example. The phase a task is "in" is defined by what must be substantially complete before the *next* phase can begin.

---

## Phase 0 — Pre-Production *(current)*

**Goal:** lock down the design foundation so every later phase builds on solid ground.

* Finalize core lore, races, classes, and world structure (this documentation set).
* Concept art and art style guide ([1300-Art-Style.md](../1300-Art/1300-Art-Style.md)).
* Prototype combat and stat formulas ([0401-Combat.md](../0400-Gameplay/0401-Combat.md), [0304-Stats.md](../0300-Characters/0304-Stats.md)).
* Stand up plugin architecture skeleton ([1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md)).
* Establish documentation standards and team structure ([0006-Documentation-Guide.md](0006-Documentation-Guide.md), [0007-Team-Structure.md](0007-Team-Structure.md)).

**Exit criteria:** lore is internally consistent, six launch classes are defined at a design level, and the technical team has validated the plugin architecture with a working prototype.

---

## Phase 1 — Core Engine Development

**Goal:** build the backbone every gameplay system will run on.

* Server plugin framework, database schema, authentication ([1201-Database.md](../1200-Technical/1201-Database.md), [1204-Authentication.md](../1200-Technical/1204-Authentication.md)).
* Launcher MVP ([1100-Launcher.md](../1100-Client/1100-Launcher.md)).
* Core UI framework and HUD.
* Networking layer and initial anti-cheat pass ([1207-Anti-Cheat.md](../1200-Technical/1207-Anti-Cheat.md)).

**Exit criteria:** a player can install the launcher, authenticate, and connect to a running server with no gameplay content yet loaded.

---

## Phase 2 — Gameplay Systems

**Goal:** implement the systems players will actually interact with, in a content-agnostic testing environment.

* Classes, talent trees, skills, itemization ([0300-Classes.md](../0300-Characters/0300-Classes.md) through [0509-Enchanting.md](../0500-Items/0509-Enchanting.md)).
* Quest and dialogue systems.
* Economy foundations ([1000-Economy.md](../1000-Economy/1000-Economy.md)).
* Party, guild, and dungeon finder scaffolding ([0800-Multiplayer/](../0800-Multiplayer/)).

**Exit criteria:** all six launch classes are playable end-to-end in a test zone, combat feels correct against the design targets in [0309-Balance.md](../0300-Characters/0309-Balance.md).

---

## Phase 3 — World Building

**Goal:** turn the systems from Phase 2 into an actual playable world.

* Continent 1 (Aurelia) and Continent 2 (Vethmoor) construction.
* First main story arc, first two dungeons, first raid wing.
* Zone-by-zone quest population following [1403-Quest-Writing-Guide.md](../1400-Development/1403-Quest-Writing-Guide.md).
* Landmark and secret placement per Pillar 1 ([0002-Core-Pillars.md](0002-Core-Pillars.md)).

**Exit criteria:** Aurelia and Vethmoor are fully built and quest-populated from level 1 to the launch level cap.

---

## Phase 4 — Closed Alpha

**Goal:** validate the core loop with a small trusted group before wider investment in polish.

* Internal and invited testers. Core loop validation, combat balance passes.
* Bug tracking and triage pipeline stood up ([1407-Bug-Tracking.md](../1400-Development/1407-Bug-Tracking.md)).
* First itemization and economy balance pass based on real player behaviour.

**Exit criteria:** testers can level a character from 1 to cap, run a dungeon, and participate in the economy without game-breaking bugs.

---

## Phase 5 — Closed Beta

**Goal:** stress-test at scale and harden the systems that only break under real load.

* Wider testing, load testing, launcher and account systems hardened.
* Server performance and instance scaling validated ([1209-Instance-System.md](../1200-Technical/1209-Instance-System.md)).
* Support and moderation tooling built ahead of public exposure ([2005-Support-System.md](../2000-Operations/2005-Support-System.md), [2003-Moderation.md](../2000-Operations/2003-Moderation.md)).

**Exit criteria:** server stability holds under target concurrent player counts, and critical/high severity bugs from Alpha are resolved.

---

## Phase 6 — Public Release

**Goal:** launch.

* Launch with Aurelia + Vethmoor, factions live, first raid tier, launcher public.
* Marketing and community channels active.
* Day-one patch plan prepared in advance ([1408-Release-Process.md](../1400-Development/1408-Release-Process.md)).

**Exit criteria:** the game is publicly available, and the live operations team is staffed and ready per [2000-Live-Service.md](../2000-Operations/2000-Live-Service.md).

---

## Phase 7 — Live Service

**Goal:** keep the game healthy and growing post-launch.

* Seasonal events, balance patches, quality-of-life updates.
* Regular content cadence per [2001-Updates.md](../2000-Operations/2001-Updates.md).
* Ongoing analytics-driven tuning ([2006-Analytics.md](../2000-Operations/2006-Analytics.md)).

**Exit criteria:** this phase does not "exit" — it is the ongoing steady state of the game, punctuated by Phase 8 expansions.

---

## Phase 8 — Future Expansions

**Goal:** grow the world.

* Additional continents and systems per [1500-Expansion-Planning.md](../1500-Expansions/1501-Expansion-Planning.md) onward.
* Confirmed directions tracked in [0005-Future-Plans.md](0005-Future-Plans.md); unscoped ideas in [9000-Future/](../9000-Future/).

---

## Phase Summary Table

| Phase | Name | Primary Output | Key Exit Signal |
| --- | --- | --- | --- |
| 0 | Pre-Production | Design foundation | Lore + classes locked |
| 1 | Core Engine | Technical backbone | Launcher connects to server |
| 2 | Gameplay Systems | Playable systems in isolation | All classes playable in test zone |
| 3 | World Building | Aurelia + Vethmoor built | Full leveling path exists |
| 4 | Closed Alpha | Core loop validated | 1–cap playable, no game-breakers |
| 5 | Closed Beta | Scale validated | Stable under target load |
| 6 | Public Release | Launch | Game is live |
| 7 | Live Service | Ongoing health | Steady state |
| 8 | Future Expansions | World growth | New continents ship |

---

## Risk Notes

* **Scope risk:** World Building (Phase 3) is historically the highest-risk phase for MMORPGs — Pillar 5 (Quality Over Quantity, see [0002-Core-Pillars.md](0002-Core-Pillars.md)) exists specifically to guard against shipping an underbuilt continent to hit a date.
* **Technical risk:** the plugin architecture validated in Phase 0/1 must hold up under the concurrent player loads targeted for Phase 5; revisiting core architecture late is the most expensive kind of rework.
* **Content risk:** narrative and quest content is easy to under-scope; [1403-Quest-Writing-Guide.md](../1400-Development/1403-Quest-Writing-Guide.md) exists to standardize output so quest density stays consistent zone to zone.

This roadmap is revisited at the start of every phase transition and whenever [0004-Version-History.md](0004-Version-History.md) shows the project has drifted meaningfully from the plan.
