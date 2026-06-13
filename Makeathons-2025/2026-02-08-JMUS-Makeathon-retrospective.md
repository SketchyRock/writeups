# JMUS Makeathon 2025 Retrospective

**Event Date:** February 8, 2025  
**Event Type:** 24-Hour Makeathon (Hackathon-style, solution-focused)  
**Theme:** Solutions for natural disasters or improving quality of life  
**Team:** Self (presentation, code review) + 2 competitive programming club members (core development) + 1 business major (strategy, pitch)  
**Final Result:** No placement in top tier, but received "Best Presentation Overall" feedback; pivoted idea was adopted by another team

## Executive Summary

JMUS Makeathon was my first experience building and pitching a consumer-facing product in a time-compressed format. Our team built **Jarvis** — a Jarvis-like AI system for intelligent home automation that learns user patterns, manages schedules, and improves daily routines and mental health. The technical execution was solid, the live demo was impressive, and judges gave us glowing feedback on presentation quality.

Yet we placed outside the top tier.

The reason? Our presentation was *so* polished and *so* focused on the presentation itself that judges misunderstood what the product actually *did*. We confused elegance with clarity. This was a harder lesson than any technical failure: great execution doesn't matter if your audience doesn't understand your value proposition.

As a silver lining, an alternative product concept I developed — **Frontline**, a missing persons locator system leveraging Verizon's disaster-response cell towers — was adopted and used by another team, validating the core idea even if we didn't pursue it.

## Project 1: Jarvis Home Automation AI

### Vision & Problem Statement

**The Problem:** Modern homes have fragmented smart systems (Philips Hue lights, Nest thermostats, Samsung appliances). No unified interface. Users spend time managing dozens of apps instead of living.

**The Solution:** Jarvis is a conversational AI that learns your routines and automates proactively:
- *Morning:* Opens curtains 15 min before alarm, brews coffee, adjusts lighting
- *Work:* Optimizes thermostat based on occupancy, dims lights to reduce distractions
- *Evening:* Gradual lighting shifts (mimics sunset), reminds about tasks, prepares bedroom for sleep
- *Benefits:* Reduced decision fatigue, better sleep hygiene, lower energy use, mental health improvement through routine automation

### Technical Implementation

**Architecture:**
- **Core AI:** LLM-based conversational interface (fine-tuned on home automation use cases)
- **Device Layer:** Multi-platform connector framework supporting Philips Hue, Nest, LIFX, Samsung SmartThings via REST APIs
- **Brain:** Learns user routines through interaction history; predicts user needs ("It's 7 AM on weekday, time to wake up")
- **Hardware Interface:** Raspberry Pi 4 as the central hub, running the orchestration logic

**Key Features Implemented:**
1. **Schedule Learning:** Watched user behavior, automatically suggested automation ("You always turn on lights at 6:30 PM, should I automate this?")
2. **Cross-Platform Command Translation:** "Hey Jarvis, make it morning" → Opens Philips Hue to 5000K, Nest to 68°F, Spotify to wake-up playlist
3. **Natural Language:** Not command-driven ("turn on lights") but conversational ("I'm tired, help me sleep")
4. **Offline Resilience:** Raspberry Pi operated locally; cloud sync was optional for learning improvements

### The Live Demo

The centerpiece of our presentation was a **full-stack live demonstration:**
- Actual Raspberry Pi running our system in real-time
- Smart bulbs, thermostat simulator, and calendar integration all visible
- Live voice commands: "Good morning, Jarvis" → Lights brightened, blinds opened, calendar read upcoming meetings

The demo was flawless. Three separate judges asked to see it again. One said, "This is production-ready."

### My Contributions

**Presentation Design:**
- Structured narrative around "decision fatigue" → "automation" → "better life"
- Visual metaphor comparing Jarvis to Iron Man's JARVIS (helpful, proactive, learns)
- Slide design: clean, minimal, focused on the demo hardware rather than text

**Code Review & Architecture:**
- Reviewed the AI prompt-tuning and device connector code
- Suggested multi-platform abstraction layer (saved 20 hours of refactoring later)
- Validated edge cases in the schedule-learning algorithm

### The Presentation Paradox

Here's where it gets interesting. Judges gave us exceptional feedback on presentation:
- "Best presentation overall" — multiple judges
- "You made us *feel* the value, not just understand it"
- "The demo was the best I've seen"

Yet we didn't place in the top tier. When we asked why, the feedback was revealing:

**Judge Comment:** "We loved the presentation, but we're not sure exactly what the product is. Is it a smart home hub? An AI assistant? A sleep improvement tool?"

**What Happened:** We had optimized the presentation for *emotional resonance* ("Imagine waking up naturally instead of jolted by alarms") but didn't clearly state the *product category* or *core differentiator*. Judges understood we were impressive, but not *why* Jarvis was different from existing solutions like Google Home or Alexa.

**The Lesson:** A beautiful presentation that confuses your audience is worse than a clunky presentation that clarifies your value. We prioritized storytelling over clarity. The irony is our presentation *skill* undermined our product *understanding*.

## Project 2: Frontline — The Idea We Didn't Pursue

### The Concept

Mid-event, our team brainstormed alternative ideas. I proposed **Frontline**, a mobile app for locating missing persons during natural disasters:

**Problem:** During hurricanes, earthquakes, and floods, cell networks go down. Missing persons become truly lost — no phone pings, no location data, no way for families to find them.

