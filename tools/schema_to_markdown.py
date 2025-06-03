"""
Converts all the schema JSON files to their Markdown representation using the
description field as the major content and other meta fields as
additional information."""

import json
import os
from pydantic import BaseModel, Field, PrivateAttr
from pathlib import Path

class ExternalReference(BaseModel):
    """Model representing an external reference with a name and URL."""
    name: str = Field(..., description="The name of the external reference.")
    url: str = Field(..., description="The URL of the external reference.")
    type: str = Field(default='website', description="The type of the external reference.", validators=[lambda v: v in ['website', 'document', 'other']])
    
    def __str__(self):
        return f"{self.name} ({self.url})"

class Framework(BaseModel):
    """Model representing a framework with its title and external references."""
    id: str = Field(default=None, description="The unique identifier for the framework.")
    ref: str = Field(default=None, description="A reference to the framework.")
    author: str = Field(..., description="The author of the framework.")
    category: list[str] = Field(
        default_factory=list, description="Categories associated with the framework.")
    created_on: str = Field(...,
                            description="The date when the framework was created.")
    description: str = Field(...,
                             description="A brief description of the framework.")
    title: str = Field(..., description="The title of the framework.")
    external_references: list[ExternalReference] = Field(
        default_factory=list,
        description="A list of external references related to the framework."
    )
    friendly_name: str = Field(
        default=None,
        description="A user-friendly name for the framework, if applicable."
    )
    title: str = Field(
        default=None,
        description="The title of the framework, if applicable."
    )
    unique_id: str = Field(
        default=None,
        description="A unique identifier for the framework, if applicable."
    )
    
    @property
    def get_id(self) -> str:
        """Returns the unique identifier for the framework."""
        return self._id
    
    def self_url(self) -> str:
        """Returns the URL to the framework's self-reference."""
        return f"frameworks/{self._id}.md"
    
    class Config:
        underscore_attrs_are_private = False


def load_frameworks() -> dict:
    """Loads all the frameworks from the JSON files in the 'frameworks' directory."""
    current_dir = Path(os.getcwd())

    # Load from the spec/frameworks directory
    frameworks_dir = current_dir / 'spec' / 'frameworks'
    frameworks = []

    if not frameworks_dir.exists():
        print(f"Frameworks directory '{frameworks_dir}' does not exist.")
        return frameworks
            
    # Convert each JSON file in the frameworks directory to a Framework model
    for f in frameworks_dir.glob('*.json'):
        with open(f, 'r', encoding='utf-8') as file:
            try:
                framework_data = json.load(file)
                framework = Framework(**framework_data).model_dump()
                frameworks.append(framework)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from {f}: {e}")
            except Exception as e:
                print(f"Error processing {f}: {e}")
        
    return frameworks


def convert_schema_to_markdown(schema_path: Path) -> str:
    """Converts a schema JSON file to Markdown format."""
    with open(schema_path, 'r', encoding='utf-8') as file:
        schema = json.load(file)

    markdown_content = f"# {schema.get('title', 'Title')}\n\n"
    markdown_content += f"## Overview\n\n{schema.get('description', 'No description available.')}\n\n"

    # If this is a capability schema, add additional information
    # this can be determined by looking at the _ref field
    if '_ref' in schema:

        if schema['_ref'].startswith('capability:'):

            loaded_frameworks = load_frameworks()
            print(loaded_frameworks)

            # Add the framework information
            frameworks = schema.get('frameworks', [])
            if len(frameworks) > 0:
                markdown_content += "## Frameworks\n"

                for framework in frameworks:
                    framework_name = "Unknown Framework"
                    references = []
                    
                    # Get the framework from the list of loaded frameworks using the _id
                    
                    framework_data = next((f for f in loaded_frameworks if f._id == framework), None)
                    print(framework_data)
                    
                    if framework_data:
                        framework_name = framework_data.title
                        references = framework_data.external_references
#
                    controls = framework_data.external_references if framework_data else []
                    markdown_content += f"### {framework_name}\n\n#### Controls\n\n"
                    for control in controls:
                        markdown_content += f"- **{control}**: \n"
                    markdown_content += "\n"

                    if references:
                        markdown_content += "#### References\n\n"
                        for reference in references:
                            if reference['type'] == 'website':
                                markdown_content += f"- [{reference['name']}]({reference['url']})\n"
                            else:
                                markdown_content += f"- {reference}\n"
                        markdown_content += "\n"

    if 'fields' in schema:
        markdown_content += "## Fields\n"
        for field in schema['fields']:
            markdown_content += f"- **{field['name']}**: {field.get('description', 'No description available.')}\n"

    return markdown_content.strip()


def main():
    """Main function to convert all schema JSON files in the current directory."""

    OUTPUT_DIR = Path('build')

    # Create the output directory if it doesn't exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Locate the current working directory of python
    current_dir = Path(os.getcwd())
    print(f"Current directory: {current_dir}")

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
        markdown_content = convert_schema_to_markdown(schema_file)
        markdown_file = schema_file.with_suffix('.md')

        with open(output_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_content)

        print(f"Converted {schema_file.name} to {markdown_file.name}")


if __name__ == "__main__":
    main()
