# 0203 — Factions

Elysium is divided between two major player-aligned factions, numerous regional powers, neutral organizations, and hostile factions.

The two major factions form the primary political divide of Elysium and function similarly to the major faction systems found in large-scale MMORPGs. Regional factions give individual territories their own identities, governments, cultures, and conflicts.

A player's race does not determine their faction. All players begin the game factionless in their race's starting area. At Level 10, players choose which major faction they will follow.

---

## Major Factions

### The Dawnbound Concord

Founded in the late Age of Ash by survivors who believe Elysium should be rebuilt in the image of the old Age of Concord.

The Concord believes the old world was not inherently flawed. Its collapse was caused by the forces that destroyed it, and civilization can be restored if its surviving peoples cooperate.

The faction values order, cooperation, established institutions, trade, and the restoration of the old capitals.

Aligned with Solthar.

Capital: Solmere ([0103-Cities.md](../0100-World/0103-Cities.md)).

**Core belief:**
"Restore what was lost."

---

### The Duskward Pact

A rival coalition formed by those who believe the old order failed and should not be rebuilt.

The Pact believes the survivors of Elysium should stop looking toward the past and instead build a new world based on strength, independence, and alliances between peoples who were previously divided.

The faction values self-reliance, military strength, freedom from the old kingdoms, and the creation of new societies.

Aligned loosely with Nyxara and Ignareth.

Capital: Ashka Vor.

**Core belief:**
"Build what comes next."

---

## Player Faction Choice

All players begin the game factionless.

Players start in the traditional starting area of their chosen race and can experience their race's culture, history, and local conflicts before choosing a major faction.

At Level 10, players choose between the Dawnbound Concord and the Duskward Pact.

Race does not restrict this choice. Any playable race can join either major faction.

The faction choice determines:

* Initial faction reputation
* Major faction questlines
* Friendly and hostile NPC relationships
* PvP allegiance
* Faction-specific quests
* Faction-specific rewards
* Access to certain faction-controlled cities and territories
* Certain faction-specific gameplay opportunities

The choice is permanent unless changed through a future story or faction-change system.

See [0804-PvP.md](../0800-Multiplayer/0804-PvP.md) for PvP allegiance.

See [0707-Factions-Reputation.md](../0700-Quests/0707-Factions-Reputation.md) for reputation systems.

---

# Regional Factions

Regional factions are independent political powers that control specific territories, cities, kingdoms, settlements, or other parts of Elysium.

Unlike the Dawnbound Concord and Duskward Pact, these factions are not necessarily global player factions.

A regional faction may be:

* Aligned with the Dawnbound Concord
* Aligned with the Duskward Pact
* Neutral toward both
* Hostile toward both
* Internally divided

Regional factions give each part of Elysium its own political identity rather than making entire continents feel like extensions of the two major factions.

### Silverwatch

A major regional power associated with the Dawnbound Concord.

Silverwatch controls territory and maintains its own military, settlements, leadership, culture, and political interests.

Although aligned with the Concord, Silverwatch is not simply a subdivision of the Concord. Its leaders and citizens may have interests that conflict with the wider Concord.

Additional Silverwatch lore, territory, leadership, cities, and questlines are documented in their respective regional and quest files.

---

### Regional Faction Template

Additional land-owning factions should follow this structure:

```text
### [Faction Name]

[Origin and history.]

[Political beliefs and goals.]

[Relationship with the Dawnbound Concord.]

[Relationship with the Duskward Pact.]

[Territory controlled.]

[Major cities or settlements.]

[Major races or cultures.]

[Leadership.]

[Current conflicts.]

[Relevant questlines.]
```

Regional factions may be added as Elysium's continents and territories are developed.

---

# Neutral Organizations

Neutral organizations operate independently of the Dawnbound Concord and Duskward Pact.

They may operate within territory controlled by either major faction and generally attempt to maintain relationships with both sides.

### The Wayfarer's Guild

A cross-faction merchant and courier organization operating out of neutral trading posts.

The Guild provides transportation, trade, courier services, and other services connecting settlements across Elysium.

It is also responsible for the Auction House's cross-faction listings.

See [1003-Auction-House.md](../1000-Economy/1003-Auction-House.md).

---

### The Cartographer's League

Scholars, explorers, and mapmakers dedicated to remapping the continents as Elysium reconnects.

The League operates expeditions into unexplored territory and documents landmarks, ruins, settlements, and other discoveries.

The organization is the source of exploration-focused achievements and much of Elysium's landmark lore.

See [0704-Achievements.md](../0700-Quests/0704-Achievements.md).

See [0105-Landmarks.md](../0100-World/0105-Landmarks.md).

---

### The Ashen Circle

A secretive scholarly order studying the remaining influence of Kaelgorath.

The Circle investigates corruption, ancient magic, and the effects of Kaelgorath's influence on Elysium.

Its activities become increasingly important during questlines connected to corruption and the Nightreach expansion.

See [1700-Expansion-03.md](../1500-Expansions/1700-Expansion-03.md).

---

# Hostile Factions

Hostile factions are groups that oppose players, settlements, or both major factions.

Unlike regional political factions, these groups are generally encountered as enemies through quests, world events, dungeons, and open-world encounters.

Hostile factions are documented alongside the regions in which they operate in [0102-Regions.md](../0100-World/0102-Regions.md).

Examples include:

* Bandit crews
* Undead cults
* Orc warbands
* Corrupted factions
* Monster tribes
* Pirate groups
* Religious cults
* Other region-specific hostile organizations

Some hostile factions may eventually become major world threats or develop into regional powers through future storylines.

---

# Faction Structure

Elysium's faction system is structured around four broad categories:

```text
Elysium
│
├── Major Factions
│   ├── The Dawnbound Concord
│   └── The Duskward Pact
│
├── Regional Factions
│   ├── Silverwatch
│   ├── [Future Faction]
│   ├── [Future Faction]
│   └── [Future Faction]
│
├── Neutral Organizations
│   ├── The Wayfarer's Guild
│   ├── The Cartographer's League
│   └── The Ashen Circle
│
└── Hostile Factions
    ├── Bandit Crews
    ├── Undead Cults
    ├── Warbands
    └── Region-Specific Enemies
```

The Dawnbound Concord and Duskward Pact define the primary political conflict of Elysium.

Regional factions define the identity and politics of individual territories.

Neutral organizations connect the world across faction boundaries.

Hostile factions provide local threats, conflicts, and world content.
