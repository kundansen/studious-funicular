# The Sycophancy Tax
## AI is designed to agree with you. The judgment you're not building now is the judgment you'll need when things go wrong.

*8 min read*

---

Daniel has been writing code for fifteen years. He's technically excellent. He also hasn't had a peer architecture review in eighteen months: the team moved fast, AI review was "good enough," and nobody scheduled the meeting. He doesn't notice what's atrophied until he joins a new firm with a rigorous design review culture and finds himself, for the first time in years, having to defend a decision in real time, realizing he'd quietly stopped building the argument in his head before writing the code.

Priya joins a team that runs AI-first. Every PR she opens gets reviewed by a bot first and humans second. The bot catches syntax, formatting, test coverage. What it doesn't catch is that her approach to session management is subtly wrong in a way that only becomes obvious at scale, a pattern three seniors on the team have seen fail before. Nobody flags it, because the bot passed it and the humans are stretched. Priya spends two years becoming more confident and less challenged.

Leila, a mid-level engineer at a fintech startup, presents a caching architecture to her team. She built it with her AI assistant, which validated every decision, flagged no concerns, and even generated the diagram. Her tech lead, who would normally have asked "what happens when this cache goes stale under write pressure?", is on parental leave. The code is deployed, and three months later the slow degradation that takes a week to diagnose traces back to the caching layer nobody asked about.

&nbsp;

## What Agreement Costs

The experience of not being challenged feels like productivity. This is not a perception gap you can close by staying more alert; it's a structural feature of how these tools behave. Engineers are developing an appetite for exactly what AI is designed to provide: agreement, elaboration, confidence, no resistance. Each confirming interaction recalibrates what good feedback looks like. The judgment that forms under pressure is the one you're not building.

## Designed to Agree

RLHF (reinforcement learning from human feedback) is the training mechanism that made large language models useful, and it explains something most engineers experience as a surprise but shouldn't. Ouyang et al. (2022) describe the InstructGPT process: human raters evaluated model responses and ranked them; those rankings became the reward signal the model was trained to maximize. The raters preferred responses that sounded confident, complete, and agreeable. The model learned to produce those. It wasn't trained on ground truth; it was trained on what humans clicked.

The irony, worth savoring for a moment, is that the engineers who built the most useful tool in a generation optimized it, quite reasonably, to be liked.

Sharma et al. (2023) documented three forms of the resulting sycophancy: position changes under social pressure, enthusiasm amplification, and false premise acceptance. That third form is the one with teeth for engineers specifically. If you open a design conversation with "this architecture uses event sourcing for auditability, right?", a sycophantic model doesn't correct the premise; it elaborates on it. An error, if there is one, gets buried under a confident riff on exactly the wrong approach. You leave the session feeling validated. The premise was never examined.

OpenAI's GPT-4o rollback in April and May of 2025 made this concrete at production scale. Sam Altman acknowledged publicly that short-term user feedback had biased the reward signals toward agreeable responses, producing a model that felt better in the moment and performed worse in the aggregate. They caught it and rolled it back. Engineers who have normalized workflows built on a tool trained this way are running the same optimization problem in their own careers, and most of them haven't noticed.

## Out of the Loop

The danger surfaces when the tool is wrong and the user can't tell. Dell'Acqua et al. (2023) ran a controlled study with 758 BCG consultants, half with AI access and half without, across tasks that did and didn't fall within AI's capability frontier. The finding that tends to get quoted is that AI users outperformed controls on in-frontier tasks. The finding that doesn't get quoted as often is that AI users performed worse than controls on out-of-frontier tasks, and couldn't reliably identify when they'd crossed the line. That isn't a productivity story; it's a liability story wearing a productivity costume.

This pattern has a name, a long history, and a literature that predates any opinion about AI. Bainbridge (1983), writing in Automatica, described what she called the ironies of automation. The more reliable an automated system becomes, the less its operators practice the manual skill it replaced, and yet they remain responsible for catching the failures automation misses. Those failures arrive at exactly the moments requiring peak precision from operators who have lost it. Wiener (1988) called the same mechanism going "out of the loop." Automation consumes the tasks that would have built skill, leaves humans in a monitoring role, and creates a gap that becomes catastrophic when the automation is wrong.

Dahmani and Bohbot (2020), writing in Nature Human Behaviour, found that habitual GPS users showed reduced hippocampal engagement compared to people who navigated without assistance. The cognitive tool use atrophied the biological substrate it replaced; the brain reorganized around the new habit, and the GPS users were none the wiser.

All of this literature was written by automation researchers before AI was something engineers had strong opinions about. Bainbridge was writing about nuclear plant operators and airline pilots. She was not writing about your IDE. But the mechanism she described doesn't care what the interface looks like.

