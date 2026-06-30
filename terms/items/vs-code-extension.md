---
title: VS Code extension
short_description: A small add-on that adds features to Visual Studio Code.
category: Tools and products
tags:
  - visual-studio-code
  - extension
  - developer-tool
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
  - Treating it as a separate app instead of something that runs inside VS Code.
  - Mixing it up with a browser extension or a generic plugin for another editor.
  - Assuming every editor uses the same word for the same thing.
related_terms:
  - Visual Studio Code
  - IDE extension
  - extension marketplace
  - plugin
  - add-on
evidence:
  - source_title: Extension Marketplace - Visual Studio Code
    source_url: https://code.visualstudio.com/docs/configure/extensions/extension-marketplace
    source_type: official_docs
    relevance: This is Microsoft’s main page for VS Code extensions and gives the clearest official definition of what they do.
    key_point: VS Code extensions let you add languages, debuggers, and tools to your installation and plug into the editor through official APIs.
  - source_title: Use extensions in Visual Studio Code
    source_url: https://code.visualstudio.com/docs/getstarted/extensions
    source_type: official_docs
    relevance: Confirms the everyday user meaning of the term and shows that extensions are installed to add new features.
    key_point: Microsoft says extensions add new features, themes, and more to VS Code.
  - source_title: VS Code API
    source_url: https://code.visualstudio.com/api/references/vscode-api
    source_type: official_docs
    relevance: Shows that a VS Code extension is not just a label but a package that uses the extension API to extend the editor.
    key_point: Microsoft describes the VS Code API as the set of JavaScript APIs used in a Visual Studio Code extension.
---

A VS Code extension is a small add-on that adds features to Visual Studio Code.

In practice, an extension can give VS Code support for a language, a debugger, a theme, or other tools that help you work inside the editor.

This matters because VS Code starts with basic features, and extensions let people tailor it for different jobs without changing the editor itself.

It is not a separate app, and it is not the code for your own programme. It is also not the same thing as a browser extension, even though the word sounds similar.
