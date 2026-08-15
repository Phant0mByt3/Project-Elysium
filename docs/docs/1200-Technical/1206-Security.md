# 1206 — Security

## Overview
Security spans account protection, server integrity, and economy protection — treated as a cross-cutting concern touching authentication ([1204-Authentication.md](1204-Authentication.md)), anti-cheat ([1207-Anti-Cheat.md](1207-Anti-Cheat.md)), and the database layer ([1201-Database.md](1201-Database.md)).

## Focus Areas
* **Account Security** — salted password hashing, planned 2FA support, session token expiry (see [1204-Authentication.md](1204-Authentication.md)).
* **Server Integrity** — input validation on all client-to-server plugin messages, rate limiting on chat/trade/auction actions to prevent spam and automation abuse.
* **Economy Protection** — monitoring for gold-selling, duplication exploits, and market manipulation, feeding into the broader economy health process in [1000-Economy.md](../1000-Economy/1000-Economy.md).
* **Infrastructure** — DDoS mitigation at the network layer ([1202-Network.md](1202-Network.md)), regular database backups.

## Process
Security should be reviewed as part of every major system's design, not treated as a separate late-stage audit — consistent with the documentation-first, quality-first pillars in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md). A dedicated security/exploit review pass is planned ahead of Closed Beta ([0003-Roadmap.md](../0000-Project/0003-Roadmap.md)).


## Incident Response Process

A documented incident response process (detection, containment, communication, post-mortem) is established ahead of Closed Beta, ensuring the team can respond quickly and transparently to any security incident once the game is live — coordinated with the community communication standards in [2004-Community-Management.md](../2000-Operations/2004-Community-Management.md).

## Regular Security Review

Beyond the pre-Closed-Beta audit, security is revisited at each major content update, particularly when new economy-affecting or account-affecting systems are introduced, keeping security posture current rather than a one-time checkbox.
