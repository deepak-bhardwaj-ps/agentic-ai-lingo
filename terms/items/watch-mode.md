---
title: Watch mode
short_description: A mode where a tool keeps running and reacts when files change.
category: Knowledge and wiki systems
tags:
  - file watching
  - rebuilds
  - development workflow
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
  - Treating watch mode as the same thing as live reload, hot reload, or auto-save. Those are related, but they are not the same.
  - Assuming watch mode only means websites. It is also used by compilers, bundlers, and note or wiki tools that rebuild content when files change.
related_terms:
  - file watching
  - incremental build
  - rebuild
  - hot reload
  - live reload
evidence:
  - source_title: Watch and WatchOptions | webpack
    source_url: https://webpack.js.org/configuration/watch/
    source_type: official_docs
    relevance: Webpack gives a clear, modern definition of watch mode for build tools.
    key_point: After the first build, webpack keeps watching resolved files and rebuilds when they change.
  - source_title: Documentation - tsc CLI Options | TypeScript
    source_url: https://www.typescriptlang.org/docs/handbook/compiler-options.html
    source_type: official_docs
    relevance: TypeScript shows that watch mode is a compiler feature, not just a web-dev feature.
    key_point: The compiler can watch input files and keep updating work while files change.
  - source_title: Building for Production | Vite
    source_url: https://vite.dev/guide/build
    source_type: official_docs
    relevance: Vite shows the same pattern in another current toolchain.
    key_point: Build tools can run in watch mode so they rebuild when source files change.
---
Watch mode is a way for a tool to keep running and notice when files change.

In practice, you start the tool once and leave it open. When you edit a file, it does the same job again, such as rebuilding a site, checking code, or updating generated output.

It matters because it saves time. You do not need to run the command again after every small change, so feedback is faster while you work.

It is not the same as hot reload or live reload. Those usually refresh what you see in a browser or app. Watch mode is the wider idea of a tool watching files and repeating work.
