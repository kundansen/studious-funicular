"""Concrete agent implementations based on the Copilot-optimized prompt."""
from .base import Agent
from . import tools
from typing import Dict, Any, List

class IdeaExpander(Agent):
    def __init__(self):
        super().__init__("IdeaExpander")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        # Expect 'prompt' and optionally 'answers' from the user
        prompt = inputs.get("prompt", "")
        questions = [
            "What annoyed you about this recently?",
            "What's the 'ugly truth' you want to expose?",
            "Give one sentence that drove you to write this."
        ]
        return {"questions": questions, "prompt": prompt}


class MarketResearcher(Agent):
    def __init__(self):
        super().__init__("MarketResearcher")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        topic = inputs.get("topic", inputs.get("prompt", ""))
        results = tools.web_search(topic, limit=3)
        summary = [r["title"] + " — " + r["url"] for r in results]
        tools.save_json(f"research_{topic.replace(' ', '_')}.json", {"results": results})
        return {"summary": summary, "results": results}


class ReferenceScout(Agent):
    def __init__(self):
        super().__init__("ReferenceScout")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        topic = inputs.get("topic", inputs.get("prompt", ""))
        # Mock: return 3 pseudo-references
        refs = [
            {"title": f"Paper {i} on {topic}", "url": f"https://doi.org/mock/{i}", "note": "Relevant background"}
            for i in range(1, 4)
        ]
        tools.save_json(f"references_{topic.replace(' ', '_')}.json", {"refs": refs})
        return {"references": refs}


class OutlineReviewer(Agent):
    def __init__(self):
        super().__init__("OutlineReviewer")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        outline = inputs.get("outline", [])
        # Very simple review: ensure at least 3 sections
        issues = []
        if len(outline) < 3:
            issues.append("Outline has fewer than 3 sections")
        return {"ok": len(issues) == 0, "issues": issues}


class MediumBlogger(Agent):
    def __init__(self):
        super().__init__("MediumBlogger")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        outline = inputs.get("outline", [])
        prompt = inputs.get("prompt", "")
        anecdote = inputs.get("anecdote", "")
        # Produce a short mock draft (in real usage, call a text generation model)
        sections = []
        for i, sec in enumerate(outline, start=1):
            sections.append(f"## {sec}\n\nParagraph 1 for section {i}. Paragraph 2. Anecdote: {anecdote}\n")
        draft = "\n".join(sections)
        path = tools.save_artifact("draft.md", draft)
        return {"draft_path": path, "draft": draft}


class BlogEditor(Agent):
    def __init__(self):
        super().__init__("BlogEditor")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        draft = inputs.get("draft", "")
        # Simple edits: ensure 'Kundan' voice flag is present
        edited = draft.replace("Paragraph", "Paragraph (Kundan voice)")
        path = tools.save_artifact("draft_edited.md", edited)
        return {"edited_path": path, "edited": edited}


class VisualPromptDesigner(Agent):
    def __init__(self):
        super().__init__("VisualPromptDesigner")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        topic = inputs.get("topic", inputs.get("prompt", ""))
        yaml_prompt = (
            "orientation: landscape\nstyle: sumi-e\nsubject: 'A lone figure coding at dawn, ink wash coastlines, metaphor for focus'\nnotes: 'leave empty space to evoke thought'\n"
        )
        path = tools.save_artifact("hero_prompt.yaml", yaml_prompt)
        return {"hero_prompt_path": path, "hero_prompt": yaml_prompt}
