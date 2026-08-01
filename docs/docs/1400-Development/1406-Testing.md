# 146 — Testing

## Overview
Testing practices spanning automated code testing, manual QA passes, and playtesting, ensuring quality per Pillar 5 in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md).

## Automated Testing
Unit and integration tests for server-side plugin logic ([1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md)), particularly around combat math ([0401-Combat.md](../0400-Gameplay/0401-Combat.md), [0304-Stats.md](../0300-Characters/0304-Stats.md)), economy transactions ([1000-Economy.md](../1000-Economy/1000-Economy.md)), and database operations ([1201-Database.md](../1200-Technical/1201-Database.md)), run automatically in CI before merge.

## Manual QA
Structured test passes for new content (quests, dungeons, raids) checking for: broken quest chains, unreachable objectives, loot table errors, and building/collision issues — using the checklist standards from [1402-Building-Standards.md](1402-Building-Standards.md) and [1403-Quest-Writing-Guide.md](1403-Quest-Writing-Guide.md).

## Playtesting
Internal playtests scheduled at the end of each major system's implementation, escalating to invited external testers during Closed Alpha and a wider pool during Closed Beta ([0003-Roadmap.md](../0000-Project/0003-Roadmap.md)).

## Bug Tracking
Issues found during any testing phase are logged per the process in [1407-Bug-Tracking.md](1407-Bug-Tracking.md).
