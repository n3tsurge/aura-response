import os
import json
from pathlib import Path
from pydantic import BaseModel, Field
from schema.external_reference import ExternalReference


class Framework(BaseModel):
    """Model representing a framework with its title and external references."""
    id: str = Field(
        default=None, description="The unique identifier for the framework.")
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

    class Config:
        underscore_attrs_are_private = False

    def self_url(self, base_dir: str = None) -> str:
        """Returns the URL to the framework's self-reference."""
        if base_dir is None:
            return f"../frameworks/{self.id}.md"
        return f"{base_dir}/frameworks/{self.id}.md"

    def generate_markdown(self) -> str:
        """Generates a Markdown representation of the framework."""
        markdown_content = f"# {self.title}\n\n"
        markdown_content += f"**Author:** {self.author}\n"
        markdown_content += f"**Created On:** {self.created_on}\n\n"
        markdown_content += f"## Overview\n\n{self.description}\n\n"

        if self.category:
            markdown_content += "## Categories\n"
            for cat in self.category:
                markdown_content += f"- {cat}\n"

        if self.external_references:
            markdown_content += "## External References\n"
            for ref in self.external_references:
                markdown_content += f"- [{ref.name}]({ref.url})\n"

        return markdown_content.strip()

    @classmethod
    def load(cls) -> dict['Framework', str]:
        """Loads all frameworks from the JSON files in the 'frameworks' directory."""
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
                    framework = cls(**framework_data)
                    frameworks.append(framework)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from {f}: {e}")
                except Exception as e:
                    print(f"Error processing {f}: {e}")

        return frameworks
