# MACCDC 2026 Qualifiers Retrospective

**Event Date:** January 17, 2026  
**Role:** Firewall Administrator (Palo Alto NextGen) & Injects Technical Support  
**Scope:** Subnet gateway security and cross-functional technical enablement

## Executive Summary

I successfully defended the network perimeter as the Palo Alto firewall administrator while providing technical support for the Injects team. By implementing a "backup-before-change" policy and establishing clear ownership of all services, I maintained 100% uptime for my firewall’s assigned scope and prevented self-inflicted downtime throughout the competition. The event highlighted the critical importance of pre-competition service ownership and exposed gaps in our credential rotation discipline.

## Defensive Operations

**Initial Hardening Phase:**
- Audited all firewall rules inherited from previous configurations and removed unnecessary permits
- Rotated administrative credentials and locked management access to the subnet CIDR block
- Established baseline logging and traffic profiles for known-good services

**Active Defense:**
- Monitored Palo Alto logs continuously to identify Red Team beacons and lateral movement attempts
- Built and maintained a dynamic Red Team blocklist, adding IPs as they were identified
- Configured granular application-layer rules to allow only required scoring services (HTTP/HTTPS, DNS, SMTP, POP3)

**Operational Resilience:**
- Implemented a pre-change snapshot system for all configuration modifications
- Maintained the ability to rollback in <5 minutes, enabling aggressive hardening without fear of cascading failures
- No rollbacks were required during the event, validating the safety-first approach

## Critical Incident Analysis: The Splunkening

Our most impactful attack occurred on the Splunk monitoring server, which had no assigned owner during preparation:

**Root Cause:** Default credentials were never rotated because no single person owned responsibility for that system.

**Attack:** Red Team gained access and modified the scoring heartbeat protocol from HTTP to HTTPS, making it incompatible with the automated scoring bot.

**Outcome:** Artificial downtime resulted in major point loss, despite the underlying infrastructure being healthy.

**Lesson:** Unowned systems will be exploited. In future competitions, every box receives a named owner before competition begins, and credential rotation occurs in round one of hardening, not after exploitation.

## Cross-Functional Support

**Injects Collaboration:**
- Acted as the technical translator between the Injects lead and system requirements, converting business objectives into technical configurations
- Prioritized uptime as the primary SLA, using low-activity periods to assist with documentation and compliance injects without compromising perimeter security
- Maintained clear boundaries: injects are completed only when they don’t degrade the defensive posture

## Growth Priorities for Regionals

1. **Service Inventory & Ownership:** Create and distribute a clear "Service Owner Matrix" at pre-competition briefing; ensure every non-firewall box has a named owner
2. **Credential Rotation Checklist:** Move credential rotation into the first 30 minutes of competition; include often-forgotten services (monitoring, backups, API endpoints)
3. **Advanced Traffic Inspection:** Move beyond IP-based blocking to application-layer anomaly detection to catch sophisticated persistence mechanisms earlier
4. **Firewall Rule Audit Velocity:** Reduce initial audit time from 90 minutes to 30 by pre-staging a template ruleset and validating it in lab conditions
