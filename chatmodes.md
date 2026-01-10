# Chatmodes for blog agents

Define interaction modes that guide how agents should behave when run in different phases.

- intake: ask Socratic questions and collect user answers; be concise and inquisitive.
- scan: search and summarize external sources, return bullet lists and URLs.
- outline: produce a metaphor-first outline of 4 sections.
- draft: produce a narrative draft (1500 words target; for now, drafts are mocked).
- edit: apply Anti-AI writing rules and polish voice.

Agents can be invoked with "mode": e.g., {"mode": "intake", "prompt": "..."} to alter behavior.
