# Return of the (Builder as) King

*March 7, 2026*

Two things churned their way through my reading pipeline this week. The first was Anthropic's research paper on AI's labor market impacts, a careful, data-heavy study measuring the gap between what AI *could* automate and what it *actually is* automating right now. The second was Malcolm Gladwell's *Revenge of the Tipping Point*, his quarter-century return to the mechanics of how small minorities drive enormous outcomes.

I read the Anthropic paper with a dozen browser tabs open and Gladwell's book folded back on the desk beside me. By the time I finished both, the same shape had formed in my head twice, a tiny minority driving an outsized share of the outcome. The collision of these two produced a question I haven't been able to shake: if the productivity gains from AI are concentrating in a fraction of the tech workforce, what does that mean for how the rest of us should spend our working hours?

The answer keeps pointing in the same direction. Build, prototype, architect. Use AI to rubber-duck your way through a design problem, to stress-test an idea, or to form your thoughts with more rigor than you could alone. The people thriving in this moment share one ideal. They make things, they tinker, and they bring their curiosity A-game.

### Stedman's highway

In *Revenge of the Tipping Point*, Gladwell tells the story of Donald Stedman, a chemist at the University of Denver who built an infrared contraption to measure car emissions on the highway. Stedman sat on the roadside and watched. Most cars flashed *good*. A rare few flashed *poor*. Those few, just 5% of vehicles, were producing 55% of Denver's automobile pollution.

Gladwell calls this the "Law of the Very, Very, Very Few." It shows up everywhere. In a British COVID challenge study, 86% of all detected virus particles came from just two out of thirty-six volunteers. In crime data, single-digit thousands of individuals drive the majority of violent incidents in cities of nine million. The distribution is, as one Los Angeles study put it, "extremely skewed."

Anthropic's labor market research reveals a version of this same skew playing out across the economy. Their new metric, dubbed "observed exposure," tracks what AI is *actually doing* to jobs based on usage data, rather than what it could theoretically do. The gap between those two numbers is enormous. Computer and math occupations show 94% theoretical exposure, yet only a fraction of that shows up in practice. The revolution has a long theoretical reach and a short actual grip.

Within that grip, the gains concentrate even further.

### The connectors, the mavens, and the rest of us

Gladwell's original *Tipping Point* introduced three archetypes for how ideas spread: Connectors (people with vast social networks), Mavens (information specialists who accumulate and share knowledge), and Salesmen (persuaders who make ideas stick). A social epidemic tips when the right combination of these few carries a message into the mainstream.

The AI adoption curve in technology follows a remarkably similar structure. The Mavens of the AI era — roughly 10% to 14% of the tech workforce — have restructured their entire workflow around AI collaboration. They experiment relentlessly, prompt iteratively, and use AI for complex system planning rather than simple autocomplete. A year-long study tracking 300 software engineers at a single enterprise illustrates the power law at work: the top 30 highest-adoption users saw a 61% increase in committed code volume. The bottom 30 — same tools, same organization, same managers — experienced an 11% *decline*. These Mavens are the super-emitters of productivity. They save 30+ minutes a day. Casual users save less than 10. Over months, that gap becomes a career chasm.

A 2025 study on AI prompting practices found something counterintuitive that captures the Maven mindset perfectly:

> *"Higher AI skill levels correlate with more exchanges per task, rather than fewer. Maximally proficient users require substantially more interactions because they use AI to tackle significantly more ambitious, complex problems."*

The best practitioners go deeper, not faster. They treat AI as a sparring partner, not a vending machine.

What makes them extraordinary goes beyond time savings. These are people whose brains have always been full of ideas — prototypes they sketched on whiteboards, architectures they debated over coffee, solutions they *knew* were right — who lacked the resources to execute. Resourcing bottlenecks, skill gaps in adjacent domains, prioritization treadmills, just life happening. Cal Newport calls this the "adjacent possible" — innovation happens at the edges of your current competence, in the territory you can almost reach. AI collapsed the distance. Mavens are now building functional prototypes in hours instead of waiting months for a sprint slot. They compress design thinking cycles from weeks to an afternoon. They fluidly convert legacy codebases — entire systems calcified in languages nobody wants to maintain — into modern tech stacks with complete rearchitecture. They tackle massive tech debt problems that sat unsolved for a decade because nobody could justify the engineering investment. The adjacent possible just got a *lot* more adjacent.

