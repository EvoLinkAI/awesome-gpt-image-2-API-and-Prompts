# Repository Maintenance

This document defines the public source of truth and the minimum update workflow for this GPT Image 2 prompt repository.

## Public source of truth

- `README.md` is the canonical English landing page and structure source.
- `README_<locale>.md` files are completed localized public variants.
- The authoritative public namespace is the English README display order: exactly 462 unique sources numbered contiguously as `Case 1` through `Case 462`. Localized README files preserve that source order and numbering.
- The README front door is prompt-first: Introduction, Quick Start, model overview, News, Menu, prompt categories, Related Repositories, then Acknowledge.
- `cases/*.md` contains category-level archive pages. Entries whose source URL belongs to the authoritative 462-case set must use the matching root Case number; archive-only historical entries remain outside that authoritative namespace until a separate archive cleanup is approved.
- `data/ingested_tweets.json` is the public source-URL registry used for deduplication and provenance.
- `docs/update-log.md` records published prompt batches and maintenance changes.
- `images/` contains the checked-in media source set. Public README media should be migrated to R2 according to the current repository contract before publication, unless an explicit exception is recorded.

Local candidate queues, semantic-review files, audit evidence, API smoke evidence, and other agent-run artifacts belong under ignored `.codex/` paths or the run evidence directory. They are not public repository content unless a future public-artifact decision explicitly changes that boundary.

## Case acceptance

A new public prompt case needs:

1. an original public source URL;
2. an author name and profile URL when available;
3. a clear reusable prompt copied from the source;
4. a category and title;
5. an input/output or output-only media decision;
6. media that can be verified and published safely;
7. a deduplication key, normally the source URL;
8. a semantic-review decision of selected/high confidence.

Deferred, unsure, dropped, duplicated, showcase-only, or incomplete candidates do not enter public prompt sections.

## Update checklist

1. Inspect the current branch, remote, dirty worktree, and prior run artifacts.
2. Use an isolated worktree when unrelated local changes exist.
3. Freeze the candidate collection window and record collection counts.
4. Review every candidate and record selected, deferred, unsure, and dropped counts with reasons.
5. Assign the next global Case number from the English README, then update `README.md`, matching `cases/*.md` entries, the source index anchor, media, and this update log.
6. Run the English gate before touching localized files.
7. Update all ten localized README and category files with real visible-text translation.
8. Run the repository, localization, media, public-link, UTM, and template audits.
9. Fix every P0/P1 finding or attach an owner-approved, run-scoped waiver.
10. Run `git diff --check`, review the exact staged scope, commit, push, and record remote readback evidence.

## Validation commands

Run from a clean checkout or isolated worktree:

```bash
python3 scripts/verify_prompt_repo.py
python3 -m json.tool data/ingested_tweets.json >/dev/null
git diff --check
find . \( -name .DS_Store -o -name __pycache__ -o -name '*.pyc' \) -print
```

The repository verifier checks the required README set, prompt-first heading and anchor order, synchronized Menu targets, absence of inline API runtime instructions, related-repository links, localized case-count parity, referenced local media, baseline community files, and JSON readability. It is intentionally narrower than the agent contract. Publication also requires:

- the shape-specific template audit;
- the public-surface link and UTM audit;
- localization semantic review;
- media inventory, R2 upload evidence, and rendered GitHub/camo checks;
- a real API smoke report or an owner-approved waiver;
- commit, push, About metadata, and public readback evidence.

## Related-repository boundary

This prompt repository may link to verified API documentation, API repositories, workflows, and installable skills. It does not claim those external surfaces passed their own release gates. Runnable API or Skill release work is audited by the sibling release agent under a separately approved scope.
