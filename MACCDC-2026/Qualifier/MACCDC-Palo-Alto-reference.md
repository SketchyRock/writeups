# 5 Minute Plan Palo Alto Firewall:

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
```bash
# 1. INITIALIZE RED TEAM BLOCKLIST

set address "RED_IP_PH" ip-netmask 192.0.2.10
# 192.0.2.10 is Test_Net1 and completely inaccessible

set address-group "RED_TEAM_BLOCKLIST" static [ RED_IP_PH ]
# PH = Place Holder


# 2. BASIC SECURITY RULES

# Block all known attackers
set rulebase security rules "BLOCK_RED_TEAM" from any to any source "RED_TEAM_BLOCKLIST" destination any application any service any action drop log-end yes

# Block all ipv6 ONLY IF NO IPV6 NEEDED (safeguard)
set rulebase security rules "BLOCK_ALL_IPV6" to any from any source any destination any service any application ipv6 action drop log-end yes

# PROTECT LAN SERVICES (Allowing only required scoring ports)
# Note: Scoring requires HTTP (80), HTTPS (443), DNS (53), SMTP (25), and POP3 (110).
set rulebase security rules "ALLOW_LAN_SERVICES" from external to internal source any destination any application [ web-browsing ssl dns smtp pop3 ] service any action allow log-end yes //change service to application-default but may break scoring

# PROTECT WLAN (More restrictive than LAN) Usually, WLAN is for users, so only allow web-based traffic out
set rulebase security rules "ALLOW_INTERNAL_OUT" from internal to external source 172.20.242.0/24 destination any application [ web-browsing ssl ] service application-default action allow log-end yes

# MAINTAIN ICMP FOR SCORING (Required by competition rules)
set rulebase security rules "ALLOW_SCORING" from external to internal source any destination any application ping service any action allow log-end yes


# 3. ORGANIZE AND COMMIT

# make sure you are in config mode
configure

# 1) Put the Red Team Blocklist at the very top
move rulebase security rules "BLOCK_RED_TEAM" top

# 2) Put the IPv6 block immediately under the Red Team block
move rulebase security rules "BLOCK_ALL_IPV6" after "BLOCK_RED_TEAM"

# 3) Put your Scoring Services rule after the blocks
move rulebase security rules "ALLOW_LAN_SERVICES" after "BLOCK_ALL_IPV6"

# 4) Put your Ping/ICMP rule after the Scoring Services
move rulebase security rules "ALLOW_SCORING" after "ALLOW_LAN_SERVICES"

# 5) Put your Internal User Outbound rule towards the bottom
move rulebase security rules "ALLOW_INTERNAL_OUT" after "ALLOW_SCORING"

commit
```

### Rule Order:
1. `BLOCK_RED_TEAM`
2. `BLOCK_ALL_IPV6`
3. `ALLOW_LAN_SERVICES`
4. `ALLOW_SCORING`
5. `ALLOW_INTERNAL_OUT`

### IMPORTANT delete permit/base rules:
```bash
# Names of base rules may differ so verify before deleting
delete rulebase security rules "Permit Outbound"
delete rulebase security rules "Permit Inbound"
```

# Extras:


**Adding new attacks to block list:**
```bash
configure

# change name to something memorable but new like "RED_IP_1"
set address "RED_IP_NEW" ip-netmask <Attacker_IP>

# add new ip name to addr group
set address-group "RED_TEAM_BLOCKLIST" static [ RED_IP_PH RED_IP_NEW ]

commit
```

**View Logs:**
```bash
# general traffic
show log traffic direction equal backwards

# identified threats
show log threat direction equal backwards

# exit with Ctrl + c
```

**Review rules:**
```bash
show rulebase security rules
```

**Set logging on rule:**
```bash
# extra security rule parameters need to be set depending on the rule
set rulebase security rules "YOUR_RULE_NAME" log-end yes
```

**Show zones:**
```bash
show interface logical
```

**Rename a rule:**
```bash
# Example
rename rulebase security rules "ALLOW_NISE_PING" to "ALLOW_SCORING_ICMP"
```

**How to remove rules:**
```bash
delete rulebase security rules "ALLOW_LAN_SERVICES" application ping
```

**Access GUI through web:**
[`https://172.20.242.150`](https://172.20.242.150)

**System resources:**
```bash
show system resources
```

## Backup Config:

```bash
# 1. Save a pre-snapshot:
CLI: save config to 1015-PRE-NAT.xml
GUI: Device > Setup > Operations > Save named configuration snapshot


# 2. Make changes then see:
CLI: show config diff
GUI: Click Commit (top right) -> Preview Changes.

# 3. Commit to push changes and then repeat steps:
commit

---

# 1. Load previous snapshot:
CLI: configure -> load config from 1015-PRE-NAT.xml
GUI: Device > Setup > Operations > Load named configuration snapshot

# 2. Commit changes from loading config and then repeat steps:
commit
```

#

| Situation | Action | Command |
| :---- | :---- | :---- |
| **Active Hack** | Kill Session | clear session all filter source \<IP\> |
| **Network Down** | Rollback | load config version last-commited |
| **Scoring Offline** | Check Logs | show log traffic |
| **CPU Lag** | Check Health | show system resources |

#

| Action: | Command: |
| :---- | :---- |
| **List all saved backups** | dir config (Run in standard prompt \>) |
| **Save a restore point** | save config to \<name\>.xml (Run in \# mode) |
| **Delete a bad/old backup** | delete config saved \<name\>.xml (Run in \>) |
| **Compare current vs active** | show config diff (Run in \>) |
| **Roll back to start of round** | load config from running-config.xml then commit |

#

| Port | Protocol | Usage | Vulnerability |
| :---- | :---- | :---- | :---- |
| **20/21** | FTP | File Transfer | Cleartext, easy to sniff. |
| **22** | SSH | Remote Mgmt | Brute-force, key theft. |
| **23** | Telnet | Remote Mgmt | **NEVER USE.** Cleartext. |
| **25** | SMTP | Email | Open relays, spam. |
| **53** | DNS | Name Res | DNS Tunneling, Poisoning. |
| **80** | HTTP | Web | Cleartext, SQLi, XSS. |
| **110** | POP3 | Email | Cleartext (as discussed). |
| **443** | HTTPS | Web | Encrypted (needs SSL Decryption). |
| **445** | SMB | File Share | EternalBlue, Ransomware. |
| **3389** | RDP | Remote Desktop | BlueKeep, brute-force. |
| **4444** | Metasploit | Shell | Common default for Red Team. |
