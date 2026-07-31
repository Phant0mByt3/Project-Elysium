# 148 — Release Process

## Overview
The process for shipping a new patch or content update to Elysium, from code-complete to live, applicable from Closed Alpha ([003-Roadmap.md](003-Roadmap.md)) onward.

## Steps
1. **Feature Freeze** — no new features merged; only bug fixes for the upcoming release.
2. **QA Pass** — full manual QA sweep per [146-Testing.md](146-Testing.md), with any Critical/Major bugs ([147-Bug-Tracking.md](147-Bug-Tracking.md)) blocking release.
3. **Staging Deployment** — deployed to an internal staging server matching production configuration for a final validation pass.
4. **Patch Notes** — written and added to [004-Version-History.md](004-Version-History.md), summarizing additions, changes, fixes, and removals.
5. **Production Deployment** — rolled out, with the launcher ([110-Launcher.md](110-Launcher.md)) notified to distribute the corresponding client update.
6. **Post-Release Monitoring** — active monitoring for the first 24–48 hours for regressions, economy anomalies ([100-Economy.md](100-Economy.md)), or server stability issues ([128-Performance.md](128-Performance.md)).

## Cadence
Regular minor patches (balance, bug fixes) on a predictable cycle; major content patches (new dungeons, raids, story chapters) on a longer cycle aligned with the roadmap ([003-Roadmap.md](003-Roadmap.md)) and seasonal calendar ([087-Seasons.md](087-Seasons.md)).
