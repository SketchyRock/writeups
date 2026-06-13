# Summit CTF 2025 Retrospective

**Event Date:** February 22-23, 2025  
**Organizer:** Virginia Tech  
**Theme:** Hack the Airport (TSA, flight systems, airport infrastructure)  
**Format:** Hybrid — Jeopardy-style CTF challenges + live network with hidden flags  
**Team:** B Team (secondary/learning-focused division)  
**Automation Tool:** Improved automated CTF solver (evolved from VMI Cyber Fusion)  
**Final Placement:** 9th out of ~35 teams  
**Competitors:** Top cyber students from across the country (UVA, VCU, William & Mary, and others)

## Executive Summary

Summit CTF was the most balanced competition I've participated in: part automation challenge, part hands-on infrastructure exploitation, part endurance test. Our B team leveraged the improved automated CTF solver from VMI to dominate the jeopardy-style challenges, leading the competition by mid-Day 1 against teams from UVA and other top programs. However, we hit a skill ceiling.

When jeopardy challenges dried up, our team's lack of hands-on network exploitation skills became apparent. We fell from first to middle-of-pack by evening of Day 1. But here's what redeemed us: **persistence and methodical work on the live network flags.** Over the remaining ~30 hours, we systematically found flags others missed — not through elite skills, but through patience, documentation, and thorough enumeration.

We placed 9th. More importantly, this competition crystallized the biggest lesson of my cybersecurity journey so far: **all the information you need is online. It just requires persistence to find, understand, and apply it.** And the corollary: I need to specialize. Automation + surface-level knowledge won't scale beyond mid-pack placements.

## The Automation Advantage: Day 1 Morning

### Improved CTF Solver (Version 2.0)

Building on VMI's lessons, we refined the automated solver significantly:

**Enhancements from VMI:**
- **Better categorization:** Used challenge metadata (category tags, difficulty ratings) to route to specialized solvers faster
- **Template library expansion:** 150+ challenge patterns for common CTF types (SQL injection variants, XOR encryption, common password cracking approaches)
- **Faster iteration:** Reduced container spinup to 4 seconds (from 8 seconds in VMI)
- **Smarter retries:** Instead of trying all permutations, implemented heuristic-guided exploration (try ROT13, base64, XOR with common keys first)

**Performance:**
- Solved ~40% of jeopardy challenges fully autonomously in the first 4 hours
- Reduced human-in-the-loop time from 30 minutes per challenge to ~5 minutes
- Parallelized across 6 containers simultaneously

### Jeopardy Dominance (Hours 1-8)

The airport theme gave us repeatable patterns:

**Crypto Challenges** (8 flags):
- TSA password resets using common cipher variants
- Flight manifest encryption (weak RC4 implementation)
- Baggage handler access codes (simple XOR)
Our solver handled 6 of 8 with minimal human review.

**Reversing Challenges** (6 flags):
- Boarding pass validation algorithm
- Airline maintenance software
- TSA checkpoint scanner logic
Solved 4 of 6 by identifying common patterns (hardcoded strings, predictable algorithms).

**Web Challenges** (5 flags):
- Airport WiFi login portal (SQL injection)
- Flight booking system (auth bypass)
- Airport staff portal (path traversal)
Solved 3 of 5; the others had non-standard vulnerability chains.

**Forensics** (4 flags):
- Airport CCTV footage metadata
- Flight data recorder analysis
- Packet captures from airport network
Solved 2 of 4; forensics requires more manual investigation.

**Miscellaneous** (3 flags):
- Steganography in airport signage images
- QR code decoding with errors
- Steganalysis on boarding pass graphics
Solved 1 of 3.

**Result at Hour 8:** We had ~23 flags from jeopardy. Next closest team had ~15. We were leading decisively.

## The Skill Ceiling: Day 1 Afternoon to Evening

### Why We Hit a Wall

**Around Hour 10**, jeopardy challenges became sparse. Teams who'd solved early challenges started pivoting to the **live network** — a simulated airport infrastructure with flags hidden in realistic systems.

This is where our team's weakness became apparent: **hands-on exploitation requires skills automation can't replicate.**

### The Live Network Setup

The VT organizers had created an impressive environment:
- **TSA security system** (Linux servers running authentication systems)
- **Flight management platform** (web application with multiple services)
- **Airport WiFi** (router with misconfigured access controls)
- **Baggage handling system** (legacy software with known vulnerabilities)
- **Air traffic control simulation** (custom protocol on obscure port)

Flags were hidden as:
- Database credentials in log files
- Hardcoded secrets in binaries
- Configuration files with access tokens
- Running processes with sensitive memory

### Where We Faltered

