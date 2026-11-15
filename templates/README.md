# Writing a new entry

1. Copy [`retrospective.md`](retrospective.md) (or [`reference.md`](reference.md)) to `<year>/<event-name>.md`. Use the year of the event, and a lowercase hyphenated name with no date prefix.
2. Fill in the front matter and write the body. The comments in the template describe the voice.
3. Run `python3 scripts/build_index.py`. It validates the front matter, rebuilds the index in the root README, and regenerates `index.json`. `--check` validates without writing.

## Front matter

| Field | Meaning |
|---|---|
| `title` | Display title, same as the H1 |
| `type` | `retrospective`, `reference`, or `project-writeup` |
| `category` | `ctf`, `cyber-defense`, `competitive-programming`, `hackathon`, or `conference` |
| `event` | Name of the event |
| `date`, `end_date` | `YYYY-MM-DD`. Use `YYYY-MM` (quoted) when the day is unknown |
| `location`, `organizer`, `role`, `format`, `team` | Context, only when it applies |
| `result` | Placement or outcome in one line |
| `tags` | Lowercase, hyphenated keywords |

Required on every document: `title`, `type`, `category`, `event`, `tags`. Retrospectives also need `date` and `result`.

## Body

One H1 matching the title, then the `[← All write-ups](../README.md)` link, then plain prose with `##` headings for the main sections. Retrospectives stay short and honest; reference notes lead with commands.
