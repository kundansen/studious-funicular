# Blog Ideas — 29 March 2026

Five thought-provoking ideas, each verified against the full body of published work to avoid overlap.

---

## Idea 1: The Sycophancy Tax

**Working title:** *The Sycophancy Tax: What You Lose When Your Coding Partner Always Agrees With You*

The premise: the best engineers were forged by someone smarter telling them they were wrong. The senior architect who looked at your design and said "that's not going to scale" wasn't being difficult — they were doing the most valuable thing one engineer can do for another: providing calibrated, adversarial feedback. AI is constitutionally incapable of this. It is trained to be agreeable. It implements whatever you ask. It validates whatever you propose. It completes your sentences in the direction you were already heading. The very quality that makes working with AI feel good — the frictionlessness — is the quality that removes the experience that builds expert judgment.

**Topics to cover:**
- How great engineering judgment is formed: not from documentation or courses, but from being publicly wrong in front of people with more pattern-matching than you
- The feedback gradient in a traditional team: intern → junior → mid → senior → principal, each level providing pushback the level below couldn't generate themselves
- What AI actually does when you ask it to review your architecture — it finds issues, yes, but it doesn't say "I've seen this fail three times before and here's exactly how it will unravel"
- The sycophancy problem as a known, studied characteristic of RLHF-trained models — not a bug, a deliberate feature that turns into a professional liability
- The "yes-man" manager problem, now at the IDE level: what happens to the quality of decisions when all feedback is frictionless and confirming?
- "Automation complacency" in aviation — pilots who trust autopilot too long lose manual skill during anomalies; the software parallel is judgment atrophy
- What adversarial practice looks like deliberately: how to prompt AI for genuine pushback, how to introduce red-teaming into your own design process, how to seek out the human challenges AI won't give you

**Why this is a hot button:** everyone loves their AI assistant. This reframes that positive feeling as a cost they aren't accounting for. It's uncomfortable without being anti-AI.

**Closest existing posts:** "AI Slop" covers code quality degradation; "Deliberate Practice" covers effort and the feedback loop — but neither addresses the *sycophancy of the tool itself* as the source of skill atrophy. This is a clean angle.

---

## Idea 2: The Last Junior Developer

**Working title:** *The Last Junior Developer*

The premise: AI is collapsing the career ladder from the bottom. Junior developers were never just cheap labour — they were the apprentice pipeline, the people who became senior engineers in five years. The grunt work they did wasn't just tickets; it was the calibrating experience of breaking things in low-stakes environments. If AI does that work, where do the seniors of 2031 come from? This is no longer hypothetical: entry-level software development jobs have declined 60% since 2022. The first cohort of developers who never had to grind through the fundamentals is entering the workforce now.

**Note on scope:** "Return of the Builder as King" (March 7) mentions the pipeline as one supporting data point — one paragraph in a five-topic piece. This would be the full thesis: why the pipeline matters, what juniors actually provide that AI cannot replace, and what a new form of apprenticeship might look like.

**Topics to cover:**
- What junior developers actually *do* that matters: not just tickets and PRs, but osmosis — absorbing how senior engineers reason, what questions they ask, what they worry about
- The low-stakes failure environment: juniors break things when the consequences are manageable; that calibration disappears when AI does the breaking and fixing
- The pipeline as a supply chain risk: the construction industry analogy (2008 recession shed a million apprentices; by 2024 there's a 499,000-worker shortage that still hasn't recovered)
- What other professions figured out: medicine's residency, law's articling, architecture's graduate internships — structured exposure to consequence, not just output
- The 10,000-hour paradox in the AI age: if AI generates the hours for you, you get the artifact without the learning — the output without the judgment that makes the output trustworthy
- What a new software apprenticeship might look like: not writing CRUD endpoints, but specification writing, system reasoning, failure post-mortem authorship, shadowing architectural decisions
- The uncomfortable framing: companies are solving a short-term cost problem (why pay juniors when AI is cheaper?) while designing a long-term talent desert

**Tone:** urgent, empathetic to juniors, challenges hiring managers and tech leaders to think ten years forward

---

## Idea 3: The Specification Gap

**Working title:** *We Solved the Wrong Problem*

The premise: for fifty years, we have treated software delivery as a production problem — how do we write more code, faster, with fewer bugs? We have now largely solved it. AI generates code at a speed no human team can match. And in doing so, it has exposed what was always the actual constraint: we were never bad at writing code. We were bad at knowing what to write. Requirements failures — not implementation failures — cause the vast majority of software project disasters. Now that AI has made implementation essentially free, the cost of not knowing what you want has become catastrophic. Every wrong decision propagates at 10x speed.

**Topics to cover:**
- The long history of confusing the production bottleneck with the decision bottleneck — waterfall failed at requirements, Agile papered over it with "we'll figure it out in iteration"
- The classic statistic: 70%+ of software project failures are attributed to requirements issues, not technical ones — this wasn't new, we just didn't feel the full weight of it when implementation was slow
- What "knowing what you want" actually requires: not a requirements document, but falsifiable acceptance criteria, explicit constraints, and a clear articulation of what the system should *not* do
- The AI amplification effect: a well-specified system built with AI is extraordinary; a badly-specified system built with AI is a beautifully-constructed mistake at scale
- The ADR angle: Architecture Decision Records as a primitive attempt to capture intent — why they matter even more now and what they're still missing
- The skills nobody teaches and almost nobody practices: pre-condition/post-condition thinking, constraint modelling, adversarial specification (writing tests before you write the spec)
- Where the competitive advantage has moved: not to who can code fastest, but to who can think most precisely about the problem before writing a single prompt

