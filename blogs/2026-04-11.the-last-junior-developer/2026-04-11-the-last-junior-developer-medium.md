# The Last Junior Developer

*April 11, 2026*

*Published on Medium: https://medium.com/@kundansen/the-last-junior-developer-4590a2f5e853*

## How We Removed the Struggle from Software Engineering (and Why We'll Regret It)

I spent my early career at Vedika Software in late 1990s Kolkata, where junior developers underwent demanding apprenticeships. A task as straightforward as debugging a race condition meant weeks of manual code tracing, careful environment setup, and learning through failure—a grueling but formative process.

Today's junior developers face a starkly different reality. AI agents can analyze entire codebases in minutes, generate working features within hours, and produce production-ready code that bypasses the traditional learning struggle entirely. Entry-level job postings have declined 45-67% since 2022. Internship postings are down 30%.

We've optimized our way into a crisis, and we're not talking about it.

## The Struggle Was the Point

For decades, we accepted that learning to code involved struggle. We called it "paying your dues." And while the phrase grates on the modern ear, the underlying principle was sound.

Psychologists call this "desirable difficulties"—the counterintuitive truth that struggle strengthens learning in ways ease never can. Ancient Vedic traditions understood this through *Tapas* (discipline) and *Shrama* (exertion) as prerequisites for wisdom. K. Anders Ericsson's research on expertise confirms it: mastery requires "tasks at the edge of competence, informative corrective feedback, and repetition with correction."

The grunt work was never about the work. It produced the engineer.

### What the Struggle Taught

When I spent three weeks understanding how our caching layer worked, I wasn't just learning caching. I was building intuition about trade-offs, failure modes, and the cascading consequences of a bad decision. I was developing judgment.

That judgment is invisible until you need it. It's the part of you that reads a code change and immediately thinks, "Wait—what happens when these two systems race?" It's the part that's already seen the failure mode, even if only in a previous context.

## The Judgment Crisis

By automating the struggle, we've removed the low-stakes environment where junior developers safely failed and built intuition about their own blind spots. They now produce senior-level output without developing senior-level judgment.

A junior developer using AI agents generates code that works. But when systems fail—when something has a race condition, or a concurrency bug, or a subtle memory leak—they lack the "scar tissue" from past mistakes needed to diagnose complex problems. They've never traced through a failed deployment. They've never spent a week understanding why their caching strategy broke under load.

They've never learned what it feels like to be wrong in a specific way that matters.

## The Architectural Paradox

The gap is widest in system design. Today's juniors are expected to make architectural decisions from day one—choosing databases, designing APIs, evaluating trade-offs—skills that once took years to develop. They have the tools to execute at a senior level. They have the judgment of someone three months into their career.

The paradox: we've given them the ability to operate as architects before they have the cognitive framework to understand what makes an architecture good or bad. They can generate the code. They can't yet see the failure modes.

And we've given them very little margin for error. A bad architecture decision in 1998 affected one team. A bad architecture decision in 2026, amplified by AI agents scaling it rapidly, affects the entire company.

## How We Got Here

It's not hard to see why we've optimized the struggle away. Productivity matters. Shipping velocity matters. The market rewards speed, and AI agents deliver it.

But we've confused two very different things:
- The ability to execute (which AI has accelerated)
- The ability to decide what to execute (which still requires human judgment developed through struggle)

We've automated the work without automating the learning. And we're hiring people who've never been forced to think deeply, because they've had AI thinking for them.

## Solutions I've Seen Work

Some organizations are pushing back intelligently:

**Aggressive code review**: Not to catch bugs, but to force architectural questioning. "Why this database over that one? What happens at 10x scale? Walk me through the trade-offs you evaluated."

**"No-flight zones" during onboarding**: Deliberately disabling AI tools for the first few months. Let juniors struggle through the codebase, the test suite, the build system, the deployment process. Let them fail safely.

**Forcing engagement with legacy systems**: Before they get AI-assisted greenfield projects, make them fix something broken. Make them read someone else's code. Make them live with the consequences of bad decisions—even if those decisions were made by someone else five years ago.

**Production postmortems as curriculum**: Involve juniors in postmortems. Have them trace through what went wrong. Have them understand that even senior engineers make mistakes, and that the learning comes from living with the consequences.

The message: "We will eventually give you AI. But first, we're going to teach you what it means to need it."

## The Question We're Not Asking

We're optimizing for feature velocity and hiring efficiency. We're not optimizing for the next generation of engineers who can make good decisions under uncertainty—the ones who've learned through their own failures what good architecture looks like.

In five years, when the codebase built by this cohort of AI-trained juniors starts to show its age, we'll have a crisis. We'll have senior engineers who've never debugged a complex system. We'll have architects who've never lived with a bad decision long enough to understand why it was bad.

The grunt work wasn't punishment. It was apprenticeship.

And we're eliminating the apprenticeship without realizing we're also eliminating the path to genuine expertise.
