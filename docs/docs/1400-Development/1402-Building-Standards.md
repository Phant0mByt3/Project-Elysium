# 142 — Building Standards

## Overview
Standards for world-building contributors constructing regions, cities, dungeons, and landmarks in-editor, ensuring consistency across a team of builders.

## Requirements
* **Scale Consistency** — buildings and terrain should match the scale established in a region's reference sketch ([0112-Maps.md](../0100-World/0112-Maps.md)) and neighboring builds, avoiding jarring scale mismatches at region borders.
* **Texture & Palette Compliance** — builds must use the approved regional texture sets ([1305-Textures.md](../1300-Art/1305-Textures.md)) and color palette ([1302-Colour-Palette.md](../1300-Art/1302-Colour-Palette.md)) — no unapproved vanilla block usage in player-facing areas.
* **Performance Budget** — entity and particle-emitter density per build should stay within the performance targets in [1208-Performance.md](../1200-Technical/1208-Performance.md), especially in high-traffic hub areas.
* **Purpose Check** — every build should map back to the region template in [0102-Regions.md](../0100-World/0102-Regions.md) (quest hub, landmark, dungeon entrance, etc.) — no unscoped decorative sprawl without design sign-off.

## Review Process
Completed builds go through a design review (gameplay function) and an art review (style compliance, per [1300-Art-Style.md](../1300-Art/1300-Art-Style.md)) before being marked content-complete in the roadmap ([0003-Roadmap.md](../0000-Project/0003-Roadmap.md)).
