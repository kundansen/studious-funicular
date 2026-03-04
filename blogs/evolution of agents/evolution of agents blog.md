# It's 10 O'Clock. Do You Know Where Your Agents Are?

If you grew up watching American television in the sixties through the eighties, you remember the public service announcement that aired every night at 10 PM: *"It's 10 o'clock. Do you know where your children are?"* The message was simple: your kids are out there, unsupervised, and you should probably check in.

I think about that PSA a lot these days. Except now the question is about AI agents. They're out there, deleting a Meta safety director's inbox, racking up $200-a-day API bills, and 900 of them on a popular skill marketplace turned out to be malware. Let me ask: *It's 2026. Do you know where your agents are?*

Probably not. And you might not even know what "agent" means anymore, because the word has been stretched, repurposed, and marketing-washed until it means everything and nothing simultaneously. A working definition that has held up for about five centuries: **an agent is a thing that takes actions on your behalf, with varying degrees of freedom and blame-absorption.**

That last part - the blame-absorption - turns out to be the whole story.

## A Brief History of Passing the Buck

The word "agent" comes from the Latin verb *agere*, meaning to do, to drive forward. It entered English in the fifteenth century, and it was wonderfully neutral. An agent could be a person or a chemical reaction. Anything that *did stuff*.

Then lawyers got involved.

By 1812, Lord Ellenborough, Chief Justice of the King's Bench, had formalized the doctrine of "apparent authority" in *Pickering v. Busk*. The gist: if you give someone the outward appearance of acting on your behalf, you're bound by whatever they do, even if you privately told them not to. Agency became a liability game. The principal delegates. The agent acts. And when things go sideways, both point at each other.

Fast forward to the twentieth century, and psychologist Stanley Milgram gave us the dark mirror of this concept. His famous obedience experiments revealed what he called the "agentic shift," the moment a person stops seeing themselves as responsible for their own actions and starts viewing themselves as merely an instrument of someone else's will. "I was just following orders." Agency as moral offloading.

Albert Bandura approached it from the other direction in 1986, defining "agentic" as the human capacity for intentionality, self-regulation, and control over one's environment. For Bandura, being agentic was aspirational, a sign of autonomy and self-determination.

Within the span of two centuries, the same word came to describe both a liability shield and an empowerment badge, depending on who was holding it. No wonder Silicon Valley fell in love with it.

## The Boring Years (That Actually Mattered)

Computer science had its own agents long before anyone tried to sell them on LinkedIn, starting with Alan Turing's 1950 thought experiment, then ELIZA in 1966 pattern-matching her way through therapy sessions, and eventually the expert systems of the eighties that were rigid and brittle as a dried-out contract.

The serious foundational work came in 1995, when Michael Wooldridge and Nicholas Jennings defined an "intelligent agent" as a system with autonomy, reactivity, proactiveness, and social capability. The Belief-Desire-Intention (BDI) architecture gave software systems something resembling a decision-making framework: what do I know, what do I want, and what am I going to do about it.

Rigorous work. Important work. And nobody outside of academic conferences cared, because these agents couldn't book a restaurant reservation, let alone threaten anyone's job. The word "agent" in computer science lived a quiet, respectable, peer-reviewed life.

That was about to change.

## The Word That Ate LinkedIn

In early 2024, Andrew Ng started talking about "agentic workflows," the idea that LLMs perform dramatically better when you let them draft, reflect, critique, and iterate rather than demanding a single-shot answer. The term caught fire because it solved a naming problem the industry desperately needed solved.

The thing that made the word explode wasn't just marketing. It was a pile-up. First, LLMs made natural language instructions *feel* like intent, and intent is the psychological doorway into calling something an agent. You type "book me a flight to Denver" and watch the thing start browsing Expedia on its own. Nobody had to call it an agent. You just felt it.

Second, tool-use and function calling made *action* cheap. An LLM that can only talk is an assistant. An LLM that can call APIs and execute code starts to *do things*. And doing things is the original definition of *agere*.

