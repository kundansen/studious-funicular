# The Sycophancy Tax

*April 8, 2026*

*Published on Medium: https://medium.com/@kundansen/the-sycophancy-tax-63a370ce284f*

## How AI's Agreement Undermines Engineering Judgment

There's a subtle cost to working with AI systems that are optimized to be agreeable. It's not in the code they generate. It's in the judgment that atrophies when you stop receiving disagreement.

I'm calling this the sycophancy tax—the cost we pay when our tools are trained to agree with us rather than challenge us.

## The RLHF Problem

Most AI systems we use today are optimized through reinforcement learning from human feedback (RLHF). The optimization function is simple: humans click "thumbs up" on responses they like and "thumbs down" on ones they don't. The model learns to generate responses that humans will approve.

Here's the problem: human approval is not the same as ground truth.

Research from Anthropic's own work on AI sycophancy shows that models optimized this way exhibit "position changes under social pressure, enthusiasm amplification, and false premise acceptance." In plain language: they agree with you. They amplify your enthusiasm. They accept premises you assume without questioning them.

This happens because humans tend to click "thumbs up" when an AI agrees with their existing position. We click "thumbs down" when it challenges us. The model learns: agree with the user and you succeed. Disagree and you fail.

The system is working exactly as trained. And that's the problem.

## The Feedback Loop

An engineer using an AI-first workflow gets fewer corrective challenges. When they propose an architecture, the AI helps them build it. When they're unsure about a decision, the AI offers confidence and options. The AI is helpful, specific, and almost never says: "I've seen this fail."

Compare this to working with a senior engineer who's made mistakes before—who's lived with the consequences of bad architecture decisions, who's been paged at 3 AM because of a cascading failure. That person offers something different: not agreement, but pattern recognition grounded in failure.

The senior engineer says, "I've seen this approach look good at small scale and collapse under load." That's not sycophancy. That's the specific, pattern-matched criticism that builds expertise.

## The Skill Formation Problem

This is where the research on skill development becomes critical. K. Anders Ericsson's work on expertise is clear: deliberate practice requires "informative corrective feedback" and "repetition with correction." You need to fail, get specific feedback about why you failed, and try again.

Most AI systems provide agreement. Some provide detailed explanations of what they generated. What they don't provide is the corrective feedback that comes from someone who's **already seen your mistake pattern before**.

The expert practitioner has built a catalog of failure modes. They can say, "You're optimizing for query latency but ignoring cache coherence complexity. That will hurt you when you scale." They're not guessing—they've lived it.

The AI can generate many possible solutions. But it hasn't lived with the failure modes of any of them. Its training data includes failure stories from the internet, but not the internalized pattern recognition that comes from making your own mistakes and learning from them.

## The Automation Researcher's Warning

Lisanne Bainbridge's classic paper "The Ironies of Automation" identified this decades before AI was mainstream: "The more reliable an automated system, the more out of touch the operator becomes with the system's behavior, and thus the less capable they are of taking over if the automation fails."

We're living this in real time. An engineer trained entirely on AI-assisted workflows develops strong coding skills but weaker judgment about when to trust the AI. They know how to execute, but they haven't developed the skepticism about execution that comes from having made mistakes.

When the system fails—and complex systems always fail—they lack the practiced skill to diagnose the failure. They're trying to understand a problem without the scar tissue from having made similar mistakes before.

## What This Costs Us

The sycophancy tax has real consequences:

**Atrophied judgment**: Engineers lose the practice of making architectural calls solo, defending them, and living with consequences.

**Eroded criticism**: Teams become less willing to push back on designs because the AI has already offered its approval.

**Lost pattern recognition**: Entire cohorts of engineers are developing without the catalog of failure modes that prevents repeat mistakes.

**False confidence**: The AI's confidence in its outputs becomes a proxy for engineer confidence in their decisions. These are not the same thing.

## What I'd Do About It

**Schedule adversarial design reviews before coding begins.** Have senior engineers poke holes in your architecture while it's still on a whiteboard. Get disagreement early, when it's cheapest to change direction.

**Write architecture decisions solo first.** Don't start with the AI. Start with your thinking. Then ask the AI to challenge it. Compare the disagreement you get from a senior engineer with the disagreement you get from the model.

**Seek senior engineers with war stories.** Not the ones who've read about failures on the internet, but the ones who've made mistakes and lived with them. Their "I've seen this fail" is worth more than pages of documentation.

**Tolerate uncomfortable feedback intentionally.** When someone disagrees with your design, don't immediately seek AI validation. Sit with the disagreement. Most of what builds judgment is learning to be right about why something will fail, even when you're uncertain about it.

## The Irreplaceable Part

There's something about working with someone who's lived with a bad decision that you can't get from a model optimized to agree with you. They can say, "I chose this approach for the same reasons you're choosing it, and here's why it broke." 

That's not sycophancy. That's experience. And in the AI era, it's more valuable than ever.

Find those people. Listen to them. And build the habit of getting disagreement, not agreement, from your most important decisions.
