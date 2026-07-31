# 142 — Building Standards

## Overview
Standards for world-building contributors constructing regions, cities, dungeons, and landmarks in-editor, ensuring consistency across a team of builders.

## Requirements
* **Scale Consistency** — buildings and terrain should match the scale established in a region's reference sketch ([22-Maps.md](22-Maps.md)) and neighboring builds, avoiding jarring scale mismatches at region borders.
* **Texture & Palette Compliance** — builds must use the approved regional texture sets ([135-Textures.md](135-Textures.md)) and color palette ([132-Colour-Palette.md](132-Colour-Palette.md)) — no unapproved vanilla block usage in player-facing areas.
* **Performance Budget** — entity and particle-emitter density per build should stay within the performance targets in [128-Performance.md](128-Performance.md), especially in high-traffic hub areas.
* **Purpose Check** — every build should map back to the region template in [12-Regions.md](12-Regions.md) (quest hub, landmark, dungeon entrance, etc.) — no unscoped decorative sprawl without design sign-off.

## Review Process
Completed builds go through a design review (gameplay function) and an art review (style compliance, per [130-Art-Style.md](130-Art-Style.md)) before being marked content-complete in the roadmap ([03-Roadmap.md](03-Roadmap.md)).
