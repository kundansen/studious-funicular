# Style Check Prompt

Use after drafting to check prose quality with Vale:

---

Run Vale on the current draft to check for style issues:

```
python blog_runner.py lint "<blog-name>"
```

Or ask Amp directly:
> "Run vale on my draft and fix the errors"

## Common Vale Issues to Address

1. **Passive voice** → Rewrite with active verbs
2. **Weasel words** (completely, usually, surprisingly) → Be specific or remove
3. **Too wordy** ("it was", "in order to") → Simplify
4. **Clichés** ("for free", "at the end of the day") → Rephrase

## Adding Custom Terms

If Vale flags valid terms (gaming jargon, tech terms), add them to:
```
blogs/.vale/styles/config/vocabularies/Blog/accept.txt
```

## Style Check Workflow

1. Write draft
2. Run `python blog_runner.py lint <blog-name>`
3. Fix errors (required) and high-priority warnings
4. Ask Amp: "Fix the Vale errors in my draft"
5. Re-run lint to confirm
