---
slug: star-topology
name: Star Topology
category: Runtime
title: Star Topology
short_description: A communication shape where one central node talks to several others.
aliases: []
tags: []
status: active
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse: []
related_terms: []
evidence: []
---

## Definition

Star topology is a way of connecting parts of a system so that one central node talks to several others.

## What it means in practice

In an agent system, the central node is usually a coordinator. It sends work to other agents or workers, collects their results, and decides what happens next.

This makes the flow easy to understand because most messages go through one place.

## Why it matters

It is useful when you want one place to manage tasks, keep track of progress, and stop the system when the job is done.

It also makes the structure simple to draw and reason about.

## What it is not

It is not a complete system design by itself.

It does not say how the central node chooses work, how shared state is stored, what happens when something fails, or how the system ends.

It is also not a special AI term. It is a borrowed network idea used to describe a simple communication shape.
