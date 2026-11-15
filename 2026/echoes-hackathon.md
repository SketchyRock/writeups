---
title: "JMU Hackathon, Fall 2026"
type: "retrospective"
category: "hackathon"
event: "JMU Hackathon"
date: 2026-11-13
end_date: 2026-11-14
format: "24-hour hackathon"
prompt: "Break out of your comfort zone"
team: "David Hilscher, Luke Bonnell, Curtis Linweaver, me"
result: "3rd place"
repo: "https://github.com/SketchyRock/echoes"
tags: [hackathon, pitching, product, echoes]
---

# JMU Hackathon, Fall 2026

[← All write-ups](../README.md)

We built Echoes: anonymous voice notes pinned to real places on campus. You can only hear or record one by standing at the spot. Popular ones become Legends, and some point to real clubs and events.

We placed third. We went in expecting first, because we had a full working demo that everyone in the room could open on their phone and use at the same time. We still came third.

## What we did

The prompt gave us a problem that is easy to say badly. Nobody can break your comfort zone for you, so we did not promise friendships. Our pitch was "you help us help you": the student takes the step, and the app makes that step smaller. To hear an echo you have to go somewhere. To post one you only have to talk, anonymously. Replies and "open doors" point at clubs and events that already exist.

I came up with the idea and wrote the outline. David and I ran most of the presentation and coordination and decided what needed to be built. Luke built almost all of the demo (a Go backend and a React frontend with a satellite map). Curtis helped us shape the idea and the presentation. The research changed how we pitched it. The core mechanic, geo-locked audio, already exists in other apps, and two of them are even called Echoes. So the outline names them and says what is different: Legends, open doors, warm replies, and guardrails learned from Yik Yak.

## What I learned

**The idea was about 90% of the work.** Once we had it, getting the app running and the presentation built was the rest. That split is fine, but it means the idea has to be settled early and be good enough to carry everything else.

**Put the effort into the demo, not the backend.** People remember the demo. It needs to be simple, make sense, work, and prove the idea does what we say. A complex backend or anything very technical does not need to exist. It can be explained. Next time we spend more time polishing the demo and the presentation and less on a fleshed-out app.

**Get the whole idea across.** This is the problem I had in the last two hackathons, and I think it is the most important one. The pitch should make sure the judges understand the full idea before it spends time on marketing and business details. We had those details ready, and they are the part to cut first.

I don't know exactly why we were third, and I have no judge feedback. My guesses: geo-locked audio is not new, we had no proof it helps, and our answers on moderation and an empty map at launch were plans and not things we had tested. A working demo that everyone could use at once did not win it alone.
