"""Composite BlogWriter agent that orchestrates the blog creation pipeline.

This agent is intended to be invoked from an interactive chat (e.g., Copilot Chat) or programmatically.
It uses the concrete agents implemented in `blog_agents.concrete` and returns a structured result with artifact paths.
"""
from typing import Dict, Any, List
from .base import Agent
from .concrete import (
    IdeaExpander,
    MarketResearcher,
    ReferenceScout,
    OutlineReviewer,
    MediumBlogger,
    BlogEditor,
    VisualPromptDesigner,
)
from . import tools


class BlogWriterAgent(Agent):
    def __init__(self):
        super().__init__("BlogWriter")
        # Instantiate sub-agents
        self.idea = IdeaExpander()
        self.researcher = MarketResearcher()
        self.ref_scout = ReferenceScout()
        self.outline_reviewer = OutlineReviewer()
        self.writer = MediumBlogger()
        self.editor = BlogEditor()
        self.visual = VisualPromptDesigner()

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Run the blog pipeline.

        inputs may include:
          - mode: one of 'intake','scan','outline','draft','edit','visual','full'
          - prompt/topic: user topic or prompt
          - anecdote: short anecdote
          - outline: optional outline to use

        Returns a dict with results and artifact paths.
        """
        mode = inputs.get("mode", "full")
        prompt = inputs.get("prompt", "")
        anecdote = inputs.get("anecdote", "")
        provided_outline = inputs.get("outline")

        result: Dict[str, Any] = {"mode": mode}

        if mode == "intake":
            out = self.idea.run({"prompt": prompt})
            result.update(out)
            return result

        if mode == "scan":
            research = self.researcher.run({"topic": prompt})
            refs = self.ref_scout.run({"topic": prompt})
            result.update({"research": research, "references": refs})
            return result

        if mode == "outline":
            # If an outline provided, review it; else create a simple metaphor-first outline
            if provided_outline:
                outline = provided_outline
            else:
                outline = ["Hook: The Lie", "Reality: The Grime", "Insight: The Metaphor", "Call to Arms: The Hope"]
            review = self.outline_reviewer.run({"outline": outline})
            result.update({"outline": outline, "outline_review": review})
            return result

        if mode == "draft":
            outline = provided_outline or ["Hook: The Lie", "Reality: The Grime", "Insight: The Metaphor", "Call to Arms: The Hope"]
            draft = self.writer.run({"outline": outline, "prompt": prompt, "anecdote": anecdote})
            result.update(draft)
            return result

        if mode == "edit":
            draft = inputs.get("draft")
            if not draft:
                raise ValueError("edit mode requires a 'draft' input")
            edited = self.editor.run({"draft": draft})
            result.update(edited)
            return result

        if mode == "visual":
            visual = self.visual.run({"topic": prompt})
            result.update(visual)
            return result

        # default: full pipeline
        # 1) Intake-derived questions -> ask user (we return questions so caller/chat UI can show them)
        idea_out = self.idea.run({"prompt": prompt})
        result["intake_questions"] = idea_out.get("questions")

        # 2) Research & refs
        research = self.researcher.run({"topic": prompt})
        refs = self.ref_scout.run({"topic": prompt})
        result["research"] = research
        result["references"] = refs

        # 3) Outline
        outline = provided_outline or ["Hook: The Lie", "Reality: The Grime", "Insight: The Metaphor", "Call to Arms: The Hope"]
        outline_review = self.outline_reviewer.run({"outline": outline})
        if not outline_review.get("ok"):
            # return early with issues for interactive resolution
            result["outline"] = outline
            result["outline_review"] = outline_review
            return result
        result["outline"] = outline
        result["outline_review"] = outline_review

        # 4) Draft
        draft = self.writer.run({"outline": outline, "prompt": prompt, "anecdote": anecdote})
        result["draft"] = draft.get("draft")
        result["draft_path"] = draft.get("draft_path")

        # 5) Edit
        edited = self.editor.run({"draft": result["draft"]})
        result["edited"] = edited.get("edited")
        result["edited_path"] = edited.get("edited_path")

        # 6) Visual
        visual = self.visual.run({"topic": prompt})
        result["hero_prompt"] = visual.get("hero_prompt")
        result["hero_prompt_path"] = visual.get("hero_prompt_path")

        # Save summary metadata
        meta = {
            "prompt": prompt,
            "anecdote": anecdote,
            "outline": outline,
            "draft_path": result.get("draft_path"),
            "edited_path": result.get("edited_path"),
            "hero_prompt_path": result.get("hero_prompt_path"),
        }
        tools.save_json(f"meta_{prompt.replace(' ', '_')}.json", meta)
        result["meta_path"] = f"blog_data/meta_{prompt.replace(' ', '_')}.json"

        return result


# Convenience top-level function for importers
def run_blog_pipeline(inputs: Dict[str, Any]) -> Dict[str, Any]:
    agent = BlogWriterAgent()
    return agent.run(inputs)
