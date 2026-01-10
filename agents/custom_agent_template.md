# Custom Agent Template

Create new agents by adding a Python module to `blog_agents/` and adding a short entry here describing the agent's role and chat instructions.

Example: `blog_agents/my_research_agent.py`

- name: MyResearchAgent
- role: Researcher — runs web searches and returns structured trends
- inputs: {"topic": str, "limit": int}
- outputs: {"trends": list, "references": list}
- chat_instructions: |
  System: You are a research agent. Ask clarifying questions if the topic is vague. Run web searches and return 3 trends and 3 references with one-line notes.

Add a test in `tests/test_agents.py` that validates expected behavior.
