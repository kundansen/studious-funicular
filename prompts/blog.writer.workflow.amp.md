# Blog Writing Workflow for Amp

A battle-tested workflow for producing intimate, magazine-grade blogs (~1500 words) for Medium.com. Topics span soft skills, career insights, GenAI, and tech realities. Voice: warm yet opinionated, humorous, non-cliché, academically grounded.

---

## Quick Start

```
User: "Write a blog about [topic]"
```

Amp will:
1. Create folder structure
2. Run Socratic intake
3. Research and outline
4. Draft with anti-AI guidelines
5. Review cycles (Vale + Oracle)
6. Generate hero image prompt
7. Create LinkedIn blurb and Medium tags

---

## Phase 1: Intake & Discovery

### Folder Setup
```
blogs/<blog-slug>/
├── <blog-name>.md              # Main draft (rename from draft.md when finalizing)
└── blog_data/
    ├── research_ledger.json    # Crash-resilient research checkpoint
    ├── references.json         # Verified citations
    └── hero_prompt.yaml        # Sumi-e image prompt
```

### Socratic Questions (Ask 3, Wait for Answers)
1. "What annoyed you about this topic recently?"
2. "What's the 'ugly truth' most people won't say?"
3. "Is there a book, article, or conversation that sparked this?"

**Do not proceed until user responds.** Their answers become the blog's soul.

---

## Phase 2: Research (Parallel Sub-Agents)

Deploy sub-agents concurrently:

### Research Agent
- `web_search` for current trends, recent articles
- `read_web_page` for deep-diving specific sources
- Save findings to `blog_data/research_ledger.json`

### Reference Scout Agent
- Find 3-5 academic/book citations
- One-line relevance note per source
- Verify URLs with `read_web_page`
- Save to `blog_data/references.json`

### Ledger Format (Crash Resilience)
```json
{
  "topic": "AI Slop and Broken Windows",
  "started": "2026-02-11",
  "phase": "research",
  "sources_found": [...],
  "key_insights": [...],
  "next_steps": "outline"
}
```

Update ledger after each phase. If thread crashes, read ledger to resume.

---

## Phase 3: Outline

### Pick a Template
8 options (pick randomly or ask user):

1. **The Lie → Truth** — Expose a common misconception, then reveal the gritty reality
2. **Problem → Solution** — Name the pain, then offer your take
3. **Contrarian** — "Everyone says X. They're wrong. Here's why."
4. **Story Arc** — Narrative structure with tension and resolution
5. **Framed Listicle** — List wrapped in a unifying metaphor
6. **Transformation** — Before/after journey
7. **Question Stack** — Build through escalating questions
8. **Then → Now → Next** — Historical context → current state → future implications

### Outline Structure
- **Hook**: The provocative opening (metaphor, question, or bold claim)
- **Context**: Background the reader needs (keep tight)
- **Core Argument**: 3-4 sections building the thesis
- **Counterpoint**: Acknowledge the other side (shows intellectual honesty)
- **Resolution**: Where this leaves us (not necessarily "the answer")

### Review Checkpoint
Consult Oracle:
```
Review this outline for logical flow, argument gaps, and whether 
it avoids common AI essay structures.
```

---

## Phase 4: Drafting

### Writing Constraints (Non-Negotiable)

**Forbidden Patterns:**
- Don't start sentences with "Here's what/where/how/why"
- Don't use "This isn't X. It's Y." (AI cliché)
- Don't use: "tensions", "real", "honest", "In the age of"
- Don't use: "landscape", "tapestry", "paradigm", "synergy"
- Don't start paragraphs with "It's worth noting" or "Interestingly"

**Required:**
- Include at least one personal anecdote or specific example
- Vary sentence length (short punchy + longer flowing)
- Use em-dashes (—) not hyphens for parenthetical asides
- End sections with forward momentum, not summaries

### Draft Settings
- Target: ~1500 words
- Sections: 5-7
- Paragraphs: narrative flow, not walls of text
- Lists: sparingly, never for the main argument

### Save Draft
Save to `blogs/<slug>/draft.md` initially. Rename to descriptive name when finalizing.

---

## Phase 5: Review Cycles

### Cycle 1: Vale Linting
```bash
cd blogs && vale <slug>/draft.md
```

