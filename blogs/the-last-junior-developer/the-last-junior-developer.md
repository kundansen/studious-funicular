# The last junior developer

## How we removed the struggle from software engineering, and why we'll regret it

*12 min read*

---

I remember my first weeks as a fresh developer straight out of undergrad school, as Engineer Kundan Sen, eager to take on the world and yet as naive as someone who had never seen a production outage, at Vedika Software in Kolkata. I was handed over "Core Java Volume 1," a nearly 1000-page monster, and asked to finish at least most of it before asking for more work. It was the late 1990s, prehistoric in today's terms. My classmate-turned-colleague and I spent weeks reading through page after page (they were physical books) until we were ready to face the challenges of the senior devs and "earn our place on the developer bench."

When I was finally given a bug ticket, it read, in its entirety: *"Race condition in the caching layer. Sometimes returns stale auth tokens."* 

For the first 2 weeks, I didn't write code. I opened the repository, a monolithic sprawling codebase that had outlived four dev leads, and traced the execution path with a notepad. I searched for documentation that didn't exist. I set up a local environment, which involved hunting down a specific version of a forgotten database dependency that only one senior engineer knew how to install. When I finally found the problem, I wrote fifteen lines of code, opened a pull request, and was promptly ripped apart by a staff engineer for breaking a boundary context I didn't even know existed.

Years later, at a different firm with modern tooling, we did this again with a proof-of-concept. I was handed a vague directive to test a new message broker. I spent four days wrestling with our internal CI/CD pipelines, fighting the VPN, and configuring Docker. By Friday, I had a working prototype and a headache, and was desperate to get back to playing Grand Theft Auto 8-bit color instead of reading one more line of Core Java. 

Or consider pair programming. Two junior developers, placed in a room, staring at a terminal, blindly stumbling through blind spots together. We made terrible architectural decisions. We reversed them days later when the system buckled under load.

None of this was fast. From a productivity standpoint, it was disastrous. But that two-week slog to fix a caching bug wasn't an inefficiency. It was the exact mechanism by which a junior developer built a cognitive map of the system. 

&nbsp;

Now meet the class of 2026.

Raj graduates from a top CS program and joins a Series B startup. On day one, he prompts an agentic framework to digest the company's codebase. By lunch, he has an architectural map that took his predecessor three months to build mentally. By end of week, he has deployed a feature. His manager calls him a "10x hire." Six months later, a cascading failure hits production at 2 AM, the agent hallucinates a fix that corrupts the database, and Raj stares at a stack trace he has never had to read without assistance.

Maria, a hiring manager at a mid-size consultancy, quietly removes the two junior developer positions from next quarter's headcount. One senior engineer with an agentic crew now covers the workload. The math is obvious. What is less obvious is that she has also removed the pipeline that would have produced her next senior engineer.

Deepak, a bootcamp graduate, "vibes" his way through his first year. Agent-generated code, agent-generated tests, agent-generated pull requests. His performance reviews are stellar. Then a client asks him to whiteboard a system design in a room with no laptop. He draws two boxes and a line. The room goes quiet.

## The compression

That old pipeline no longer exists. 

A newly hired junior developer today, equipped with an agentic orchestration framework, does not spend two weeks reading code. They do not trace execution paths on a notepad. They prompt a tool like LangGraph or Claude Agent to digest a three-million-line repository. In minutes, the agent returns a complete architectural map, pinpoints the undocumented race condition, and drafts the necessary fifteen lines of code.

Spec-kits have eliminated the crucible of environment setup. You don't hunt down obscure database dependencies; you ask MetaGPT or AutoGen to construct the Dockerfile, write the configuration, and spin up the container. When it's time to test the message broker, the agent writes the CI/CD pipeline, generates the integration tests, and opens a pull request that will likely pass review because the agent already cross-referenced the company's style guide.

What used to represent a month of grueling, disorienting work now takes a few hours. The productivity gains are staggering. A savvy junior dev with agentic coding tools exits their first month at a firm with an output that rivals a mid-level engineer with three years of tenure. Tasks that would previously span entire Jira epics are resolved before lunch. 

The numbers confirm the shift. Entry-level software engineering job postings have dropped between 45% and 67% from their 2022 peaks, and actual hiring for junior roles has declined even faster, with some analyses reporting a 73% drop. Internship postings are down 30%. The industry is not gradually phasing out the junior role. It is amputating it.

A ledger exists here, and the bill is coming due. We are wiping out an entire phase of career development.

## The loss of resistance

