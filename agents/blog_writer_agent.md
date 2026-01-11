# BlogWriter Agent

This document describes the composite `BlogWriterAgent` (in `blog_agents/blog_writer_agent.py`) which orchestrates the full blog production pipeline.

Usage
- Import and call from Python or wire into a chat UI (e.g., GitHub Copilot Chat) by copy/pasting the prompts:

```python
from blog_agents.blog_writer_agent import BlogWriterAgent
agent = BlogWriterAgent()
# run full pipeline
res = agent.run({"prompt": "Why text editors matter", "anecdote": "I once lost a patch in an editor crash"})
```

Modes
- `intake` — returns Socratic intake questions
- `scan` — performs research + references
- `outline` — reviews or creates an outline
- `draft` — returns draft and path
- `edit` — edits a provided draft
- `visual` — returns hero prompt
- `full` — runs the entire pipeline and saves artifacts in `blog_data/`

Integration with Copilot Chat
- Copy/paste the `chat_instructions/intake_prompt.md`, `chat_instructions/research_prompt.md`, and `chat_instructions/draft_prompt.md` into Copilot Chat to run parts of the pipeline interactively. The agent is a programmatic wrapper that provides a reproducible sequence for the chat-driven flow.
