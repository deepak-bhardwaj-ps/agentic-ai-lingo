---
title: Browser Use
short_description: Browser use means letting an agent interact with a website through
  a browser instead of an API.
category: Core
tags:
- browser
- automation
- web
- agents
status: established
aliases:
- browser automation
- web browser use
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: established
common_misuse:
- Treating it as a formal standard
- Assuming it is safer or more reliable than using an API
- Confusing it with web search or general browsing
related_terms:
- computer use
- browser automation
- web agent
- prompt injection
evidence:
- source_title: Computer use tool
  source_url: https://docs.anthropic.com/en/docs/build-with-claude/computer-use
  source_type: official_docs
  relevance: Shows the browser-and-desktop interaction pattern that browser use builds
    on.
  key_point: Anthropic describes computer use as a model observing screens and taking
    actions such as clicking and typing, which includes browser-based work.
- source_title: Computer use
  source_url: https://developers.openai.com/api/docs/guides/tools-computer-use
  source_type: official_docs
  relevance: Gives practical guidance for browser-style agent work.
  key_point: OpenAI says page content should be treated as untrusted and high-impact
    actions should be reviewed.
- source_title: Browser Use Open Source
  source_url: https://docs.browser-use.com/open-source/introduction
  source_type: industry_article
  relevance: Shows how the term is used in current tooling.
  key_point: Browser Use is presented as a Python library for AI browser automation
    that lets an agent interact with websites.
---

Browser use means an agent uses a web browser to look at a page and do tasks on it, like clicking, typing, scrolling, and moving between pages.

In practice, the agent is acting through the same kind of screen a person would use. It may fill in a form, open a link, or check information on a website. This is useful when there is no good API for the job, or when the task is easiest to do directly on the site.

This term matters because many real tasks still live inside websites. Browser use can help automate repetitive web work, but it is usually less reliable than using an API because websites change often and can be designed to mislead the agent.

It is not the same as web search. It is not just reading pages, and it is not a formal technical standard. It also does not mean the agent should trust what it sees on a page; web content can contain instructions that should not be followed.
