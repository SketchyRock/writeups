# Palo Alto NextGen Firewall Reference Guide

Quick reference for securing and managing Palo Alto firewalls during MACCDC competitions.

## Password and login:
```bash
# 1. Change Password -> Purple-Defender-Fire26!

configure
set mgt-config users admin password


# 2. Lock Management Access to your subnet (e.g., 172.20.0.0/16)

set deviceconfig system permitted-ip 172.20.242.0/24
# gives access to firewall from all linux boxes


# 3. disable ipv6 in memory ONLY DISABLE IF NO IPV6 NEEDED

set deviceconfig setting session ipv6-firewalling no //no ipv6 in memory

commit
```

## Security Rules

### Initialize Red Team Blocklist
```bash
set address "RED_IP_PH" ip-netmask 192.0.2.10
set address-group "RED_TEAM_BLOCKLIST" static [ RED_IP_PH ]
```

### Core Security Rules
```bash
# Block all known Red Team IPs (priority: top)
set rulebase security rules "BLOCK_RED_TEAM" from any to any source "RED_TEAM_BLOCKLIST" destination any application any service any action drop log-end yes

# Block IPv6 if not needed (safeguard against tunneling attacks)
set rulebase security rules "BLOCK_ALL_IPV6" from any to any source any destination any application ipv6 service any action drop log-end yes

# Allow required scoring services inbound
set rulebase security rules "ALLOW_LAN_SERVICES" from external to internal source any destination any application [ web-browsing ssl dns smtp pop3 ] service any action allow log-end yes

# Allow internal user outbound (web only)
set rulebase security rules "ALLOW_INTERNAL_OUT" from internal to external source 172.20.242.0/24 destination any application [ web-browsing ssl ] service application-default action allow log-end yes

# Permit ICMP/ping for scoring (required by competition)
set rulebase security rules "ALLOW_SCORING" from external to internal source any destination any application ping service any action allow log-end yes
```

### Apply Rule Order
```bash
configure

move rulebase security rules "BLOCK_RED_TEAM" top
move rulebase security rules "BLOCK_ALL_IPV6" after "BLOCK_RED_TEAM"
move rulebase security rules "ALLOW_LAN_SERVICES" after "BLOCK_ALL_IPV6"
move rulebase security rules "ALLOW_SCORING" after "ALLOW_LAN_SERVICES"
move rulebase security rules "ALLOW_INTERNAL_OUT" after "ALLOW_SCORING"

commit
```

### Delete Default Permits
These overly permissive base rules should be deleted after verification:
```bash
delete rulebase security rules "Permit Outbound"
delete rulebase security rules "Permit Inbound"
```

### Adding New Red Team IPs to Blocklist
```bash
configure
set address "RED_IP_NEW" ip-netmask <Attacker_IP>
set address-group "RED_TEAM_BLOCKLIST" static [ RED_IP_PH RED_IP_NEW ]
commit
```

### Monitoring & Diagnostics

**View Traffic Logs:**
```bash
show log traffic direction equal backwards     # general traffic
show log threat direction equal backwards      # identified threats
```
(Exit with Ctrl+C)

**Inspect Configuration:**
```bash
show rulebase security rules                   # list all rules
show config diff                               # compare pending vs committed
show interface logical                         # list zones
show system resources                          # check CPU/memory
```

### Rule Management
```bash
# Enable logging on a specific rule
set rulebase security rules "YOUR_RULE_NAME" log-end yes

# Rename a rule
rename rulebase security rules "OLD_NAME" to "NEW_NAME"

# Delete part of a rule (e.g., remove an application)
delete rulebase security rules "ALLOW_LAN_SERVICES" application ping
```

### Web GUI Access
Palo Alto GUI: `https://172.20.242.150` (when accessible)

## Backup & Recovery

### Create Snapshots (Before Major Changes)
```bash
# CLI mode
configure
save config to [NAME].xml

# GUI mode
Device > Setup > Operations > Save named configuration snapshot
```

### Restore from Snapshot
```bash
# CLI mode
configure
load config from [NAME].xml
commit

# GUI mode
Device > Setup > Operations > Load named configuration snapshot
```

### List & Manage Snapshots
```bash
dir config                                      # List all saved configs
save config to [NAME].xml                       # Save restore point
delete config saved [NAME].xml                  # Delete old backup
show config diff                                # Compare pending vs active
```

---

## Emergency Response Reference

| Situation | Action | Command |
|:---|:---|:---|
| Red Team Active | Kill Session | `clear session all filter source <IP>` |
| Network Down | Rollback | `load config from last-committed` |
| Scoring Offline | Check Logs | `show log traffic direction equal backwards` |
| CPU Spiking | Check Health | `show system resources` |
| Need Quick Restore | Load Start-of-Round | `load config from running-config.xml` then `commit` |

---

## Common Ports & Vulnerabilities

| Port | Protocol | Service | Security Risk |
|:---|:---|:---|:---|
| 20/21 | FTP | File Transfer | Cleartext credentials |
| 22 | SSH | Remote Mgmt | Brute-force, key-based attacks |
| 23 | Telnet | Remote Mgmt | **AVOID** — All cleartext |
| 25 | SMTP | Email | Open relay attacks, spam |
| 53 | DNS | Name Resolution | DNS tunneling, cache poisoning |
| 80 | HTTP | Web | Cleartext, SQLi, XSS |
| 110 | POP3 | Email | Cleartext credentials |
| 443 | HTTPS | Web | Encrypted but needs inspection |
| 445 | SMB | File Share | EternalBlue, ransomware |
| 3389 | RDP | Remote Desktop | BlueKeep, credential attacks |
| 4444 | Custom | Metasploit | Red Team default shell |