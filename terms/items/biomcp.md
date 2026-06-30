---
title: BioMCP
short_description: A biomedical MCP tool and server for searching trusted health and research data from one command surface.
category: Tools and products
tags:
  - MCP
  - biomedical
  - research
status: draft
aliases:
  - Biomedical Model Context Protocol
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating BioMCP as a benchmark, model, or general MCP standard rather than a specific biomedical tool.
related_terms:
  - Model Context Protocol
  - biomedical search
  - clinical trials
  - PubMed
  - genomic variants
evidence:
  - source_title: BioMCP home page
    source_url: https://biomcp.org/
    source_type: official_docs
    relevance: This is the project’s own description and shows what BioMCP is intended to do.
    key_point: BioMCP presents itself as a single command surface for biomedical search and retrieval across trusted sources.
  - source_title: BioMCP GitHub repository
    source_url: https://github.com/genomoncology/biomcp
    source_type: official_docs
    relevance: The repository confirms the product name and explains the workflow for researchers, clinicians, and agents.
    key_point: BioMCP is described as a biomedical MCP toolkit that lets users query multiple biomedical sources with one command grammar.
  - source_title: What Is BioMCP?
    source_url: https://biomcp.org/concepts/what-is-biomcp/
    source_type: official_docs
    relevance: This page defines the project more plainly and separates the command-line tool from the MCP server surface.
    key_point: BioMCP combines a stable command grammar with an MCP interface for research and clinical-informatics workflows.
---

BioMCP is a biomedical tool and server that helps people search trusted health and research data from one place.

In practice, it gives a single command surface for looking up things like clinical trials, published papers, and gene or variant data without jumping between many different websites.

The term matters because biomedical information is spread across many systems, and BioMCP is designed to make that work faster and more consistent for researchers, clinicians, and agents.

BioMCP is not a medical model, and it is not a benchmark for judging other systems. It is a specific tool built around the Model Context Protocol so software can reach biomedical data sources in a structured way.
