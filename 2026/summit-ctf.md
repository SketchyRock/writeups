---
title: "Summit CTF 2026"
type: "retrospective"
category: "ctf"
event: "Summit CTF"
date: "2026-02"
location: "Virginia Tech"
organizer: "Virginia Tech"
theme: "Airport infrastructure (Hack the Airport)"
format: "Hybrid: jeopardy + live network"
team: "B team"
result: "9th out of ~35"
tags: [ctf, privilege-escalation, enumeration, teamwork]
---

# Summit CTF 2026

[← All write-ups](../README.md)

48 hours. Probably the most educational event I've done so far, partly because the arc went wrong in an instructive way.

We came in with the upgraded automation framework from VMI and dominated the jeopardy portion early — had more flags than anyone else by hour 8. Teams from UVA, William & Mary, VCU all behind us on the scoreboard.

Then jeopardy dried up and we hit the live network. That's where automation stops helping and actual hands-on skill takes over. Privilege escalation, custom exploit chains, service enumeration under time pressure — we were slow at all of it. The scoreboard flipped as teams with real experience pulled ahead. We fell from first to mid-pack fast. It stung.

What pulled us back was just stubbornness. We started treating the live network like a documentation project — listing every service, every port, every failed attempt. Rotating shifts so someone was always fresh. A lot of the flags in a realistically-designed environment aren't in clever places, they're in predictable ones that only get found by being thorough. Found another 17+ flags over the next 36 hours through patient enumeration and following attacker logic.

9th place.

## The big lesson

All the information you need is online. The gap between teams isn't usually secret knowledge, it's how much they've practiced applying what's publicly available. The top teams had 2-3 deep specializations — UVA was strong on priv esc, William & Mary owned web exploitation. We were 6 people trying to cover 6 categories and were mediocre at all of them.

Depth beats breadth in competition. I need to pick something and go deep.
