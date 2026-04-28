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

---

## Idea 6: The Fluid Intelligence Cliff

**Working title:** *The Fluid Intelligence Cliff (Or: Why AI Threatens the Wrong People)*

**Book hook:** Arthur Brooks, *From Strength to Strength*

Brooks argues that fluid intelligence (raw processing speed, novelty, pattern-matching) peaks around 30 and then declines — while crystallized intelligence (wisdom, synthesis, judgment-from-experience) keeps compounding into your 60s. His career advice: stop competing on fluid, start leveraging crystallized.

**The AI angle:** AI is maximally good at fluid intelligence tasks — novel code generation, pattern matching across thousands of examples, rapid iteration. It's poor at crystallized intelligence — knowing when a rule doesn't apply, recognizing the smell of a system that will fail in ways that don't show up in tests yet.

This creates a brutal inversion: AI doesn't threaten the 55-year-old architect who spent decades accumulating scar tissue. It threatens the 28-year-old who was betting on out-processing everyone with raw cognitive speed. The people who thought fluid horsepower was their moat just had their moat filled in.

For senior engineers who've already made the Brooks transition? AI is the great equalizer — they finally have a fluid-intelligence engine to pair with their crystallized wisdom. For the bright junior who assumed they'd grind their way to seniority through sheer throughput? The ladder just got much steeper.

**Topics to cover:**
- Brooks' fluid vs. crystallized intelligence arc — not a decline story, a transition story
- AI capability profile: exceptionally strong at fluid tasks (generation, pattern-matching, novelty), weak at crystallized tasks (judgment, context, knowing when the rules don't apply)
- The conventional wisdom is wrong: senior engineers are not the ones most threatened
- The 28-year-old who bet on raw horsepower — this is the person who should be worried
- The complementarity angle: crystallized wisdom + AI fluid engine = the most powerful combination in the room
- What "investing in crystallized intelligence" looks like deliberately — the kinds of experiences that build it (and which ones AI short-circuits)
- The career advice Brooks never got to give: in an AI world, the transition from fluid to crystallized work should happen earlier, not later

**Why this is un-mined:** Every AI-and-careers piece focuses on "will AI take my job." This reframes it as "which *kind* of intelligence are you building, and does AI help or hurt that?" Counterintuitive, uncomfortable, hopeful for one group and challenging for another.

---

## Idea 7: The Wrong Kind of Noise

**Working title:** *We Fixed the Wrong Problem (The Noise Edition)*

**Book hook:** Daniel Kahneman, *Noise* (2021)

The thesis: we obsess over bias (systematic error in one direction) but ignore noise (random variation in judgment). Two radiologists examine the same X-ray and give different diagnoses. Two judges see the same case and deliver wildly different sentences. Same input, wildly different outputs. Kahneman's finding: noise causes as much damage as bias, possibly more, and is almost never measured.

**The AI angle:** AI was supposed to eliminate noise — same input, same output, always. And it does. But it may be replacing random human noise with locked-in, at-scale systematic error. Your hiring manager was noisy — some days they favored candidates who reminded them of themselves, some days they didn't. Your AI resume screener is consistent — it's just consistently wrong about the same candidates, at 10,000-applications-a-day scale.

Kahneman's insight about noise is that it's *invisible* — you only see individual decisions, not the distribution. AI's locked-in errors are even more invisible, because the consistency reads as confidence. We replaced variance with certainty. Certainty about the wrong thing.

**Topics to cover:**
- Kahneman's distinction between bias and noise — why noise gets ignored (it's invisible in individual decisions, only visible in aggregates)
- The audit of noise in traditional knowledge work: code review, hiring, performance evaluation, incident triage — all deeply noisy, rarely acknowledged
- AI's actual promise: consistency. Same input, same output. Noise eliminated.
- The trap: eliminated variance ≠ eliminated error. We may have frozen in the bias and turned it up to 11.
- The organizational seduction: consistency feels like rigor. Deterministic outputs feel trustworthy. The audit trail exists. This is more dangerous than noise, not less — because it's harder to detect.
- What "noise audits" looked like before AI (Kahneman ran them with judges, doctors, insurers) and what the equivalent would look like for AI systems
- The counterintuitive recommendation: for some decisions, engineered noise (diverse reviewers, random assignment) might be the right answer even in an AI world

**Why this is un-mined:** Everyone writes about AI bias. Nobody writes about AI's relationship to *noise* — which is the actual subject of Kahneman's second, underread book. The "we eliminated noise but locked in error" frame is genuinely novel.

---

## Idea 8: Default to Truth

