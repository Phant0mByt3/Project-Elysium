# 19 — World Events

World events are time-limited, server-wide activities layered on top of the persistent world — seasonal celebrations, story-driven invasions, and recurring dynamic content.

## Categories

### Dynamic Events
Recurring, unscheduled happenings within a region (a bandit raid on a village, a resource caravan needing an escort). These respawn on cooldowns and are meant to be stumbled into while exploring, not queued for.

### Invasions
Larger, story-tied events where an enemy faction pushes into contested territory (see [86-Territory-Control.md](86-Territory-Control.md)), requiring organized player defense. Tied narratively to the main story ([37-Main-Story.md](37-Main-Story.md)).

### Seasonal Events
Real-world-calendar-aligned content — see [87-Seasons.md](87-Seasons.md) for the full seasonal calendar and reward tracks.

## Launch World Events

**The Fens Uprising** — a recurring Greywater Fens event where an undead warband attempts to overrun Fenwick Crossing; failing to repel it three times in a row temporarily disables that village's vendors until players clear a follow-up mini-dungeon.

**The Ashenclaw Incursion** — a large-scale Duskward Pact push into Frostgate Approach, requiring cross-guild Concord defense; ties into the Vethmoor faction storyline.

## Technical Notes
World events depend on the same scheduling and state-tracking systems as world bosses ([18-World-Bosses.md](18-World-Bosses.md)); see [120-Plugin-Architecture.md](120-Plugin-Architecture.md).
