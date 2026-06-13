# VMI Cyber Fusion 2025 Retrospective

**Event Date:** February 15, 2025  
**Competition:** Microsoft-Hosted Digital CTF (Secondary Division)  
**Team:** Jack Nelson & Self  
**Result:** 1st Place Overall  
**Format:** Pure Digital CTF (contrast to main VMI event which includes physical challenges)

## Executive Summary

As part of VMI's secondary CTF team, I placed 1st overall in the Microsoft-hosted digital competition through a radically different approach: rather than solving challenges manually, Jack Nelson and I engineered an automated exploitation platform. We built a containerized Kali Linux automation framework that identified, categorized, and autonomously solved CTF challenges with minimal human intervention. Despite significant engineering overhead (hundreds of hours of development and debugging), this platform allowed us to solve every challenge at speeds that competitors solving manually couldn't match, securing first place against teams using traditional approaches.

This competition highlighted both the power of strategic automation and the hidden costs of building versus buying in time-constrained environments.

## Technical Approach: Autonomous CTF Solver

### Architecture Overview

Rather than compete in the traditional sense, we shifted the problem: build a framework that solves CTF challenges faster than humans can compete.

**Core Components:**
1. **Container Orchestration Layer:** Spun up isolated Kali Linux containers for each challenge, preventing cross-contamination and enabling parallel solving
2. **Challenge Ingestion Engine:** Automatically downloaded, parsed, and categorized challenges (reversing, crypto, web, forensics, pwn)
3. **Automated Payload Generation:** Used standard pentesting tools (Metasploit, sqlmap, John the Ripper, GDB) orchestrated via Python scripts to generate exploits
4. **Feedback Loop:** Integrated stderr/stdout parsing to detect solution success and advance to the next challenge automatically

### Key Technical Wins

**Parallel Solving:** Instead of sequential manual attempts, we could spin up 8-10 containers simultaneously, each working on independent challenges. This alone provided a 5-10x speedup over traditional teams.

**Reusable Payloads:** Built a library of common exploitation patterns (SQL injection templates, ROP gadget generation, steganography detection) that could be applied across multiple challenges with minimal customization.

**Intelligent Retry Logic:** When a payload failed, the system automatically tried common variations (different encoding schemes, alternative injection points, different wordlists) before escalating to human review.

## Development Journey: The Cost of Ambition

### The Build vs. Compete Dilemma

The fundamental trade-off became apparent immediately: spending 200+ hours engineering automation meant we **didn't** participate in practice rounds or build foundational CTF skills. We were betting that automation would outpace traditional skill acquisition.

**Phase 1: Proof of Concept (50 hours)**
- Basic Kali container spinup and tool orchestration
- Solved 2-3 simple challenges manually to validate the concept
- Realized our initial architecture had severe containerization overhead — each container took 45 seconds to boot

**Phase 2: Optimization & Scaling (100 hours)**
- Refactored to use container image caching, reducing boot time to 8 seconds
- Built the challenge parser to automatically identify vulnerability type
- Integrated the Metasploit framework's Python API (non-trivial — documentation was sparse)
- Discovered and worked around race conditions in concurrent exploit delivery

**Phase 3: Expansion & Hardening (50+ hours)**
- Extended the framework to handle web challenges (URL-based payloads, session management)
- Added forensics module (automated carving, file analysis, hash cracking orchestration)
- Implemented rollback logic so failed exploits didn't corrupt containers
- Handled edge cases: services listening on random ports, custom protocols, obfuscated binaries

### Critical Challenges Overcome

**Docker in Docker Complexity:** Running containers inside containers (for sandboxing exploits) caused network isolation issues that weren't obvious until 40 hours in. Required swapping to Docker socket mounting with careful privilege restrictions.

**Metasploit Integration:** The framework's Python bindings were underdocumented. Spent 30 hours reverse-engineering module behavior before achieving reliable payload generation.

**Encoding & Obfuscation:** Some challenges intentionally broke our assumptions (custom file formats, unusual architectures). Building a fallback to human-assisted solving during the event prevented complete stalls.

## Competition Performance

**Execution Phase:**
- All challenges solved within 3 hours (traditional teams took 6-8 hours for similar counts)
- Zero false positives: every automated solution was correct on first try
- Only 2 challenges required human intervention (a custom binary format and a steganography challenge that our classifiers misidentified)

**Reliability Metrics:**
- 94% of challenges solved fully autonomously
- 6% required human review and manual payload tweaking
- 0% failure rate on the final solutions (all automated attempts succeeded)

## Lessons Learned

### 1. Automation Pays for Itself, But Only If It Works
The 200+ hours spent engineering automation earned us a 5-10x performance multiplier. In a time-boxed competition, this was worth the upfront cost. In a skills-building context, we likely missed critical learning opportunities.

**Application:** For future CTF competitions, we'll reserve automation for **repetitive** challenge types (SQL injection variants, common reversing patterns) rather than attempting to automate everything.

### 2. Premature Optimization is Expensive
We spent 50 hours optimizing container boot time before validating that the framework would work at all. A leaner MVP would have revealed architectural flaws faster.

**Application:** Next time, aim for "working in 48 hours" rather than "optimized in 48 hours."

### 3. Documentation Debt Compounds
The Metasploit and Docker integration challenges could have been solved faster with better documentation of our own code. By hour 150, we'd forgotten why certain design decisions were made.

**Application:** Maintain a design document and decision log in parallel with implementation.

### 4. Human Fallback is Essential
The 6% of challenges that required human intervention would have stalled us completely without a built-in override. Automation that fails silently is worse than no automation.

**Application:** Design automation systems with clear escalation paths, not as black boxes.

## Collaboration & Team Dynamics

**Jack Nelson's Contributions:**
- Led the challenge parser and category detection (60% of development time)
- Built the Metasploit integration framework
- Handled debugging infrastructure issues (Docker socket, networking)

**My Contributions:**
- Architected the overall orchestration pipeline
- Built the payload library and exploit templates
- Implemented feedback loop and success detection
- Handled forensics and web challenge modules

**Synergy:** Jack and I had complementary strengths — he excels at low-level tool integration, I focused on high-level system design. This enabled us to parallelize development effectively rather than step on each other's toes.

## Growth Priorities for Future Competitions

1. **CTF Fundamentals Deep Dive:** Next competition, I'll solve 50+ Kattis/HackTheBox challenges before the event to build hands-on skills independent of automation. Relying on automation cost us learning.

2. **Containerization Mastery:** Spend 20 hours pre-event understanding Docker, Kubernetes, and privilege separation. This would have saved significant debugging time.

3. **Metasploit & Burp Integration:** Build sample exploits using Metasploit's Python API and Burp's REST interface before the event, not during it.

4. **Hybrid Approach:** For the next major CTF, blend automation (handles 70% of challenges) with strong manual skills (handles 30% of edge cases and novel challenges).

5. **Documentation Practice:** Maintain a living technical journal during development so future versions of this framework can be built faster.

## Conclusion

VMI Cyber Fusion demonstrated that creative approaches to CTF competitions can yield outsized results, but at a significant time cost. Automation enabled us to dominate through speed and reliability, but we learned the hard way that engineering excellence doesn't substitute for foundational cybersecurity skills.

The framework Jack and I built won't be our competitive advantage next time — it'll be our understanding of the vulnerabilities we were solving for.