**Privilege Escalation:** Our team was weak on Linux privilege escalation. We found initial access through web applications but couldn't escalate to root on several boxes. UVA team, visible on the scoreboard, was escalating faster.

**Service Identification:** Given the airport theme, services had non-standard ports. One team at the top had clearly done this event before and knew the topology. We spent 2 hours discovering services; they spent 20 minutes.

**Exploit Development:** Some services required custom exploitation. Our team lacked experience writing exploit POCs from scratch. We'd automate existing payloads but struggled to adapt when standard tools didn't work.

**Persistence Techniques:** We were finding flags but not understanding how they were left behind or how to find similar patterns elsewhere. Missing the meta-understanding of the attacker's thinking.

**The Spiral:** By Hour 14, we'd plateaued at ~28 flags. The scoreboard showed UVA, William & Mary, and VCU teams pulling ahead. We were frustrated, demoralized, and doubting the automation-heavy strategy.

**Moment of Truth:** Around 8 PM on Day 1, our team had a discussion: "Are we wasting effort on automation that doesn't translate to real exploitation?" 

The answer was nuanced: automation solved the *easy* problems efficiently, but we'd neglected building the *foundational skills* that open doors to hard problems.

## The Comeback: Persistence & Methodical Work (Hours 14-48)

### Strategy Shift: Document Everything

Realizing we couldn't out-skill competitors with deeper hands-on experience, we adopted a different approach:

**Systematic Enumeration:**
- Listed every service, every port, every accessible resource
- Documented what we tried and what failed
- Kept a "low-hanging fruit" checklist: default credentials, common misconfigurations

**Persistence Over Brilliance:**
- Set team members to rotating shifts so we could work 24+ hours straight
- Assigned one person to "flag hunting" full-time (reading logs, checking config files, examining memory dumps)
- Created a "lessons log": every new technique we learned, we documented for others

**Collaboration Over Silos:**
- Unlike the first 14 hours where our automated solver was a "black box," we now explained what it was finding to the team
- Cross-trained on different systems so if one person found a vulnerability, others could replicate it

### Flags from Persistence

**Hours 14-24 (Night 1):**
- Found TSA system default credentials in a comments section of a README file on a public share
- Identified airport WiFi router admin panel accessible via path traversal
- Discovered baggage system logs containing API keys
- +7 flags

**Hours 24-36 (Day 2 Morning):**
- Privilege escalation on flight management system using kernel version mismatch exploit
- Database backup files with credentials in an unprotected NFS share
- Strace output revealing environment variables with secrets
- +6 flags

**Hours 36-48 (Day 2 Afternoon):**
- Memory dump analysis of air traffic control process (found decryption key)
- Source code leak in a git directory accidentally exposed on the web server
- Service configuration files with hardcoded tokens
- +4 flags

**Final count:** 40 flags. Placed 9th.

### Why Persistence Worked

The airport theme encouraged realistic (messy) infrastructure. Flags weren't "designed" like jeopardy challenges — they were **placed realistically**. This meant:
- Flags weren't in obvious places (standard paths, common techniques)
- Finding one flag often revealed patterns that led to others
- The competition rewarded *patience* more than *flashiness*

Teams that blazed through quick wins (jeopardy) sometimes missed the slow-burn flags on the network. We took the opposite approach and it paid off.

## What We Did Well

### 1. Pragmatic Tool Usage
We didn't insist the automated solver solve everything. When it reached diminishing returns, we pivoted to manual work without ego.

### 2. Shift-Based Work
Taking turns meant someone was always fresh and thinking clearly. Fatigue-driven mistakes were minimal.

### 3. Documentation Discipline
Keeping a log of attempts prevented us from re-investigating the same dead ends. It also helped newer team members learn faster.

### 4. Realistic Expectations
By Hour 15, we accepted we wouldn't beat UVA's top team. We focused on maximizing *our* score, not their score.

## Critical Gaps: Why We Plateaued

### 1. Linux Privilege Escalation
We knew the theory (SUID binaries, sudo misconfig, kernel exploits) but lacked hands-on practice. Spent 4 hours on escalations that experienced teams solved in 30 minutes.

**What to do:** Dedicated practice on HackTheBox's Linux privilege escalation path. 10 boxes would have changed our trajectory.

### 2. Service Enumeration Speed
Identifying services, versions, and known vulns is a learned skill. We were slow; top teams had this down to muscle memory.

**What to do:** Practice rapid enumeration (nmap, service identification, banner grabbing) on intentionally complex networks.

### 3. Exploit Customization
When off-the-shelf Metasploit modules didn't work, we were stuck. Writing custom Python exploits requires comfort with target architecture and protocol details.

**What to do:** Write 5 custom exploits from scratch, even simple ones, to build confidence.

