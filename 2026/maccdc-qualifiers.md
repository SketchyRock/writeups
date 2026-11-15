---
title: "MACCDC 2026 Qualifiers"
type: "retrospective"
category: "cyber-defense"
event: "MACCDC"
date: 2026-01-17
role: "Palo Alto Firewall Administrator"
result: "Solid individual performance, but a wake-up call on team prep gaps"
tags: [maccdc, blue-team, palo-alto, incident-response]
---

# MACCDC 2026 Qualifiers

[← All write-ups](../README.md)

First defensive competition. I was on the firewall the whole time — Palo Alto NextGen managing the subnet gateway. That part went well: kept the rules clean, built a Red Team blocklist as IPs showed up, maintained rollback capability so I could harden aggressively without risking cascading failures. No self-inflicted downtime.

The thing that went wrong wasn't on my box. Our Splunk monitoring server got taken because nobody owned it. Nobody rotated the default credentials, nobody confirmed it was locked down. Red Team found it, changed the scoring heartbeat protocol from HTTP to HTTPS, and the automated scoring bot stopped reaching it. We lost major points from a box that was completely healthy underneath.

That's the lesson: unowned systems get exploited. In a competition, every box needs a named owner before the event starts, and credential rotation needs to happen in the first 30 minutes, not whenever someone gets around to it. A service owner matrix would've caught this.

Going into regionals, that's the main thing I want to fix: ownership assigned before we go live, and hardening treated like a checklist with a timer, not a free-form activity.
