---
slug: agentic-browser
title: Agentic Browser
short_description: A browser that lets an AI inspect web pages and carry out tasks for a user.
category: Core
tags:
  - browser
  - agents
  - web
status: Emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a formal web standard
  - Assuming it can safely use every website without checks
  - Confusing it with simple browser automation that follows a fixed script
related_terms:
  - computer use
  - browser automation
  - agentic web
  - function calling
  - human approval
evidence:
  - source_title: Computer use
    source_url: https://developers.openai.com/api/docs/guides/tools-computer-use
    source_type: official_docs
    relevance: Shows a current vendor definition of software that can operate a user interface by looking at screenshots and returning UI actions.
    key_point: OpenAI describes computer use as letting a model operate software through the user interface, which matches the action-taking part of an agentic browser.
  - source_title: Computer use tool
    source_url: https://docs.anthropic.com/en/docs/build-with-claude/computer-use
    source_type: official_docs
    relevance: Confirms that major model providers now support browser-like UI control as a distinct capability.
    key_point: Anthropic treats computer use as client-side UI control with screenshots, mouse actions, and keyboard input, which is the practical basis for an agentic browser.
  - source_title: Introducing ChatGPT agent: bridging research and action
    source_url: https://openai.com/index/introducing-chatgpt-agent/
    source_type: engineering_blog
    relevance: Shows the term in product use, where a browser-capable agent completes tasks like research and bookings with user guidance.
    key_point: OpenAI describes an agent that thinks and acts using tools to complete tasks, which reflects how agentic browsers are commonly understood in practice.
  - source_title: Introducing ChatGPT Atlas
    source_url: https://openai.com/index/introducing-chatgpt-atlas/
    source_type: engineering_blog
    relevance: Gives a current example of a browser with built-in ChatGPT support rather than a separate assistant.
    key_point: OpenAI frames Atlas as a browser with ChatGPT built in, which shows how vendors are blending browsing and agent-like help.
  - source_title: Go behind the browser with Chrome's new AI features
    source_url: https://blog.google/products-and-platforms/products/chrome/new-ai-features-for-chrome/
    source_type: engineering_blog
    relevance: Shows another major browser vendor adding AI features directly into the browser experience.
    key_point: Google describes AI built into Chrome to help people get things done while staying safe online, supporting the idea that the browser itself can become agent-like.
---

An agentic browser is a browser that can look at web pages and take actions for a user.

In practice, it can open pages, click buttons, fill in forms, scroll, and move through a site to finish a task. A person still sets the goal and should check important or risky steps.

The term matters because many everyday jobs happen in browsers. If the browser can act for you, it can reduce repetitive work like searching, booking, and form filling.

It is not a formal standard. It is also not the same as simple browser automation that follows one fixed script. The key idea is that the browser can inspect what is on the page and choose the next step.

The term is still unsettled. People often use it to mean a browser with built-in AI help that can act, not just explain what is on the page.
