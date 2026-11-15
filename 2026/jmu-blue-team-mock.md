# JMU Blue Team Mock Competition

**Date:** April 25, 2026  
**Organizer:** JMU Competitive Cybersecurity Club (internal)  
**Role:** Windows defense  
**Format:** Experienced members attack, newer members defend — real-time feedback

First internal competition the club has run. The format was exactly what you'd want for actually learning something: attackers who explain what they did and why it worked.

I took Windows because nobody else was doing it and it seemed like a gap worth filling. Also, after regionals I wanted to own a host instead of just a firewall.

Started by doing what every Windows hardening guide says — changed the admin password, turned on Windows Defender, enabled audit logging. Felt good about it for about 15 minutes. The attacker got in through a misconfigured IIS app pool I hadn't touched, found credentials in a batch script I hadn't noticed, and leveraged an unpatched service from 2023. The password change did basically nothing.

The part that actually worked was staying curious when things went wrong. I asked the attackers why each exploit worked, not just what it did. That loop — attack, explain, fix, then attack again — accelerated learning more than any external competition I've been to. By the end of the session the box was meaningfully harder to crack. Not secure, but visibly better. Real iteration.

Real-time feedback from someone actively trying to break what you built is how you actually improve. Delayed scoreboard updates don't come close.

**Where I landed:**  
Windows defense as a specialization going forward. Underrepresented in the club, common in enterprise environments, and it turned out to be genuinely interesting. Next semester I want to try the red team side of the same event — learn how to break what I'm building to defend.
