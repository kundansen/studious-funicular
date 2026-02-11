# AI Slop: The New Broken Windows

Broken Windows has become my Bad Wolf - the Doctor Who phenomenon where a phrase you'd never noticed suddenly appears everywhere. I hadn't heard the term until a few months ago; now it keeps surfacing in my reads and listens. Malcolm Gladwell references it often, including in his talk yesterday (a topic for another post).

AI slop, on the other hand, is a term that didn't exist for anyone until a few quarters ago. Now it's everywhere too.

I'm connecting the two to make a claim: AI slop in our code is the broken windows of our generation in the code empires we build. I don't have the answers - people much smarter than me are working on solutions. Read this as raising questions, and as an invitation. I'd love to hear via comments what you think we should do.

## The Theory in Thirty Seconds

In 1982, criminologists James Q. Wilson and George Kelling published an article in *The Atlantic* that would reshape urban policy for decades. Their thesis was disarmingly simple:

> "One unrepaired broken window is a signal that no one cares, and so breaking more windows costs nothing."

The theory drew on a 1969 experiment by Stanford psychologist Philip Zimbardo. He parked two identical cars - both with their hoods up and no license plates - one on a street in the Bronx, one in Palo Alto. The Bronx car was attacked within ten minutes. A family arrived first - father, mother, and young son - and removed the radiator and battery. Within twenty-four hours, virtually everything of value had been stripped. Then the random destruction began: windows smashed, parts torn off, upholstery ripped. Children used the car as a playground.

The Palo Alto car sat untouched for over a week. Same car, same signals of abandonment, different neighborhood. Then Zimbardo took a sledgehammer to it himself and smashed part of the windshield. Within a few hours, passersby were joining in. By nightfall, the car had been flipped upside down and utterly destroyed. The vandals in both locations, Zimbardo noted, appeared to be primarily respectable, well-dressed adults - not stereotypical criminals.

The lesson wasn't about neighborhoods or demographics. It was about *signals*. A single crack communicates abandonment. Abandonment invites further decay. Decay accelerates until the system collapses. The first broken window grants permission for the second.

## The Theory Enters Software

The broken windows metaphor found its way into programming through *The Pragmatic Programmer*, the 1999 classic by Andrew Hunt and David Thomas:

> "Don't leave broken windows unrepaired. Fix each one as soon as it is discovered. If there is insufficient time to fix it properly, then board it up… Take some action to prevent further damage and to show that you're on top of the situation."

Their warning was specific: **neglect accelerates rot faster than any other factor**. A clean codebase encourages clean contributions. A messy one signals that mess is acceptable.

Jeff Atwood, co-founder of Stack Overflow, expanded on this in his *Coding Horror* blog:

> "Programming is insanely detail oriented, and perhaps this is why: if you're not on top of the details, the perception is that things are out of control, and your project will eventually spin out of control. Maybe we should be sweating the small stuff."

Robert Martin (*Clean Code*) framed it as entropy: systems naturally drift toward disorder unless energy is constantly applied to maintain them.

Malcolm Gladwell helped bring the theory to mainstream audiences through *The Tipping Point*, where he used it to explain New York City's dramatic crime drop in the 1990s. He later revisited the concept in his *Revisionist History* podcast, auditing his own earlier claims. The theory has since appeared in management books, leadership seminars, and countless blog posts about organizational culture - anywhere the question of "small signals, big consequences" applies.

The advice seemed timeless. Fix small problems before they become big ones. Maintain standards. Don't walk past the graffiti.

## The Velocity Problem

I want to pause and ask something uncomfortable:

**What happens when the windows break faster than you can possibly fix them?**

The broken windows theory assumes a stable building with occasional damage. A window cracks, you repair it, order is restored. The ratio of new damage to repair capacity stays manageable.

That's not the world we're living in anymore.

## The Obvious (Wrong) Answer

When code quality slips, the instinct is to slow down. More code review. Stricter linting. Approval gates. Mandatory pair programming. If the windows keep breaking, add more inspectors.

This worked reasonably well when humans wrote all the code. The bottleneck was typing speed and cognitive load. A senior engineer could review a junior's output and catch the cracks before they became structural.

We've crossed a threshold.

These agentic coding systems - Claude Code, Codex, Cursor, Amp in YOLO mode - don't just autocomplete. They generate entire modules, refactor across hundreds of files, write tests, run them, fail, fix, and iterate. A single developer can now produce in hours what used to take teams weeks.

The code isn't necessarily *bad*. Much of it is cleaner and better-documented than what stressed humans produce under deadline pressure. But the *volume* has changed by orders of magnitude.

If you're generating a thousand windows a day, how many inspectors do you need?

And before you suggest the obvious workarounds: sample-based review misses systemic drift - the patterns that only become visible across dozens of files. Stricter CI gates recreate the bottleneck you were trying to escape. Smaller changesets don't help when an agent refactors broadly by design. The traditional toolkit assumes human-scale output.

## Digging Deeper

AI-generated code differs from traditional broken windows in one critical way:

