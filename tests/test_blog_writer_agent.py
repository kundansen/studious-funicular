from blog_agents.blog_writer_agent import BlogWriterAgent


def test_intake_mode():
    ag = BlogWriterAgent()
    res = ag.run({"mode": "intake", "prompt": "test topic"})
    assert "questions" in res and isinstance(res["questions"], list)


def test_scan_mode():
    ag = BlogWriterAgent()
    res = ag.run({"mode": "scan", "prompt": "python tooling"})
    assert "research" in res and "references" in res


def test_outline_mode_and_review():
    ag = BlogWriterAgent()
    outline = ["Hook", "Reality", "Insight"]
    res = ag.run({"mode": "outline", "outline": outline})
    assert res.get("outline_review", {}).get("ok")


def test_draft_edit_visual_full():
    ag = BlogWriterAgent()
    res = ag.run({"mode": "full", "prompt": "Why text editors matter", "anecdote": "I once lost a patch"})
    assert res.get("draft")
    assert res.get("edited")
    assert res.get("hero_prompt")
    # meta file should be saved
    assert res.get("meta_path")
