# 1301 — UI Style

## Overview
Visual standards for Elysium's fully custom UI, built natively in Unreal Motion Graphics (UMG) ([1101-Client-Modules.md](../1100-Client/1101-Client-Modules.md)).

## Principles
* **Diegetic Feel** — UI frames and icons should look hand-illuminated/forged rather than flat modern UI, matching the overall art style ([1300-Art-Style.md](1300-Art-Style.md)).
* **Faction-Reactive Theming** — subtle palette shifts (gold accents for Dawnbound, deep red/purple for Duskward) on faction-specific UI elements, per [0203-Factions.md](../0200-Lore/0203-Factions.md).
* **Clarity First** — health/resource bars, cooldowns, and status effect icons ([0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md)) must remain legible even in the busiest raid encounters.

## Key Screens
* **HUD** — action bars, health/resource, buffs/debuffs, minimap.
* **Character Sheet** — stats ([0304-Stats.md](../0300-Characters/0304-Stats.md)), equipped gear.
* **Talent Tree** — [0303-Talent-Trees.md](../0300-Characters/0303-Talent-Trees.md) visualization.
* **Auction House / Bank / Guild** panels — [1003-Auction-House.md](../1000-Economy/1003-Auction-House.md), [1006-Banking.md](../1000-Economy/1006-Banking.md), [0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md).

## Accessibility
UI scaling and colorblind-safe status icon design are required, not optional — see [1106-Accessibility.md](../1100-Client/1106-Accessibility.md).


## Frame and Panel Construction

UI frames use a modular 9-slice construction technique, allowing panels to resize cleanly for different content lengths (a short tooltip vs. a long quest description) without stretching or distorting the hand-illuminated border art.

## Motion and Transitions

Panel open/close and notification animations use short, purposeful easing curves rather than instant snaps or overly long flourishes, keeping the UI feeling polished without slowing down gameplay-critical interactions like opening a loot window mid-combat.

## Cross-Screen Consistency

The same frame, button, and icon language is reused across every UI screen (inventory, character sheet, guild panel, auction house) so players build one mental model of "how Elysium's UI works" rather than relearning conventions screen to screen.
