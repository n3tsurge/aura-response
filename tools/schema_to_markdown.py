"""
Converts all the schema JSON files to their Markdown representation using the
description field as the major content and other meta fields as
additional information."""

import json
import os
from pathlib import Path

def convert_schema_to_markdown(schema_path: Path) -> str:
    """Converts a schema JSON file to Markdown format."""
    with open(schema_path, 'r', encoding='utf-8') as file:
        schema = json.load(file)

    markdown_content = f"# {schema.get('name', 'Schema')}\n\n"
    markdown_content += f"## Description\n{schema.get('description', 'No description available.')}\n\n"

    if 'fields' in schema:
        markdown_content += "## Fields\n"
        for field in schema['fields']:
            markdown_content += f"- **{field['name']}**: {field.get('description', 'No description available.')}\n"

    return markdown_content.strip()

def main():
    """Main function to convert all schema JSON files in the current directory."""
    current_dir = Path(__file__).parent
    schema_files = list(current_dir.glob('*.json'))

    for schema_file in schema_files:
        markdown_content = convert_schema_to_markdown(schema_file)
        markdown_file = schema_file.with_suffix('.md')
        
        with open(markdown_file, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_content)
        
        print(f"Converted {schema_file.name} to {markdown_file.name}")
        
if __name__ == "__main__":
    main()