### 4. Active Directory / LDAP
One of the live network's access controls used LDAP. Our team had zero familiarity. Lost maybe 2-3 hours fumbling.

**What to do:** Understand LDAP, Kerberos, and Windows/Linux domain structures. These are real infrastructure.

## The Biggest Learning: Information > Skill

### Reflection

By Hour 30 of the competition, I'd learned more cybersecurity in 30 hours than in the previous 3 months of study. The difference? **Application.**

Every technique I used at Summit CTF was available online:
- Kernel exploit for privilege escalation? Exists on ExploitDB.
- LDAP query syntax? Man pages and Stack Overflow.
- Memory analysis technique? HackTheBox walkthroughs.

The difference between our 9th place and someone's 1st place wasn't that they knew secret techniques. It was:
1. They'd *practiced* these techniques before
2. They *recognized* patterns faster
3. They *persisted* through dead ends
4. They'd built *muscle memory*

**Realization:** Cybersecurity isn't gatekept by secret knowledge. It's unlocked by persistence and deliberate practice. The information is all online. You just need to find it, understand it, and apply it repeatedly until it becomes reflex.

### Corollary: I Need to Specialize

But here's the hard truth: I can't be good at *everything*. Our team tried to be generalists (bit of web, bit of crypto, bit of reversing, bit of network exploitation) and we were mediocre at all of it.

Top teams had clear specializations:
- UVA's team was *strong* on privilege escalation; they'd practice it obsessively
- William & Mary had web exploitation down to an art
- VCU's team specialized in reversing and binary analysis

We were 6 people trying to solve 6 categories. They were 6 people with 2-3 deep specializations each.

**Implication for my growth:** I need to choose. Do I want to specialize in:
- **Network exploitation & privilege escalation?** (feels most practical)
- **Cryptography & reversing?** (feels most intellectually satisfying)
- **Web application security?** (most marketable)
- **Offensive automation?** (leveraging our VMI framework)

I'm currently broad. Breadth got us to 9th place. Depth would get us to top 5.

## Team Dynamics: The Good & The Learning

### What Worked

**Shift rotation:** Keeping everyone fresh was crucial for a 48-hour grind.

**Psychological safety:** When someone made a wrong turn, the team didn't blame. We just noted it and moved on. This kept morale high even when we were falling behind.

**Clear specialization roles:** By Day 2, it was obvious who was best at each category. We optimized for that.

### What Could Improve

**Handoff communication:** When a team member found something, explaining it to others took 10+ minutes. Better documentation would have helped.

**Decision speed:** We spent 90 minutes debating whether to focus on network flags vs. continuing jeopardy challenges. Clear decision-making authority would have helped.

**Cross-training on automation:** Only 2 team members understood how the automated solver worked. If it broke mid-competition, we'd be lost.

## Growth Plan Moving Forward

### Immediate (Next 4 Weeks)

1. **Deep Dive: Linux Privilege Escalation**
   - Complete HackTheBox "Linux Privilege Escalation" path (10 medium difficulty boxes)
   - Document every technique in a personal playbook
   - Time goal: escalate from user to root in <15 minutes on unfamiliar systems

2. **Service Enumeration Muscle Memory**
   - 5 practice sessions on random intentionally vulnerable networks
   - Time nmap output → exploit choice → initial access
   - Goal: from enumeration to shell in <30 minutes

### Medium-term (Next 3 Months)

3. **Choose a Specialization**
   - Decision: Network exploitation + Linux hardening (feels aligned with both offense and defense)
   - Deep dive into Metasploit framework internals
   - Advanced exploitation workshop or course (e.g., OSCP preparation)

4. **CTF Participation**
   - Compete in 2-3 more CTFs as B team (low stakes, high learning)
   - Each event, focus on one specialization
   - Build muscle memory

### Long-term (6+ Months)

5. **From B Team to A Team**
   - Shift from "learning-focused" to "competitive" mindset
   - Contribute to main team's strategy, not just personal learning
   - Specialize to the point where I'm valuable for specific challenge categories

## Conclusion

Summit CTF was the most educational competition I've done. Not because I won, but because I *lost the lead, then clawed back.* That arc — from dominance via automation to humility via skill gap to redemption via persistence — taught me more than a first-place finish would have.

**The three core insights:**
1. Automation solves easy problems, but real exploitation requires hands-on skill
2. All information is online; victory is determined by persistence + practice, not intelligence
3. Specialization beats generalization in competitive cybersecurity

**The path forward:** Deep practice on privilege escalation + network exploitation, 2-3 more CTFs as B team, then (hopefully) competitive ability to contribute meaningfully to A team.

Summit CTF reminded me why I'm doing this: not for rankings, but because there's always more to learn, and the learning never stops.
