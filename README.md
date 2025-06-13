# Adaptive Unified Response Architecture: Response

## Overview

The AURA project aims to create a unified structure for mapping security detection, response, and remediation across various security tools, frameworks, and standards. This project is designed to enhance the efficiency and effectiveness of security operations by providing a standardized approach to incident response.

## Documentation

Full documentation here: [AURA Response Documentation](./docs/index.md)

## TODO

- Introduce the concept of "relevance" or "effectiveness".  For example Microsoft DNS may be a good source for hosts communicating with a domain but the SIEM may be a more relevant tool as it collects DNS logs from across multiple tools and environments. Tools can have their effectiveness rated on a scale of 1-5 (including up to 2 decimals).  Tools with more documentation, data source mapping, capabilities mapped can also have their effectiveness dynamically raised.  Tools get sorted by most effective to least-effective on capability pages.
- Introduce the concept of "partial" coverage or "configure" coverage where a control can be coveraged based on certain pre-existing conditions or scenarios.  For example, SentinelOne can see URL information if the browser extension is installed.  Or SentinelOne can determine communication with internal domains but only using DNS resolution and IP Connect correlation.
- Introduce new capabilities:
  - Enrich IP address (identify)
  - Enrich domain name (identify)
  - Enrich URL (identify)
  - Enrich asset information (identify) - owner, make, model, os, business unit, geography, groups, etc.
  - Enrich user information (identify) - groups, owned assets, geography, etc.
  - List certificates issued for domain (identify)
  - Gather WHOIS information for domain (identify)
  - Gather DNS history for a domain (identify)
  - Gather memory dump from endpoint (identify)
  - Image disk (identify)
  - Isolate endpoint from network (containment)
  - Reconnect endpoint to network (recovery)
  - Block external USB devices (containment)
  - Unblock external USB devices (recovery)

## Building the Documentation

```bash
pip install poetry
poetry install
poetry run python tools/schema_to_markdown.py
```

## Serving the Documentation

```bash
poetry run mkdocs serve
```