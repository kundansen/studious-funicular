"""CLI to orchestrate blog creation with per-blog folder structure and Vale style checking."""
import argparse
import os
from blog_agents import tools
from blog_agents.concrete import (
    IdeaExpander,
    MarketResearcher,
    ReferenceScout,
    OutlineGenerator,
    OutlineReviewer,
    MediumBlogger,
    BlogEditor,
    StyleChecker,
    VisualPromptDesigner,
)


def run_pipeline(blog_name: str, prompt: str, anecdote: str = "", skip_lint: bool = False, template: str = None):
    """
    Run the full blog pipeline.
    
    Creates folder structure:
        blogs/
            <blog-slug>/
                draft.md
                draft_edited.md
                blog_data/
                    research_*.json
                    references_*.json
                    outline.json
                    hero_prompt.yaml
    """
    blog_dir = tools.set_blog_context(blog_name)
    print(f"[Setup] Blog folder: {blog_dir}")
    
    idea = IdeaExpander()
    mr = MarketResearcher()
    ref = ReferenceScout()
    outliner = OutlineGenerator()
    reviewer = OutlineReviewer()
    writer = MediumBlogger()
    editor = BlogEditor()
    style = StyleChecker()
    visual = VisualPromptDesigner()

    print("\n[1/8] IdeaExpander: collecting questions...")
    ideas = idea.run({"prompt": prompt})
    print("Questions to ask user:")
    for q in ideas["questions"]:
        print(" - ", q)

    print("\n[2/8] MarketResearcher: scanning web...")
    research = mr.run({"topic": prompt})
    print("Top results:")
    for s in research["summary"]:
        print(" - ", s)

    print("\n[3/8] ReferenceScout: finding refs...")
    refs = ref.run({"topic": prompt})
    for r in refs["references"]:
        print(" - ", r["title"])

    print("\n[4/8] OutlineGenerator: creating outline...")
    outline_result = outliner.run({"topic": prompt, "template": template})
    outline = outline_result["outline"]
    print(f"  Template: {outline_result['template_name']}")
    for section in outline:
        print(f"    - {section}")

    print("\n[5/8] OutlineReviewer: reviewing outline")
    review = reviewer.run({"outline": outline})
    if not review["ok"]:
        print("Outline issues:", review["issues"])
        print("Please edit outline and retry.")
        return

    print("\n[6/8] MediumBlogger: writing draft...")
    draft = writer.run({"outline": outline, "prompt": prompt, "anecdote": anecdote})
    print("Draft saved to:", draft["draft_path"])

    print("\n[7/8] BlogEditor: editing draft...")
    edited = editor.run({"draft": draft["draft"]})
    print("Edited draft saved to:", edited["edited_path"])

    if not skip_lint:
        print("\n[7.5/8] StyleChecker: running Vale...")
        lint_result = style.run({"draft_name": "draft_edited.md"})
        if lint_result["error_count"] == -1:
            print("  ⚠️ ", lint_result["output"])
        else:
            print(f"  Errors: {lint_result['error_count']}, Warnings: {lint_result['warning_count']}")
            if lint_result["error_count"] > 0 or lint_result["warning_count"] > 0:
                print("  Run `vale <draft>` for details, or ask Amp to fix style issues.")

    print("\n[8/8] VisualPromptDesigner: creating hero prompt")
    hero = visual.run({"topic": prompt})
    print("Hero prompt saved to:", hero["hero_prompt_path"])

    print(f"\n✅ Pipeline complete. Files in: {blog_dir}/")
    print(f"   - draft.md (raw)")
    print(f"   - draft_edited.md (edited)")
    print(f"   - blog_data/ (research, refs, hero prompt)")


def lint_blog(blog_name: str, draft_name: str = "draft_edited.md"):
    """Run Vale on an existing blog's draft."""
    tools.set_blog_context(blog_name)
    style = StyleChecker()
    result = style.run({"draft_name": draft_name})
    
    if result["error_count"] == -1:
        print(result["output"])
        return
    
    print(result["output"])
    print(f"\nSummary: {result['error_count']} errors, {result['warning_count']} warnings")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blog creation pipeline with Vale style checking")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # create command
    create_parser = subparsers.add_parser("create", help="Create a new blog")
    create_parser.add_argument("name", help="Blog name (used for folder)")
    create_parser.add_argument("prompt", help="Topic or seed prompt")
    create_parser.add_argument("--anecdote", help="Short personal anecdote", default="")
    create_parser.add_argument("--template", help="Outline template name (random if not specified)", default=None)
    create_parser.add_argument("--skip-lint", action="store_true", help="Skip Vale style check")
    
    # lint command
    lint_parser = subparsers.add_parser("lint", help="Run Vale on existing blog")
    lint_parser.add_argument("name", help="Blog folder name")
    lint_parser.add_argument("--draft", help="Draft filename", default="draft_edited.md")
    
    # list command
    list_parser = subparsers.add_parser("list", help="List existing blogs")
    
    args = parser.parse_args()
    
    if args.command == "create":
        run_pipeline(args.name, args.prompt, args.anecdote, args.skip_lint, args.template)
    elif args.command == "lint":
        lint_blog(args.name, args.draft)
    elif args.command == "list":
        blogs_dir = os.path.join(os.path.dirname(__file__), "blogs")
        if os.path.exists(blogs_dir):
            blogs = [d for d in os.listdir(blogs_dir) 
                     if os.path.isdir(os.path.join(blogs_dir, d)) and not d.startswith('.')]
            if blogs:
                print("Existing blogs:")
                for b in sorted(blogs):
                    print(f"  - {b}")
            else:
                print("No blogs yet. Create one with: python blog_runner.py create <name> <prompt>")
        else:
            print("No blogs folder yet.")
    else:
        parser.print_help()
