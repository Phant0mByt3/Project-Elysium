# 0109 — World Events

World events are time-limited, server-wide activities layered on top of the persistent world — seasonal celebrations, story-driven invasions, and recurring dynamic content.

## Categories

### Dynamic Events
Recurring, unscheduled happenings within a region (a bandit raid on a village, a resource caravan needing an escort). These respawn on cooldowns and are meant to be stumbled into while exploring, not queued for.

### Invasions
Larger, story-tied events where an enemy faction pushes into contested territory (see [0806-Territory-Control.md](../0800-Multiplayer/0806-Territory-Control.md)), requiring organized player defense. Tied narratively to the main story ([0207-Main-Story.md](../0200-Lore/0207-Main-Story.md)).

### Seasonal Events
Real-world-calendar-aligned content — see [0807-Seasons.md](../0800-Multiplayer/0807-Seasons.md) for the full seasonal calendar and reward tracks.

## Launch World Events

**The Fens Uprising** — a recurring Greywater Fens event where an undead warband attempts to overrun Fenwick Crossing; failing to repel it three times in a row temporarily disables that village's vendors until players clear a follow-up mini-dungeon.

**The Ashenclaw Incursion** — a large-scale Duskward Pact push into Frostgate Approach, requiring cross-guild Concord defense; ties into the Vethmoor faction storyline.

## Major World Events
Large-scale events that permanently or temporarily affect the world.
Events can change zones, cities, factions, and gameplay.
The Collision Event (example)
A reality collision event affecting Aurelia.
Creates a connection between two worlds.
Introduces a new dimension and new civilizations.

### Event Phases

World events exist in multiple states:

**Phase 1: Before Event**

Original world state.
Normal NPCs, cities, and quests.

**Phase 2: Event Occurrence**

Special instance.
Only active during the storyline.
Used for cinematic moments and major transitions.

**Phase 3: After Event**

Permanent changed world state.
New content unlocked.

## Technical Notes
World events depend on the same scheduling and state-tracking systems as world bosses ([0108-World-Bosses.md](0108-World-Bosses.md)); see [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md).
