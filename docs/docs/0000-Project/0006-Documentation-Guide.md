# 0006 — Documentation Guide

**Project:** Elysium MMORPG
**Category:** Project
**Status:** Living Document

---

This guide is a map of the entire `docs/` tree. Every file gets a short summary (≤5 lines) so any dev can skim this one document and understand what exists and where, without reading all 300+ files individually. Summaries are written from the live content of each file, not just the filename — read the linked file itself for full detail.

For the raw folder tree, see [Doc-Structure.md](../Doc-Structure.md).

## Table of Contents

- [0000 — Project](#0000--project)
- [0100 — World](#0100--world)
- [0200 — Lore](#0200--lore)
- [0300 — Characters](#0300--characters)
- [0400 — Gameplay](#0400--gameplay)
- [0500 — Items](#0500--items)
- [0600 — Professions](#0600--professions)
- [0700 — Quests](#0700--quests)
- [0800 — Multiplayer](#0800--multiplayer)
- [0900 — Player Systems](#0900--player-systems)
- [1000 — Economy](#1000--economy)
- [1100 — Client](#1100--client)
- [1200 — Technical](#1200--technical)
- [1300 — Art](#1300--art)
- [1400 — Development](#1400--development)
- [1500 — Expansions](#1500--expansions)
- [2000 — Operations](#2000--operations)
- [9000 — Future](#9000--future)

---

## 0000 — Project

High-level identity of the project: what it is, why it exists, and how the team runs.

- **[0000-Overview.md](0000-Overview.md)** — Elysium is a handcrafted MMORPG built natively on Unreal Engine (used for rendering/physics/networking, not as a survival sandbox). Players pick a race, class, and faction and explore a world fractured by a cataclysm 800 years ago. Defines the target audience and states that `docs/` is the full GDD.
- **[0001-Vision.md](0001-Vision.md)** — The founding philosophy: Unreal Engine is the engine, Elysium is the experience. Lists which default engine/template systems are removed/restricted/replaced, the handcrafted-world philosophy, city/continent scale targets, and the "I forgot this was built in an engine" success test.
- **[0002-Core-Pillars.md](0002-Core-Pillars.md)** — The six non-negotiable design pillars every feature is measured against: rewarding exploration, purposeful areas, meaningful progression, cooperative multiplayer, quality over quantity, and documentation-first development.
- **[0003-Roadmap.md](0003-Roadmap.md)** — High-level development phases from Pre-Production through Core Engine, Gameplay Systems, World Building, Closed Alpha/Beta, Public Release, Live Service, and Future Expansions.
- **[0004-Version-History.md](0004-Version-History.md)** — Living changelog template (Added/Changed/Fixed/Removed per version). Currently empty — project is still in Pre-Production.
- **[0005-Future-Plans.md](0005-Future-Plans.md)** — Committed-but-unscheduled long-term ideas: Continents 3–5 (Sylvaneth, Kharzul Wastes, Nightreach), guild housing neighborhoods, cross-faction events, a third faction, and player ships. Raw brainstorms instead live in [9999-Ideas.md](../9000-Future/9999-Ideas.md).
- **[0006-Documentation-Guide.md](0006-Documentation-Guide.md)** — This file: a summary index of the entire documentation tree.
- **[0007-Team-Structure.md](0007-Team-Structure.md)** — Roles and discipline teams (Creative Director, Lead Game Designer, World Director, Narrative Lead, Technical Lead, Art Director, Client Lead, QA Lead), decision-making authority, and onboarding steps.
- **[0008-Development-Philosophy.md](0008-Development-Philosophy.md)** — Expands on documentation-first development, quality-over-quantity, handcrafted-world priority, a player-experience conflict-resolution hierarchy, and long-term architectural thinking.
- **[0009-Project-Glossary.md](0009-Project-Glossary.md)** — Living A–Z glossary of proper nouns and terms (Sundering, Aurum, Elysian Circle, Kaelgorath, Aurelia, Vethmoor, factions, etc.) used across all other docs.

## 0100 — World

The physical world: continents, regions, settlements, points of interest, and the environmental systems layered on top of them.

- **[0100-World.md](../0100-World/0100-World.md)** — Entry point for the World category. Elysium is a shattered realm slowly reforming since the Sundering; players start in the current "Age of Reclamation." Covers launch scale (Aurelia + Vethmoor, three more continents planned), the no-procedural-generation design approach, and the Overworld/Instance/City layer split.
- **[0101-Continents.md](../0100-World/0101-Continents.md)** — Describes all five continents: launch continents Aurelia (human heartland, levels 1–30) and Vethmoor (dwarves vs orcs, levels 25–50), plus planned Sylvaneth, Kharzul Wastes, and Nightreach expansions.
- **[0102-Regions.md](../0100-World/0102-Regions.md)** — Defines the region template (level range, theme, faction presence, key locations, local conflict) and lists all launch regions across Aurelia and Vethmoor with their level bands.
- **[0103-Cities.md](../0100-World/0103-Cities.md)** — Major faction hub cities: Solmere (Aurelia/Concord capital), Ashka Vor (orc capital), Ironpeak Hold (dwarf capital). Lists mandatory city features (bank, auction house, trainers, fast travel, guild hall).
- **[0104-Villages.md](../0100-World/0104-Villages.md)** — Smaller settlements that anchor a region's local questline and flavor. Defines sizing/design rules and gives launch examples (Millhaven, Fenwick Crossing, Sunspire Vale).
- **[0105-Landmarks.md](../0100-World/0105-Landmarks.md)** — Non-quest-hub points of interest rewarding pure exploration (ruins, natural wonders, secrets, memorials). Every region must have at least one. Gives concrete examples like the Sundered Spire.
- **[0106-Dungeons.md](../0100-World/0106-Dungeons.md)** — 5-player instanced group content between questing and raiding. Defines required structure (bosses, framing narrative, loot), difficulty modes (Normal/Heroic/Mythic), and lists the four launch dungeons.
- **[0107-Raids.md](../0100-World/0107-Raids.md)** — Endgame 10–20 player instances. Design principles (mechanic identity, difficulty tiers, weekly lockouts) and details the launch raid, The Sunken Concord, and its three wings.
- **[0108-World-Bosses.md](../0100-World/0108-World-Bosses.md)** — Open-world timed/triggered bosses for spontaneous large-group play. Design rules plus three launch examples (Grothmar, the Ashen Colossus, Maelith's Herald).
- **[0109-World-Events.md](../0100-World/0109-World-Events.md)** — Time-limited server-wide content: dynamic events, invasions, and seasonal events, plus a "Major World Events"/phase system (Before/During/After) for large permanent world changes like the example Collision Event.
- **[0110-Travel.md](../0100-World/0110-Travel.md)** — Travel philosophy (purposeful early, frictionless late) and the base movement methods: on foot, mounts, ships, and portals, plus travel-related design rules.
- **[0111-Fast-Travel.md](../0100-World/0111-Fast-Travel.md)** — The progressive fast-travel layer: waypoint shrines (unlocked by exploration), NPC flight routes, and per-character Hearthstone recall, plus where fast travel is disabled.
- **[0112-Maps.md](../0100-World/0112-Maps.md)** — Staging area for continent/region layout maps used before construction; describes the map-to-build production process and current draft layouts for Aurelia and Vethmoor.
- **[0113-Biomes.md](../0100-World/0113-Biomes.md)** — Authored (not generated) biome categories mapped to specific regions, plus design rules and how biome choice affects enemy placement, profession nodes, weather, and art direction.
- **[0114-Weather-System.md](../0100-World/0114-Weather-System.md)** — Region-aware, biome-driven weather types (rain, storms, fog, blizzard, ashfall, Sundering Storm) with real gameplay effects, scheduling rules, and server-authoritative implementation notes.
- **[0115-Day-Night-Cycle.md](../0100-World/0115-Day-Night-Cycle.md)** — Shared, continuous ~2.5–3 hour day/night cycle with timing table, gameplay effects (visibility, enemy behavior, NPC routines), and server-authoritative sync notes.
- **[0116-World-Generation.md](../0100-World/0116-World-Generation.md)** — States explicitly that Elysium uses zero runtime procedural generation. Details the offline Unreal Landscape-based production pipeline from concept sketch to locked, versioned world template, and the few controlled exceptions (dungeons, events, housing).
- **[0117-Environmental-Hazards.md](../0100-World/0117-Environmental-Hazards.md)** — Persistent/temporary terrain and weather dangers (lava, toxic gas, blizzard wind, etc.) with a hazard table, design rules (always telegraphed, never soft-locking), and links to status effects and resistances.

## 0200 — Lore

The Sundering, the pantheon, factions, races, kingdoms, and the narrative campaign built on top of them.

- **[0200-Lore.md](../0200-Lore/0200-Lore.md)** — Entry point to the Lore category. Summarizes the core lore premise: the Elysian Circle's golden Age of Concord, the eighth god Kaelgorath's betrayal (the Sundering), the Age of Ash, and the present Age of Reclamation. Lists recurring themes and writing-consistency requirements.
- **[0201-Timeline.md](../0200-Lore/0201-Timeline.md)** — Chronological ages of Elysium (Dawn, Concord, the Sundering, Ash, Reclamation) with dates, plus the "timeline system" concept for preserving historical world-states without deleting old versions.
- **[0202-Gods.md](../0200-Lore/0202-Gods.md)** — The seven-member Elysian Circle pantheon (Solthar, Nyxara, Terravox, Maelithir, Ignareth, Voranthe, Aeloria) and the fallen eighth god Kaelgorath, with domains and design-use notes for classes/architecture/holidays.
- **[0203-Factions.md](../0200-Lore/0203-Factions.md)** — The two player factions (Dawnbound Concord vs. Duskward Pact), their philosophies, capitals, and dominant races, plus neutral organizations (Wayfarer's Guild, Cartographer's League, Ashen Circle).
- **[0204-Races.md](../0200-Lore/0204-Races.md)** — The six playable races (Humans, High Elves, Dwarves, Orcs, Beastkin, Revenants) with culture, class affinities, and faction leanings.
- **[0205-Kingdoms.md](../0200-Lore/0205-Kingdoms.md)** — The political nations distinct from factions: the Concord Dominion, Sylvaria Enclave, Ironpeak Holds, and Ashenclaw Warbands, and how kingdom politics surface via reputation and territory-control systems.
- **[0206-History.md](../0200-Lore/0206-History.md)** — Expanded historical events referenced in quests: the fall of Aethercrest, founding of the Concord and Pact, the first Revenant sighting, and the recent reopening of travel between continents that kicks off the main story.
- **[0207-Main-Story.md](../0200-Lore/0207-Main-Story.md)** — The three-act main campaign structure: Act I Reconnection (Aurelia, 1–20), Act II Fracture Lines (Vethmoor, 20–40), Act III The Sunken Concord (45–50, leads into the launch raid). Includes design rules for faction-flavored but non-gating story.
- **[0208-Side-Stories.md](../0200-Lore/0208-Side-Stories.md)** — Design principles for optional questlines that enrich but never gate the main story, with three launch examples ("The Miller's Debt," "Echoes of Aethercrest," "Clanbreaker").
- **[0209-NPCs.md](../0200-Lore/0209-NPCs.md)** — NPC categories (quest givers, merchants/trainers, rulers, companions, named enemies) and naming/flavor requirements, plus key launch NPCs like High Councilor Aldwin Rae and Warmother Ushka Dren.
- **[0210-Dialogue-System.md](../0200-Lore/0210-Dialogue-System.md)** — Design for an MMORPG-style branching dialogue UI (portrait, reputation display, multiple response options affecting reputation/quests), a data-driven NPC dialogue format, and future ideas like voice acting and cinematic conversations.
- **[0211-Languages.md](../0200-Lore/0211-Languages.md)** — Flavor-only in-world languages (Common, Aurelian, High Elven, Dwarven, Orcish, Beastongue, Revenant Cant, Old Concord) used for immersion and optional lore-decoding, never blocking quest progress.
- **[0212-Religions.md](../0200-Lore/0212-Religions.md)** — The seven faiths tied to the gods (Solar Path, Night Vigil, Stone Covenant, Forge Flame, Green Communion, Quiet Road, Storm Call), their cultural associations, and rules for how religion colors flavor without gating progression.
- **[0213-Mythology.md](../0200-Lore/0213-Mythology.md)** — In-world myths and legends (creation myth, Sundering prophecy, the gods' silence, drifting continents) that are deliberately contradictory/incomplete, plus rules for regional legends and seeding future reveals.
- **[0214-Ancient-Civilisations.md](../0200-Lore/0214-Ancient-Civilisations.md)** — Pre- and post-Sundering cultures (the Concord Civilisation, Pre-Concord Kingdoms, Forge Clans, Star-Singers, Beastkin Ancestors, Sundered Remnants) and rules for layering ruins/loot flavor and leaving history incomplete for future expansions.
- **[0215-Ancient-Archivarium.md](../0200-Lore/0215-Ancient-Archivarium.md)** — Brainstorm/concept doc for a hidden, time-spanning lore dimension (portals hidden across the world) containing archives of history, creatures, players' world-first achievements, cut ideas, and prophecies — with the design rule that it should never reveal everything.

## 0300 — Characters

Classes, specializations, stats, leveling, character creation, and death.

- **[0300-Classes.md](../0300-Characters/0300-Classes.md)** — The eight launch classes (Warrior, Paladin, Rogue, Ranger, Mage, Necromancer, Cleric, Druid), their roles (Tank/Healer/Damage), patron gods, and the design rule that any race can play any class.
- **[0301-Specializations.md](../0300-Characters/0301-Specializations.md)** — Each class's two level-10 specializations (e.g. Warrior → Vanguard/Berserker) with design rules for mechanical distinctness and free respeccing.
- **[0302-Skills.md](../0300-Characters/0302-Skills.md)** — Skill categories (Core, Specialization, Utility, Ultimate), the "skill anatomy" documentation format, and unlock pacing philosophy.
- **[0303-Talent-Trees.md](../0300-Characters/0303-Talent-Trees.md)** — The main build-customization system: one tree per spec with three sub-paths, no trap talents, build-defining capstones, and cheap full respec.
- **[0304-Stats.md](../0300-Characters/0304-Stats.md)** — Primary stats (Strength, Intellect, Agility, Stamina) and secondary stats (Crit, Haste, Mastery, Versatility, Armor, Resistance), plus formula/scaling philosophy.
- **[0305-Leveling.md](../0300-Characters/0305-Leveling.md)** — Level cap 50, XP sources weighted toward quests/dungeons/exploration over grinding, pacing tied to regional level bands, and reward milestones at levels 10/15/25/50.
- **[0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md)** — Buffs, debuffs, crowd control, and elemental conditions, plus PvP diminishing-returns rules for CC and PvE boss CC immunity.
- **[0307-Elements.md](../0300-Characters/0307-Elements.md)** — The seven damage types (Fire, Frost, Nature, Shadow, Holy, Arcane, Physical), their associated gods/status effects, elemental combo interactions, and enemy resistance design.
- **[0308-Class-Progression.md](../0300-Characters/0308-Class-Progression.md)** — The detailed timeline binding classes/leveling/skills/talents/specializations together: three parallel point currencies, level-by-level unlock tables (1–9), milestone levels (10/20/30/40/50/60), specialization evolution tiers, Advanced Class Paths (level 40+), and endgame horizontal progression via Mastery Points and Legendary upgrades.
- **[0309-Balance.md](../0300-Characters/0309-Balance.md)** — Balance philosophy as an ongoing process (not pre-launch checkbox), viability goals, review cadence across dev phases, and the rule that major balance shifts get logged in version history.
- **[0310-Character-Creation.md](../0300-Characters/0310-Character-Creation.md)** — The six-step creation flow (Race → Faction → Class → Appearance → Name → Confirmation), what's permanent vs. respeccable, and technical notes on when data is committed.
- **[0311-Character-Customisation.md](../0300-Characters/0311-Character-Customisation.md)** — Creation-time appearance options (body, face, skin, hair, markings) vs. ongoing cosmetic systems, plus design principles (silhouette readability, preserved racial identity).
- **[0312-Character-Animations.md](../0300-Characters/0312-Character-Animations.md)** — Animation categories (locomotion, combat stance, ability, hit reaction, emotes, death) and design rules emphasizing telegraphing and class-fantasy weight.
- **[0313-Death-System.md](../0300-Characters/0313-Death-System.md)** — Death as a low-punishment setback: spirit/release/resurrect flow, respawn locations by content type, modest durability loss, and no experience debt.

## 0400 — Gameplay

Combat, enemy/AI design, difficulty, physics, and onboarding.

- **[0400-Game-Mechanics.md](../0400-Gameplay/0400-Game-Mechanics.md)** — Broad mechanics overview: MMORPG-first design philosophy, ability-based combat, the default WASD + QERT/Tab/1-2 control scheme, the ultimate-ability energy system, class movement abilities (Alt), the custom inventory/character UI (replacing the engine's default template), and key rebinding.
- **[0401-Combat.md](../0400-Gameplay/0401-Combat.md)** — Core action-targeted combat loop (target → use abilities on cooldown/resource → manage telegraphed positioning), the requirement that each class be visually/audibly distinct, and how damage/threat/status effects interact.
- **[0402-Enemy-Design.md](../0400-Gameplay/0402-Enemy-Design.md)** — Enemy categories (Trash, Elite, Mini-Boss, Boss, World Boss) and design principles: readable identity, regional flavor, one signature mechanic per enemy, no "pure sponge" difficulty.
- **[0403-Boss-Mechanics.md](../0400-Gameplay/0403-Boss-Mechanics.md)** — Requirements every boss must meet (unique mechanic, telegraphs, framing narrative, phases), the Normal/Heroic/Mythic difficulty tiers, common mechanic families, and the no-untelegraphed-one-shots fairness rule.
- **[0404-AI-Behaviour.md](../0400-Gameplay/0404-AI-Behaviour.md)** — Reusable AI behavior modules (Idle/Patrol, Acquire Target, Melee/Ranged Loop, Special Ability, Flee/Reset, Call for Help) and rules for purposeful, non-cheating, performance-budgeted AI.
- **[0405-Aggro-System.md](../0400-Gameplay/0405-Aggro-System.md)** — Threat/aggro mechanics: how damage/healing/tank abilities generate threat, tank identity tools, threat-dumping utility, and open-world vs. instance social aggro rules.
- **[0406-Difficulty-System.md](../0400-Gameplay/0406-Difficulty-System.md)** — Discrete difficulty tiers per content type (open-world baseline; Normal/Heroic/Mythic for dungeons/raids; scaled world bosses), what changes between tiers, and the philosophy that difficulty comes from mechanics, not just numbers.
- **[0407-World-Interactions.md](../0400-Gameplay/0407-World-Interactions.md)** — Non-combat interaction types (lore objects, ambient NPC dialogue, environmental storytelling, utility interactions, profession nodes, rest/social spots) and rules keeping critical-path interactions unmissable.
- **[0408-Physics-Systems.md](../0400-Gameplay/0408-Physics-Systems.md)** — How Unreal Engine's physics substrate is customized for MMORPG combat/traversal: server authority, no sequence-breaking, and customized falling/knockback/mount/swimming/projectile behavior.
- **[0409-Tutorial-System.md](../0400-Gameplay/0409-Tutorial-System.md)** — Tutorial folded into the real starting zone rather than a separate mode; teaching sequence for the first session and rules against forced, unskippable tutorial gates.

## 0500 — Items

Weapons, armor, loot, itemization tiers, and everything that lives in a player's inventory.

- **[0500-Weapons.md](../0500-Items/0500-Weapons.md)** — Weapon types (1H/2H swords/axes/maces, daggers, bows, staves, shields) mapped to class access, design rules on stat scaling with item level, and acquisition sources including Blacksmithing.
- **[0501-Armour.md](../0500-Items/0501-Armour.md)** — Four armor categories (Cloth/Leather/Mail/Plate) mapped to classes, slot list, set-bonus mechanics, progression path from quests → dungeons → crafted → raids, and silhouette-readability standards.
- **[0502-Accessories.md](../0500-Items/0502-Accessories.md)** — Rings, necklace, trinkets, and cloak slot design; trinkets are the primary build-defining accessory and should synergize with specs rather than be generic stat sticks.
- **[0503-Loot.md](../0500-Items/0503-Loot.md)** — General loot philosophy: the six rarity tiers (Common through Relic), need/greed/pass and personal loot distribution rules, and the goal of loot feeling like a celebratory story beat.
- **[0504-Loot-Tables.md](../0500-Items/0504-Loot-Tables.md)** — Framework for how per-encounter loot tables should be structured (guaranteed drops, rare-or-higher pool, drop chance by difficulty, set tagging) and design rules for role coverage.
- **[0505-Legendary-Items.md](../0500-Items/0505-Legendary-Items.md)** — Design rules for unique, lore-tied Legendary gear (name, lore blurb, multi-step acquisition) with two launch examples: Aldric's Last Stand and The Warden's Seed.
- **[0506-Relics.md](../0500-Items/0506-Relics.md)** — The rarest item tier, tied directly to the gods/pre-Sundering artifacts, extremely low drop rate, with the launch example Shard of the Sunspire and its role in the future Nightreach story.
- **[0507-Consumables.md](../0500-Items/0507-Consumables.md)** — Potions, food/drink, scrolls, and bandages/field kits; design rules on cooldown categories and keeping buffs optional outside Heroic/Mythic content.
- **[0508-Crafting.md](../0500-Items/0508-Crafting.md)** — The umbrella crafting loop connecting gathering to production professions: gather → learn recipe → craft → sell/use, with rules keeping crafted gear competitive and profession-exclusive item types.
- **[0509-Enchanting.md](../0500-Items/0509-Enchanting.md)** — Permanent stat-boosting enchants layered on base item stats: disenchant → learn recipe → apply, with rules against a single best-in-slot enchant and raid-tier material gating.
- **[0510-Item-Rarity.md](../0500-Items/0510-Item-Rarity.md)** — The color-coded rarity tier table (White through Gold/Relic) with sources and UI/visual design rules including colorblind-safe requirements.
- **[0511-Item-Upgrading.md](../0500-Items/0511-Item-Upgrading.md)** — Upgrade paths (rank/reinforcement, enchanting, socketing, Legendary empowerment) letting players invest in favorite gear instead of only chasing item level, plus economy/inflation-control tie-ins.
- **[0512-Item-Sets.md](../0500-Items/0512-Item-Sets.md)** — Armor set structure (2/4/6-piece bonus thresholds), design rules that bonuses reinforce spec fantasy without being mandatory, and set tracking via the Collections UI.
- **[0513-Transmog-System.md](../0500-Items/0513-Transmog-System.md)** — Cosmetic appearance system separating look from stats; unlock rules, armor/weapon type restrictions, and a small Aurum cost to apply.
- **[0514-Item-Binding.md](../0500-Items/0514-Item-Binding.md)** — Binding types (Bind on Pickup, Bind on Equip, Bind on Use, Account Bound, Unbound) and rules governing which content tiers use which binding and trade-window exceptions.
- **[0515-Item-Durability.md](../0500-Items/0515-Item-Durability.md)** — Light, modest gold/material sink tied to death and combat wear, repaired via NPC vendors or crafting professions; never meant to be punishing.
- **[0516-Item-Attributes.md](../0500-Items/0516-Item-Attributes.md)** — The numerical/mechanical attribute categories on items (primary/secondary stats, defensive, weapon, special/unique) bridging items to the character stat system.
- **[0517-Unique-Effects.md](../0500-Items/0517-Unique-Effects.md)** — Non-standard item mechanics — on-use, proc, conditional, build-defining, utility — with rules on readability and reserving build-defining power for Legendary/Relic tiers.
- **[0518-Artifact-Items.md](../0500-Items/0518-Artifact-Items.md)** — A story-rich item tier above/alongside Legendaries tied to gods and major history, with multi-stage "awakening" upgrades and iconic, recognizable visual design.
- **[0519-Item-Storage.md](../0500-Items/0519-Item-Storage.md)** — Storage layers (personal inventory, personal bank, guild bank, specialized bags, void/overflow) and design rules ensuring items are never silently lost.

## 0600 — Professions

Gathering and production professions, materials, recipes, and long-term profession progression.

- **[0600-Professions.md](../0600-Professions/0600-Professions.md)** — Overview of the profession system: every character learns up to two of the gathering/production professions plus universal Enchanting, the two-profession pairing rule, and how profession level caps track the character level cap.
- **[0601-Mining.md](../0600-Professions/0601-Mining.md)** — Gathering profession for ore/stone from veins, densest in Vethmoor; feeds Jewelcrafting (gems) and Blacksmithing (bars), with notes on vein respawn tuning.
- **[0602-Woodcutting.md](../0600-Professions/0602-Woodcutting.md)** — Gathering profession for timber, densest in Wildwood Reach, feeding Tailoring and general materials; positioned as a low-friction "casual" gathering profession.
- **[0603-Fishing.md](../0600-Professions/0603-Fishing.md)** — A relaxed secondary gathering activity open to all characters regardless of profession slots, feeding Cooking, with rare "gacha-style" catches placed near landmarks.
- **[0604-Herbalism.md](../0600-Professions/0604-Herbalism.md)** — Gathering profession for herbs/reagents feeding Alchemy (and secondarily Cooking), with rarer herbs concentrated in higher-danger zones.
- **[0605-Alchemy.md](../0600-Professions/0605-Alchemy.md)** — Production profession turning herbs into potions across healing, combat, utility, and transmutation recipe categories, with raid-gated best-in-slot potions.
- **[0606-Blacksmithing.md](../0600-Professions/0606-Blacksmithing.md)** — Production profession turning ore into weapons and Plate/Mail armor, culturally tied to the dwarven Ironpeak Holds, plus shields and gathering-tool upgrades.
- **[0607-Cooking.md](../0600-Professions/0607-Cooking.md)** — Production profession turning fishing/farm materials into buff food (stat food, regen food, group feasts), positioned as the most casually accessible profession.
- **[0608-Jewelcrafting.md](../0600-Professions/0608-Jewelcrafting.md)** — Production profession cutting gems (from Mining) into socketable gems and crafted rings/necklaces, with broad relevance similar to Enchanting.
- **[0609-Tailoring.md](../0600-Professions/0609-Tailoring.md)** — Production profession turning cloth into Cloth armor plus the unique cross-class Bags recipe line and cosmetic cloth items.
- **[0610-Leatherworking.md](../0600-Professions/0610-Leatherworking.md)** — Production profession for leather/hide armor and utility items (bags, quivers, drums) serving leather-wearing classes, sourced from skinning.
- **[0611-Profession-Progression.md](../0600-Professions/0611-Profession-Progression.md)** — The Apprentice → Journeyman → Expert → Artisan/Master skill-tier structure, paced against regional level bands, with catch-up mechanisms for alts.
- **[0612-Profession-Materials.md](../0600-Professions/0612-Profession-Materials.md)** — Five material tiers roughly matching regional progression, design rules for regional material flavor and Auction House economy interaction.
- **[0613-Resource-Nodes.md](../0600-Professions/0613-Resource-Nodes.md)** — Hand-placed gathering node types (ore veins, herb patches, trees, fishing pools) and rules on biome fidelity, density near travel routes, and respawn timing.
- **[0614-Profession-Recipes.md](../0600-Professions/0614-Profession-Recipes.md)** — Recipe data structure (materials, station, reagents, gates) and acquisition sources (trainers, drops, quests, vendors, discovery).
- **[0615-Profession-Specialisations.md](../0600-Professions/0615-Profession-Specialisations.md)** — High-skill-threshold specialization branches per profession (e.g. Blacksmithing's Weaponsmith/Armoursmith), creating market niches without hard-locking players out of the rest of the profession.
- **[0616-Profession-Mastery.md](../0600-Professions/0616-Profession-Mastery.md)** — Post-cap horizontal progression track rewarding crafting/gathering dedication with passive bonuses, cosmetics, titles, and prestige recipes — never mandatory for combat power.

## 0700 — Quests

The quest system end-to-end: types, chains, repeatables, achievements/titles, reputation, main quest, and the technical scripting layer.

- **[0700-Quests.md](../0700-Quests/0700-Quests.md)** — Entry point covering quest types (Main Story, Side, Chains, Daily/Weekly), the "quest anatomy" documentation format, and design standards (no unmotivated fetch quests, scaled rewards).
- **[0701-Quest-Chains.md](../0700-Quests/0701-Quest-Chains.md)** — Structure of multi-step questlines (hook, rising steps, climax, resolution) with pacing and signposting rules for chains gating dungeons/raids.
- **[0702-Daily-Quests.md](../0700-Quests/0702-Daily-Quests.md)** — Repeatable once-per-day, mostly max-level objectives; rotation rules, non-mandatory design, and launch daily hub examples per faction.
- **[0703-Weekly-Quests.md](../0700-Quests/0703-Weekly-Quests.md)** — Once-per-week, larger-reward objectives tied to group content (raid clears, dungeon rotations, world events), layered as bonus rather than primary incentive.
- **[0704-Achievements.md](../0700-Quests/0704-Achievements.md)** — Permanent accomplishment tracking across exploration, story, combat, PvP, collection, and profession categories; rewards are titles/cosmetics, not power.
- **[0705-Titles.md](../0700-Quests/0705-Titles.md)** — Cosmetic name modifiers earned from achievements/milestones, examples ("the Reclaimer," "of the Sunken Concord"), plus a note on historical/legacy titles; purely cosmetic, no gameplay bonus.
- **[0706-Reputation.md](../0700-Quests/0706-Reputation.md)** — The general per-organization reputation tier system (Hated → Exalted), sources, and the rule that reputation gates cosmetics/vendors, not core power.
- **[0707-Factions-Reputation.md](../0700-Quests/0707-Factions-Reputation.md)** — Reputation specifically with the Concord/Pact factions: starting standing, tier rewards (Honored/Revered/Exalted), the costly faction-change service, and the cross-faction PvP-parity rule.
- **[0708-Main-Quest.md](../0700-Quests/0708-Main-Quest.md)** — Implementation-level detail on the critical-path campaign (soloable, faction-aware, matches leveling curve), its three-act structure, and a note on story-gated world-state unlocks.
- **[0709-Side-Quests.md](../0700-Quests/0709-Side-Quests.md)** — Design principles and types (Regional, Character-driven, Exploration, Faction, Profession/Reputation) for optional content that enriches without gating the Main Quest.
- **[0710-Quest-Objectives.md](../0700-Quests/0710-Quest-Objectives.md)** — Objective types (Kill, Collect, Interact, Escort/Defend, Reach/Discover, Craft/Deliver, Choice) and rules for motivation, clarity, and recoverable fail states.
- **[0711-Quest-Rewards.md](../0700-Quests/0711-Quest-Rewards.md)** — Reward types (XP, Aurum, gear choice, reputation, items, cosmetics, recipes) and tuning rules so quest rewards keep pace with leveling and never feel arbitrary.
- **[0712-Cinematics.md](../0700-Quests/0712-Cinematics.md)** — Sparing use of in-engine cutscenes for major story beats: usage guidelines, skippability, and the rule that cinematics never carry critical mechanical info exclusively.
- **[0713-Quest-Tracking.md](../0700-Quests/0713-Quest-Tracking.md)** — UI elements for tracking active quests (Quest Log, Tracker Panel, Map Markers, World Indicators, Chapter Frame) and the goal of players never being unsure what to do next.
- **[0714-Quest-Branches.md](../0700-Quests/0714-Quest-Branches.md)** — Player-choice branch types (dialogue, faction, reputation/prior choice, ending) and rules keeping the Main Quest lightly branched while side stories carry heavier branching.
- **[0715-Dynamic-Quests.md](../0700-Quests/0715-Dynamic-Quests.md)** — Quests that appear/change/expire based on world state or events (village defenses, caravan escorts) reinforcing the living-world fantasy without blocking permanent progression.
- **[0716-World-Quest-System.md](../0700-Quests/0716-World-Quest-System.md)** — Rotating, short, location-based repeatable objectives spread across the open world for mid/max-level players, designed to spread players across the map.
- **[0717-Quest-Scripting.md](../0700-Quests/0717-Quest-Scripting.md)** — The technical layer turning quest designs into runnable, data-driven content: objective tracking, dialogue triggers, branching, cinematics, and reward grants, all server-authoritative.

## 0800 — Multiplayer

Guilds, parties, raiding logistics, matchmaking, PvP, social tools, and competitive systems.

- **[0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md)** — Persistent player organizations: creation cost, ranks/permissions, guild bank, chat/roster, level-based perks, and the single-faction-only membership rule.
- **[0801-Parties.md](../0800-Multiplayer/0801-Parties.md)** — Temporary up-to-5-player groups for questing/dungeons: formation, shared quest credit, loot rules, and the single-faction restriction.
- **[0802-Raiding.md](../0800-Multiplayer/0802-Raiding.md)** — The social/logistical layer around raid instances: group formation (10–20 players), weekly per-character lockouts, role composition expectations, and guild progress tracking.
- **[0803-Dungeon-Finder.md](../0800-Multiplayer/0803-Dungeon-Finder.md)** — Automated role-based matchmaking tool for queued dungeons, role-balance incentives, same-faction pooling, and which difficulties are queueable (Mythic excluded).
- **[0804-PvP.md](../0800-Multiplayer/0804-PvP.md)** — Overview of faction-based PvP (open-world contested zones + Arenas), Aurelia being PvP-safe by default, and balance considerations like separate PvP damage modifiers and a resilience-style stat.
- **[0805-Arenas.md](../0800-Multiplayer/0805-Arenas.md)** — Structured 2v2/3v3 ranked PvP: seasonal ladder resets, cosmetic/title rewards over power, and symmetrical, lore-free arena map design.
- **[0806-Territory-Control.md](../0800-Multiplayer/0806-Territory-Control.md)** — Large-scale open-world PvP over capturable objectives in contested Vethmoor regions, control benefits, and design rules against runaway single-guild dominance.
- **[0807-Seasons.md](../0800-Multiplayer/0807-Seasons.md)** — The 10–12 week seasonal umbrella structure tying together Arena resets and rotating themed world events, with an illustrative launch calendar (Reclamation Festival, Emberfall, The Long Dusk, Dawnrise).
- **[0808-Leaderboards.md](../0800-Multiplayer/0808-Leaderboards.md)** — Competitive/prestige ranking categories (Arena, Raid Progression, World/Region, Profession, Achievement) with seasonal resets and opt-out privacy.
- **[0809-Friend-System.md](../0800-Multiplayer/0809-Friend-System.md)** — Persistent cross-session friend list with online status, notes, quick invite, privacy controls, and account-level cross-character visibility.
- **[0810-Social-Features.md](../0800-Multiplayer/0810-Social-Features.md)** — Broader social toolset: chat channels, emotes, player inspection, ignore/block/report, group-finder integration, and notifications, with toxicity countermeasures as first-class.
- **[0811-Party-Finder.md](../0800-Multiplayer/0811-Party-Finder.md)** — Player-driven group-listing tool (activity type, roles, requirements, free text) complementing the automated Dungeon Finder.
- **[0812-Voice-Communication.md](../0800-Multiplayer/0812-Voice-Communication.md)** — Optional built-in party/raid/guild voice chat with push-to-talk, privacy/consent controls, and accessibility considerations.
- **[0813-Group-Roles.md](../0800-Multiplayer/0813-Group-Roles.md)** — Tank/Healer/Damage role definitions mapped from specializations, and rules for how roles affect matchmaking UI vs. manual grouping.
- **[0814-Guild-Progression.md](../0800-Multiplayer/0814-Guild-Progression.md)** — Guild-level XP/perks, guild achievements, hall upgrades, and reputation tracks rewarding consistent activity over top-end-only clears.
- **[0815-Guild-Halls.md](../0800-Multiplayer/0815-Guild-Halls.md)** — Shared guild social/trophy spaces with customizable décor, basic services, and rank-gated access, upgraded via Guild Progression.
- **[0816-World-PvP.md](../0800-Multiplayer/0816-World-PvP.md)** — Open-world Concord vs. Pact conflict concentrated in contested regions, design goals (faction identity, spontaneous objectives, hub safety), and flagging rules.
- **[0817-Competitive-Systems.md](../0800-Multiplayer/0817-Competitive-Systems.md)** — The formal competitive layer (rated matchmaking, seasonal structure, leaderboards, fairness/anti-cheat) spanning both PvP and high-end PvE racing, always opt-in.

## 0900 — Player Systems

Housing, mounts/pets/cosmetics, collections, inventory/bank, loadouts, and the umbrella progression/reward layers.

- **[0900-Housing.md](../0900-Player-Systems/0900-Housing.md)** — Personal instanced housing plots with curated decoration palettes and raid/achievement trophy displays; explicitly no combat power, and a note on the future guild-neighborhood expansion.
- **[0901-Mounts.md](../0900-Player-Systems/0901-Mounts.md)** — Speed-boost travel unlocked at level 15; acquisition sources (starter, faction-reputation, world/raid boss drops, achievements); ground-only at launch with standardized speed to keep mounts purely cosmetic.
- **[0902-Pets.md](../0900-Player-Systems/0902-Pets.md)** — Purely cosmetic non-combat companions (distinct from Ranger/Necromancer combat pets), sourced from quests/exploration/achievements/vendors, themed around regional bestiaries.
- **[0903-Cosmetics.md](../0900-Player-Systems/0903-Cosmetics.md)** — Umbrella system for transmog, dyes, cosmetic pets/mounts/housing/emotes; acquisition philosophy favoring earned-through-play rewards and a hard rule that no cosmetic ever carries a stat.
- **[0904-Emotes.md](../0900-Player-Systems/0904-Emotes.md)** — Basic, racial, and unlockable emote categories for social expression/roleplay, with rules against combat disruption and lore-consistent racial emotes.
- **[0905-Player-Progression.md](../0900-Player-Systems/0905-Player-Progression.md)** — A map tying together all long-term progression layers (level, spec/talents, gear, professions, reputation, achievements, collections, guild standing) and the philosophy that no single layer is mandatory.
- **[0906-Simulated-Civilisation.md](../0900-Player-Systems/0906-Simulated-Civilisation.md)** — Concept doc for making the world feel alive independent of players (NPC routines, jobs, relationships, faction decisions), cross-referencing most world/lore/economy docs, plus a proposed (unused) three-digit renumbering scheme.
- **[0907-Collections.md](../0900-Player-Systems/0907-Collections.md)** — Unified tracking UI/data layer for mounts, pets, appearances, toys, titles, and emotes, favoring account-wide unlocks.
- **[0908-Journals.md](../0900-Player-Systems/0908-Journals.md)** — In-game codex recording discovered lore, bestiary, regions, and NPCs met — pure enrichment, never gating progression.
- **[0909-Achievement-Tracking.md](../0900-Player-Systems/0909-Achievement-Tracking.md)** — The technical/UX system behind achievements: event listening, progress counters, reward granting, and design rules on visible criteria and playstyle variety.
- **[0910-Player-Statistics.md](../0900-Player-Systems/0910-Player-Statistics.md)** — Tracked metrics (combat, PvP, exploration, crafting, social) feeding the character profile and achievements; personal-interest focused, privacy-controlled.
- **[0911-Character-Profile.md](../0900-Player-Systems/0911-Character-Profile.md)** — The inspectable player summary (name, title, gear, guild, stats, bio) and design rules on readability and privacy control.
- **[0912-Loadouts.md](../0900-Player-Systems/0912-Loadouts.md)** — Saved spec/talent/gear configurations for quick switching between roles or content types, restricted in combat/instances.
- **[0913-Inventory-System.md](../0900-Player-Systems/0913-Inventory-System.md)** — Day-to-day carried-item management: auto/manual loot, equip comparisons, stacking, sorting, and protection of quest items.
- **[0914-Bank-System.md](../0900-Player-Systems/0914-Bank-System.md)** — Persistent storage beyond inventory: personal bank, guild bank, and reagent/material tabs, with logged deposits/withdrawals.
- **[0915-Player-Rewards.md](../0900-Player-Systems/0915-Player-Rewards.md)** — Cross-cutting reward design principles (clarity, variety, fairness, pacing, account value) spanning quests, loot, seasons, and achievements.
- **[0916-Player-Milestones.md](../0900-Player-Systems/0916-Player-Milestones.md)** — One-time celebrated moments (first max level, first raid clear, first Legendary) with modest flavorful rewards and clear in-game acknowledgment.
- **[0917-Account-Progression.md](../0900-Player-Systems/0917-Account-Progression.md)** — Cross-character, account-level progression (collections, account achievements, seasonal tracks, shared unlocks) that runs parallel to, never replacing, character progression.

## 1000 — Economy

Currency, marketplaces, trading, banking, and the ongoing work of keeping the player economy healthy.

- **[1000-Economy.md](../1000-Economy/1000-Economy.md)** — Entry point: Aurum + Auction House as the core player-driven economy, design goals (meaningful sinks, profession relevance, price stability), and a link to anti-exploitation/security concerns.
- **[1001-Currency.md](../1000-Economy/1001-Currency.md)** — The two currencies: Aurum (primary, earned broadly) and Sundered Shards (rarer, account-bound endgame currency), with rules against real-money Aurum purchases.
- **[1002-Vendors.md](../1000-Economy/1002-Vendors.md)** — NPC vendor types (general goods, class trainers, profession trainers, reputation quartermasters, Shard vendors) and the rule that vendors are a reliability floor, not an Auction House replacement.
- **[1003-Auction-House.md](../1000-Economy/1003-Auction-House.md)** — The central player marketplace: listings/bidding, search/filters, cross-faction access via the Wayfarer's Guild, and the rule that BoP items aren't tradeable.
- **[1004-Trading.md](../1000-Economy/1004-Trading.md)** — Direct player-to-player trade window with double-confirmation anti-scam protection, use cases, and single-faction restriction.
- **[1005-Mail.md](../1000-Economy/1005-Mail.md)** — Asynchronous item/Aurum transfer system (also delivers Auction House sales), delivery costs, expiration windows, and cross-faction restriction.
- **[1006-Banking.md](../1000-Economy/1006-Banking.md)** — Personal bank, guild bank, and account-wide storage tabs, with scaling expansion costs and the deliberate city-only access friction point.
- **[1007-Market-System.md](../1000-Economy/1007-Market-System.md)** — The broad framework tying Auction House, direct trade, and NPC vendors together, with design goals for a healthy, monitorable economy.
- **[1008-Economic-Balance.md](../1000-Economy/1008-Economic-Balance.md)** — Ongoing practice of keeping currency/item values stable long-term: goals (avoid inflation/deflation), tools (sources/sinks tuning), and review process.
- **[1009-Inflation-Control.md](../1000-Economy/1009-Inflation-Control.md)** — Specific levers preventing Aurum devaluation: sinks, source tuning, itemization binding rules, time gates, and material sinks.
- **[1010-Currency-Sinks.md](../1000-Economy/1010-Currency-Sinks.md)** — Catalog of major Aurum sinks (repairs, training/respec, vendor purchases, crafting, transmog, housing, fast travel, AH fees) and scaling design rules.
- **[1011-Currency-Sources.md](../1000-Economy/1011-Currency-Sources.md)** — Catalog of Aurum sources (quest rewards, drops, vendor sell, AH sales, events, achievements) with front-loaded-for-leveling design philosophy.
- **[1012-Player-Trading-Rules.md](../1000-Economy/1012-Player-Trading-Rules.md)** — Rules on what can be traded and how, safeguarding against RMT/boosting/duplication, with server-side enforcement.
- **[1013-Merchant-System.md](../1000-Economy/1013-Merchant-System.md)** — Full NPC vendor taxonomy (general goods, gear, profession suppliers, repair, reputation, special/rotating) and hub-coverage/immersion design rules.
- **[1014-NPC-Economy.md](../1000-Economy/1014-NPC-Economy.md)** — How NPCs participate economically (vendor inventories, caravans, trade routes, reputation-gated stock) without a full real-market simulation.
- **[1015-Regional-Economies.md](../1000-Economy/1015-Regional-Economies.md)** — How different regions produce different goods/materials reflecting geography and culture, without creating frustrating economic isolation.
- **[1016-Economic-Events.md](../1000-Economy/1016-Economic-Events.md)** — Temporary supply/demand-affecting events (demand surges, seasonal festivals, caravan events) layered on the world-event scheduling system.

## 1100 — Client

The launcher, mods, content pack, audio/visual presentation, controls, and every UI surface.

- **[1100-Launcher.md](../1100-Client/1100-Launcher.md)** — Custom Python/PyQt6 desktop launcher handling one-click install (the Unreal Engine runtime, mods, content pack), auto-updates, account login, and patch-note display.
- **[1101-Client-Modules.md](../1100-Client/1101-Client-Modules.md)** — The curated the Unreal Engine client runtime mod bundle (custom UI framework, performance optimization, immersion mods, accessibility mods) installed and versioned as one unit via the launcher.
- **[1102-Content-Pack.md](../1100-Client/1102-Content-Pack.md)** — Scope of the custom content pack: block/terrain retexturing, custom item/mob models, sound design, and UI art replacing all default engine template assets.
- **[1103-Custom-Models.md](../1100-Client/1103-Custom-Models.md)** — Custom 3D model categories (character, creature, item, environmental), production pipeline, and polycount budget considerations.
- **[1104-Soundtrack.md](../1100-Client/1104-Soundtrack.md)** — Original score structure: continent themes, faction themes, dynamic combat music layers, and recurring story themes, with smooth-crossfade requirements.
- **[1105-Shaders.md](../1100-Client/1105-Shaders.md)** — Custom rendering pipeline for lighting/weather/water/post-processing, tiered performance presets, and a reduced-effects accessibility mode.
- **[1106-Accessibility.md](../1100-Client/1106-Accessibility.md)** — Planned accessibility features (colorblind modes, reduced effects, UI scaling, screen-reader consideration, remappable keybinds) reviewed alongside every major feature addition.
- **[1107-Controls.md](../1100-Client/1107-Controls.md)** — The full default keybind reference and rebinding architecture: movement, the fixed QERT ability bar, ALT class-movement reservation, inventory/UI shortcuts, controller mapping, and future VR compatibility notes.
- **[1108-UI-Systems.md](../1100-Client/1108-UI-Systems.md)** — Comprehensive HUD/interface design: main HUD modules, resource bars, ability bar, cooldown displays, buff/debuff trays, quest tracker, minimap, character/inventory/skill/map/social/guild interfaces, and performance mitigations for large raids.
- **[1109-Settings.md](../1100-Client/1109-Settings.md)** — The full settings persistence system across controls, graphics, rendering effects, audio, UI, gameplay, accessibility, account, privacy, and performance, with account-level storage and cross-instance sync rules.
- **[1110-Loading-Screens.md](../1100-Client/1110-Loading-Screens.md)** — Region/continent-themed loading art, lore tips, and progress indicators, with rules against lecturing tips and unnecessarily long load times.
- **[1111-Animations.md](../1100-Client/1111-Animations.md)** — Client-side animation playback/blending/LOD handling and synchronization with server-authoritative combat state.
- **[1112-Cutscenes.md](../1100-Client/1112-Cutscenes.md)** — Client-side cutscene playback behavior: trigger sources, skippability, subtitles, and the rule that critical info is never cutscene-exclusive.
- **[1113-Client-Optimisation.md](../1100-Client/1113-Client-Optimisation.md)** — Cross-cutting performance work (rendering, entity caps, UI efficiency, tiered graphics presets) to keep min-spec hardware playable.
- **[1114-Main-Menu.md](../1100-Client/1114-Main-Menu.md)** — The first client screen after launcher handoff: logo/key art, primary actions, and fast path to Character Select.
- **[1115-Character-Select.md](../1100-Client/1115-Character-Select.md)** — Character list/carousel with preview, creation/deletion flows, and entry into the game world.
- **[1116-Interface-Layouts.md](../1100-Client/1116-Interface-Layouts.md)** — Principles for arranging/scaling/customizing major UI elements: clarity first, consistent visual language, and default layout goals.
- **[1117-Dialogue-UI.md](../1100-Client/1117-Dialogue-UI.md)** — Structured NPC conversation UI (name/title/portrait, response options, quest controls) replacing a generic default chat interaction.
- **[1118-Inventory-UI.md](../1100-Client/1118-Inventory-UI.md)** — Bag grid, equipment paper-doll, currency display, sorting/filtering, and comparison tooltips.
- **[1119-Map-UI.md](../1100-Client/1119-Map-UI.md)** — World/zone/minimap navigation interface with hand-authored art, POI icons, and fast-travel interaction.
- **[1120-Quest-UI.md](../1100-Client/1120-Quest-UI.md)** — Quest log, on-screen tracker, and accept/decline/complete panels, with Main Quest visually distinguished from optional content.
- **[1121-Combat-UI.md](../1100-Client/1121-Combat-UI.md)** — Action bars, unit frames, nameplates, cast bars, and buff/debuff icons, prioritizing critical info and colorblind-safe design.
- **[1122-Notification-System.md](../1100-Client/1122-Notification-System.md)** — Toasts, combat text, chat/system messages, and social notifications, prioritized so combat info is never drowned out.
- **[1123-Client-Configuration.md](../1100-Client/1123-Client-Configuration.md)** — Overview of all user-configurable option categories and storage/sync rules, with sensible first-time-player defaults.

## 1200 — Technical

Server architecture, database, networking, security, instancing, and backend infrastructure.

- **[1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md)** — The server runs on Unreal Engine (C++) as modular plugins (elysium-core, -combat, -quests, -economy, -social, -pvp) sharing a core library and communicating via an event bus, all persisting through PostgreSQL.
- **[1201-Database.md](../1200-Technical/1201-Database.md)** — PostgreSQL as the single persistent store, accessed only through the core plugin's data access layer; core schema areas (accounts, inventory, progression, social, economy, lockouts) and versioned migrations.
- **[1202-Network.md](../1200-Technical/1202-Network.md)** — Networking architecture: Unreal Engine protocol over the Unreal Engine dedicated server, auxiliary services (launcher backend, website/account services, economy APIs), horizontal scalability, and security coordination.
- **[1203-Server-Structure.md](../1200-Technical/1203-Server-Structure.md)** — Deployment-level server types (Overworld, Instance, Arena/PvP, Login/Proxy) and cross-version update support via the proxy layer.
- **[1204-Authentication.md](../1200-Technical/1204-Authentication.md)** — Account-to-client authentication flow (launcher login → session token → server validation), password hashing, short-lived tokens, and planned 2FA.
- **[1205-API.md](../1200-Technical/1205-API.md)** — Internal APIs (combat logging, economy data, guild data) and a planned future read-only public API, all authenticated, rate-limited, and versioned from day one.
- **[1206-Security.md](../1200-Technical/1206-Security.md)** — Cross-cutting security: account security, server integrity/input validation, economy protection (gold-selling/duping monitoring), and infrastructure DDoS/backup concerns.
- **[1207-Anti-Cheat.md](../1200-Technical/1207-Anti-Cheat.md)** — Server-authoritative anti-cheat approach: movement validation, action rate limiting, duplication prevention, and log-first (not auto-ban-first) enforcement philosophy.
- **[1208-Performance.md](../1200-Technical/1208-Performance.md)** — Server- and client-side performance targets and strategy (instance isolation, DB caching, tiered graphics presets, asset budgets) with load testing planned for Closed Beta.
- **[1209-Instance-System.md](../1200-Technical/1209-Instance-System.md)** — Detailed architecture for splitting the world into independent instances (open world, dungeon, raid, event): why instances are used, instance types, the player-transfer handoff sequence, creation/shutdown lifecycle, scaling via "layers," and a note on story-phasing (different world states per quest progress).
- **[1210-World-Management.md](../1200-Technical/1210-World-Management.md)** — Engineering reference for the handcrafted-world pipeline: Unreal Landscape terrain workflow, flat base world concept, mountains/floating islands/underground handling, dungeon world templates, region/city management, world protection rules (removed default template systems), continent sizes, streaming cell management, and backups.
- **[1211-Server-Synchronisation.md](../1200-Technical/1211-Server-Synchronisation.md)** — The backend layer keeping instances/database/client in agreement: per-system sync rules (player, character, inventory, quest, economy, guild, party, achievement, reputation), instance-transfer sequence, consistency guarantees (strong vs. eventual), and failure/recovery handling.
- **[1212-Logging.md](../1200-Technical/1212-Logging.md)** — Log categories (application, combat, economy, security, admin, performance), structured-logging and sensitive-data rules, and retention policy.
- **[1213-Backup-System.md](../1200-Technical/1213-Backup-System.md)** — Backup scope (database, world templates, config), automation/testing requirements, and off-host storage rules.
- **[1214-Admin-Tools.md](../1200-Technical/1214-Admin-Tools.md)** — Staff moderation/support tooling (player lookup, kick/mute/ban, item/currency adjustment, teleport/instance inspection) with mandatory audit logging and granular permissions.
- **[1215-Developer-Tools.md](../1200-Technical/1215-Developer-Tools.md)** — Internal debug/inspection/profiling tools for engineering and design iteration, gated by permission/environment and never exposed to players.
- **[1216-Monitoring.md](../1200-Technical/1216-Monitoring.md)** — Real-time/historical health visibility across infrastructure, game servers, database, gameplay, and security metrics, with actionable, low-noise alerting.
- **[1217-Server-Architecture.md](../1200-Technical/1217-Server-Architecture.md)** — High-level component list (Proxy/Gateway, Auth Service, Instance Manager, World Processes, Shared Services, Database/Cache) and resilience/scaling design rules.
- **[1218-Plugin-Communication.md](../1200-Technical/1218-Plugin-Communication.md)** — Patterns for how plugins exchange events/data: in-process event bus, service interfaces, cross-process messaging, and avoiding tight circular dependencies.
- **[1219-Data-Storage.md](../1200-Technical/1219-Data-Storage.md)** — Persistence strategy principles: authoritative DB for player/economy state, versioned files for world templates, disposable rebuildable caches, and encryption-at-rest for sensitive data.
- **[1220-Database-Schema.md](../1200-Technical/1220-Database-Schema.md)** — High-level schema domains (Account, Character, Inventory/Items, Progression, Social, Economy, World/Instance) and migration/integrity design rules.
- **[1221-Caching-System.md](../1200-Technical/1221-Caching-System.md)** — In-memory/distributed caching use cases (character lookups, item defs, AH listings, guild snapshots) with the rule that cache is never the source of truth.
- **[1222-Load-Balancing.md](../1200-Technical/1222-Load-Balancing.md)** — Distributing connections and instance workload across hardware, prioritizing player experience over pure utilization evenness, with automatic health-check-based node removal.
- **[1223-Server-Scaling.md](../1200-Technical/1223-Server-Scaling.md)** — Scaling dimensions (open-world layering, on-demand instances, horizontal shared services, DB read replicas, future geographic scaling) and data-driven capacity planning.
- **[1224-Region-Servers.md](../1200-Technical/1224-Region-Servers.md)** — Characteristics of always-on continent/region servers (persistent state, higher soft-caps, layering) as the counterpart to ephemeral dungeon/raid instances.
- **[1225-Matchmaking-Architecture.md](../1200-Technical/1225-Matchmaking-Architecture.md)** — Services forming groups for queued content (dungeons, raids, arenas) and handing them to the Instance Manager, with fairness and graceful-failure design rules.
- **[1226-Command-System.md](../1200-Technical/1226-Command-System.md)** — Unified text-command registration/parsing/permission-checking/execution framework for players, moderators, and developers.
- **[1227-Permission-System.md](../1200-Technical/1227-Permission-System.md)** — Layered permission model (Player, Guild Rank, Staff/Admin, System) answering "is this actor allowed," enforced server-side on every sensitive action.
- **[1228-Account-System.md](../1200-Technical/1228-Account-System.md)** — Top-level player identity management: credential storage, session lifecycle, account-wide unlocks, and launcher-to-server auth linkage.
- **[1229-Player-Data-System.md](../1200-Technical/1229-Player-Data-System.md)** — The authoritative service layer between gameplay plugins and the database for character state, enforcing transactional integrity and disallowing raw SQL from gameplay code.
- **[1230-Server-Maintenance.md](../1200-Technical/1230-Server-Maintenance.md)** — Planned/emergency maintenance procedures: scheduled restarts, rolling updates, migrations, rollback plans, and post-maintenance verification, coordinated with Live Ops.

## 1300 — Art

Visual identity standards spanning UI, color, typography, models, animation, VFX, and environment art.

- **[1300-Art-Style.md](../1300-Art/1300-Art-Style.md)** — The master visual identity reference: grounded high-fantasy direction prioritizing silhouette/readability, distinct regional identities per continent, and the governance rule that no asset ships without a consistency review.
- **[1301-UI-Style.md](../1300-Art/1301-UI-Style.md)** — Diegetic, hand-forged UI look, faction-reactive palette theming, clarity-first requirements for combat-critical elements, and key screens covered.
- **[1302-Colour-Palette.md](../1300-Art/1302-Colour-Palette.md)** — The core color language: faction colors, rarity colors, elemental colors, regional palettes, and mandatory colorblind-safe contrast checks.
- **[1303-Fonts.md](../1300-Art/1303-Fonts.md)** — Typeface roles (display/header, body, decorative flourishes) and rules limiting active typefaces per screen and ensuring small-size legibility.
- **[1304-Icons.md](../1300-Art/1304-Icons.md)** — Icon legibility standards at action-bar size, meaningful visual hints per skill/status effect, and rarity-coded border colors.
- **[1305-Textures.md](../1300-Art/1305-Textures.md)** — Texture resolution standard, regional texture sets matching each continent's material language, and the rule against unmodified default engine starter-content textures in player-facing zones.
- **[1306-Models.md](../1300-Art/1306-Models.md)** — 3D model production standards: tiered polycount budgets, shared base rigs for animation reuse, and the per-model style review process.
- **[1307-Animation-Style.md](../1300-Art/1307-Animation-Style.md)** — The motion language of the game (readable-first, weight/material, class identity, grounded fantasy) applied across characters, creatures, and cinematics.
- **[1308-VFX.md](../1300-Art/1308-VFX.md)** — Spell/combat/environmental visual effects principles: elemental color/shape consistency, unmistakable telegraphs, and controlled density for legibility in raids.
- **[1309-Cinematics.md](../1300-Art/1309-Cinematics.md)** — Art direction for scripted story sequences: camera language, lighting, and performance style aimed at emotional clarity over Hollywood scale.
- **[1310-Environment-Art.md](../1300-Art/1310-Environment-Art.md)** — Terrain/foliage/prop/skybox treatment principles, hero-prop vs. background detail balance, and a short "world creation philosophy" on unique identity and storytelling terrain.
- **[1311-Character-Art.md](../1300-Art/1311-Character-Art.md)** — Visual design of playable races and NPCs: silhouette readability, preserved racial identity under customization, and shared-mesh efficiency.
- **[1312-Weapon-Art.md](../1300-Art/1312-Weapon-Art.md)** — Weapon visual language: type recognizability, careful rarity-driven ornamentation, and cultural/class flavor within type constraints.
- **[1313-Armour-Art.md](../1300-Art/1313-Armour-Art.md)** — Armor visual design across weight classes and rarities, set cohesion, and transmog-friendly construction.
- **[1314-Architecture-Style.md](../1300-Art/1314-Architecture-Style.md)** — Regional architectural languages (Aurelia/Concord, Vethmoor Dwarven, Vethmoor Orcish) and principles for lived-in, legible cities.
- **[1315-Iconography.md](../1300-Art/1315-Iconography.md)** — The broader symbol language across UI/maps/factions/signage, extending icon standards with consistent metaphor language and colorblind-safe faction/elemental symbols.
- **[1316-Particle-Effects.md](../1300-Art/1316-Particle-Effects.md)** — Particle building blocks (sparks, smoke, magic motes, weather) with strict per-scene budgets and telegraph-priority hierarchy.
- **[1317-Lighting-Style.md](../1300-Art/1317-Lighting-Style.md)** — How light/shadow express time of day, weather, and regional mood, with budgeted dynamic lighting for spells/torches/events.
- **[1318-Animation-Guidelines.md](../1300-Art/1318-Animation-Guidelines.md)** — Practical production rules for animators: naming/folder conventions, loop standards, hit-frame tagging, LOD/compression, and review checklist.
- **[1319-Art-Asset-Pipeline.md](../1300-Art/1319-Art-Asset-Pipeline.md)** — The full concept-to-in-game asset pipeline stages (brief, concept, production, technical pass, review, export, verification) and quality-gate rules.

## 1400 — Development

Coding, building, writing, and process standards for every discipline, from local dev setup through release.

- **[1400-Development-Standards.md](../1400-Development/1400-Development-Standards.md)** — Umbrella document tying together all discipline standards (code, building, quest/NPC writing, naming, testing, bug tracking, release), with the rule that nothing is "done" until documented and reviewed.
- **[1401-Coding-Standards.md](../1400-Development/1401-Coding-Standards.md)** — C++/Unreal Build Tool tooling, style enforcement via CI, modularity within the plugin architecture, server-authority requirement, and shared data-access-layer rule.
- **[1402-Building-Standards.md](../1400-Development/1402-Building-Standards.md)** — World-building contributor requirements: scale consistency, texture/palette compliance, performance budgets, and the "purpose check" against the region template.
- **[1403-Quest-Writing-Guide.md](../1400-Development/1403-Quest-Writing-Guide.md)** — Tone (grounded high fantasy) and structure (hook, objective text, completion text) standards for quest writing, plus lore/NPC/main-story consistency checks.
- **[1404-NPC-Writing-Guide.md](../1400-Development/1404-NPC-Writing-Guide.md)** — Requirements for every NPC (name, location, role, one-line voice, idle dialogue), race/culture and faction consistency rules, and reuse-before-creating guidance.
- **[1405-Naming-Conventions.md](../1400-Development/1405-Naming-Conventions.md)** — Naming standards across code (C++ conventions, `elysium-` plugin prefix), in-world content (regions, NPCs, items), and asset files.
- **[1406-Testing.md](../1400-Development/1406-Testing.md)** — Testing layers: automated CI tests for combat/economy/database logic, manual QA passes for content, and scheduled playtesting through Alpha/Beta.
- **[1407-Bug-Tracking.md](../1400-Development/1407-Bug-Tracking.md)** — Bug report requirements, severity levels (Critical/Major/Minor/Trivial), and triage cadence tied to the release process.
- **[1408-Release-Process.md](../1400-Development/1408-Release-Process.md)** — The six-step patch shipping process (feature freeze, QA pass, staging, patch notes, production deploy, post-release monitoring) and release cadence.
- **[1409-Content-Pipeline.md](../1400-Development/1409-Content-Pipeline.md)** — End-to-end content path (design brief → prototype → production → review → QA → staging → release) with the rule that content isn't done without documentation.
- **[1410-Developer-Environment.md](../1400-Development/1410-Developer-Environment.md)** — Standard local engineering setup (Unreal Build Tool / Unreal Engine dev server/DB/IDE config) to minimize environment drift.
- **[1411-Git-Workflow.md](../1400-Development/1411-Git-Workflow.md)** — Branching, commit, and merge practices: small focused commits, feature branches, mandatory CI and reviews, no force-push to protected branches.
- **[1412-Code-Review.md](../1400-Development/1412-Code-Review.md)** — Mandatory review focus areas (correctness, server authority/anti-cheat, performance, readability, test coverage) and approval requirements.
- **[1413-Documentation-Standards.md](../1400-Development/1413-Documentation-Standards.md)** — Rules for writing/linking/maintaining the GDD itself: four-digit structure, status lines, updating docs alongside behavior changes, marking speculative content.
- **[1414-Asset-Management.md](../1400-Development/1414-Asset-Management.md)** — Naming, storage, versioning, and ownership rules for art/audio/data assets from source to runtime.
- **[1415-Version-Control.md](../1400-Development/1415-Version-Control.md)** — Git as source of truth for code/config/docs, secrets-never-committed rule, and tag/release alignment with version history.
- **[1416-Branch-Strategy.md](../1400-Development/1416-Branch-Strategy.md)** — Long-lived vs. short-lived branch model (main/trunk, feature branches, release/hotfix branches) prioritizing predictability.
- **[1417-Development-Tools.md](../1400-Development/1417-Development-Tools.md)** — Preferred IDEs, linters, profilers, and internal utilities documented for onboarding, with formatters/static analysis in CI.
- **[1418-Local-Testing.md](../1400-Development/1418-Local-Testing.md)** — Pre-push engineer checks: unit tests, dev-server smoke start, and a documented minimal "boot and login" path.
- **[1419-Staging-Environment.md](../1400-Development/1419-Staging-Environment.md)** — Production-mirroring staging environment for patch validation, with QA sign-off as part of the release checklist.
- **[1420-Production-Deployment.md](../1400-Development/1420-Production-Deployment.md)** — Controlled live deployment process: release checklist, backup/rollback plans, launcher/server version compatibility, mandatory post-deploy monitoring.
- **[1421-Build-Automation.md](../1400-Development/1421-Build-Automation.md)** — CI/CD compiling, testing, and packaging on every change, with required-passing CI and versioned traceable artifacts.
- **[1422-Quality-Assurance.md](../1400-Development/1422-Quality-Assurance.md)** — QA discipline overview: test plans, regression suites, exploratory play, release certification, and early involvement on large features.
- **[1423-Performance-Testing.md](../1400-Development/1423-Performance-Testing.md)** — Load-testing server tick health, instance capacity, database load, and client frame times against the Performance doc's budgets.
- **[1424-Security-Testing.md](../1400-Development/1424-Security-Testing.md)** — Probing authentication, economy integrity, and exploit classes, with severity-based triage and possible external review before major launches.
- **[1425-Developer-Guidelines.md](../1400-Development/1425-Developer-Guidelines.md)** — Practical "how we work" expectations: document as you build, small reviewable changes, escalate risk early, respect the vision/pillars.

## 1500 — Expansions

Planned post-launch content additions and the process for scoping them.

- **[1500-Expansion-01.md](../1500-Expansions/1500-Expansion-01.md)** — First planned expansion: Sylvaneth, the elven world-tree continent (levels 50–65), introducing Wood Elves, new dungeons/raid, Sylvaneth profession materials, and a story thread about Aeloria's silence. Not yet scheduled.
- **[1501-Expansion-Planning.md](../1500-Expansions/1501-Expansion-Planning.md)** — The process for turning a Future Plans idea into a scoped, scheduled expansion: graduate idea → define fantasy/focus/level band → draft outlines → estimate cost → place on roadmap.
- **[1502-Expansion-Story-Structure.md](../1500-Expansions/1502-Expansion-Story-Structure.md)** — Principles for organizing an expansion's campaign: continuity with prior threads, clear act structure, optional non-gating side stories.
- **[1503-Expansion-World-Design.md](../1500-Expansions/1503-Expansion-World-Design.md)** — Rules for scoping new continents/zones in expansions: handcrafted purposeful spaces, pacing-matched level bands/travel times, distinct identity, early instance planning.
- **[1504-Expansion-Feature-Planning.md](../1500-Expansions/1504-Expansion-Feature-Planning.md)** — Framework for listing and prioritizing new systems/classes/professions per expansion, with must-have vs. nice-to-have and pillar justification.
- **[1505-Expansion-Release-Strategy.md](../1500-Expansions/1505-Expansion-Release-Strategy.md)** — PTR/beta plans, staggered unlocks, communication, and support-staffing rules for major content drops.
- **[1600-Expansion-02.md](../1500-Expansions/1600-Expansion-02.md)** — Second planned expansion: Kharzul Wastes, the beastkin desert continent (levels 65–80), with a heat/exposure mechanic, buried Age of Concord ruins, and a narrative hook foreshadowing Nightreach. Not yet scheduled.
- **[1601-Expansion-Planning.md](../1500-Expansions/1601-Expansion-Planning.md)** — A short generic GDD-scope statement for "the expansion" (zones, mechanics, narrative arcs, technical requirements) — appears to be an early/duplicate planning stub.
- **[1700-Expansion-03.md](../1500-Expansions/1700-Expansion-03.md)** — Third planned expansion: Nightreach, the Sundering-warped endgame continent (levels 80–95), revealing the Revenant race origin, a corruption/exposure mechanic, and the culminating raid confrontation with Kaelgorath. Not yet scheduled.
- **[1800-Expansion-04.md](../1500-Expansions/1800-Expansion-04.md)** — Placeholder for the fourth expansion; unscoped, with candidate directions listed (player ships, guild housing neighborhoods, a third faction) to be defined after Expansion 03.
- **[1900-Expansion-05.md](../1500-Expansions/1900-Expansion-05.md)** — Placeholder for the fifth expansion, reserved to signal multi-year live-service intent; entirely unscoped.

## 2000 — Operations

Live-service operations docs. All are currently placeholder-stage ("ownership and intent" stubs to be expanded near Closed Beta), sharing the same core principles: player trust/clarity first, documented repeatable processes, explicit Ops/Support/Dev handoffs, and metrics informing (not replacing) design judgment.

- **[2000-Live-Service.md](../2000-Operations/2000-Live-Service.md)** — The overarching model for running Elysium as a persistent online game (update cadence, support, community, long-term health).
- **[2001-Updates.md](../2000-Operations/2001-Updates.md)** — How content/system updates are planned, communicated, and shipped on a regular cadence.
- **[2002-Patch-Notes.md](../2000-Operations/2002-Patch-Notes.md)** — Standards for writing clear patch notes aligned with Version History.
- **[2003-Moderation.md](../2000-Operations/2003-Moderation.md)** — Policies and tools for enforcing community standards and handling disruptive behavior.
- **[2004-Community-Management.md](../2000-Operations/2004-Community-Management.md)** — Channels, tone, and practices for official community presence.
- **[2005-Support-System.md](../2000-Operations/2005-Support-System.md)** — Player support tickets, knowledge base, and escalation paths.
- **[2006-Analytics.md](../2000-Operations/2006-Analytics.md)** — Metrics collection/analysis for gameplay, economy, and retention insight.
- **[2007-Player-Reports.md](../2000-Operations/2007-Player-Reports.md)** — How player reports are submitted, triaged, and actioned.
- **[2008-Staff-Tools.md](../2000-Operations/2008-Staff-Tools.md)** — Operational interfaces for support/moderation/live ops, extending the technical Admin Tools doc.
- **[2009-Community-Events.md](../2000-Operations/2009-Community-Events.md)** — Official contests, streams, and community-driven activities.
- **[2010-Seasonal-Events.md](../2000-Operations/2010-Seasonal-Events.md)** — Calendar-aligned in-game events and their ops requirements.
- **[2011-Server-Restarts.md](../2000-Operations/2011-Server-Restarts.md)** — Scheduled and emergency restart procedures and player communication.
- **[2012-Maintenance.md](../2000-Operations/2012-Maintenance.md)** — Ops-facing maintenance windows coordinated with the technical maintenance doc.
- **[2013-Player-Feedback.md](../2000-Operations/2013-Player-Feedback.md)** — How feedback is gathered, reviewed, and fed into design.
- **[2014-Bug-Reports.md](../2000-Operations/2014-Bug-Reports.md)** — Player-facing bug report handling and handoff to development triage.
- **[2015-Game-Metrics.md](../2000-Operations/2015-Game-Metrics.md)** — Key gameplay KPIs monitored for system/content health.
- **[2016-Player-Retention.md](../2000-Operations/2016-Player-Retention.md)** — Strategies and metrics for keeping players returning over time.
- **[2017-Community-Guidelines.md](../2000-Operations/2017-Community-Guidelines.md)** — Public rules for player behavior in-game and in official spaces.
- **[2018-Operations-Checklist.md](../2000-Operations/2018-Operations-Checklist.md)** — Recurring checklists for launches, resets, seasons, and incidents.

## 9000 — Future

Speculative/unscoped holding ground for ideas, mysteries, and long-term story direction — nothing here is committed. Most files 9005–9015 share an identical template (Purpose + four rules: not commitments, promotion needs scoping, rejects go to Rejected Ideas, reviewed each expansion planning cycle) and are currently empty ("None recorded yet").

- **[9000-Ancient-Mysteries.md](../9000-Future/9000-Ancient-Mysteries.md)** — Unresolved in-world mysteries (lost civilizations, sealed locations, unknown entities, unexplained historical events) meant to seed years of player curiosity; includes a documented "mystery structure" template and example cryptic Archivarium prophecies.
- **[9001-Future-Characters.md](../9000-Future/9001-Future-Characters.md)** — Appears to duplicate 9000's mystery-structure content verbatim rather than covering future characters specifically; likely mistitled/unfinished.
- **[9002-Future-Regions.md](../9000-Future/9002-Future-Regions.md)** — Planned but unavailable continents/regions/dimensions (hidden continents, new realms, changed regions), with a documented region-entry template and the rule that new regions expand rather than replace the world.
- **[9003-Future-Threats.md](../9000-Future/9003-Future-Threats.md)** — Future enemies/disasters/conflicts categorized as world-level, regional, or hidden threats, with a threat-entry template and the rule that threats feel like consequences of prior events.
- **[9004-Long-Term-Story.md](../9000-Future/9004-Long-Term-Story.md)** — The multi-year narrative arc framed as five "Ages" (First through Final), each with a story focus, plus long-term principles (consequences persist, no content made irrelevant).
- **[9005-Unused-Concepts.md](../9000-Future/9005-Unused-Concepts.md)** — Holding doc for deliberately set-aside ideas, to avoid re-litigating them without context. Currently empty.
- **[9006-Future-Gameplay-Systems.md](../9000-Future/9006-Future-Gameplay-Systems.md)** — Holding doc for uncommitted post-launch gameplay systems. Currently empty.
- **[9007-Future-Technologies.md](../9000-Future/9007-Future-Technologies.md)** — Holding doc for possible future engine/tooling/platform adoptions. Currently empty.
- **[9008-Future-Classes.md](../9000-Future/9008-Future-Classes.md)** — Holding doc for class concepts beyond the launch eight. Currently empty.
- **[9009-Future-Races.md](../9000-Future/9009-Future-Races.md)** — Holding doc for additional playable/cultural races tied to future continents. Currently empty.
- **[9010-Future-Expansions.md](../9000-Future/9010-Future-Expansions.md)** — Holding doc for unscoped expansion ideas beyond the numbered Expansion docs. Currently empty.
- **[9011-Experimental-Mechanics.md](../9000-Future/9011-Experimental-Mechanics.md)** — Holding doc for prototype-stage mechanics needing playtesting before commitment. Currently empty.
- **[9012-Rejected-Ideas.md](../9000-Future/9012-Rejected-Ideas.md)** — Holding doc for explicitly rejected proposals with reasons, to prevent repeat debate. Currently empty.
- **[9013-Prototype-Systems.md](../9000-Future/9013-Prototype-Systems.md)** — Holding doc tracking active/archived prototypes and lessons learned. Currently empty.
- **[9014-Community-Suggestions.md](../9000-Future/9014-Community-Suggestions.md)** — Holding doc for promising player suggestions parked for planning review. Currently empty.
- **[9015-Unconfirmed-Features.md](../9000-Future/9015-Unconfirmed-Features.md)** — Holding doc for publicly/internally mentioned features not yet design-confirmed. Currently empty.
- **[9999-Ideas.md](../9000-Future/9999-Ideas.md)** — The raw brainstorm sandbox (gameplay, lore/world, technical ideas — e.g. photo mode, a hidden sixth continent, Mythic+-style dungeon keys) that promising ideas graduate out of into [0005-Future-Plans.md](../0000-Project/0005-Future-Plans.md).