Traditional broken windows are **visible damage to existing structures**. You see the crack, you fix it. The graffiti appears on a wall that was already built.

AI slop is different. It's not graffiti on an existing building. It's **graffiti embedded in the bricks as they're being manufactured**. By the time you see it, it's structural. The wall was built with the crack already inside.

By slop, I don't mean syntax errors or failing tests - those are easy. I mean code that is locally plausible but globally unmoored: duplicated business logic across services, weak domain modeling, missing rationale, brittle edges that pass CI today but degrade the system's comprehensibility tomorrow. An agent might "improve" a module's style while quietly replicating validation rules that now exist in three places.

Detection and response look completely different in this world.

You can't walk through the neighborhood looking for broken windows when the neighborhood is being constructed around you as you walk. The traditional human-in-the-loop model - where a reviewer examines each change before it merges - becomes a bottleneck that defeats the purpose of the acceleration.

We're left with a choice: slow down to human review speed and lose the leverage, or ship faster and risk accumulating debt we can't see until it's load-bearing.

## A Counterpoint: Good Enough Is Good Enough

Before I propose solutions, I need to acknowledge something: not all windows need to be perfect.

I've written before about how motion beats perfection. The career escalator keeps moving whether you're ready or not. The latency between idea and implementation is where momentum dies. If you wait until every window is pristine before shipping, you'll never ship.

The Pragmatic Programmer itself makes this distinction - "board it up" is an acceptable temporary measure. Comment out the code. Throw a "Not Implemented" error. Acknowledge the crack, contain the damage, move on.

The question isn't "should we tolerate any broken windows?" The answer to that is obviously yes - we always have. The question is: **which windows matter?**

## A Different Architecture

I think the solution isn't more human inspectors. It's a different architecture entirely.

**Human above the loop, not in the loop.**

Instead of reviewing every line, set the constraints. Define the architectural guardrails. Establish the patterns. Then let the agents build within those boundaries - and let *other* agents review their work.

The human role shifts from line-by-line inspection to system-level judgment:

- Does this module belong in this service?
- Does this abstraction make sense for where we're headed?
- Is this the right trade-off between speed and rigor for this context?

**Agents reviewing agents.**

If AI can generate code, AI can review it. Linting, security scanning, architectural conformance - these can run continuously, at machine speed, without human fatigue or inconsistency. The human reviews the aggregate: trends, exceptions, anomalies.

The key is giving agents something to review *against*. Machine-checkable intent changes everything. Write the specification first - not as documentation, but as an executable contract - then let agents generate code that conforms to it. Review becomes validation against intent rather than line-by-line inspection. Tools like GitHub's Spec Kit and Spec Kitty are building exactly this workflow. The spec is the blueprint; the code is just one possible instantiation.

**Disposable code as a feature, not a bug.**

A heretical thought: if we can regenerate code as easily as Kubernetes respawns a crashed pod, does legacy code mean what it used to?

The old fear was that bad code would calcify into permanent architecture. But if the cost of replacement drops low enough, maybe the right response to a broken window isn't repair - it's demolition and rebuild.

We already think this way about infrastructure. Cattle, not pets. Immutable deployments. Burn it down and spin up fresh.

What if code becomes the same? Not precious artifacts to preserve, but ephemeral expressions of intent that can be regenerated when the intent changes or the implementation rots?

## New Questions This Opens

I don't have clean answers yet. I have better questions:

- **What's the new definition of technical debt?** If code is disposable, debt might shift from "code we need to fix" to "understanding we failed to capture." The danger isn't the bad implementation - it's losing the *why* behind the good one.

- **Who owns the windows now?** When agents generate the code and other agents review it, accountability becomes diffuse. The human sets the intent. The system executes. Who's responsible when the intent was clear but the execution was subtly wrong?

- **What skills matter in this world?** Maybe the discipline isn't fixing broken windows anymore. Maybe it's knowing which buildings to tear down. Architectural judgment. System-level taste. The ability to recognize when regeneration is cheaper than repair.

## The Uncomfortable Truth

The broken windows theory was always about *signals*, not windows. The crack in the glass wasn't the problem - it was what the crack *communicated*. Abandonment. Indifference. Nobody's watching.

With AI-generated code, the signal has changed. A hundred imperfect files don't necessarily mean nobody cares. They might mean someone cared enough to ship quickly, knowing they could rebuild later.

The new broken window might be something else entirely: **a system without clear intent**. Code without context. Architecture without rationale. Generated output disconnected from the human judgment that should have shaped it.

Maybe that's what we should be policing now. Not the cracks in the glass - but the absence of a blueprint.

---

*Further reading: The original broken windows article by Wilson and Kelling appeared in The Atlantic in March 1982. The Pragmatic Programmer by Hunt and Thomas was first published in 1999, with a twentieth anniversary edition in 2019. Malcolm Gladwell popularized the theory in The Tipping Point (2000) and later revisited it in his Revisionist History podcast. Robert Martin's Clean Code (2008) frames the problem as entropy. GitHub's Spec Kit and Spec Kitty tools explore specification-driven code generation.*


