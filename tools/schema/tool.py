from typing import Optional
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
    mitre_attack_datasources: Optional[list[str]] = Field(
        default_factory=list,
        description="A list of MITRE ATT&CK data sources related to the tool."
    )
    
    @classmethod
    def generate_index_md(cls, tools: list['Tool']) -> str:
        """Generates a Table of Contents for the tools."""
        toc = "# Tools\n\n"
        toc += "| Tool | Category | ID | Description |\n"
        toc += "|------|----------|----|-------------|\n"
        
        for tool in tools:
            toc += f"| [{tool.title}]({tool.self_url()}) | {', '.join(tool.category)} | {tool.id} | {tool.description} |\n"
        
        return toc.strip()

    def generate_markdown(self) -> str:
        """Generates a Markdown representation of the tool."""
        markdown_content = f"# {self.title}\n\n"
        markdown_content += f"## Overview\n\n{self.description}\n\n"

        _capabilities = Capability.load()
        
        if self.category:
            markdown_content += "## Categories\n\n"
            for cat in self.category:
                markdown_content += f"- {cat}\n"
            markdown_content += "\n"

        if self.capability:
            markdown_content += "## Capabilities\n\n"
            
            markdown_content += "| Capability | ID | Phase | Description |\n"
            markdown_content += "|------------|----|-------|-------------|\n"
            
            for cap in self.capability:
                capability = next((
                    c for c in _capabilities if c.id == cap), None)

                if capability:
                    markdown_content += f"| [{capability.title}]({capability.id}.md) | [{capability.id}](../{capability.self_url()}) | {capability.phase_friendly_name.capitalize()} | {capability.description} |\n"

            markdown_content += "\n"
            
        if self.mitre_attack_datasources:
            markdown_content += "## MITRE ATT&CK Data Sources\n\n"
            for datasource in self.mitre_attack_datasources:
                markdown_content += f"- {datasource}\n"
                
            markdown_content += "\n"

        if self.external_references:
            markdown_content += "## External References\n\n"
            for ref in self.external_references:
                markdown_content += f"- [{ref.name}]({ref.url})\n"

        return markdown_content.strip()
