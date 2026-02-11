Draft prompt (use in Blog Writer mode after outline is accepted):

"You are a Blog Writer in the 'Kundan' voice. Use the accepted outline and anecdote. Produce a ~1500-word draft divided into 5–7 sections, metaphor-first, with varied sentence rhythms and one strong personal anecdote woven across sections. Follow the Anti-AI Writing Guidelines in `blog_writing_instructions.md`. Return a title, 3 headline options, the draft in Markdown, and a 100–150 word blurb."

---

## Post-Draft: Style Check

After drafting, run Vale to check prose quality:

```bash
python blog_runner.py lint "<blog-name>"
```

Or ask Amp: "Run vale on my draft and fix any errors"

Fix errors before proceeding to the visual prompt stage. See `style_check_prompt.md` for details.
