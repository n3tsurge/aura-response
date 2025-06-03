from pydantic import BaseModel, Field
from schema.external_reference import ExternalReference
from schema.capability import Capability


class Tool(BaseModel):

    id: str = Field(
        default=None, description="The unique identifier for the tool.")
    ref: str = Field(default=None, description="A reference to the tool.")
    author: str = Field(..., description="The author of the tool.")
    capability: list[str] = Field(
        default_factory=list, description="Capabilities associated with the tool.")
    category: list[str] = Field(
        default_factory=list, description="Categories associated with the tool.")
    created_on: str = Field(...,
                            description="The date when the tool was created.")
    description: str = Field(...,
                             description="A brief description of the tool.")
    external_references: list[ExternalReference] = Field(
        default_factory=list,
        description="A list of external references related to the tool."
    )
    friendly_name: str = Field(
        default=None,
        description="A user-friendly name for the tool, if applicable."
    )
    title: str = Field(
        default=None,
        description="The title of the tool, if applicable."
    )
    unique_id: str = Field(
        default=None,
        description="A unique identifier for the tool, if applicable."
    )

    def self_url(self, base_dir: str = None) -> str:
        """Returns the URL to the tool's self-reference."""
        if base_dir is None:
            return f"../tools/{self.id}.md"
        return f"{base_dir}/tools/{self.id}.md"

    def generate_markdown(self) -> str:
        """Generates a Markdown representation of the tool."""
        markdown_content = f"# {self.title}\n\n"
        markdown_content += f"## Overview\n\n{self.description}\n\n"

        _capabilities = Capability.load()

        if self.capability:
            markdown_content += "## Capabilities\n\n"
            for cap in self.capability:
                markdown_content += f"- {cap}\n"
            markdown_content += "\n"

        if self.category:
            markdown_content += "## Categories\n\n"
            for cat in self.category:
                markdown_content += f"- {cat}\n"
            markdown_content += "\n"

        if self.external_references:
            markdown_content += "## External References\n\n"
            for ref in self.external_references:
                markdown_content += f"- [{ref.name}]({ref.url})\n"

        return markdown_content.strip()

    @classmethod
    def load(cls, base_dir: str = None) -> list['Tool']:
        """Loads all tools from the specified directory."""
        import json
        from pathlib import Path

        tools = []
        if base_dir is None:
            base_dir = Path(__file__).parent / 'tools'

        for tool_file in Path(base_dir).glob('*.json'):
            with open(tool_file, 'r', encoding='utf-8') as file:
                tool_data = json.load(file)
                tools.append(cls(**tool_data))

        return tools