**Solution:** 
- Distributed peer-to-peer mesh network using phones' Bluetooth
- Users opt-in to "broadcast" their location (even without cellular)
- Caching layer: phones remember last-seen locations of others and relay them when networks come back online
- Integration with Verizon's new disaster-response mobile cell towers (temporary infrastructure deployed post-disaster)

**Key Innovation:** The "offline-first" architecture. Instead of relying on infrastructure, Frontline leveraged the phones themselves as the network.

### Why We Didn't Pursue It

**Team Discussion:**
- Jarvis was nearly complete (8 hours into the 24-hour event)
- Frontline would require cryptography work (secure peer-to-peer), mesh networking, and regulatory considerations with Verizon
- Risk of shipping an incomplete product vs. polishing a complete one
- Business major argued Jarvis had clearer product-market fit

**Decision:** We doubled down on Jarvis. Reasonable choice given time constraints.

### The Irony

On the final day of presentations, **another team presented Frontline** — nearly identical concept, using the same Verizon tower integration, same peer-to-peer approach. They must have independently developed the idea, or overheard it from us.

Importantly, their version was *less* fleshed out than what I'd sketched:
- No mention of the caching layer (critical for offline resilience)
- Vague on the encryption/security model
- Unclear incentive structure for users to participate

But they placed higher than us.

**Reflection:** This stings a bit, but it also validates the concept. Frontline appears to be a genuine unmet need. If we'd pursued it, we might have placed higher. But we also might have shipped incomplete work. The decision was reasonable; the outcome is just... ironic.

## Team Dynamics

### What Went Well

**Collaboration:** Our team had complementary strengths:
- Comp programming members: Strong technical execution, rapid prototyping
- Business major: Product positioning, user research, pitch refinement
- Self: Bridging layer, ensuring technical and narrative coherence

**Division of Labor:** Clear roles meant minimal duplicated effort. We never had two people working on the same thing.

**Morale:** 24-hour hackathons are tiring. Our team stayed focused and supportive. When a team member struggled with an API integration, others jumped in without resentment.

### Lessons on Team Composition

**What We Did Right:**
- Included a non-technical team member (business major); they asked questions engineers would skip
- Mixed skill levels; junior comp programmers learned from seniors
- Built a product we'd actually use (many hackathon teams build throwaway projects)

**What We Could Improve:**
- Should have assigned someone to "judge empathy" — clarifying what judges would understand, not just what impressed them
- Could have done user research interviews (even 10 minutes during setup) to validate product positioning

## Presentation Lessons: Clarity > Elegance

### What We Got Right

- **Visual Design:** Minimal, professional, supported the demo
- **Narrative Arc:** Emotional hook ("decision fatigue") → solution → vision
- **Live Demo:** Functional, impressive, showed real value

### What We Got Wrong

**Ambiguous Value Proposition:** We never clearly answered:
- Who is this for? (We said "busy professionals" but also "families" and "elderly")
- What problem does it solve better than alternatives? (Didn't mention Google Home, Alexa, or HomeKit)
- Why now? (No mention of market shifts or technological breakthroughs enabling this)

**The Mistake:** We optimized for judges' *emotions* rather than judges' *comprehension*. We should have answered the above three questions in the first 60 seconds, then spent the remaining time on emotional resonance.

## What I'd Do Differently

### For Makeathons/Product Competitions

1. **Clarify Before You Polish**
   - Spend first 2 hours answering: "What is this? Who needs it? Why now?"
   - Only *then* build the beautiful presentation around these answers

2. **User Testing, Not Just Demos**
   - 10 minutes of a potential user saying "I don't understand what this does" is worth more than a flawless demo
   - Use early feedback to sharpen your pitch

3. **Assign a "Clarity Lead"**
   - Someone whose job is to ask dumb questions ("I still don't know who this is for")
   - Prevent your team from disappearing up the 'polished presentation' rabbit hole

4. **Practice Pitching to Non-Domain People**
   - Pitch to your business major, not your CS peers
   - If someone not familiar with the problem space understands your value prop, you're in good shape

### For Technical Execution

1. **Build Around a Core Demo**
   - Don't overthink features; focus on one impressive, real thing
   - Our Raspberry Pi + lights + live demo was the right call

2. **Leave Time for Polish**
   - We finished code at hour 20; spent hour 20-24 on presentation
   - That 4 hours of presentation prep made a difference in judge perception

## Growth Priorities Moving Forward

1. **Product Positioning:** Take a course on product strategy or pitch coaching. Understand how to clearly communicate value to non-technical audiences.

2. **User Research:** Learn rapid user interview techniques. 10 questions can prevent hours of misalignment.

3. **Presentation Design:** Study how successful startups pitch (Y Combinator videos, Product Hunt launches). Identify the pattern they use to communicate.

4. **Entrepreneurial Mindset:** Makeathons reward executable ideas. Build faster, validate assumptions early, cut scope ruthlessly.

## Conclusion

JMUS Makeathon taught me that technical excellence and beautiful execution aren't enough. The product that wins isn't always the one judges *like best* — it's the one judges *understand best*.

Jarvis is a genuinely good idea with solid technical execution. But we buried the lead in narrative elegance. Next time, I'll lead with clarity, then add polish.

As for Frontline: it validated an idea I'll carry forward. Maybe in another hackathon, or maybe as a side project. Seeing another team use the concept — even if imperfectly — is proof that the problem is real.

The best lesson from a makeathon isn't technical. It's that **clear communication of a good idea beats beautiful communication of a confusing one.**
