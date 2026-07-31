# 126 — Security

## Overview
Security spans account protection, server integrity, and economy protection — treated as a cross-cutting concern touching authentication ([124-Authentication.md](124-Authentication.md)), anti-cheat ([127-Anti-Cheat.md](127-Anti-Cheat.md)), and the database layer ([121-Database.md](121-Database.md)).

## Focus Areas
* **Account Security** — salted password hashing, planned 2FA support, session token expiry (see [124-Authentication.md](124-Authentication.md)).
* **Server Integrity** — input validation on all client-to-server plugin messages, rate limiting on chat/trade/auction actions to prevent spam and automation abuse.
* **Economy Protection** — monitoring for gold-selling, duplication exploits, and market manipulation, feeding into the broader economy health process in [100-Economy.md](100-Economy.md).
* **Infrastructure** — DDoS mitigation at the network layer ([122-Network.md](122-Network.md)), regular database backups.

## Process
Security should be reviewed as part of every major system's design, not treated as a separate late-stage audit — consistent with the documentation-first, quality-first pillars in [002-Core-Pillars.md](002-Core-Pillars.md). A dedicated security/exploit review pass is planned ahead of Closed Beta ([003-Roadmap.md](003-Roadmap.md)).
