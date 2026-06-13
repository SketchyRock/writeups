# MACCDC 2026 Regionals Retrospective

**Event Date:** January 25-26, 2026  
**Location:** University of Maryland  
**Role:** Palo Alto Firewall Administrator  
**Team Context:** CTF-oriented group competing in defensive security for the first time  
**Overall Result:** Significant learning; minimal service uptime due to preparation gaps

## Executive Summary

MACCDC Regionals at UMD was my first serious engagement with live network defense in a competitive environment. As the sole Palo Alto firewall administrator for a team with minimal blue team experience, I faced a humbling reality: competitive programming and CTF skills don't transfer directly to defending unknown infrastructure under time pressure and active attack.

Spent 48 hours chasing a phantom firewall rule, convinced our blocking was killing service connectivity. The actual problem was a packet loop in the network layer — an issue I would never have discovered through frantic rule adjustments. This experience crystallized a critical gap: **our team didn't know our own network well enough to defend it.**

## The CTF-to-Blue Team Mismatch

### Why We Struggled

**Context:** My team excels at CTF competitions. We think like attackers: find the vulnerability, exploit it, move on. We're comfortable with time pressure and ambiguous problems. But blue team defense is fundamentally different.

**The Blind Spot:** 
- CTF mindset: "Here's a challenge. Solve it."
- Blue team reality: "Here's infrastructure you've never seen. Keep it running while someone actively breaks it."

CTF teaches you to *attack systems you understand*. Defense requires understanding systems *before they're attacked*. We showed up with Palo Alto commands but without network topology knowledge, service inventory, or baseline traffic patterns.

### Specific Gaps We Faced

**Network Topology Unknown:**
- Didn't know which systems were internal vs. external
- Couldn't identify critical service dependencies
- Learned the hard way that the "scoring server" wasn't where we thought it was
- Spent 90 minutes troubleshooting a firewall rule that wasn't even blocking the right traffic

**Service Inventory Missing:**
- Which systems ran HTTP? HTTPS? Custom protocols?
- Where did authentication happen?
- What were the network's legitimate traffic patterns?
- No baseline to compare anomalies against

**Monitoring Blindness:**
- Palo Alto logs showed "traffic blocked" but not *why*
- Couldn't correlate firewall events with service failures
- No visibility into internal network communication

## The Two-Day Struggle

### Day 1: Panic & Rule Chasing

**Morning Setup Phase (1-2 hours):**
I inherited a firewall with existing rules from previous rounds. Rather than carefully auditing them, I trusted they were reasonable. This was a mistake.

**Scoring Failures (Hours 2-8):**
- Services started failing to connect to the scoring system
- Red Team attacks began almost immediately
- I assumed: "The firewall is blocking legitimate traffic"

**The Solution Spiral:**
- Created more permissive rules
- Didn't block known Red Team IPs (I hadn't collected them yet)
- Added exception after exception, each time thinking "this is the one"
- By hour 8, firewall rules were a disaster of overlapping, conflicting policies

**Mindset Error:** I approached firewall administration like troubleshooting a CTF. Throw things at the wall, see what sticks. Real infrastructure defense isn't iterative guessing — it's systematic isolation.

### Day 2: The Packet Loop Discovery

By morning of Day 2, services were still failing. I finally did what I should have done on Day 1: captured network traffic.

**Using tcpdump to Debug:**
```bash
tcpdump -i eth0 -w /tmp/capture.pcap
```

Opened the PCAP in Wireshark and immediately saw something wrong: **packets from the scoring server were looping back to themselves**, creating a broadcast storm. The same packet appeared 50+ times in sequence, each time with a slightly different TTL (time-to-live).

**The Root Cause:**
This wasn't a firewall issue at all. It was a **layer 2 network loop** — two switches were creating redundant paths, and the network lacked proper spanning tree configuration. Packets were bouncing infinitely between them.

**The Realization:**
I had spent 30+ hours adjusting firewall rules to solve a problem that had nothing to do with the firewall. The packet loop had started on Day 1 and would never be fixed by any rule I wrote.

### Impact

- Services were down for most of the 48-hour competition
- Minimal or no points from scoring
- Time invested in troubleshooting: ~40 hours
- Actual diagnosis time: <2 hours (after I finally captured traffic)

## What Went Wrong: Root Causes

### 1. Skipped the Preparation Phase

**What We Should Have Done (Pre-Competition):**
- Network walkthrough: "Here's your topology, these are your critical systems"
- Service mapping: "HTTP runs on these boxes, HTTPS on those"
- Baseline traffic capture: "This is what normal looks like"
- Alert thresholds: "If X service isn't passing Y packets/second, something's broken"

**What We Did:**
- Showed up 10 minutes before the event
- Got a quick briefing we didn't retain
- Started troubleshooting immediately

### 2. Assumed Firewall = Bottleneck

Because my role was "firewall admin," I unconsciously blamed the firewall for everything. This cognitive bias ("When you're a hammer, everything's a nail") cost us hours.