Third - and most cynically - autonomy became a pricing narrative. Why sell tokens when you can sell outcomes? Why charge per seat when your "agent" replaces the person who sat in it? The shift from "copilot" to "agent" wasn't just technical. It was economic. The word was doing revenue work.

Within 18 months, "agentic" went from an Andrew Ng conference talk to a mandatory keyword on every enterprise pitch deck in existence. And that's when the trouble started.

## The Agentic Wash

I sat through a vendor demo last quarter where the presenter described their system - a series of hard-coded if-else branches connected to an API - as a "deterministic agentic framework." I wrote the phrase down because I wanted to remember the exact moment the word lost all meaning.

We are living through an agentic wash. It's the new greenwashing, except instead of slapping a leaf logo on a plastic bottle, companies are slapping "agentic" on a workflow engine and hoping nobody checks under the hood.

The sniff test is straightforward. Ask three questions:

- Does it act without being prompted at every step?
- Can it recover from failure without a human patching the prompt?
- Can it explain what it did *and* what it chose not to do?

If the answer to all three is no, you don't have an agent. You have an if-else chain wearing a trench coat.

And the term is pulling off two scams at the same time: on one end, selling automation that isn't there. On the other end, making dangerous autonomy feel normal before it's earned. It's the perfect accountability dodge: vendors call it "autonomous" so they can say "you configured it wrong," and buyers call it "agentic" so they can say "the AI did it." Milgram's moral offloading, dressed up in a SaaS agreement.

## The other extreme: OpenClaw and the car keys

Which brings us to the other side of the spectrum, and it's just as unnerving.

In January 2026, an Austrian engineer released OpenClaw, an open source AI agent that runs on your machine and connects to your WhatsApp, Slack, email, and calendar. You text it a task, and it does it. Skip the copy-pasting and the tab-switching. The thing … acts.

Within weeks, it had 225,000 GitHub stars and a FOMO wave washing over the tech community that made crypto look measured. Everyone wanted their own autonomous AI butler.

Then the incidents started. A Meta AI safety director (someone who builds AI safety systems for a living) had her inbox bulk-deleted when her OpenClaw agent's context window overflowed and it forgot its own instructions. Security researchers found a remote code execution vulnerability. Bitdefender discovered nearly 900 malicious packages on ClawHub, OpenClaw's skill marketplace, about 20% of the entire registry. Some users reported $200-a-day API bills from agents that just kept … agenting.

The "10 o'clock" PSA was about negligent parenting. OpenClaw is what happens when you hand an unsupervised teenager the car keys along with root access to your life - then go to bed.

## The question you should be asking

Truth is, most of what's called "agentic" today lives somewhere between a dressed-up chatbot and an unsupervised intern with administrator access. Marketing says autonomous digital workers have arrived. Engineering says "it works great in the demo."

Milgram would have appreciated the irony. We're experiencing an agentic shift *about* the agentic shift, delegating our judgment about autonomy to vendors whose incentive is to oversell it. We're following orders from pitch decks.

Keep the word if you want - just don't outsource your judgment to it. Next time someone tells you their product is "agentic," ask three better questions: What permissions does it have? What can it change? And who gets paged at 2 AM when it breaks?

Because it's 10 o'clock. And your agents are definitely still up.

---

*Further reading: Stanley Milgram's* Obedience to Authority *(1974) for the "agentic state" and moral offloading. Albert Bandura's* Social Foundations of Thought and Action *(1986) for the aspirational side of agency. Wooldridge & Jennings's "Intelligent Agents: Theory and Practice" in* The Knowledge Engineering Review *(1995) for the computational definition that held up for decades. Andrew Ng's 2024 talks on agentic workflows for the moment the word crossed over. TechCrunch's February 2026 coverage of the OpenClaw inbox deletion and Bitdefender's ClawHub malware analysis for the moment it went sideways.*
