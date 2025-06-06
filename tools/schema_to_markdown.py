"""
Converts all the schema JSON files to their Markdown representation using the
description field as the major content and other meta fields as
additional information."""

import json
import os
from schema import Framework, ExternalReference, Tool, Capability

from pathlib import Path


def convert_schema_to_markdown(schema_path: Path) -> str:
    """Converts a schema JSON file to Markdown format."""
    with open(schema_path, 'r', encoding='utf-8') as file:
        schema = json.load(file)

    markdown_content = ""

    # If this is a capability schema, add additional information
    # this can be determined by looking at the _ref field
    if 'ref' in schema:

        if schema['ref'].startswith('framework:'):
            framework = Framework(**schema)
            markdown_content += framework.generate_markdown()
            return markdown_content

        if schema['ref'].startswith('tool:'):
            tool = Tool(**schema)
            markdown_content += tool.generate_markdown()
            return markdown_content

        if schema['ref'].startswith('capability:'):
            # Generate the markdown content for the capability
            capability = Capability(**schema)
            markdown_content += capability.generate_markdown()
            return markdown_content

        markdown_content = f"# {schema.get('title', 'Title')}\n\n"
        markdown_content += f"## Overview\n\n{schema.get('description', 'No description available.')}\n\n"

    if 'fields' in schema:
        markdown_content += "## Fields\n"
        for field in schema['fields']:
            markdown_content += f"- **{field['name']}**: {field.get('description', 'No description available.')}\n"

    return markdown_content.strip()


def main():
    """Main function to convert all schema JSON files in the current directory."""

    OUTPUT_DIR = Path('docs')
    FILES_DIR = Path('docs/files')

    # Create the output directory if it doesn't exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Locate the current working directory of python
    current_dir = Path(os.getcwd())

    # Generate index pages
    registry = {}
    registry['tool'] = Tool.load()
    registry['capability'] = Capability.load()
    # registry['framework'] = Framework.load()

    # Generate the framework coverage matrix
    output_file_path = current_dir / OUTPUT_DIR / \
        "capability" / "framework_coverage.md"
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(Capability.generate_framework_matrix(Capability.load()))

    # Generate the phase matrix for capabilities
    output_file_path = current_dir / OUTPUT_DIR / "capability" / "phase_matrix.md"
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(Capability.generate_phase_matrix())

    # Generate the tool coverage matrix for capabilities
    output_file_path = current_dir / OUTPUT_DIR / "capability" / "tool_coverage.md"
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(Capability.generate_tool_matrix())

    # Generate the tool coverage matrix for capabilities as a CSV file
    output_file_path = current_dir / FILES_DIR / "tool_coverage.csv"
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file_path, 'w', encoding='utf-8') as csv_file:
        csv_file.write(Capability.generate_tool_matrix_csv())

    # Generate the index.md file for each component type
    for k in registry.keys():
        items = registry[k]
        print(f"Generating index for {k} with {len(items)} items.")
        _cls = items[0].__class__

        # Add index.md to the output directory
        output_file_path = current_dir / OUTPUT_DIR / \
            f'{_cls.__name__.lower()}' / "index.md"

        output_file_path.parent.mkdir(parents=True, exist_ok=True)

        content = _cls.generate_index_md(items)
        with open(output_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(content)

    # Locate all the schema files nested under the spec directory
    schema_files = list(current_dir.rglob('spec/**/*.json'))
    print(f"Found {len(schema_files)} schema files to convert.")

    for schema_file in schema_files:

        # Determine the folder structure for the markdown file about to be created
        relative_path = schema_file.relative_to(current_dir)

        # Remove the 'spec' part of the path
        relative_path = relative_path.relative_to('spec')

        # Replace the file extension with .md
        relative_path = relative_path.with_suffix('.md')

        # Create the folder structure in the output directory
        # if it does not exist
        output_file_path = OUTPUT_DIR / relative_path
        output_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Convert the schema to markdown
        print(f"Converting {schema_file.name} to {output_file_path.name}")
        markdown_content = convert_schema_to_markdown(schema_file)
        markdown_file = schema_file.with_suffix('.md')

        with open(output_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_content)

        print(f"Converted {schema_file.name} to {markdown_file.name}")


if __name__ == "__main__":
    main()