Then come the Connectors — engineers and technical leads who spread AI-native practices across teams, establishing "Golden Paths" and reference architectures that help others adopt with discipline. They multiply the Mavens' gains by encoding them into organizational muscle memory.

The Salesmen are the leaders who frame AI around revenue growth and capability expansion rather than cost-cutting. BCG's data shows that when AI is positioned as a cost-reduction tool, only 50% of companies hit their targets. Frame the same capabilities around growth, and the success rate jumps to 63%. The framing determines whether an organization freezes or moves.

Below these three groups sits the majority of users that still experiments sporadically, bolting AI onto legacy habits rather than rethinking the work itself. The encouraging part: Gladwell's Few show up in this story twice. The Mavens use AI with discipline and compound the gains. The next group I'm about to describe — the super-emitters of damage — use it carelessly and flood the system with slop. Both adopted early and both crossed the threshold of engagement, which means the gap between them is discipline, not willingness — and discipline can be taught through better prompting habits, stronger architectural guardrails, and structured review practices.

### The Stedman problem

Every super-emitter story has a mirror image. Stedman's 5% of cars were actively poisoning the air for everyone else. The AI workforce has its own version.

The cultural phenomenon of "vibe coding" — prompting an AI to generate working logic without deeply inspecting what comes out — has created measurable code degradation. GitClear's analysis of over 150 million lines of code found that copy-pasted code surged 48%, while code refactoring collapsed by 60%. A Veracode study found 45% of AI-generated code fails standard security tests. Daniel Stenberg, the creator of cURL, put it bluntly: "AI slop is DDoS-ing open source." Maintainers are drowning in pull requests that look superficially correct yet contain deep logical flaws.

Laura Tacho, CTO at DX, captured the broader pattern in her 2025 research:

> *"AI exposes organizational flaws rather than fixing them. If systemic constraints are not addressed before scaling AI, organizations simply carry them into space with us."*

The critical insight is that these super-emitters of damage are also early adopters, engaged with the tools yet lacking the architectural discipline to wield them well. The antidote is the same thing that creates AI productivity: structured building, where architects define strict reference paths and engineers understand what generated code is *doing*, not just that it compiles. The Stedman problem gets solved with precision, not by treating every car on the highway as equally guilty.

### The Word-Excel-PowerPoint trap

If you work in technology and your daily tools are primarily Word, Excel, PowerPoint, Outlook, and a calendar full of status meetings, you have the clearest opportunity to reclaim leverage. You also have the least time to wait.

Over the past decade, a quiet drift occurred. Experienced, well-compensated tech professionals migrated away from building. They stopped writing code, stopped reviewing architectures, and stopped debugging production systems. They became information routers — consolidating updates, formatting reports, synthesizing meeting notes, managing Jira backlogs. The drift was gradual enough that it felt like career progression.

AI performs every one of those tasks faster and cheaper. Managers spend up to 40% of their time on documentation and administrative work. GenAI reduces that load by 35% to 45%. Dr. Nicole Forsgren, lead researcher behind the DORA metrics, put it sharply:

> *"AI operates as an accelerator of existing friction."*

If your organization's developer experience is plagued by slow CI pipelines, convoluted deployments, and poor documentation, AI-equipped developers simply crash into those bottlenecks 10 to 100 times faster. The "frozen middle," the management layer where 88% of technically successful AI pilots stall, resists adoption for rational reasons. Middle managers use AI at higher rates than senior leaders. They understand the technology well enough to recognize that fully adopting it means automating the coordination work that justifies their compensation.

Boston Consulting Group's "10-20-70 Rule" frames the escape route: 70% of AI's value comes from redesigning how people work. Only 21% of companies actually do this. Organizations that break through frame AI as a building tool, not a headcount optimizer. Individuals who break through do the same, picking up a prototype, spinning up a proof of concept, or getting their hands back on the material of their craft.

The escape hatch from administrative drift has always been the same door: **START BUILDING AGAIN**.

### New chairs at the table

When administrative coordination shrinks and developer productivity climbs, something interesting happens. Budget and headcount open up for roles that previously couldn't be justified. The displacement conversation tends to focus exclusively on what disappears. The creation side deserves equal airtime.

AI QA Strategists, professionals who orchestrate test generation, edge-case validation, and security oversight rather than writing manual scripts, now command a 20-40% salary premium. AI Decision Designers sit between algorithms and business outcomes, shaping how automated systems make high-stakes calls in fraud detection, lending, and compliance. AI Ethics and Compliance Officers audit systems for bias, enforce data privacy, and navigate global regulations like the EU AI Act. Gartner predicts 60% of enterprises will establish AI ethics boards by the end of 2026.

