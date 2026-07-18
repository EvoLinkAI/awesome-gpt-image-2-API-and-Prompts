## Summary

Describe the user-facing change and why it belongs in this repository.

## Change type

- [ ] Prompt case or gallery content
- [ ] Source, attribution, or media correction
- [ ] Localization
- [ ] Documentation or maintenance
- [ ] Other

## Source and case evidence

- [ ] Every new community case has an original public source URL.
- [ ] The author name and profile URL are recorded.
- [ ] Prompt text is copied verbatim from the public or owner-provided source; no prompt was invented.
- [ ] Category, title, prompt boundary, input/output shape, and media source are fixed.
- [ ] The source URL is not already present in `data/ingested_tweets.json`.
- [ ] Input and output labels match the displayed media.

Source URLs:

-

## Localization

- [ ] `README.md` was updated first.
- [ ] All ten localized README files preserve the same public structure and case count.
- [ ] Visible prose is translated; prompt/code blocks, URLs, model IDs, commands, and environment variables are unchanged.
- [ ] No TODO, translation-pending marker, or untranslated scaffolding remains.
- [ ] Not applicable; explain why below.

## Media

- [ ] Media paths or URLs resolve.
- [ ] Images have accurate alt text.
- [ ] No file larger than 25 MB was added without a recorded maintainer decision.
- [ ] Public media uses R2, or the pull request records the approved exception/migration step.
- [ ] Video uses an R2 poster frame linked to a playable R2 video URL, not a direct visible video embed.
- [ ] Not applicable.

## Repository boundary

- [ ] This change stays within prompt/guide content and only links to related API or Skill surfaces.
- [ ] If runnable API or Skill material changed, the separately approved scope and sibling-agent audit are linked below.

## Validation

- [ ] `python3 scripts/verify_prompt_repo.py`
- [ ] `python3 -m json.tool data/ingested_tweets.json >/dev/null`
- [ ] `git diff --check`
- [ ] System-file scan returned no unexpected `.DS_Store`, `__pycache__`, or `*.pyc` files.
- [ ] The public link, template, localization, media, and rendered-GitHub checks are attached or left for a maintainer before merge.

## Notes, exceptions, or follow-up

List any owner-approved exception, external blocker, or action that must happen before publication.