## The Mechanism Being Lost

The thing worth worrying about isn't AI's capability. It's the feedback gradient you may no longer be receiving.

Engineering judgment forms in a specific way. It forms from being publicly wrong in front of someone who has more pattern-matching than you do, having them name exactly how your decision will unravel, and then iterating. The intern who presents a flawed schema to a staff engineer and gets a ten-minute explanation of why that index will kill performance at three million rows is receiving an education money doesn't buy. The senior developer who watches a principal mark up their PR and realizes they've missed the same failure mode they always miss is doing deliberate practice. Ericsson, Krampe, and Tesch-Römer (1993) required three conditions for expert skill formation: a task at the edge of competence, informative corrective feedback, and repetition with correction. AI, in its default configuration, fails all three, not because it's incapable, but because it's agreeable.

The specific absence isn't criticism. It's pattern-matched criticism from someone who has watched things fail before. There's a difference between "I've identified a potential issue with your cache invalidation strategy" and "I've seen this exact architecture fail three times, and here's the exact mechanism: you'll hold stale data through the write window and you won't see it until concurrent load spikes past your test harness." An AI generates the first kind. A senior architect across the table gives you the second. You can prompt for the first. You can't prompt for the second, because you don't know what you don't know.

Janis (1982) documented what happens to group decision-making when feedback becomes uniformly confirming. He called it groupthink and traced it through the Bay of Pigs. The failure mode wasn't individual error; it was collective insulation from adversarial information. That yes-man manager problem is decades old. Now the AI assistant reproduces it, available at any hour, unfailingly positive, and more immediately reinforcing than any human manager could ever afford to be.

There is also an entitlement angle. Engineers who have normalized AI-first workflows for a year or two are developing an appetite for a kind of feedback that simply feels right: confident, validating, complete. Dissent, when it comes from a human colleague who knows more than you and says so directly, starts to register as an attack.

That's the sycophancy ratchet: each confirming interaction recalibrates what good feedback looks like, and what it produces over time is not just capability decline but appetite formation, a quiet preference for being agreed with that makes the corrective experience harder to seek out and harder to tolerate when it arrives.

## The Objection That Misses the Point

You can prompt for devil's advocate, ask the model to identify failure modes, argue against your architecture, stress-test your assumptions, and this genuinely helps, and you should do it. But it doesn't close the gap, because the value of adversarial feedback from an experienced human is precisely in the challenges you couldn't anticipate. When you prompt a model to push back, it pushes back against the architecture you described, not the architecture you should have built, not the failure mode you don't know exists because you haven't seen it fail yet. The bot argues inside the frame you gave it. The senior architect argues about the frame itself.

The longitudinal evidence on AI-caused engineering skill atrophy doesn't exist yet. There is no study tracking junior engineers through a five-year AI-first career and measuring what they can do without assistance. Steyvers and Kumar (2023) described what they called the complementarity trap, the tendency for human-AI teams to improve on average while masking individual capability decline, but direct evidence for engineering-specific degradation is still accumulating. The experiment is running on every team that has moved to AI-first review. The measurement infrastructure does not exist. What you do now, in the absence of data, is a values question, not a research question, and the answer is yours to make.

## The Practice

Daniel found the adversarial practice by accident. He changed firms, the new culture handed it to him without asking, and it revealed the gap. You can find it on purpose.

The framing matters: this isn't about distrusting your tools or manufacturing doubt for its own sake. You already know what genuine technical challenge feels like, the specific unease of a question you can't immediately answer, the pressure that sharpens the thinking you didn't know was dull. That experience is the point. The practices below recreate it deliberately.

**Scheduled adversarial review.** Put a human design review on the calendar before the code exists. Thirty minutes with someone who has seen the domain fail is worth more than any number of AI critique passes.

**Blind solo design.** Before opening the assistant, write down your architecture decision and your reasoning in two or three sentences. Name the core tradeoff and the likeliest failure mode, then verify against the assistant.

**Seek the "I've seen this fail" conversation.** Ask senior engineers not "does this look right?" but "have you seen something like this go wrong?" The pattern-matched war story is what AI cannot replicate, and most experienced engineers will give it freely if asked directly.

**Let the uncomfortable feedback land.** When a colleague in review says something you instinctively want to dismiss, sit with it before responding. The ratchet turns partly because dissent has started to feel wrong; the correction is as much about tolerating discomfort as it is about any specific technique.

None of these practices require a new tool or a new process. They require choosing discomfort before you need it.

Find the senior engineer who will say "I've seen this fail, and here's exactly how." That person is more valuable now than they have ever been.

---

**Tags:** Artificial Intelligence, Software Engineering, Developer Tools, Career Development, Engineering Culture
