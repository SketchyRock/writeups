# writeups

Retrospectives and reference notes from the cybersecurity competitions, makeathons, and conferences I take part in. The retrospectives are written for myself first: what happened, what went wrong, and what I'd change. The reference notes are cheat sheets I used mid-competition.

Each file is one Markdown document with YAML front matter, so the repo can be read by a person, parsed by a script, or pulled into my portfolio site without extra processing.

## Contents

### 2025

| File | Event | Result |
|---|---|---|
| [`icpc.md`](2025/icpc.md) | ICPC regional, Virginia Tech | ~50th percentile, 5 solved |
| [`jmus-makeathon.md`](2025/jmus-makeathon.md) | JMUS Makeathon | No placement |
| [`summit-ctf.md`](2025/summit-ctf.md) | Summit CTF, Virginia Tech | 9th of ~35 |
| [`vmi-cyber-fusion.md`](2025/vmi-cyber-fusion.md) | VMI Cyber Fusion | 1st |

### 2026

| File | Event | Result |
|---|---|---|
| [`maccdc-qualifiers.md`](2026/maccdc-qualifiers.md) | MACCDC qualifiers | Advanced to regionals |
| [`maccdc-regionals.md`](2026/maccdc-regionals.md) | MACCDC regionals, UMD | Low uptime, lots learned |
| [`jmu-blue-team-mock.md`](2026/jmu-blue-team-mock.md) | JMU Blue Team Mock | Club event |
| [`vmi-cyber-fusion.md`](2026/vmi-cyber-fusion.md) | VMI CyberFusion 2026 | 1st overall |
| [`vmi-cyber-fusion-platform.md`](2026/vmi-cyber-fusion-platform.md) | Overview of the CTF orchestrator built for it | Project write-up |
| [`rvasec15.md`](2026/rvasec15.md) | RVASEC15 conference | Contacts and one pending offer |
| [`echoes-makeathon.md`](2026/echoes-makeathon.md) | JMU Makeathon, Fall 2026 | 3rd |
| [`palo-alto-reference.md`](2026/palo-alto-reference.md) | Palo Alto firewall cheat sheet for MACCDC | Reference |

The Echoes code lives in its own repo: [SketchyRock/echoes](https://github.com/SketchyRock/echoes).

## Conventions

Files live in a folder named for the year of the event and are named for the event in lowercase with hyphens. There are no date prefixes, since the date is in the front matter.

Every document starts with this front matter. Only `title`, `type`, `category`, and `tags` appear on every file; the rest are included when they apply.

| Field | Meaning |
|---|---|
| `title` | Display title, same as the H1 |
| `type` | `retrospective`, `reference`, or `project-writeup` |
| `category` | `ctf`, `cyber-defense`, `competitive-programming`, `makeathon`, or `conference` |
| `event` | Name of the event |
| `date`, `end_date` | ISO dates (`YYYY-MM-DD`). Some entries only have a month (`YYYY-MM`) |
| `location`, `organizer`, `role`, `format`, `team` | Context about the event |
| `result` | Placement or outcome in one line |
| `tags` | Lowercase, hyphenated keywords |

The body has one H1 matching the title, then plain prose with `##` headings for the main sections. Retrospectives stay short and honest. Reference notes lead with commands.

## Adding an entry

1. Create `<year>/<event-name>.md` with the front matter above.
2. Write the H1, then what happened, then what I'd change.
3. Add a row to the table in this README.
