# studious-funicular
Kundan's Personal Stash of Goodies

## Blog Agents — Copilot-Optimized

A lightweight agent framework to orchestrate writing Medium-style blogs with style checking via Vale.

### Folder Structure

```
studious-funicular/
├── blog_runner.py          # Main CLI
├── blog_agents/            # Agent implementations
├── blogs/                  # All blogs live here
│   ├── .vale.ini           # Vale config
│   ├── .vale/styles/       # Vale style packages
│   └── <blog-slug>/        # One folder per blog
│       ├── draft.md        # Raw draft
│       ├── draft_edited.md # Edited draft
│       └── blog_data/      # Research, refs, hero prompt
├── chat_instructions/      # Prompts for each stage
├── copilot_modes/          # Copilot Chat mode templates
└── tests/                  # pytest tests
```

### Quick Start

1. **Setup**:
   ```bash
   python -m venv .venv && . .venv/bin/activate
   pip install pytest
   brew install vale  # for style checking
   ```

2. **Create a blog**:
   ```bash
   python blog_runner.py create "my-first-post" "Why text editors matter" --anecdote "I once lost a patch"
   ```

3. **Check style**:
   ```bash
   python blog_runner.py lint "my-first-post"
   ```

4. **List blogs**:
   ```bash
   python blog_runner.py list
   ```

### Pipeline Stages

| Step | Agent | Output |
|------|-------|--------|
| 1 | IdeaExpander | Socratic questions |
| 2 | MarketResearcher | Web search summary |
| 3 | ReferenceScout | References JSON |
| 4 | OutlineReviewer | Outline validation |
| 5 | MediumBlogger | draft.md |
| 6 | BlogEditor | draft_edited.md |
| 7 | **StyleChecker** | Vale lint results |
| 8 | VisualPromptDesigner | hero_prompt.yaml |

### Style Checking with Vale

Vale checks for:
- Passive voice
- Weasel words ("completely", "usually")
- Wordiness ("it was", "in order to")
- Clichés

**Add custom terms** to `blogs/.vale/styles/config/vocabularies/Blog/accept.txt`

**Run manually**:
```bash
cd blogs && vale <blog-slug>/draft.md
```

### Working with Amp

Ask Amp to:
- "Create a new blog about X"
- "Run vale on my draft and fix errors"
- "Add these gaming terms to the Vale vocabulary"

### Chat Instructions

- `chat_instructions/intake_prompt.md` — Socratic intake
- `chat_instructions/research_prompt.md` — Research stage
- `chat_instructions/draft_prompt.md` — Drafting + style check
- `chat_instructions/style_check_prompt.md` — Vale workflow

### Contributing

Add new agents under `blog_agents/` and tests in `tests/`

---
Created by GitHub Copilot — Raptor mini (Preview)
