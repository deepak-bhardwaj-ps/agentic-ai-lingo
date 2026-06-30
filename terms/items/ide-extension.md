---
title: IDE extension
short_description: A small add-on that adds features to an integrated development environment.
category: Tools and products
tags:
- ide
- extension
- plugin
- developer-tool
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating it as a separate app instead of something that runs inside an IDE.
- Mixing it up with a browser extension or a code library.
- Assuming every editor uses the word "extension"; some call the same thing a plugin or add-on.
related_terms:
- IDE
- plugin
- extension
- VS Code extension
- JetBrains plugin
- editor extension
evidence:
  - source_title: Extension Marketplace - Visual Studio Code
    source_url: https://code.visualstudio.com/docs/configure/extensions/extension-marketplace
    source_type: official_docs
    relevance: Shows a major IDE vendor using "extensions" for add-ons that expand the editor.
    key_point: Microsoft says VS Code extensions add languages, debuggers, and tools to the editor and plug into the UI through official APIs.
  - source_title: Install plugins | IntelliJ IDEA Documentation
    source_url: https://www.jetbrains.com/help/idea/managing-plugins.html
    source_type: official_docs
    relevance: Shows that another major IDE calls the same kind of add-on a plugin.
    key_point: JetBrains says plugins extend the core functionality of IntelliJ IDEA and add features such as version control, coding help, and file support.
  - source_title: Managing IDE extensions :: Eclipse Che Documentation
    source_url: https://www.eclipse.org/che/docs/stable/administration-guide/managing-ide-extensions/
    source_type: official_docs
    relevance: Confirms that "IDE extensions" is also used as a general category across developer environments.
    key_point: Eclipse Che documents IDE extensions as things that can be trusted, pre-installed, and managed across different IDE types.
---

An IDE extension is a small add-on that adds features to an integrated development environment, or IDE.

In practice, it can add things like support for a language, a debugger, code hints, or tools that help you work faster inside the editor.

This matters because an IDE starts with basic features, and extensions let people customise it for a job or a team.

It is not a separate app, and it is not the code for your own programme. It is also not the same thing as a browser extension, even though the word sounds similar.