Malcolm Gladwell popularized the psychological concept of "desirable difficulties" in *David and Goliath*. The term, originally coined by psychologists Robert and Elizabeth Bjork, refers to the counterintuitive idea that introducing struggle into a learning process actually strengthens long-term retention. 

Ancient Indian educational tradition reached this conclusion thousands of years earlier. The concept of ***Tapas***—literally "heat" or "burning"—was considered the primary requirement for knowledge acquisition. It was the belief that true wisdom was not merely heard, but forged through the internal fire of discipline and toil. They spoke of ***Shrama*** (exertion) as the necessary antidote to the brittleness of superficial information. In the Vedic tradition, learning progressed through three stages: *Śravaṇa* (hearing the word), *Manana* (the intense, often painful intellectual struggle of thinking through the concept), and finally *Nididhyāsana* (the internalization where the knowledge becomes part of one's being). 

If you learn a concept smoothly and effortlessly, your brain discards the information almost as quickly as it acquired it. It feels like learning, but it is an illusion of fluency. When you introduce resistance, when you force someone to retrieve information, wrestle with confusion, or fail repeatedly, the brain builds durable, structural connections. Through *Manana*—the "wrestling"—information is tempered into ***Vidya***: embodied, lived knowledge.

K. Anders Ericsson's research on deliberate practice reinforces this. Expert performance requires three conditions: a task at the edge of competence, informative corrective feedback, and repetition with correction. The old junior pipeline satisfied all three. The new one, where an agent handles the task and the junior reviews the output, satisfies none. You cannot practice at the edge of competence when the tool has already solved the problem for you. Without the heat of *Tapas*, the mind remains soft.

In software engineering, the desirable difficulty was the grunt work. The grueling process of mapping a legacy codebase by hand built a structural understanding of how state transitions fail. The misery of configuring a CI pipeline taught you how deployment actually works under the hood. 

We automated more than the typing. We automated the struggle itself. 

By removing the "grunt work," we removed the low-stakes environment where junior developers safely failed. This was an apprenticeship masquerading as a job. The junior developer produced almost no business value, but the business tolerated the inefficiency because it was the only way to manufacture a senior developer capable of handling production-ending crises five years later.

Now, the agent removes the struggle. The code works. The pull request merges. The junior developer moves on to the next ticket, having achieved the outcome without enduring the process. The cognitive map is never built.

## The judgment deficit

This matters because the role of human engineers is fundamentally shifting. Adam Grant has written extensively on how AI alters the landscape of knowledge work. As AI becomes adept at generating content (whether that is prose, analysis, or code) the human premium moves away from creation and toward curation and judgment. 

Grant argues we must adopt the mindset of a scientist. If the AI is generating hypotheses in the form of code, the human must design the experiment, evaluate the results, and decide whether the thesis holds water. 

Scientific evaluation requires deep domain intuition. How do you review a complex event-driven architecture proposed by an AI if you have never felt the pain of a distributed system failing in production? How do you recognize a subtle security flaw in a generated authentication module if you never spent two weeks hunting down a race condition?

Judgment is the residue of corrected mistakes. 

AI, by making us immediately successful at the point of creation, deprives us of the mistakes. 

The industry is already feeling this shift. Hiring managers are quietly pulling up the ladder, prioritizing senior engineers who can wield AI as a force multiplier over junior developers who require mentorship. The logic is economically sound in the short term: why hire three juniors when one senior with an agentic crew can out-produce them?

Moreover, there is a deeper structural problem: companies that invest in junior development are subsidizing their competitors. The junior you train for two years leaves for a 40% raise. AI makes this worse. If a junior with agents produces senior-level output, their market value inflates faster, and they leave sooner. Training juniors has become a collective action problem, and no individual company has an incentive to solve it alone.

The long-term risk is a talent desert. If we stop manufacturing senior engineers today, we face architectural collapse within a decade. The systems we built with AI need maintenance, scaling, and debugging. The engineers tasked with that work have relied on AI for their entire careers. When the automation inevitably hallucinates or fails to comprehend a novel scaling constraint, the humans in the loop lack the fundamental, grit-forged intuition required to save the system.

Medicine understood this long ago. Doctors do not skip residency because they have AI diagnostic tools. They still do rounds, still get grilled by attending physicians, still make mistakes on patients under supervision. The medical profession recognized that competence requires supervised struggle, and that no amount of AI-assisted accuracy can replace the judgment built by seeing hundreds of cases go wrong in person. Software engineering is the profession that decided to skip residency.

## The new junior is a team lead

We are simultaneously expecting juniors to think like senior architects while removing the developmental pipeline that teaches them how.

Here is the paradox nobody prepared for. The junior developer of 2026 is expected to operate like a three-to-five-year veteran from day one.

Because AI compresses the ramp-up, the expectations compress with it. A junior who can prompt an agentic framework to digest a codebase, generate a working feature, and open a clean pull request within a week has, on paper, the output profile of a mid-level engineer. Organizations begin treating them like one. They assign them a small pod of agents, or a mixed team of agents and contractors, and ask them to deliver outcomes, not tickets.

This means the skills that matter for a junior are no longer "can you write a for-loop" or "do you understand polymorphism." The skills that matter are: can you unblock a team? Can you decompose a vague product requirement into clear, delegatable instructions? Can you evaluate whether the architecture your agent proposed is scalable and sustainable, or whether it solves today's problem while creating tomorrow's outage?

AI accelerates development. It does not turn a bad architecture into a well-coded application. It cannot make a non-programmer into a great programmer. The code compiles, the tests pass, and the system collapses under load six months later because nobody asked whether the data model could handle concurrent writes at scale.

The thinking required has jumped several rungs of the traditional career ladder. A junior developer today needs the instincts of a team lead: give clear instructions, delegate with responsibility, review with skepticism, and focus relentlessly on whether the system works rather than whether the code runs. The craft has shifted from writing code to shepherding systems, and the junior who thrives is not the one who prompts fastest but the one who thinks most clearly about what should be built and why.

## The counterargument, and why it's incomplete

The optimistic case is worth stating honestly: AI *is* the new apprenticeship. Juniors learn faster with AI. They see more patterns, encounter more codebases, and iterate more rapidly than any previous generation of developers. The cognitive map builds differently, not worse.

A real truth exists here. A junior who uses an agent to explore five architectural approaches in an afternoon has been exposed to more design patterns than a 1990s junior would see in a year. Exposure is real. Speed is real.

What is missing is consequence. The 1990s junior who chose the wrong architecture lived with it for months. They debugged the cascading failures. They explained the outage to their manager. They felt the weight of a decision that cost the team two sprints of rework. That weight is what converts exposure into judgment. You can show someone five architectures in an afternoon, but if the agent picked the right one and the junior never felt the cost of the wrong one, the lesson is academic. It is information without scar tissue.

## Rebuilding the crucible

We cannot put the automation back in the box. Deliberately ignoring agentic frameworks is professional malpractice. But we must fundamentally rethink what we do with junior developers.

If the technology removes the resistance, the organization must reintroduce it intentionally.

This means changing how we review code. When an agent generates a solution, the junior developer needs to defend the architecture. They need to be asked, specifically, and aggressively, what alternative approaches the AI discarded, and why the chosen path is superior. The human must become adversarial to the machine.

It means carving out "no-flight zones" for onboarding. Giving a new hire an agent and telling them to deploy a feature isn't onboarding; it's delegating. Start them on tasks where the AI is turned off. Force them to trace the execution path. Let them struggle with the pipeline. Make them fail in a sandbox before you give them the tools to succeed effortlessly in production.

If I had a junior developer sitting across from me today in Kolkata, at the same desk where I once stared at page 400 of Core Java Volume 1, I would still hand them something heavy. Not the same book. But something that resists easy answers, something that makes them sit with confusion long enough for the understanding to root. Maybe a failed system design. Maybe a production postmortem with the names redacted and the logs intact, and an instruction: figure out what went wrong before you open any tool. 

The grunt work was never about the work.

It produced the engineer.

Our tools have evolved to the point where they can bypass the struggle entirely. If we want engineers who can fix the systems of tomorrow, we have chosen a dangerous process to optimize away.

---

*Further reading: Malcolm Gladwell explores "desirable difficulties" in David and Goliath (2013), a concept originally developed by Robert and Elizabeth Bjork (1992) to describe how struggle improves long-term retention. K. Anders Ericsson’s seminal 1993 paper, "The role of deliberate practice in the acquisition of expert performance," establishes the framework for skill mastery through focused repetition and corrective feedback. Adam Grant’s Think Again (2021) argues for adopting the "mindset of a scientist" when navigating complexity. The ancient Indian educational tradition, documented in the Upanishads and Vedic texts, describes the necessity of Tapas (discipline) and Shrama (toil) in the transition from information to Vidya (embodied wisdom).*

**Tags:** artificial intelligence, software engineering, career development, developer tools, agentic frameworks
