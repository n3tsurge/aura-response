from typing import Optional
from pydantic import BaseModel, Field
from schema.external_reference import ExternalReference
from schema.framework import Framework
from pathlib import Path
import json
import os


class BaseComponent(BaseModel):
    """Base model for components with common fields."""
    id: str = Field(
        default=None, description="The unique identifier for the component.")
    ref: str = Field(
        default=None, description="A reference to the component.")
    author: str = Field(
        ...,
        description="The author of the component."
    )
    description: str = Field(
        ...,
        description="A brief description of the component."
    )
    created_on: str = Field(
        ...,
        description="The date when the component was created."
    )
    unique_id: str = Field(
        default=None,
        description="A unique identifier for the component, if applicable."
    )
    title: str = Field(
        ...,
        description="The title of the component."
    )
    friendly_name: str = Field(
        default=None,
        description="A user-friendly name for the component, if applicable."
    )
    author: str = Field(
        ...,
        description="The author of the component."
    )

    def self_url(self, base_dir: str = None) -> str:
        """Returns the URL to the component's self-reference."""
        if base_dir is None:
            return f"../{self.__class__.__name__.lower()}/{self.id}.md"
        return f"{base_dir}/{self.__class__.__name__.lower()}/{self.id}.md"

    def generate_markdown(self) -> str:
        return ""

    @classmethod
    def load(cls) -> dict['BaseComponent', str]:
        """Loads all components from the JSON files in the components directory."""
        current_dir = Path(os.getcwd())

        # Load from the spec/frameworks directory
        dir = current_dir / 'spec' / cls.__name__.lower()
        items = []

        if not dir.exists():
            print(f"{cls.__name__} directory '{dir}' does not exist.")
            return items

        # Convert each JSON file in the capabilities directory to a Framework model
        glob_pattern = '*.json'
        # If this is a tool class set the glob pattern as **/*.json to include all subdirectories
        if cls.__name__ == 'Tool':
            glob_pattern = '**/index.json'
        for f in dir.glob(glob_pattern):
            with open(f, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    capability = cls(**data)
                    items.append(capability)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from {f}: {e}")
                except Exception as e:
                    print(f"Error processing {f}: {e}")

        return items