**Working title:** *Default to Truth (And Why That's Killing Your Judgment)*

**Book hook:** Malcolm Gladwell, *Talking to Strangers*

Gladwell's central claim: humans are wired to "default to truth" — we assume people are honest unless overwhelmed by contrary evidence. This isn't stupidity, it's adaptive. The cost of treating every stranger as a liar is catastrophically high; the cost of occasionally being fooled is low. We're calibrated for a world of humans who bear social costs for deception.

**The AI angle:** We're applying our truth-default to a system that bears no social cost for being wrong. AI produces maximally fluent, confident, authoritative prose. Our brains process fluency as credibility — documented, not controversial. We're applying a trust mechanism that evolved for humans-who-can-be-embarrassed to outputs from a system that cannot be embarrassed.

This is why AI hallucinations feel so betraying — not just wrong, but *wronging*. Gladwell's insight about why intelligent people keep getting fooled by con artists applies directly: the betrayal isn't a failure of intelligence, it's a mismatch between our trust calibration and the entity we're trusting.

**Topics to cover:**
- Gladwell's "default to truth" mechanism — why it's adaptive, not stupid, in a human context
- The specific cognitive mechanism: fluency → credibility. We've known this since the 1970s.
- Why AI is maximally fluent: RLHF optimizes for responses that feel right, not responses that are right
- The no-skin-in-the-game problem: humans who lie bear social costs; AI bears none. Our truth-default evolved for the former.
- Why AI errors feel like betrayal — and why that emotional response is the *right* diagnostic signal
- What a "calibrated skepticism" practice looks like for AI — not paranoia, but situational skepticism based on the type of claim (factual vs. structural vs. reasoning)
- The institutional version: teams that have defaulted to truth at scale — and the failure modes that revealed it

**Why this is un-mined:** "AI hallucinates" is everywhere. "Our evolutionary truth-default makes us systematically bad at detecting AI errors — and here's the precise mechanism" is not.

---

## Idea 9: The Micro-Interruption Tax

**Working title:** *The Micro-Interruption Tax (What Tab-Complete Did to Your Thinking)*

**Book hook:** Cal Newport, *Deep Work*

Newport's 2016 argument: deep work (cognitively demanding, distraction-free, sustained) is increasingly rare and increasingly valuable. His villain was Slack — the always-on communication layer that shattered 4-hour focus blocks into 8-minute fragments.

**The AI angle nobody's taken:** AI coding assistants may be doing to flow states what Slack did to deep work — just more invisibly. Flow state requires complete immersion in a problem. But tab-complete means every two sentences, you evaluate a suggestion. Accept or reject. Continue. Every 15 seconds, a micro-decision about someone else's proposed completion of your thought.

Newport's research on task-switching wasn't about big interruptions — it was about *attention residue*, the cognitive tail that follows even brief context switches. When you reject a tab-complete suggestion, you've still briefly inhabited an alternative path. That residue accumulates.

The uncomfortable question: AI coding tools have demonstrably increased output metrics — lines committed, PRs merged, tickets closed. Have they measured what happened to the *quality* of thinking that preceded the output? Increased throughput, degraded depth.

**Topics to cover:**
- Newport's attention residue concept — even brief task switches leave cognitive tails
- Flow state requirements: the psychological literature on what creates and breaks it
- The tab-complete loop as a 15-second interruption cycle — not Slack-scale, but continuous
- Output metrics vs. thinking quality metrics — why we measure one and not the other
- The paradox: AI tools make engineers more productive by the metrics that matter to managers and less deep by the metrics that matter to engineers
- What "deep work with AI" looks like deliberately — using AI in bounded sessions rather than continuous suggestion mode
- Newport's "any benefit" fallacy applied to AI: we adopt tools because they have some benefit, not because the net benefit is positive

**This isn't anti-AI** — it's about naming the specific cognitive cost that nobody measures, so practitioners can make the tradeoff consciously.

---

## Idea 10: The Specification That Never Says No

**Working title:** *Epistemic Cowardice at the Architecture Level*

**Book hook:** Adam Grant, *Think Again*

Grant's epistemic cowardice concept: giving deliberately vague answers to avoid conflict or controversy. The scientist updates their beliefs; the preacher defends them; the prosecutor attacks others'. Grant argues most people in organizations operate as preachers or prosecutors, rarely as scientists — because updating your belief publicly looks like weakness.

**The AI angle:** AI models are the ultimate epistemic cowards. They're trained to hedge, to say "it depends," to present multiple perspectives without advocating one. A model asked "is this architecture correct?" produces a thorough exploration of tradeoffs and a non-answer. This isn't a bug — it's the training objective. But it has infected how engineers write specifications.

The spec that lists every feature and no constraints. The architecture doc that presents three options with equal-weight pros and cons. The PRD that says "the system should handle high load" without defining "high." Technical cowardice — the refusal to commit to a falsifiable claim — has always existed. But AI, which confirms whatever you bring to it and generates balanced-sounding hedges on demand, has made epistemic cowardice frictionless.

Real expertise is the willingness to say *no, not this* — not the ability to generate a comprehensive exploration of why both options have merit.

**Topics to cover:**
- Grant's scientist/preacher/prosecutor framework — why scientists are rare and why organizations suppress them
- Epistemic cowardice: the vague answer that protects the speaker but fails the decision
- What an actually good specification does: makes falsifiable claims, defines what the system should NOT do, commits to a tradeoff
- AI's contribution: generates balanced, hedged, non-committal output by training objective — this is now the template engineers are learning from
- The organizational amplifier: AI cowardice + conflict-avoidance culture = specifications that commit to nothing
- What "epistemic courage" in engineering looks like: the ADR that says "we chose X and will not support Y," the spec that defines the out-of-scope, the architecture review that ends with a decision
- The connection to the Specification Gap: not just that engineers can't specify, but that the combination of AI tools and organizational dynamics has made *not specifying* feel like thoroughness

**Note:** This connects to Idea 3 (Specification Gap) but approaches from Grant's angle — the *psychological* mechanism (cowardice, identity protection) rather than the structural one (production bottleneck vs. decision bottleneck). Could be a companion piece or a merged angle.

---

## Cross-cutting notes (updated)

The newer ideas follow a complementary structural tension: **a cognitive mechanism that evolved for human-scale interaction is now being applied at AI scale, and the mismatch is invisible until it's catastrophic.**

- Fluid Intelligence Cliff → Brooks' transition insight applied to AI: the wrong demographic is worried
- Wrong Kind of Noise → Kahneman's second insight: we eliminated variance, may have locked in error
- Default to Truth → Gladwell's trust mechanism: calibrated for humans-with-stakes, misapplied to AI-without-stakes
- Micro-Interruption Tax → Newport's attention residue: output up, depth down, nobody measuring the latter
- Epistemic Cowardice → Grant's scientist frame: AI makes hedging frictionless, specs commit to nothing
