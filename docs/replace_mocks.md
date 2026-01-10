# Replacing Mocks with Real Tools

This document explains how to replace the lightweight mock implementations in `blog_agents.tools` and `blog_agents.concrete` with production-ready integrations (web search, webpage fetchers, and model APIs).

1) Install dev dependencies
   - Create virtualenv and install pytest: `python -m venv .venv && . .venv/bin/activate && pip install pytest requests`

2) Web search & fetch
   - Replace `blog_agents.tools.web_search` with a real search client (SerpAPI, Bing, Google Custom Search, or an internal search).
   - Implement `fetch_webpage(url)` using `requests` or an HTML client; if you need parsed content, use `beautifulsoup4` or `readability-lxml`.
   - Return structured JSON with `title`, `url`, `text`, `published` fields.

3) Text generation model
   - In `MediumBlogger.run`, replace the mock composition with a call to your chosen model API (OpenAI, Cohere, Anthropic, or a local model wrapper).
   - Keep the `outline`, `prompt`, and `anecdote` as structured inputs; implement a `compose_article(outline, prompt, anecdote)` helper.

4) Persistence
   - `blog_agents.tools.save_artifact` currently writes to `blog_data/`. Replace with a storage connector (S3, GCS, or a CMS) if needed.

5) QA / Oracle
   - Add an `Oracle` module to run deeper reasoning checks. It can be a composite agent that checks logic, stats, and citation validity.

6) Tests & Fixtures
   - Add fixtures for web search and fetch responses to `tests/fixtures/` and use them to simulate API responses while testing.

7) Security & Rate Limits
   - Store API keys in env vars; add helper functions to read them via `os.environ` or a secret manager.

8) Example: Hooking an OpenAI call (pseudocode)

```python
# in blog_agents/tools.py
import openai

def web_search(query, limit=5):
    # Use an external tool or a Search API
    pass

# in blog_agents/concrete.py
class MediumBlogger(Agent):
    def run(self, inputs):
        outline = inputs['outline']
        prompt = inputs['prompt']
        anecdote = inputs.get('anecdote', '')
        final = call_text_model(outline, prompt, anecdote)
        save_artifact('draft.md', final)
        return {'draft': final}
```

If you'd like, I can add sample implementations for one or two integrations (e.g., a SerpAPI adapter and an OpenAI writer) and tests. Ask which provider(s) you prefer and I'll stub them in.
