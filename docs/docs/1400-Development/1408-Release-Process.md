# 148 — Release Process

## Overview
The process for shipping a new patch or content update to Elysium, from code-complete to live, applicable from Closed Alpha ([0003-Roadmap.md](../0000-Project/0003-Roadmap.md)) onward.

## Steps
1. **Feature Freeze** — no new features merged; only bug fixes for the upcoming release.
2. **QA Pass** — full manual QA sweep per [1406-Testing.md](1406-Testing.md), with any Critical/Major bugs ([1407-Bug-Tracking.md](1407-Bug-Tracking.md)) blocking release.
3. **Staging Deployment** — deployed to an internal staging server matching production configuration for a final validation pass.
4. **Patch Notes** — written and added to [0004-Version-History.md](../0000-Project/0004-Version-History.md), summarizing additions, changes, fixes, and removals.
5. **Production Deployment** — rolled out, with the launcher ([1100-Launcher.md](../1100-Client/1100-Launcher.md)) notified to distribute the corresponding client update.
6. **Post-Release Monitoring** — active monitoring for the first 24–48 hours for regressions, economy anomalies ([1000-Economy.md](../1000-Economy/1000-Economy.md)), or server stability issues ([1208-Performance.md](../1200-Technical/1208-Performance.md)).

## Cadence
Regular minor patches (balance, bug fixes) on a predictable cycle; major content patches (new dungeons, raids, story chapters) on a longer cycle aligned with the roadmap ([0003-Roadmap.md](../0000-Project/0003-Roadmap.md)) and seasonal calendar ([0807-Seasons.md](../0800-Multiplayer/0807-Seasons.md)).