Should have asked: "Is this definitely a firewall issue?" and validated with packet captures before making rule changes.

### 3. No Escalation Strategy

When firewall rules didn't fix the problem, I should have escalated to other team members:
- Network admin: "Check layer 2 for loops"
- System admin: "Verify services are running"
- Red Team lead: "What attacks are you seeing?"

Instead, I stayed siloed, convinced I could solve it alone.

### 4. Panic Decision-Making

By hour 12, I was exhausted and frustrated. Rules became increasingly haphazard. Under pressure, my troubleshooting approach shifted from *systematic* to *desperate*.

Should have stepped away, taken a break, and approached the problem fresh.

## Mental & Preparation Lessons (The Real Takeaway)

This wasn't primarily a technical failure — it was a **preparation and mindset failure**.

### Lesson 1: Preparation is 80% of Performance
- 2 hours of pre-event network understanding = 40 hours of competition troubleshooting saved
- The time to understand your infrastructure is *before* Red Team attacks, not during

**How to Apply:** For next regionals, I'll request a detailed network diagram 2 weeks prior, capture 30 minutes of baseline traffic, and document every service's expected behavior.

### Lesson 2: Systematic Troubleshooting > Panic Guessing
The OSI model exists for a reason. When services fail:
1. Layer 1/2: Check physical/switch level (my missing step)
2. Layer 3: Check routing and IP connectivity
3. Layer 4: Check open ports and protocols
4. Layer 7: Check application logs

Instead, I jumped to Layer 7 (firewall rules) and stayed there.

**How to Apply:** Always start with packet captures and network diagnostics before adjusting security policies.

### Lesson 3: Blue Team Requires Different Mental Preparation
CTF tournaments reward quick pivots and creative problem-solving. Blue team demands discipline, documentation, and patience.

- **CTF mindset:** "What's the exploit?"
- **Defense mindset:** "What's the baseline? What changed?"

I need to reprogram myself. This is hard.

### Lesson 4: First Live Network Experience is Humbling
This was my first time defending actual infrastructure. The stress is different from CTFs:
- Not just "solve a problem" — "keep 20+ people's work running"
- Not just "find one flag" — "maintain availability for 48 hours straight"
- Not just "technical challenge" — "emotional pressure from team members saying 'Why is scoring down?'"

That pressure made me rush. Next time, I'll expect it and manage my mental state accordingly.

## What I Did Well

### 1. Didn't Panic Break Things Irreversibly
Despite the chaos, I never fully deleted critical rules or made truly catastrophic changes. I had good instincts about what not to touch.

### 2. Eventually Investigated Properly
Once I realized rule-tweaking wasn't working, I pivoted to packet capture. This is the correct troubleshooting reflex, even if it came too late.

### 3. Admitted the Firewall Wasn't the Problem
Many people would have doubled down ("The firewall is definitely the issue"). I eventually said, "I don't think this is firewall-related." That intellectual honesty is the foundation for learning.

## Technical Growth Plan

1. **Network Monitoring Tools:** Master tcpdump, Wireshark, and Palo Alto's traffic logs *in a lab environment* before the next event. Know what normal looks like.

2. **Network Fundamentals:** Study spanning tree protocol (STP), VLAN configuration, and layer 2 switching. My blindness to the packet loop came from weak layer 2 knowledge.

3. **Palo Alto Deep Dive:** Move beyond rule syntax to understanding traffic flow through the firewall (zones, interfaces, NAT). Write playbooks for common troubleshooting scenarios.

4. **Pre-Event Preparation Checklist:**
   - [ ] Request network topology diagram 2 weeks before
   - [ ] Set up lab environment with same Palo Alto configuration
   - [ ] Practice on historical MACCDC scenarios
   - [ ] Document expected services, ports, and traffic patterns
   - [ ] Create escalation procedures (who to contact for network vs. system vs. application issues)

## Mental & Professional Growth Plan

1. **Stress Management:** Regionals are intense. Next time, I'll schedule breaks, practice breathing techniques, and remember that panic-driven decisions are worse than no decisions.

2. **Ask for Help Earlier:** Blue team success requires collaboration. I'll actively reach out to other team members rather than trying to solve everything solo.

3. **Document as You Go:** Keep a running log of:
   - Changes made and why
   - Results observed
   - Rules added/modified
   - Next steps

   This forces discipline and prevents rehashing the same investigations.

4. **Embrace Being New:** This was my first blue team competition and my first live network defense. Being bad is expected. Next time, I'll set realistic expectations and focus on incremental improvement rather than perfection.

## Conclusion

MACCDC Regionals at UMD was a healthy dose of reality. I'm competent at CTF competitions because I can control the environment — I know the target, I know the constraints, and I can iterate quickly. Blue team defense is harder because it demands understanding *before* action, patience instead of velocity, and collaboration instead of independence.

The packet loop will stay with me: a symbol of how much I still don't know about networking and infrastructure. But that's exactly why I'm doing this. Each competition teaches a lesson. This one was: **preparation matters more than skill.**

Next regionals, I'll be ready.
