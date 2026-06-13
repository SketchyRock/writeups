# JMU Blue Team Mock Competition Retrospective

**Event Date:** April 25, 2026  
**Organizer:** JMU Competitive Cybersecurity Club (Internal)  
**Format:** Live defense simulation — Coaches/experienced members attack; newer members defend  
**Theme:** Realistic blue team scenarios (multi-OS, live attackers, real-time feedback)  
**Personal Role:** Windows Defender (host-level defense, hardening, incident response)  
**Significance:** First time hosting internal competition; emphasis on learning over placement

## Executive Summary

JMU's first internal blue team mock competition was a turning point for me, not as a competitor, but as a learner. After three external CTF competitions and one defensive competition (MACCDC Regionals), I finally experienced the thing that separates casual learning from real skill development: **live feedback from an attacker trying to break your defense.**

Unlike MACCDC Regionals (where we couldn't see attacks clearly) or other competitions (where feedback is delayed), this mock competition gave us real-time information: "Your firewall rule doesn't work because..." or "I found your credentials because..." This turned flags from abstract "complete the challenge" into concrete "here's what you did wrong."

I specialized in Windows defense for the first time, implementing a hardening plan under pressure, and discovering that defending is fundamentally different from attacking. It's humbling, educational, and surprisingly fun.

## The Setup: Learning-Focused Design

### Why This Format Works Better Than External Competitions

Our coaches and experienced members designed the competition thoughtfully:

**Real Attackers, Real Feedback:**
- Not automated checks or delayed feedback
- Live attackers saying "I got in because..."
- Immediate learning: change → test → verify

**Graduated Difficulty:**
- Beginners defended while experienced members attacked
- Attacks were challenging but not insurmountable
- Goal: learn, not destroy

**Flags as Learning Signals, Not Goals:**
- Flags hidden on compromised systems
- Capturing flags meant "you found what the attacker did"
- Forced us to think like defenders: "What did they touch? Where would they hide it?"
- Explicit guidance: "The attacker used X technique; learn to detect it"

### The Environment

**Three parallel defensive scenarios:**
1. **Linux Box** (hardened and maintained by experienced member)
2. **Windows Box** (my specialization)
3. **Network Perimeter** (firewall, router, managed by senior team members)

**Realistic Services Running:**
- Windows: IIS web server, Active Directory simulation, file shares, custom database
- Linux: Apache, SSH, SQL database, custom application
- Network: DNS, DHCP, various protocols

**Attackers:** Rotating team of coaches and experienced members, each targeting different systems

## My Experience: Windows Defense Specialization

### The Decision

Before the event, I chose to specialize in Windows defense. Why?

**Reasoning:**
- MACCDC Regionals taught me I'm weak at host-level defense (I only managed firewalls)
- VMI/Summit CTF showed me that specialization matters
- Windows is underrepresented in our club (everyone focuses on Linux)
- Windows is common in real enterprises (good practical skill)

**The Challenge:** I'd never seriously hardened a Windows box before. This was apprentice-level work in a learning environment — perfect conditions.

### The 5-Minute Hardening Plan

I adapted a simplified version of the Palo Alto reference format I'd created, but for Windows:

**Immediate Actions (Minutes 1-5):**
```powershell
# 1. Change Administrator Password
net user Administrator P@ssw0rd2026!Changed

# 2. Disable Unnecessary Services
Disable-NetAdapterBinding -Name "Ethernet" -ComponentID ms_netbios_smb
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True

# 3. Enable Windows Defender Real-time Protection
Set-MpPreference -DisableRealtimeMonitoring $false

# 4. Set Strong Audit Logging
auditpol /set /category:"Logon/Logoff" /success:enable /failure:enable
auditpol /set /category:"Object Access" /success:enable /failure:enable

# 5. Create Initial Baseline (for later comparison)
Get-NetTCPConnection | Export-Csv baseline_connections.csv
Get-Process | Export-Csv baseline_processes.csv
```

**Phase 2 (First Hour):**
- Remove default shared folders (C$, IPC$, ADMIN$)
- Configure Windows Firewall rules (allow only required services)
- Enable logging on all file share access
- Review Event Viewer for suspicious activity
- Research running services (netstat, tasklist) and disable unnecessary ones

### Challenges Faced

**Challenge 1: Didn't Know What "Necessary" Meant**

I started disabling services aggressively. Broke IIS. Disabled critical Windows services by accident. Learned the hard way:
- IIS requires specific services (Windows Process Activation Service, HTTP.sys)
- Disabling services at random causes cascading failures
- Better approach: identify what the box *should* do, disable everything else

**Lesson:** Always know your environment's purpose before hardening. Hardening a web server differently than a file server.

**Challenge 2: Auditing is Overwhelming**

Enabled audit logging on everything. Generated 50+ event log entries per minute. Tried to monitor them manually.

Attackers: "I accessed these files." Me: *searching through 5000 log entries* "...which file?"

**Lesson:** Audit selectively. Enable logging on high-value targets (admin actions, file access to sensitive shares), not everything.

**Challenge 3: Passwords are Only the Beginning**

Changed the administrator password immediately. Felt secure. Attacker within 15 minutes: "I accessed the box through a weak IIS configuration, not credentials."

**Lesson:** Password hardening is necessary but insufficient. Need to harden *every surface*: web applications, file shares, remote access vectors.

### What Went Well

**1. Proactive Monitoring**
I set up a simple spreadsheet tracking:
- Services running and their purpose
- Open ports and what was listening
- User accounts and their privileges
- Recent changes I'd made

When the attacker compromised the box, I could compare "current state" vs. "baseline" and identify what changed.

**2. Real-Time Pivot**
When the attacker got in, I watched what they did (they demonstrated instead of hiding). I immediately:
- Closed the vulnerability they exploited
- Re-hardened that surface
- Blocked the technique they used

By end of event, we'd iterated 3 times on my box. Each iteration got harder to crack.

**3. Learning Questions**
I asked the attackers why their exploits worked. They explained:
- Why weak IIS permissions allowed file access
- How credential theft happened (I'd left credentials in a script)
- What they were looking for (what makes a good flag location)

This Q&A was gold. Better than reading blogs about these topics.

### The Attacks (and What I Learned)

**Attack 1: IIS Configuration Weakness**
- **Attacker:** "Your IIS app pool is running as a user with too many permissions"
- **What happened:** They accessed the underlying filesystem through the web application
- **Fix:** Configured app pool identity principle of least privilege
- **Learning:** Applications should run as restricted users, not administrators

**Attack 2: Credentials in Plaintext**
- **Attacker:** "You have a batch script with cleartext database credentials"
- **What happened:** They found SQL credentials in `C:\backup\script.bat`
- **Fix:** Removed credentials, used Windows authentication instead
- **Learning:** Never store secrets in code/scripts; use environment or credential managers

**Attack 3: Unpatched Service**
- **Attacker:** "This service has a known vulnerability from 2023"
- **What happened:** They exploited a local privilege escalation
- **Fix:** Applied Windows Update, patched the service
- **Learning:** Patch management is critical; even seemingly "internal" services matter

**Attack 4: SMB Share Enumeration**
- **Attacker:** "You left file shares visible with loose permissions"
- **What happened:** They enumerated shares, found sensitive documents
- **Fix:** Disabled unnecessary shares, restricted access lists (ACLs)
- **Learning:** File sharing is powerful but dangerous; lock it down tightly

**All Four Attacks → All Four Flags Found and Learned**

### Growth in Real-Time

By the end of the 2-hour event, my Windows box had:
- Started: vulnerable to 4 separate attack vectors
- Ended: vulnerable only to sophisticated, multi-step attacks

I didn't achieve "completely secure" (impossible), but I achieved "significantly harder to break."

## Comparison to External Competitions

### What Made This Different (Better)

| Aspect | MACCDC Regionals | JMU Mock | Winner |
|:---|:---|:---|:---|
| **Feedback** | Delayed, if at all | Real-time from attacker | JMU |
| **Iteration** | No time to fix; moves on | Fix → test → attack again | JMU |
| **Pressure** | High (ranked) | Low (learning) | JMU for learning |
| **Scope** | Defend entire infrastructure | Specialize on one system | JMU |
| **Questions** | Can't ask | Can ask attackers directly | JMU |
| **Learning Curve** | Steep | Gentle | JMU for beginners |

**The trade-off:** JMU mock lacks the competitive urgency and complexity of real competitions. But for *learning* defensive skills, it's superior.

### Lesson for Future Defensive Careers

Real companies likely have internal red teams or security testing. This mock competition simulates that environment better than external CTFs. The learning model (defender + attacker in same room, real-time feedback) is more realistic than competition formats.

**Implication:** If I pursue security professionally, this environment is closer to actual work than any external competition.

## Club Dynamics & Community Building

### Why This Mattered Beyond the Competition

**Mentorship Formalized:**
Our experienced members became teachers. They:
- Explained *why* attacks worked, not just that they did
- Helped newcomers understand their mistakes in real-time
- Answered questions patiently (not rushed by competition timer)

**Peer Learning:**
Newer members learned from each other's mistakes:
- "I saw how the attacker broke into Linux; now I understand that vector"
- "The Windows defender shared what they learned; I'll apply that to my network"

**Community Over Competition:**
The goal was explicitly "get better together," not "rank highest." This created psychological safety:
- No shame in being compromised (expected)
- Questions welcomed
- Sharing vulnerabilities celebrated (learning opportunity)

**Club Development:**
This event validated the model. We'll repeat next semester with improvements:
- Better documentation of attack vectors
- More realistic infrastructure
- Graduated difficulty tiers
- Recorded walkthroughs for asynchronous learning

## What We Did Well

### 1. Accessibility for Beginners
The environment was designed for people like me (new to defense). Not too hard, not too easy.

### 2. Learning-Focused Design
Flags guided learning, not just point-scoring. Structure encouraged reflection.

### 3. Mentorship Quality
Our experienced members were excellent teachers. Patient, clear, encouraging.

### 4. Iterative Improvement
We ran 2-hour cycles with breaks in between. Allowed iteration and reflection.

## What We Could Improve (For Next Semester)

### 1. Better Service Baseline Documentation
Spend 30 minutes pre-event documenting "what should be running." Would have saved me hours.

### 2. Attack Playbooks
Attackers had variety in approach. Written attack playbooks would ensure we learn consistent lessons.

### 3. Capture-and-Preserve Approach
Once an attack succeeded, we should preserve evidence (not immediately patch) so defenders can analyze it.

### 4. Graduated Difficulty
Next semester, have "easy," "medium," "hard" boxes. Let defenders self-select based on confidence.

## Personal Growth & Specialization Reaffirmation

### Decision: Deepen Windows Defense Specialization

Before this event: "Should I specialize in Windows? Linux? Network?"

After this event: **Definitely Windows defense.** Here's why:

1. **Discovered a Gap:** Our club (and cybersecurity generally) under-prioritizes Windows defense. Opportunity.
2. **Found Enjoyment:** Hardening Windows was fun. (Hardening Linux feels like it's already done by others.)
3. **Practical Value:** Windows is 70%+ of enterprise infrastructure. Marketable skill.
4. **Leadership Opportunity:** I could teach others Windows defense. (Someone has to.)

**Next Steps:**
- Deep dive into Windows hardening (Group Policy, Active Directory, BitLocker)
- Study Windows attack/defense techniques (MITRE ATT&CK for Windows)
- Lead a workshop on Windows defense for club members
- Volunteer to defend Windows at next external competition

## Conclusion: Learning Beats Competition

MACCDC Regionals taught me preparation matters. Summit CTF taught me specialization matters. JMU's internal mock competition taught me something more fundamental: **learning beats winning.**

The environment where you get real-time feedback from an expert is the environment where you grow fastest. Doesn't matter if there are points or rankings. What matters is: can you get feedback, iterate, and improve?

This mock competition was lower-stakes than external competitions, but higher-impact for my learning. I'll compete at external events again, but I'll come back here to learn.

Also: Our club now has a repeatable format for developing new members. That's huge. Every club member who comes next semester can have this same experience.

**Special thanks to our coaches and experienced members for designing this so well.** You took the risk of hosting an event, the effort to set up realistic infrastructure, and the patience to teach beginners. That's community.

Next semester, I'm running the Windows box again. And I'm planning to attack it too — from the red team side. Time to learn how to break what I'm learning to defend.
