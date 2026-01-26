# Competition Retrospective: 2026 MACCDC Qualifiers
**Date:** 1/17/2026
**Role:** Firewall Administrator (Palo Alto) & Injects Technical Support
**Infrastructure:** Subnet-specific Linux boxes and networking.

## Executive Summary
In this round, I was responsible for securing the subnet gateway via a Palo Alto firewall and supporting the Injects Lead with technical tasks. By maintaining a backup before change policy and balancing security hardening with business objectives (Injects), I ensured no downtime was of my own fault for my assigned services throughout the event.

## Technical Defense & Hardening
* **Firewall Management:** Leveraged the initial soft grace period to audit security rules, rotate administrative credentials, and establish a baseline for known good traffic.
* **Traffic Analysis:** Monitored logs to identify and block malicious beacons and unauthorized traffic attempts targeting the Linux subnet.
* **Resilience Strategy:** Implemented a manual backup system for all configuration changes. This fail safe approach allowed for aggressive hardening with the insurance of rapid recovery, though no rollbacks were ultimately required.

## Lessons Learned: The Splunkening
The Red Team’s most effective attack targeted our Splunk server, a system that lacked a dedicated owner during our pre-competition prep.
* **The Vulnerability:** Default credentials were not rotated during the initial hardening phase.
* **The Attack:** Red Team gained access and changed the scoring heartbeat protocol from `http` to `https`.
* **The Impact:** While technically "more secure," the scoring bot did not recognize the change, resulting in artificial downtime and major loss of points.
* **Takeaway:** Every service must have a named owner. In future rounds, Unassigned boxes will be the first priority for credential rotation.

## Injects & Team Synergy
* **Dual Role:** Acted as the technical bridge for the Injects lead, translating complex system requirements into completed business tasks.
* **Uptime vs. Injects:** Prioritized uptime as the primary metric. I utilized periods of low activity from the Red Team to assist with documentation and technical inject requirements without compromising the firewall's perimeter.

## Action Plan for Regionals and Future Competitions
1.  **Selective Traffic Filtering:** Move beyond basic blocking to more granular traffic inspection to better identify sophisticated Red Team persistence.
2.  **Initial Audit Speed:** Improve the first minutes checklist to include a sweep for misconfigured services that could trigger failures.
3.  **Ownership Grid:** Ensure the team has a clear "Owner Matrix" so that no box is left with default settings.
