---
slug: computer-use
title: Computer Use
short_description: Computer use is when a model interacts with a computer by looking
  at the screen and using mouse and keyboard actions.
category: Core
tags:
- agentic-ai
- ui-automation
- computer-use
- desktop-automation
status: established
aliases:
- computer use
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the same thing as full autonomy.
- Assuming it is more reliable than using a proper API.
- Thinking it is only for websites, when it can also mean desktop apps.
related_terms:
- tool use
- browser automation
- ui automation
- agents
evidence:
- source_title: Computer use tool
  source_url: https://docs.anthropic.com/en/docs/build-with-claude/computer-use
  source_type: official_docs
  relevance: Defines computer use as a model interacting with computer environments
    through screenshots plus mouse and keyboard control.
  key_point: Anthropic describes computer use as autonomous desktop interaction through
    screen viewing and mouse or keyboard actions.
- source_title: Computer use
  source_url: https://developers.openai.com/api/docs/guides/tools-computer-use
  source_type: official_docs
  relevance: Shows the same concept in OpenAI's docs as software operation through
    the user interface.
  key_point: OpenAI says computer use lets a model operate software through the user
    interface by inspecting screenshots and returning interface actions.
- source_title: Computer-Using Agent
  source_url: https://openai.com/index/computer-using-agent/
  source_type: engineering_blog
  relevance: Explains that computer-using agents work with graphical user interfaces
    the way people do.
  key_point: OpenAI describes a computer-using agent as one trained to interact with
    GUIs such as buttons, menus, and text fields.
- source_title: Automate web and desktop apps with computer use
  source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use
  source_type: official_docs
  relevance: Confirms the practical scope across websites and desktop apps, and notes
    the value when no API is available.
  key_point: Microsoft describes computer use as interacting with websites and desktop
    apps through a virtual mouse and keyboard.
---

## Meaning

Computer use is when a model works with a computer by looking at the screen and using mouse and keyboard actions instead of calling a software API.

## What it means in practice

The model can click buttons, open menus, type text, and scroll through a web page or desktop app. It is useful when there is no clean API to use, or when the task has to happen inside a normal app that people also use.

## Why it matters

This gives agents access to many real systems that were not built for automation. It can help with older software, websites without APIs, and tasks that only exist in a graphical interface.

## What it is not

Computer use is not the same as full autonomy. It can still make mistakes, miss details on the screen, or click the wrong thing. It is also not the best choice when a proper API is available, because APIs are usually more reliable and easier to check.
