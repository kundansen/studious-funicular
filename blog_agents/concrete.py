"""Concrete agent implementations based on the Copilot-optimized prompt."""
from .base import Agent
from . import tools
from typing import Dict, Any, List
import random


OUTLINE_TEMPLATES = [
    # Classic narrative arc
    {
        "name": "The Lie → Truth",
        "sections": [
            "Hook: The Lie",
            "Reality: The Grime", 
            "Insight: The Metaphor",
            "Call to Arms: The Hope"
        ]
    },
    # Problem-solution
    {
        "name": "Problem → Solution",
        "sections": [
            "The Pain Point",
            "Why It Matters",
            "The Unexpected Fix",
            "How to Apply It",
            "The Payoff"
        ]
    },
    # Contrarian take
    {
        "name": "Contrarian",
        "sections": [
            "The Popular Belief",
            "Why Everyone's Wrong",
            "The Evidence",
            "A Better Mental Model",
            "What Changes Now"
        ]
    },
    # Story-driven
    {
        "name": "Story Arc",
        "sections": [
            "Once Upon a Time",
            "The Turning Point",
            "The Struggle",
            "The Breakthrough",
            "The Lesson"
        ]
    },
    # Listicle with frame
    {
        "name": "Framed Listicle",
        "sections": [
            "The Setup",
            "Point 1: [specific]",
            "Point 2: [specific]",
            "Point 3: [specific]",
            "The Thread That Connects"
        ]
    },
    # Before/After transformation
    {
        "name": "Transformation",
        "sections": [
            "Where I Started",
            "The Catalyst",
            "The Messy Middle",
            "Where I Landed",
            "What You Can Steal"
        ]
    },
    # Question-driven
    {
        "name": "Question Stack",
        "sections": [
            "The Question Nobody Asks",
            "The Obvious (Wrong) Answer",
            "Digging Deeper",
            "The Real Answer",
            "New Questions This Opens"
        ]
    },
    # Historical/evolutionary
    {
        "name": "Then → Now → Next",
        "sections": [
            "How It Used to Work",
            "What Changed",
            "Where We Are Now",
            "What's Coming",
            "How to Prepare"
        ]
    },
]


class IdeaExpander(Agent):
    def __init__(self):
        super().__init__("IdeaExpander")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
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
        tools.save_json(f"research_{tools.slugify(topic)}.json", {"results": results})
        return {"summary": summary, "results": results}


class ReferenceScout(Agent):
    def __init__(self):
        super().__init__("ReferenceScout")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        topic = inputs.get("topic", inputs.get("prompt", ""))
        refs = [
            {"title": f"Paper {i} on {topic}", "url": f"https://doi.org/mock/{i}", "note": "Relevant background"}
            for i in range(1, 4)
        ]
        tools.save_json(f"references_{tools.slugify(topic)}.json", {"refs": refs})
        return {"references": refs}


class OutlineGenerator(Agent):
    """Generate varied blog outlines from templates."""
    def __init__(self):
        super().__init__("OutlineGenerator")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        template_name = inputs.get("template")
        topic = inputs.get("topic", inputs.get("prompt", ""))
        
        if template_name:
            template = next((t for t in OUTLINE_TEMPLATES if t["name"] == template_name), None)
            if not template:
                template = random.choice(OUTLINE_TEMPLATES)
        else:
            template = random.choice(OUTLINE_TEMPLATES)
        
        outline = template["sections"].copy()
        
        tools.save_json("outline.json", {
            "template": template["name"],
            "sections": outline,
            "topic": topic
        })
        
        return {
            "template_name": template["name"],
            "outline": outline,
            "all_templates": [t["name"] for t in OUTLINE_TEMPLATES]
        }


class OutlineReviewer(Agent):
    def __init__(self):
        super().__init__("OutlineReviewer")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        outline = inputs.get("outline", [])
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
        sections = []
        for i, sec in enumerate(outline, start=1):
            sections.append(f"## {sec}\n\nParagraph 1 for section {i}. Paragraph 2. Anecdote: {anecdote}\n")
        draft = "\n".join(sections)
        path = tools.save_draft("draft.md", draft)
        return {"draft_path": path, "draft": draft}


class BlogEditor(Agent):
    def __init__(self):
        super().__init__("BlogEditor")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        draft = inputs.get("draft", "")
        edited = draft.replace("Paragraph", "Paragraph (Kundan voice)")
        path = tools.save_draft("draft_edited.md", edited)
        return {"edited_path": path, "edited": edited}


class StyleChecker(Agent):
    """Run Vale prose linter on the current draft."""
    def __init__(self):
        super().__init__("StyleChecker")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        draft_name = inputs.get("draft_name", "draft.md")
        result = tools.lint_draft(draft_name)
        return result


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
