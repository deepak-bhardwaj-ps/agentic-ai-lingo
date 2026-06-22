# Contributing

This repository is a glossary of agentic AI terms. Each term lives in `terms/items/<slug>.md` and the root `README.md` is generated from those files.

## Adding a term

1. Create a new markdown file in `terms/items/`.
2. Add complete YAML frontmatter.
3. Include `short_description` in the frontmatter.
4. Write the body with useful detail, not just the one-line summary.
5. Run `python scripts/rebuild-dictionary.py`.
6. Commit the updated term file and regenerated `README.md`.

## Frontmatter expectations

Required:

- `title`
- `category`
- `short_description`

Recommended:

- `slug`
- `name`
- `aliases`
- `tags`
- `status`
- `signalScore`
- `buzzScore`
- `enterpriseReadiness`
- `firstSeen`
- `popularizedBy`
- `trend`

`short_description` should describe the meaning of the term from a reader’s point of view. It should not describe the project, the file, or the fact that the term exists in the dictionary.

## Build rules

The build script is the source of truth for:

- frontmatter validation
- wikilink normalisation and auto-linking
- `README.md` regeneration

If `short_description` is missing, the build fails. That is intentional. The author must add it manually.

## Local hook setup

To run the pre-commit hook from this repo:

```sh
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

After that, every commit will run the rebuild script before the commit is accepted.

## PR expectations

Pull requests must include:

- the new or updated term file
- the regenerated `README.md` if the term list changed

CI will fail if the build is out of date or a term is missing required metadata.
