from typing import Optional
from pydantic import Field, BaseModel
from schema.external_reference import ExternalReference
from schema.capability import Capability
from schema.base import BaseComponent

class ToolMaturityScore(BaseModel):
    management: int = Field(
        default=None,
        description="Management maturity score for the tool, on a scale of 1 to 5."
    )
    deployment_scope: int = Field(
        default=None,
        description="Deployment scope maturity score for the tool, on a scale of 1 to 5."
    )
    functionality: int = Field(
        default=None,
        description="Functionality maturity score for the tool, on a scale of 1 to 5."
    )
    knowledge: int = Field(
        default=None,
        description="Knowledge maturity score for the tool, on a scale of 1 to 5."
    )
    lifecycle: int = Field(
        default=None,
        description="Lifecycle maturity score for the tool, on a scale of 1 to 5."
    )
    vendor_risk: int = Field(
        default=None,
        description="Vendor risk maturity score for the tool, on a scale of 1 to 5."
    )


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
    maturity_score: Optional[ToolMaturityScore] = Field(
        default=None,
        description="Maturity score for the tool, including management, deployment scope, functionality, knowledge, lifecycle, and vendor risk."
    )

    @classmethod
    def generate_index_md(cls, tools: list['Tool']) -> str:
        """Generates a Table of Contents for the tools."""
        toc = "# Tools\n\n"
        toc += "| Tool | Category | ID | Description | Maturity Score | \n"
        toc += "|------|----------|----|-------------|----------------|\n"

        for tool in tools:
            toc += f"| [{tool.title}]({tool.self_url()}) | {', '.join(tool.category)} | {tool.id} | {tool.description} | {tool.calculate_overall_maturity_score() } |\n"

        return toc.strip()
    
    def calculate_overall_maturity_score(self) -> Optional[float]:
        """Calculates the overall maturity score based on individual scores."""
        if not self.maturity_score:
            return 0
        
        print(self.maturity_score)

        scores = [
            self.maturity_score.management,
            self.maturity_score.deployment_scope,
            self.maturity_score.functionality,
            self.maturity_score.knowledge,
            self.maturity_score.lifecycle,
            self.maturity_score.vendor_risk
        ]

        valid_scores = [score for score in scores if score is not None]
        if not valid_scores:
            return 0

        return sum(valid_scores) / len(valid_scores)

    def generate_markdown(self) -> str:
        """Generates a Markdown representation of the tool."""
        markdown_content = f"# {self.title}\n\n"
        markdown_content += f"## Overview\n\n{self.description}\n\n"

        _capabilities = Capability.load()
        
        if self.category:
            markdown_content += "## Categories\n\n"
            for cat in self.category:
                markdown_content += f"- {' '.join([p.capitalize() for p in cat.split(' ')])}\n"
            markdown_content += "\n"
            
        if self.maturity_score:
            markdown_content += "## Maturity Score\n\n"
            markdown_content += "The maturity score is a measure of how well the organization has implemented and utilized the tool. It is based on several aspects, each scored from 1 to 5, where 1 is the lowest and 5 is the highest. "
            markdown_content += "The overall maturity score is calculated as the average of the individual scores. **Note that these values can be overridden when generating this documentation for internal use.**\n\n"
            markdown_content += "The following table summarizes the maturity score for the tool:\n\n"
            markdown_content += "| Aspect | Score | Description |\n"
            markdown_content += "|--------|-------|-----------|\n"
            markdown_content += f"| Management | {self.maturity_score.management} | How well does the organization manage the tool.|\n"
            markdown_content += f"| Deployment Scope | {self.maturity_score.deployment_scope} | Does the organization have good penetration on target assets. |\n"
            markdown_content += f"| Functionality | {self.maturity_score.functionality} | How well does the tool function. |\n"
            markdown_content += f"| Knowledge | {self.maturity_score.knowledge} | How well does the organization understand the tool. |\n"
            markdown_content += f"| Lifecycle | {self.maturity_score.lifecycle} | Does the tool have a good lifecycle, e.g. enhancements track with technology and landscape changes. |\n"
            markdown_content += f"| Vendor Risk | {self.maturity_score.vendor_risk} | Does the vendor for the tool have any potential risk that would cause the tool to be unavailable. |\n"
            markdown_content += f"| Overall | {self.calculate_overall_maturity_score()} | Overall maturity score for the tool. |\n\n"
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