Karat's 2026 survey of 400 engineering leaders found that 73% now say strong engineers are worth at least 3x their total compensation — a sharp jump since 2023 driven entirely by AI leverage. The profile of "strong" has shifted too: companies care less about whether a candidate can write a sorting algorithm from memory and more about how they think *with* AI. Firms are redesigning interviews around open problems solved with AI coding agents, then asking for the chat session transcript to evaluate the candidate's reasoning, their ability to steer the model, and how they handle hallucinated outputs.

The roles of the future reward people who build, verify, and govern. The administrative middleman role — the one that existed to route information between people who build and people who decide — is the one quietly emptying out. That shift opens new seats at the table and raises a harder question: who gets enough reps to grow into them?

### The pipeline question

Anthropic's study surfaced one finding that deserves more attention than it received. While overall unemployment rates for AI-exposed workers show no meaningful change, the *hiring rate* for workers aged 22 to 25 into exposed occupations has dropped roughly 14% since late 2022. The signal is faint, but it is consistent with a much louder trend.

Entry-level software development positions have declined 60% since 2022. Salesforce announced it would hire zero new software engineers in 2025. Stanford researchers documented a 20% employment drop for developers aged 22-25 in just three years. Some companies are pivoting their strategy entirely: replace traditional coding interviews with AI-collaborative assessments where candidates solve open-ended problems alongside AI agents, then submit the chat session for review. The hiring screen is shifting: solve this open-ended problem with AI as your partner, then show us the chat session so we can evaluate how you *think*.

We have seen the pipeline problem before. When the construction industry shed nearly a million workers during the 2008 recession, it stopped training apprentices. The pipeline never recovered. Today the industry is short an estimated 499,000 workers to meet baseline demand.

If the "very, very few" power users are doing the work of entire teams, and companies respond by eliminating junior roles, who forges the next generation of builders? As one veteran architect put it:

> *"You do not learn how to keep a platform standing by reading documentation or copying AI-generated output. You learn it by being on call when a site goes down during a product launch, or by discovering how a shortcut taken six months ago is now breaking three other systems."*

No amount of AI-generated boilerplate substitutes for that kind of learning. Senior architects develop through years of breaking and rebuilding systems alongside experienced engineers.

This one is solvable, through intentional apprenticeship models, AI-paired mentoring, and companies that recognize the pipeline as a design problem rather than an inevitable collapse.

### Return of the builder king

Gladwell ends *Revenge of the Tipping Point* with an observation that has been rattling around in my head since I read it: "The day when we could use broad-brush solutions to complicated problems is over."

The AI era in technology confirms this. Blanket hiring freezes, org-wide mandates with no workflow redesign, and treating every role as equally exposed — all of these miss the deeply skewed nature of what is actually happening. A small number of builders are achieving extraordinary things while a small number of reckless practitioners degrade code quality for everyone, and a large middle drifts through administrative work that AI will happily consume. New roles are emerging for those willing to learn how to build, verify, and govern in this new world.

The path forward is specific: pick up a prototype, use AI to rubber-duck a design decision, build a small application that solves a problem you have been PowerPointing about for six months, or stress-test an architecture with an AI sparring partner instead of scheduling another review meeting.

The builders, the people who maintain the tacit knowledge of how systems actually work, are the ones writing the next chapter. AI gives them a forge they have never had before. The question for everyone else in technology is simple and ancient and suddenly urgent again: ***what are you building?***

---

*Further reading: Anthropic's labor market research was published in February 2026 at <http://Anthropic.com/research/labor-market-impacts>. Malcolm Gladwell's Revenge of the Tipping Point (2024) extends his original Tipping Point (2000) framework into super-spreaders and social engineering. Cal Newport explores the adjacent possible in So Good They Can't Ignore You (2012). The METR study on developer productivity was published in early 2025. GitClear's code quality analysis covers 150 million lines across 2024-2025. BCG's 10-20-70 Rule appears in their 2025 AI transformation research. Dr. Nicole Forsgren's DORA findings are from her 2025 keynote. The DeputyDev longitudinal study tracked 300 engineers over 12 months through 2024-2025. Karat's engineering leadership survey was published in early 2026.*
