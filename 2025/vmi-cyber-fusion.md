---
title: "VMI Cyber Fusion 2025"
type: "retrospective"
category: "ctf"
event: "VMI Cyber Fusion"
date: 2025-02-15
format: "Digital CTF, secondary division (Microsoft-hosted)"
team: "Me + Jack Nelson"
result: "1st place"
tags: [ctf, automation, docker]
---

# VMI Cyber Fusion 2025

[← All write-ups](../README.md)

We didn't really compete in the traditional sense. Jack and I built an automated CTF solver — a containerized Kali environment that could identify, categorize, and solve challenges with minimal human input. About 94% of challenges were handled autonomously. Everything got solved faster than any team doing it manually.

It worked. We won.

But there's an honest accounting: we spent hundreds of hours building this instead of actually practicing CTF skills. We won by engineering around the problem, not by being better at it. That's not obviously wrong given the goal was first place and we got it. But I walked away knowing how to orchestrate Docker containers better than I know how to exploit a binary.

The engineering was real — parallel solving across 8-10 containers, intelligent retry logic, fallback to manual for edge cases. Jack drove the challenge parser and tool integrations; I built the orchestration pipeline and exploit templates. We worked well together. The 6% of challenges that needed human review were the most instructive part. Those were the gaps automation couldn't paper over.

## Takeaway

Automation multiplies what you already know. It doesn't teach you what you don't.
