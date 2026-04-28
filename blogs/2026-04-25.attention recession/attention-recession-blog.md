<!--
PRE-PUBLISH CHECKLIST:
1. [DONE 2026-04-25] Tobi Lütke memo wording verified against Yahoo Finance reporting (https://finance.yahoo.com/news/shopify-ceo-tells-employees-prove-105933498.html). Quote trimmed to a two-sentence excerpt; full quote available if a longer pull is preferred.
2. [DONE 2026-04-25] Cal Newport quote from Deep Work verified by user.
3. [DONE 2026-04-25] Previous "importance of technical writing" post link substituted: https://medium.com/@kundansen/the-importance-of-technical-writing-d584f780a7ea
4. [DONE 2026-04-25] OpenClaw post link substituted: https://www.linkedin.com/pulse/its-10-oclock-do-you-know-where-your-agents-kundan-sen-t6sne/

ALL PRE-PUBLISH TODOS RESOLVED. The piece is ready to paste into Medium.
-->

# The Attention Recession
## Production exploded, consumption collapsed, and Newport's prescription stopped working. Here's what I'm trying instead.

*9 min read*

---

### The Question I Couldn't Answer

It was the usual rhythm for our internal AI show-and-tell: a Zoom, gallery view, thirty or so tiles, half the cameras off. We run the program across teams every couple of weeks, the same demo in name only, since the art of the possible keeps acquiring new shiny toys to walk through. Each gathering of like-minded folks gets a slightly different show. This week I was the one sharing my screen. I walked through emails written in seconds, an ADR that would have taken a careful afternoon, a design doc with diagrams I hadn't drawn, and one of those elaborate posts on Jive and Confluence that used to be a weekend's labor. Reactions popped in the chat, the energy was good, and I was genuinely impressed with the tools, not pretending otherwise.

Then a hand went up in the participants panel. The question that stayed with me for weeks came from someone I respect, asked without theater:

> *"What's the point of creating all of the documentation automatically when we no longer have the capacity to read any of the docs, and the reader will most likely send their AI agent to read and summarize?"*

I gave the kind of answer you give when you don't have one. Something about layering. Something about the volume problem being real but solvable. I watched the polite tile-nod you give on Zoom when you've registered that the speaker hasn't answered. I closed the laptop thinking about it. The next morning I was still thinking about it. I am still thinking about it now.

### We Used To, Now We

You know the feeling. We used to capture meeting minutes only for the meetings that mattered, because writing minutes was a tax and somebody had to pay it. Now Zoom Intelligence captures every detail of every conversation. Including the throat-clearing. We used to write design docs to a bare minimum because writing was slow, and the slowness was a forcing function on what you actually included. Now ADRs arrive with diagrams, scenarios, and prose that reads like it had a copy editor. Library and infrastructure docs, the long-running joke of our profession, have genuinely never been better, and I want to honor that, because the README that used to say "TODO: write README" is, in many repos, a small work of patient teaching.

That is the production side. The consumption side is where the math stops working, since everyone is busy creating. I often find myself running two or three Claude Code windows at once, watching them grind in parallel, glancing across to make sure none of the agents have wandered into a drawer they shouldn't be in. We are producing more code than we ever did, and we have less time than we ever did to read what got produced. Tobi Lütke's "AI baseline" memo last year reframed all of this from trend to mandate: at Shopify, AI fluency became a performance criterion, not a personal preference.

> *"I don't think it's feasible to opt out of learning the skill of applying AI in your craft. Stagnation is almost certain, and stagnation is slow-motion failure."*
>
> Tobi Lütke, Shopify CEO, internal memo (April 2025)

The volume isn't a vibe. It is being measured.

What I didn't see clearly until that show-and-tell question is that the meta-reading is also drowning. It isn't only the docs in our own repos. New models drop every few weeks, and each one reshuffles the leaderboard you were already behind on. New agent harnesses. New agent-to-agent protocols, MCP and A2A and ACP, with their own specs to digest. Prompt-injection 0-days. System prompt leaks. [The OpenClaw fiasco](https://www.linkedin.com/pulse/its-10-oclock-do-you-know-where-your-agents-kundan-sen-t6sne/) landed in our inboxes in February and a lot of us stopped what we were doing for a week. The professional reading we do *about* the tools we use to produce the documents we can't read is also broken. The recession is everywhere we look up. There is no clean perch.

I should add the half-sentence I owe the long tail: documentation has never been better at the head of the distribution, where active maintainers use AI assist on widely-used libraries. It is not better in the unloved corners of every enterprise codebase, where it is about the same as ever, only longer.

### Fifteen Years Late to a Cultural Arc

YouTube has been the largest single share of US TV viewing since mid-2024, per Nielsen's "The Gauge." The biggest "TV network" in America is now a feed of mostly short, algorithmically-served clips watched on a couch by people of every age. That is mainstream household behavior, not generational behavior, and it is the punchline of a long arc that has been running for forty years: four-hour epics gave way to two-hour studio films, which gave way to one-hour prestige TV, which gave way to thirty-minute episodes, which have given way, on the same living-room screen, to clips measured in seconds. We watched it happen to film and television without much surprise. Documentation is fifteen years late to the same arc, and it is arriving at our writing desks now.

### The ADR That Used to Fit on a Napkin

When did the ADR get fat? If you came up after 2018 you have only ever seen the second one, and you will have to take my word for the first. Michael Nygard's original 2011 template was embarrassingly modest: five paragraphs in roughly STAR or PAR shape (context, decision, status, consequences), plus two C4 diagrams if you wanted to be thorough, and the whole thing fit on a printed page. Nygard's framing line, which I keep coming back to, was disarming:

> *"A few sentences, in a numbered sequence."*
>
> Michael Nygard, *Documenting Architecture Decisions* (2011)

The ADRs I read this quarter run eight thousand words. They have decision matrices, tradeoff tables, alternatives-considered sections that recap options nobody seriously argued for, three architecture diagrams in different abstraction layers, a risk register, and a glossary. They are, in their way, beautiful. They are also unread. The strange part is that the original ADR was already layered: a one-sentence status, a short context, a short decision. Skimmable on top, depth where you needed it. Somewhere along the way we stopped trusting the layering and started covering ourselves by writing every layer at full prose density.

### The File Already in Your Repo

What I missed about my own working life, until I sat with that audience question for long enough, is this. There is already a file in your repo that you wrote entirely for a non-human reader, and you wrote it without flinching. It is called `CLAUDE.md`, or `.cursorrules`, or `AGENTS.md`. You did not agonize over its prose. You did not run it past anyone. You wrote it the way you would write notes for a colleague who is fast, literal, and slightly forgetful, because that is exactly the colleague you were writing for. The recession isn't only happening to us. We have already started adapting; we just hadn't named what we were doing.

The named version of the same instinct is llms.txt, which Jeremy Howard and the Answer.AI group proposed in September 2024: a literal `/llms.txt` file at the root of a website, telling language models which docs are the canonical machine-readable versions. It is the documentation analog of robots.txt, except instead of telling crawlers to keep out, it tells readers which door to use. The formalized end of the same spectrum is GitHub's spec-kit, where the spec is the source of truth and code is one possible instantiation of it. Three artifacts, one trend: documents written, on purpose, for non-human readers, with humans authoring the intent on top.

What those three artifacts have in common, and what I am trying to apply more deliberately to my own work, is layered documents: a short, human-shaped executive summary at the top, written in prose, for the colleague who has thirty seconds; a structured machine-readable block underneath, in whatever shape the agent reading it will most easily metabolize; and full prose only where it is genuinely earned, in the places that need argument or narrative or dissent that cannot be compressed without losing the point. The summary is for the human who will not read the rest. The block is for the agent the human will probably send. The prose is for the moments when both of them need to slow down. I am not claiming this works. It is what I am trying.

One more thing, owed and quickly paid: this piece is not about AI as labor displacement, and I know that is the elephant in the room. Different piece, maybe.

### Newport Was Right About the Diagnosis

Cal Newport's *Deep Work* came out in 2016, and the diagnosis has held up.

> *"The ability to perform deep work is becoming increasingly rare at exactly the same time it is becoming increasingly valuable in our economy."*
>
> Cal Newport, *Deep Work* (2016)

Sustained attention is the scarce resource, and the workplace was already eroding it before any of this. The chapters on cognitive residue and shallow-work creep read, ten years on, like dispatches from a slightly earlier version of the same recession. He was not wrong, and I am not pretending he was.

The prescription is where I quietly part ways with him. *Retreat, batch, defend the deep block* was the right move for 2016, when the work itself still rewarded sustained attention in something like the old proportions. The work has changed. The artifacts I produce now have agentic readers as a substantial fraction of their audience, volume is mandated rather than chosen, and the half-life is shorter than it used to be. Withdrawal isn't available, and even where it is, it doesn't pay the same dividend. (Drew DeVault is the slow-craft engineering voice I am respectfully not following here, and I would rather name him than dodge the disagreement.)

So the consumer-side discipline I am trying isn't withdrawal. It is triage, layered reading, and trust calibration. Triage is the ruthless prior step: deciding what gets the careful read at all, and accepting that most things won't. Layered reading is the cousin of layered writing, executive summary first, then the structured block, then the prose only when the prose is doing work I can feel. Trust calibration is the weakest of the three and I want to ground it with a single concrete example: I trust the AI summary for a status update, because the worst case is I miss a name. I do not trust the AI summary for a postmortem, because the worst case is I miss the dissent that would have changed my mind, and dissent is the load-bearing content of a postmortem.

Which leads to the small list of places where this whole approach fails, and I want to name them rather than wave at them. Legal and compliance documents, where the words themselves are the artifact. Leadership decisions, where tone carries information that summary will erase. Onboarding, where the reader is exactly the person who cannot triage yet. Cross-functional alignment, where the disagreement is the work. And two failure modes that show up specifically when an agent is between you and the document: **loss of dissent**, where minority positions and hedges get regressed to the mean, and **hallucination of consensus**, where "two engineers argued for X, one for Y, one abstained" becomes "the team agreed on X" by the time it reaches you. The ADR is, in this sense, the worst possible document for an agent to read on your behalf. In a decision document, the dissent *is* the content.

The question isn't whether the recession is real, but which documents we still owe a human reader, and which ones we are quietly already writing for the agent.

### I Made the Case Once Already

I made the case for writing it down, in a [previous post on the importance of technical writing](https://medium.com/@kundansen/the-importance-of-technical-writing-d584f780a7ea). The case still stands. I have changed how I write, layered now, machine-block underneath, prose only where it is earned. When I read, I triage first, then layer, then calibrate trust by document type. The earlier argument hasn't been repudiated; it has been metabolized.

I wrote this for myself, mostly. You will probably summarize it. I have made my peace with that, and the only honest move I have left is to admit that the piece you are reading was structured, on purpose, for the way you are going to read it. The summary is at the top. The argument is in the middle. The dissent, as always, is in the prose.

---

*Further reading: Michael Nygard's "Documenting Architecture Decisions" (November 2011) remains the cleanest statement of the original form, including the "few sentences in a numbered sequence" framing. Cal Newport's *Deep Work* (Grand Central, 2016) is the foil for the diagnosis-versus-prescription split here. Nielsen's "The Gauge" has had YouTube as the leading share of US TV viewing since mid-2024. Jeremy Howard and Answer.AI proposed llms.txt at llmstxt.org in September 2024; GitHub's spec-kit is the formalized end of the same spectrum. Tobi Lütke's April 2025 Shopify memo named AI fluency as a performance criterion. Drew DeVault's "Please don't use AI to write documentation" (2023) is the slow-craft counter-position worth reading on its own terms.*

---

**Tags:** AI, Software Engineering, Technical Writing, Documentation, Productivity
