# The Attention Recession

*April 25, 2026*

*Published on Medium: https://medium.com/@kundansen/the-attention-recession-4f544045e5e4*

## The Core Problem

The author describes a paradox in modern knowledge work: AI tools enable unprecedented documentation production, yet human capacity to consume that documentation continues to decline. During an internal demo, a colleague posed a question that crystallized the issue: "What's the point of creating all documentation automatically when we no longer have the capacity to read any of the docs?"

## The Production vs. Consumption Imbalance

Documentation quality has objectively improved—meeting minutes are comprehensive, architecture decision records (ADRs) are thorough, library docs are better than ever. However, this abundance coincides with information overload from multiple sources: new AI models dropping every few weeks, competing specifications, security disclosures, and mandatory AI adoption policies.

The author notes that Shopify CEO Tobi Lütke framed AI competency as a performance requirement, making volume measurement a workplace mandate rather than optional.

## Documentation's Format Evolution

Similar to how television evolved from long-form films to short-form clips on YouTube, documentation is experiencing compression. ADRs have ballooned from Michael Nygard's original "few sentences in a numbered sequence" to 8,000-word documents with matrices, glossaries, and multiple diagram layers—yet remain largely unread.

## Practical Adaptation: Layered Documentation

Rather than following Cal Newport's "Deep Work" prescription of withdrawal and batching, the author proposes layered documentation:

1. **Human-readable summary** (executive layer for quick scanning)
2. **Machine-readable structured block** (for AI agent consumption)
3. **Detailed prose** (only where argumentation is necessary)

Examples include `.cursorrules` files, `llms.txt` standards, and GitHub's spec-kit approach.

## Critical Failures in Agent-Mediated Reading

The author identifies specific document types unsuitable for AI summarization:

- **Legal/compliance documents** where exact language matters
- **Leadership decisions** where tone carries meaning
- **Onboarding materials** for readers unable to triage yet
- **Postmortems and ADRs** where dissent is the load-bearing content

The specific risk: AI summaries may erase minority positions and hallucinate false consensus, particularly dangerous in decision documents where disagreement is essential information.

## Reading Discipline

The proposed consumer-side approach emphasizes:

- **Triage:** Ruthlessly deciding what deserves careful reading
- **Layered reading:** Scanning summaries first, structured blocks second
- **Trust calibration:** Matching reading depth to document type (AI summaries work for status updates; they fail for postmortems)

## Structural Honesty

The author acknowledges writing this piece with AI summarization in mind—deliberately structuring content for both human and agent readers, treating the inevitability of agent-mediated consumption as a design constraint rather than an obstacle.

## Key Takeaway

The "attention recession" reflects a fundamental mismatch: abundant content production meets constrained human attention. Rather than resisting this dynamic, the author advocates designing documentation explicitly for layered, delegated reading where humans and AI agents handle different comprehension depths based on document type and stakes.
