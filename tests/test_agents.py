import os
from blog_agents.concrete import IdeaExpander, MarketResearcher, ReferenceScout, OutlineReviewer, MediumBlogger, BlogEditor, VisualPromptDesigner

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "blog_data")


def test_idea_expander():
    ag = IdeaExpander()
    out = ag.run({"prompt": "testing prompts"})
    assert "questions" in out and len(out["questions"]) >= 1


def test_market_researcher_and_reference_scout(tmp_path):
    mr = MarketResearcher()
    res = mr.run({"topic": "python testing"})
    assert "results" in res and len(res["results"]) == 3

    rs = ReferenceScout()
    refs = rs.run({"topic": "python testing"})
    assert "references" in refs and len(refs["references"]) == 3


def test_outliner_and_writer():
    reviewer = OutlineReviewer()
    outline = ["Hook", "Reality", "Insight"]
    review = reviewer.run({"outline": outline})
    assert review["ok"]

    writer = MediumBlogger()
    draft = writer.run({"outline": outline, "prompt": "topic", "anecdote": "once"})
    assert "draft" in draft and "Anecdote" in draft["draft"]

    editor = BlogEditor()
    edited = editor.run({"draft": draft["draft"]})
    assert "edited" in edited


def test_visual_prompt_designer():
    v = VisualPromptDesigner()
    out = v.run({"topic": "focus"})
    assert "hero_prompt" in out and "sumi-e" in out["hero_prompt"]
