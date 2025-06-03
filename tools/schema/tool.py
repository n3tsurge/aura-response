from pydantic import Field
from schema.external_reference import ExternalReference
from schema.capability import Capability
from schema.base import BaseComponent


class Tool(BaseComponent):
    capability: list[str] = Field(
        default_factory=list, description="Capabilities associated with the tool.")
    category: list[str] = Field(
        default_factory=list, description="Categories associated with the tool.")
    external_references: list[ExternalReference] = Field(
        default_factory=list,
        description="A list of external references related to the tool."
    )

    def generate_markdown(self) -> str:
        """Generates a Markdown representation of the tool."""
        markdown_content = f"# {self.title}\n\n"
        markdown_content += f"## Overview\n\n{self.description}\n\n"

        _capabilities = Capability.load()

        if self.capability:
            markdown_content += "## Capabilities\n\n"
            for cap in self.capability:
                capability = next((
                    c for c in _capabilities if c.id == cap), None)

                if capability:
                    markdown_content += f"### {capability.title}\n\n"
                    markdown_content += f"{capability.description}\n\n"
                    if capability.self_url():
                        markdown_content += f"[More details]({capability.self_url()})\n\n"

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
