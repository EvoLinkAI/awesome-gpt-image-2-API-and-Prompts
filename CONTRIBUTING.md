# Contributing

Thank you for helping improve this curated GPT Image 2 prompt collection. Contributions should be source-backed, reproducible, and easy for readers to reuse.

## What belongs here

- Public GPT Image 2 prompts with a clear prompt boundary and at least one representative output.
- Corrections to source attribution, author links, prompt text, media, or categorization.
- Documentation, accessibility, localization, and repository-maintenance improvements.

Showcase-only posts without a public prompt can be proposed for a gallery, but they must not be presented as reproducible prompt cases.

## Submit a prompt

The simplest path is the [prompt submission issue form](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/issues/new?template=submit-prompt.yml).

Every proposal must include:

- a short title;
- the complete prompt exactly as publicly shared;
- the original public source URL, or a statement that the issue is the original publication;
- the original author name and profile URL;
- a category;
- at least one output image;
- input or reference media when the result depends on it;
- confirmation that the submitter has the right to share the prompt and media.

Do not invent missing prompt text, authors, dates, model claims, or results.

## Open a pull request

1. Create a focused branch.
2. Update the English source, `README.md`, first.
3. Keep the matching `cases/*.md` page and `data/ingested_tweets.json` source index consistent.
4. Update all ten localized README files when visible structure or public copy changes. Prompt blocks, URLs, model IDs, commands, and environment variables remain unchanged.
5. Add an entry to `docs/update-log.md`.
6. Complete every item in the pull request template.

Localized files must not contain TODO markers, translation placeholders, or untranslated scaffolding. If a contributor cannot complete localization, the pull request should remain a draft until a maintainer finishes that work.

## Case and media rules

- Preserve the existing category and case shape.
- Put source attribution in the case title or an explicit source line.
- Keep public prompt text in an unlabelled fenced code block.
- Use descriptive image alt text.
- Do not add raw video as the visible README media. Use a poster image linked to a playable video URL.
- Do not commit secrets, private exports, internal review notes, or local `.codex/` evidence.
- Do not add files larger than 25 MB without a recorded maintainer decision.
- Avoid third-party hotlinks for accepted public media. Maintainers may migrate media to EvoLink R2 before publication.

## Repository boundary

This repository's primary content surface is the prompt collection. Related API and installable-skill surfaces are linked as separate repositories or documentation targets. A pull request that changes runnable API or skill-release material requires a separately approved scope and the corresponding sibling-agent audit.

## Validate your change

Run these commands from the repository root:

```bash
python3 scripts/verify_prompt_repo.py
python3 -m json.tool data/ingested_tweets.json >/dev/null
git diff --check
find . \( -name .DS_Store -o -name __pycache__ -o -name '*.pyc' \) -print
```

The final command should print nothing. Maintainers also run template, public-link, localization, and rendered-media audits before publication.

## Review expectations

Maintainers may request changes when evidence is incomplete, the source is duplicated, the prompt boundary is unclear, media cannot be verified, or the submission does not add reusable value. Acceptance is based on quality and evidence, not submission order.
