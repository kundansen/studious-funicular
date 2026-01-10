"""Simple CLI to orchestrate blog creation using the agents."""
from blog_agents.concrete import (
    IdeaExpander,
    MarketResearcher,
    ReferenceScout,
    OutlineReviewer,
    MediumBlogger,
    BlogEditor,
    VisualPromptDesigner,
)


def run_pipeline(prompt: str, anecdote: str = ""):
    idea = IdeaExpander()
    mr = MarketResearcher()
    ref = ReferenceScout()
    reviewer = OutlineReviewer()
    writer = MediumBlogger()
    editor = BlogEditor()
    visual = VisualPromptDesigner()

    print("[1/7] IdeaExpander: collecting questions...")
    ideas = idea.run({"prompt": prompt})
    print("Questions to ask user:")
    for q in ideas["questions"]:
        print(" - ", q)

    print("[2/7] MarketResearcher: scanning web...")
    research = mr.run({"topic": prompt})
    print("Top results:")
    for s in research["summary"]:
        print(" - ", s)

    print("[3/7] ReferenceScout: finding refs...")
    refs = ref.run({"topic": prompt})
    for r in refs["references"]:
        print(" - ", r["title"])

    print("[4/7] Create outline (mock)")
    outline = ["Hook: The Lie", "Reality: The Grime", "Insight: The Metaphor", "Call to Arms: The Hope"]

    print("[5/7] OutlineReviewer: reviewing outline")
    review = reviewer.run({"outline": outline})
    if not review["ok"]:
        print("Outline issues:", review["issues"])
        print("Please edit outline and retry.")
        return

    print("[6/7] MediumBlogger: writing draft...")
    draft = writer.run({"outline": outline, "prompt": prompt, "anecdote": anecdote})
    print("Draft saved to:", draft["draft_path"])

    print("[7/7] BlogEditor: editing draft...")
    edited = editor.run({"draft": draft["draft"]})
    print("Edited draft saved to:", edited["edited_path"])

    print("[Optional] VisualPromptDesigner: creating hero prompt")
    hero = visual.run({"topic": prompt})
    print("Hero prompt saved to:", hero["hero_prompt_path"])

    print("Pipeline complete. Review the files in blog_data/")


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("prompt", help="Topic or seed prompt for the blog")
    p.add_argument("--anecdote", help="Short personal anecdote to include", default="")
    args = p.parse_args()
    run_pipeline(args.prompt, args.anecdote)
