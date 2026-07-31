# 146 — Testing

## Overview
Testing practices spanning automated code testing, manual QA passes, and playtesting, ensuring quality per Pillar 5 in [02-Core-Pillars.md](02-Core-Pillars.md).

## Automated Testing
Unit and integration tests for server-side plugin logic ([120-Plugin-Architecture.md](120-Plugin-Architecture.md)), particularly around combat math ([44-Combat.md](44-Combat.md), [45-Stats.md](45-Stats.md)), economy transactions ([100-Economy.md](100-Economy.md)), and database operations ([121-Database.md](121-Database.md)), run automatically in CI before merge.

## Manual QA
Structured test passes for new content (quests, dungeons, raids) checking for: broken quest chains, unreachable objectives, loot table errors, and building/collision issues — using the checklist standards from [142-Building-Standards.md](142-Building-Standards.md) and [143-Quest-Writing-Guide.md](143-Quest-Writing-Guide.md).

## Playtesting
Internal playtests scheduled at the end of each major system's implementation, escalating to invited external testers during Closed Alpha and a wider pool during Closed Beta ([03-Roadmap.md](03-Roadmap.md)).

## Bug Tracking
Issues found during any testing phase are logged per the process in [147-Bug-Tracking.md](147-Bug-Tracking.md).
