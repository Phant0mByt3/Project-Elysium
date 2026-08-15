# 0002 — Core Pillars

**Project:** Elysium MMORPG
**Category:** Project
**Status:** Living Document
**Related:** [0001-Vision.md](0001-Vision.md) · [0008-Development-Philosophy.md](0008-Development-Philosophy.md)

---

Every system, quest, and feature in Project Elysium should be measurable against these six pillars. If a proposed feature doesn't clearly support at least one, it should be reconsidered. If it actively works against one, it should be rejected or redesigned, regardless of how fun it might be in isolation.

The pillars exist so design decisions made by different people, on different days, still add up to one coherent game.

---

## 1. Exploration is Always Rewarding

No region is filler. Every zone hides at least one landmark, secret, or piece of lore (see [0105-Landmarks.md](../0100-World/0105-Landmarks.md)) that isn't required by any quest — pure discovery content for players who wander off the path.

**In practice this means:**
* Every region ships with at least 3–5 unmarked points of interest.
* Vertical space (cliffs, towers, ruins) is built to be climbable or reachable, not just decorative backdrop.
* Hidden lore items (books, journals, murals) contribute to [0209-NPCs.md](../0200-Lore/0209-NPCs.md) and [0206-History.md](../0200-Lore/0206-History.md) without being quest-gated.
* Cosmetic-only rewards (titles, transmog pieces, mounts) are placed in hard-to-reach locations to reward exploration for its own sake.

**Anti-pattern:** a zone that exists only as a corridor between two quest hubs, with no reason to leave the road.

---

## 2. Every Area Has Purpose

Zones are scoped to a level range, a faction presence, and a narrative beat before a single block is placed. See [0102-Regions.md](../0100-World/0102-Regions.md) for how regions are planned against the leveling curve in [0305-Leveling.md](../0300-Characters/0305-Leveling.md).

**In practice this means:**
* Every region has a design brief before construction begins: level range, dominant faction, climate/biome, and the one narrative question it answers.
* No "leftover" space — if an area doesn't serve combat, story, or exploration, it is cut or repurposed.
* Regions connect logically to their neighbors, both geographically and narratively.

**Anti-pattern:** a beautiful but empty region with no quests, no mobs of appropriate level, and no lore justification for existing.

---

## 3. Progression is Meaningful

Talent choices, gear upgrades, and profession milestones (see [0303-Talent-Trees.md](../0300-Characters/0303-Talent-Trees.md), [0600-Professions.md](../0600-Professions/0600-Professions.md)) should change how a player plays, not just their numbers on a tooltip.

**In practice this means:**
* Talent nodes are evaluated on "does this change a decision the player makes in combat," not just "does this increase a stat by X%."
* Gear upgrades are visually distinct, not just numerically distinct — see [1300-Art-Style.md](../1300-Art/1300-Art-Style.md).
* Profession milestones unlock new recipes or capabilities, not just faster versions of the same recipe.

**Anti-pattern:** a talent tree where every "choice" is actually mandatory because the alternative is strictly worse in all situations.

---

## 4. Multiplayer Encourages Cooperation

Systems favor group play without punishing solo players — dungeon finder queues, guild perks, and world events (see [0803-Dungeon-Finder.md](../0800-Multiplayer/0803-Dungeon-Finder.md), [0109-World-Events.md](../0100-World/0109-World-Events.md)) are built to make grouping the natural, rewarding choice.

**In practice this means:**
* Group content rewards are better than solo content rewards, but solo content remains fully completable alone.
* World bosses and events scale to the number of participants so a small group isn't excluded and a large group doesn't trivialize the fight.
* Social tools (party finder, guild browser, cross-realm grouping where relevant) reduce the friction of finding people to play with.

**Anti-pattern:** content that requires a full group but offers no in-game tool to find one, forcing players into external Discords just to progress.

---

## 5. Quality Over Quantity

A smaller, polished continent beats a larger, empty one. Content is not shipped until it meets the bar set in [1400-Development-Standards.md](../1400-Development/1400-Development-Standards.md).

**In practice this means:**
* Scope is cut before quality is cut. If a milestone is at risk, the answer is fewer zones done well, not more zones done poorly.
* Every dungeon, raid, and major quest line goes through a dedicated polish pass before ship — see [1406-Testing.md](../1400-Development/1406-Testing.md).
* Reused assets are acceptable; reused *experiences* (copy-pasted dungeon layouts, identical boss mechanics with a new skin) are not.

**Anti-pattern:** shipping a continent on schedule with known unpolished zones because the date mattered more than the content.

---

## 6. Documentation is Part of Development

No system is considered "done" until it is documented here. Undocumented features are treated as unfinished features — see [1400-Development-Standards.md](../1400-Development/1400-Development-Standards.md) for the documentation-first workflow.

**In practice this means:**
* Design documents are written before implementation begins wherever practical.
* If implementation diverges from the document during development, the document is updated before the feature is considered complete.
* PRs, commits, or building sessions that add a new system without a corresponding doc update are treated the same as a bug — something to be fixed before merge.

**Anti-pattern:** a system that exists in the game but nowhere in `docs/`, forcing new contributors to reverse-engineer it from code or world files.

---

## Using the Pillars in Practice

When evaluating a new feature proposal, ask:

1. Which pillar(s) does this support?
2. Does it work against any pillar? If so, can it be redesigned to avoid that, or is the tradeoff worth it?
3. Is it consistent with how similar features have already been built?

If a feature can't answer question 1 with a clear "yes," it likely doesn't belong in Elysium — or belongs in [0005-Future-Plans.md](0005-Future-Plans.md) / [9000-Future/](../9000-Future/) until it can.

---

## Pillar Conflicts

Occasionally two pillars pull in different directions — for example, Pillar 4 (Cooperation) might push toward gating a landmark behind a group encounter, which could reduce solo accessibility under Pillar 1 (Exploration). When pillars conflict, resolve using the priority order defined in [0008-Development-Philosophy.md](0008-Development-Philosophy.md) Section 5, and document the reasoning in the relevant system's design file so future contributors understand why the tradeoff was made.
