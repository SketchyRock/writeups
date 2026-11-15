# MACCDC 2026 Regionals

**Date:** January 25-26, 2026 | University of Maryland  
**Role:** Palo Alto Firewall Administrator  
**Result:** Minimal service uptime, significant learning

48 hours of live network defense. First time doing this in a serious competitive environment. Results were bad. Learning was good.

Services started failing early and I assumed it was the firewall. My role was firewall admin so naturally I blamed the firewall. I spent most of 30 hours writing, rewriting, and overwriting rules — each time convinced the next change would fix it. By hour 8 the ruleset was a mess of overlapping, conflicting policies.

On day 2 I finally did what I should have done on day 1: ran tcpdump and opened the capture in Wireshark. The problem was immediately obvious. Packets from the scoring server were looping back to themselves — a layer 2 network loop, two switches with no spanning tree configuration, packets bouncing infinitely. Nothing I was ever going to do with firewall rules would have fixed that.

That was hard to sit with. 30+ hours on a problem that had nothing to do with my job.

The root cause wasn't really technical. We showed up without understanding our own network. No topology diagram, no service inventory, no baseline to compare against. When things started breaking we had no reference for what "working" looked like. CTF mindset applied wrong — in CTFs you understand your target before you attack it. In blue team you understand your infrastructure before someone attacks it. If you don't, you're guessing from the start.

Also: when I'm a hammer, everything looks like a firewall rule. Should have escalated to someone checking layer 2 on day 1 instead of staying siloed for 30 hours.

**What changes next time:**  
Preparation is the actual work. Network topology diagram a week out. Service inventory and ownership assigned before going live. Traffic baseline captured in a quiet moment. Always capture packets before touching rules.
