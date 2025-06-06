# Adaptive Unified Response Architecture: Response

## Overview

The AURA project aims to create a unified structure for mapping security detection, response, and remediation across various security tools, frameworks, and standards. This project is designed to enhance the efficiency and effectiveness of security operations by providing a standardized approach to incident response.

## Documentation

Full documentation here: [AURA Response Documentation](./docs/index.md)

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