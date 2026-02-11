# AGENTS.md — Instructions for Amp

## Project Overview

This is a blog writing pipeline for Amp. No API keys needed — Amp drives the workflow interactively.

## Amp Workflow (Primary)

### 1. Start a Blog
User says: "Write a blog about X" or "Start a new blog on Y"

1. Create folder: `blogs/<slug>/`
2. Ask 3 Socratic intake questions
3. Pick an outline template from `chat_instructions/outline_templates.md`
4. Draft the post (~1500 words)
5. Save to `blogs/<slug>/draft.md`

### 2. Style Check
User says: "Run vale on my draft" or "Check style"

```bash
cd blogs && vale <slug>/draft.md
```

Fix errors, then offer to add unknown terms to vocabulary.

### 3. Edit
User says: "Edit my draft" or "Polish this"

Apply Anti-AI Writing Guidelines, vary sentence rhythm, ensure anecdote is present.

## Outline Templates

8 templates in `chat_instructions/outline_templates.md`:
- The Lie → Truth (classic)
- Problem → Solution
- Contrarian
- Story Arc
- Framed Listicle
- Transformation
- Question Stack
- Then → Now → Next

Pick randomly or ask user preference.

## CLI (for testing only)

```bash
python3 blog_runner.py create "<name>" "<topic>" --template "Contrarian"
python3 blog_runner.py lint "<name>"
python3 blog_runner.py list
```

## Folder Structure

Each blog gets its own folder under `blogs/`:
```
blogs/<blog-slug>/
├── draft.md           # Raw draft (main file)
├── draft_edited.md    # After editing pass
└── blog_data/         # Artifacts
    ├── research_*.json
    ├── references_*.json
    └── hero_prompt.yaml
```

## Style Checking

- Vale config: `blogs/.vale.ini`
- Custom vocabulary: `blogs/.vale/styles/config/vocabularies/Blog/accept.txt`
- Run: `cd blogs && vale <path-to-draft>`

### Adding Terms to Vocabulary

If Vale flags valid terms, add them to `accept.txt` (one per line).

## Code Conventions

- Agents are in `blog_agents/concrete.py`
- Tools (file I/O, Vale integration) are in `blog_agents/tools.py`
- Use `tools.set_blog_context(name)` before any file operations
- Drafts go in blog root; artifacts go in `blog_data/`

## Testing

```bash
pytest -q
```

Tests are in `tests/`. Add new tests when adding agents.