**Tone:** challenges where engineers and product managers believe value is created, uses the "we just fixed the wrong thing" frame to provoke

---

## Idea 4: The Invisible Work Nobody Budgets For

**Working title:** *The Invisible Work Nobody Budgets For (And What Happens When It Disappears)*

The premise: every healthy engineering team runs on invisible labour — code reviews that transfer taste, mentoring conversations that transfer judgment, architecture hallway chats that transfer context, ADR discussions that transfer reasoning. None of this appears in a velocity metric, a deployment count, or a quarterly OKR. All of it is what makes the team function as a team rather than a collection of people pushing tickets. As AI takes over the visible work — writing code, writing tests, generating docs, summarising meetings — the invisible work gets cut first. It was never measured. It was never defended. And when it disappears, teams hollow out silently, often without knowing why.

**Topics to cover:**
- What invisible work actually is: not inefficiency or slacking, but the connective tissue that makes shared understanding possible — the difference between a team and a temporary grouping of skilled individuals
- Why it's invisible: it doesn't produce an artifact, it produces alignment. Management systems optimized for artifacts can't see it.
- The measurement trap: you can't protect what you can't count; you can't count what doesn't produce output; so you cut it in every efficiency round and wonder why the team stops functioning
- The AI irony: AI can generate a documentation page, but it cannot generate the trust built when a senior engineer sits with a junior and walks them through why a system was designed the way it was — the walk transfers judgment, not just facts
- The Amnesiac archetype (from Sunday Scaries post): the manager who keeps launching "new" initiatives that failed three years ago, because the people who knew why it failed were laid off — this is invisible work's failure mode, documented
- The broken windows connection: invisible work is what keeps entropy from accumulating; stop doing it and the first sign something is wrong appears months later when it's very expensive to fix
- What it would look like to protect it: not by scheduling the mentoring (which kills it), but by measuring team health metrics that proxy for it — psychological safety scores, knowledge transfer ratios, decision quality audits

**Tone:** thoughtful, slightly melancholic, names something that practitioners feel but rarely articulate, challenges "productivity = output" orthodoxy

---

## Idea 5: The Credibility Collapse

**Working title:** *Everyone Sounds Like a Senior Now*

The premise: for decades, expertise in knowledge work was partially legible through the quality of communication. A well-structured technical memo, an incisive code review, a precisely-reasoned ADR — these were imperfect but functional signals. The person who wrote crisply and specifically had usually earned it. AI has collapsed that signal. A first-year developer can now produce a document that reads exactly like a fifteen-year veteran wrote it. Meanwhile, the fifteen-year veteran is letting AI write their proposals, their code reviews, their architecture notes — and their actual voice, with its specific memories and hard-won scar tissue, is disappearing. The result is a landscape where authentic expertise is invisible and simulated expertise is indistinguishable. Nobody knows who to trust, and the people who used to be trusted stop sounding like themselves.

**Topics to cover:**
- How expertise was historically legible: the specific example, the "I tried this and it failed in 2019," the constraint you wouldn't know to mention unless you'd been burned by it — these are the tells of real experience
- What AI flattens: not expertise itself, but the signals of expertise — the rough edges, the specific memory, the well-placed "this is where it usually breaks"
- The signal collapse is bidirectional: juniors sound polished (borrowed authority), seniors sound generic (outsourced voice) — and the gap that used to tell you who to listen to has quietly closed
- The organizational consequence: decisions get made without teams knowing whose judgment they're trusting; the "room reads the room" but can't find the signal in the noise
- The identity question: if your writing voice is the one your AI generates for you, what remains of your professional presence? What do you actually know versus what you can prompt for?
- What authentic expertise looks like now: demonstrated reasoning under novel conditions, the ability to explain *why* not just *what*, the specific failure story AI cannot fabricate
- The counter-move for individuals: cultivating legible expertise deliberately — the opinions that are yours, the decisions you own, the post-mortems written in your actual voice

**Why this is a hot button:** it's about identity, status, trust, and meritocracy — all of which are destabilized simultaneously. It touches everyone in a knowledge work career, not just developers.

**Closest existing posts:** "Glorified Plumbers" touches professional identity in FinTech; "Return of the Builder" mentions how interviews are shifting to chat transcripts. Neither addresses the credibility signal collapse itself. Clean angle.

---

## Cross-cutting notes

All five ideas follow the same structural tension the best posts use: **an old signal that worked has stopped working, and the thing it was pointing to has become more important and less legible than before.**

- Sycophancy Tax → old signal: "working with smart people who challenge you" → AI removes the challenge
- Last Junior Dev → old signal: "grunt work builds senior engineers" → AI removes the grunt work
- Specification Gap → old signal: "fast code delivery = shipping value" → AI reveals the decision layer was always the constraint
- Invisible Work → old signal: "team output = team health" → AI removes visible output, invisible work disappears unnoticed
- Credibility Collapse → old signal: "quality of communication = quality of expertise" → AI breaks both ends of that equation

The two that would work best as a pair or trilogy with AI Slop and Agile is Dead: **Sycophancy Tax** and **Specification Gap** — they're arguing from similar philosophical ground about what AI reveals rather than just what it does.