**Custom Vale Rules** (in `blogs/.vale/styles/Blog/`):
- `AIPatterns.yml` — catches "This isn't X. It's Y."
- `HeresStart.yml` — catches "Here's what/where/how/why"
- `Dashes.yml` — flags improper dash usage

**Handle Results:**
- Fix errors
- Add valid terms to vocabulary: `blogs/.vale/styles/config/vocabularies/Blog/accept.txt`
- Warnings are acceptable for blog prose (passive voice, headline capitalization)

### Cycle 2: Oracle Review
```
Review this blog draft for:
1. Argument strength — gaps, weak transitions
2. Voice consistency — casual opinion piece throughout
3. AI cliche detection — phrases that sound model-generated
4. Structure — pacing, sections that drag or rush
5. Ending — satisfying or trails off

Writing constraints to verify:
- No "Here's what/where/how/why" sentence starts
- No "This isn't X. It's Y." pattern
- No banned words: tensions, real, honest, "In the age of"
```

### Cycle 3: Human Review
Present Oracle feedback to user. Ask:
- "Which of these should I address?"
- "Any sections you want me to rework?"

Iterate until user approves.

---

## Phase 6: Finalization

### Rename Draft
```bash
mv blogs/<slug>/draft.md blogs/<slug>/<descriptive-name>.md
```

### Hero Image Prompt
Create `blog_data/hero_prompt.yaml`:

```yaml
title: "Descriptive Title"
orientation: landscape
style: sumi-e ink wash, minimalist

elements:
  - element_1: "description with ink wash aesthetic"
  - element_2: "description"
  - element_3: "description"

mood: descriptive mood words

color_palette: deep blacks and soft grays; optional single accent color; mostly monochromatic

negative_prompt: "no robots, no computers, no text, no logos, no photorealism, no bright colors"

notes: "Key metaphor from the blog and how image should capture it"
```

### LinkedIn Promo Blurb
**First line is critical** — only thing visible before "More..."

Structure:
1. **Hook** (1 line): Provocative, counterintuitive, specific
2. **Context** (2-3 lines): What the post is about
3. **Questions/Stakes** (2-4 lines): Why reader should care
4. **CTA** (1 line): Invite engagement

Keep under 200 words. Less preachy, more curious.

### Medium Tags
5 tags mixing broad and niche:
```
Example: AI, Software Development, Code Quality, Technical Debt, Programming
```

---

## Phase 7: Final Assembly

Compile deliverables:
1. ✅ Blog post (Markdown, renamed to descriptive filename)
2. ✅ Hero image prompt (YAML)
3. ✅ LinkedIn blurb
4. ✅ Medium tags
5. ✅ References list (if applicable)

---

## Crash Recovery

If thread crashes mid-process:

1. Read `blog_data/research_ledger.json` for current phase
2. Read existing draft to understand progress
3. Resume from last checkpoint
4. Update ledger when resuming

---

## Anti-AI Voice Checklist (Final Pass)

Before declaring done, verify:

- [ ] No forbidden words/phrases
- [ ] Personal anecdote present
- [ ] Sentence rhythm varies
- [ ] Em-dashes used correctly
- [ ] Ending is decisive, not trailing
- [ ] Section headers are specific, not generic/grandiose
- [ ] Tone is casual and curious, not preachy

---

## Example Conversation Flow

```
User: Write a blog about broken windows theory applied to AI code

Amp: [Creates folder] I have a few questions before we start:
     1. What made you think about this connection recently?
     2. What's the thing about AI-generated code that bothers you most?
     3. Any books or articles that shaped your thinking here?

User: [Answers]

Amp: [Runs parallel research agents, saves to ledger]
     [Drafts outline using "Then → Now → Next" template]
     [Consults Oracle on outline]
     [Writes draft applying all constraints]
     [Runs Vale, fixes issues]
     [Consults Oracle for review]
     [Presents findings to user]

User: [Gives feedback]

Amp: [Iterates on feedback]
     [Creates hero prompt]
     [Generates LinkedIn blurb]
     [Provides Medium tags]
     Done! Here's your complete package.
```

---

## File References

- Vale config: `blogs/.vale.ini`
- Custom Vale rules: `blogs/.vale/styles/Blog/`
- Vocabulary: `blogs/.vale/styles/config/vocabularies/Blog/accept.txt`
- Outline templates: `chat_instructions/outline_templates.md`
- Ink wash image style: `blogs/inkwash_image_prompt.md`
