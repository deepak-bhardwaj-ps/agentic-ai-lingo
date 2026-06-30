---
title: Lint
short_description: A lint tool checks source code for mistakes, risky patterns, and style problems before the code is run.
category: Software engineering
tags:
  - software
  - code-quality
  - static-analysis
status: draft
aliases: []
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: established
common_misuse:
  - Confusing lint with a formatter, which only changes how code looks.
  - Treating lint as the same as compilation, which checks whether code can be built.
  - Assuming lint always means the same thing in every tool; different linters flag different rules.
related_terms:
  - Linter
  - Linting
  - Static analysis
  - Formatter
  - Compiler
evidence:
  - source_title: ESLint homepage
    source_url: https://eslint.org/
    source_type: official_docs
    relevance: Shows the modern meaning of lint in common JavaScript toolchains.
    key_point: ESLint says it statically analyses code to find problems before and during development.
  - source_title: Pylint documentation
    source_url: https://pylint.readthedocs.io/
    source_type: official_docs
    relevance: Confirms that lint-style tools inspect code without running it and report errors, code smells, and style issues.
    key_point: Pylint analyses code without executing it and checks for errors, standards, and code smells.
  - source_title: Lint, a C Program Checker
    source_url: https://wolfram.schneider.org/bsd/7thEdManVol2/lint/lint.html
    source_type: standards_doc
    relevance: Gives the original meaning of lint as a code checker for C, which explains why the word is used this way today.
    key_point: The original lint command examined C source programs for bugs, portability issues, and wasteful or error-prone constructions.
---

Lint is a tool that checks source code for mistakes, risky patterns, and style problems before the code is run.

In practice, a lint tool scans code and warns you about things like unused variables, suspicious logic, or rules your team has chosen to follow. It does not usually change the code for you. It only points out possible problems.

Lint matters because it catches small mistakes early, before they turn into harder bugs or messy code. Teams also use it to keep code consistent across many people and many files.

Lint is not the same as formatting. A formatter changes how code looks. Lint is also not the same as compiling. A compiler checks whether code can be turned into a working programme. Different lint tools can also disagree because each one has its own rules.
