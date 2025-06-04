from typing import Optional,Any
from pydantic import BaseModel, Field
from schema.external_reference import ExternalReference
from schema.framework import Framework
from schema.base import BaseComponent


class DocumentationElement(BaseModel):
    title: str = Field(
        ...,
        description="The name of the documentation element."
    )
    type: str = Field(
        ...,
        description="The type of the documentation element, e.g., 'list-item', 'section', etc."
    )
    description: str = Field(
        ...,
        description="A brief description of the documentation element."
    )


class Capability(BaseComponent):
    documentation: Optional[dict[str, list[DocumentationElement]]] = Field(
        default_factory=dict,
        description="A dictionary containing documentation elements categorized by their type."
    )
    frameworks: dict = Field(
        default_factory=list,
        description="A list of frameworks associated with the capability."
    )
    external_references: Optional[list[ExternalReference]] = Field(
        default_factory=list,
        description="A list of external references related to the capability."
    )
    phase: Optional[str] = Field(
        default=None,
        description="The phase of the capability, if applicable."
    )
    phase_friendly_name: Optional[str] = Field(
        default=None,
        description="A user-friendly name for the phase of the capability, if applicable."
    )
    stakeholders: Optional[list[str]] = Field(
        default_factory=list,
        description="A list of stakeholders associated with the capability."
    )
    actors: Optional[list[str]] = Field(
        default_factory=list,
        description="A list of actors associated with the capability."
    )
    references: Optional[list[ExternalReference]] = Field(
        default_factory=list,
        description="A list of references related to the capability."
    )
    
    
    @classmethod
    def generate_index_md(cls, items: list[Any]) -> str:
        """Generates a Table of Contents for the component"""
        raise NotImplementedError
    
    @classmethod
    def generate_framework_matrix(cls, items: list[Any]) -> str:
        """Generates a Markdown table of all capabilities and their associated frameworks with
        each framework as a column and the associated capabilities as rows with the covered
        controls listed in the cells."""
        markdown_content = "# Framework Coverage Matrix\n\n"
        markdown_content += "This matrix shows the coverage of capabilities across different frameworks.\n\n"
        markdown_content += "| Capability | " + " | ".join(f"[{f.title}]({f.self_url()})" for f in Framework.load()) + " |\n"
        markdown_content += "| :--- | " + " | ".join(":---" for _ in Framework.load()) + " |\n"
        
        for capability in items:
            markdown_content += f"| [{capability.title}]({capability.self_url()}) | "
            framework_coverage = []
            for framework in Framework.load():
                if framework.id in capability.frameworks:
                    controls = capability.frameworks[framework.id]
                    framework_coverage.append(", ".join(controls))
                else:
                    framework_coverage.append("")
                    
            markdown_content += " | ".join(framework_coverage) + " |\n"
        markdown_content += "\n"          
            
        return markdown_content.strip()        
        
    
    @classmethod
    def load(cls) -> dict['Capability', str]:
        """Loads all capabilities from the JSON files in the 'capabilities' directory."""
        return super().load()

    def generate_markdown(self) -> str:
        """Generates a Markdown representation of the capability."""
        markdown_content = f"# {self.title}\n\n"
    
        if self.phase:
            markdown_content += f"![](https://img.shields.io/badge/{self.phase}-{self.phase_friendly_name}-white)\n\n"
            
        markdown_content += f"## Overview\n\n{self.description}\n\n"

        if self.stakeholders:
            markdown_content += "## Stakeholders\n"
            markdown_content += "Stakeholders are individuals or groups who have an interest in the capability.\n\n"
            for stakeholder in self.stakeholders:
                markdown_content += f"- {stakeholder}\n"
            markdown_content += "\n"

        if self.actors:
            markdown_content += "## Actors\n"
            markdown_content += "Actors are individuals or systems that interact with the capability.\n\n"
            for actor in self.actors:
                markdown_content += f"- {actor}\n"
            markdown_content += "\n"
            
        if self.documentation:
            for key in self.documentation.keys():
                doc_part = self.documentation[key]
                if len(doc_part) > 0:
                    markdown_content += f"## {key.title().capitalize()}\n\n"
                    for item in doc_part:
                        if item.type == "list-item":
                            markdown_content += f"- **{item.title}**: {item.description}\n"
                        else:
                            markdown_content += f"### {item.title}\n\n{item.description}\n\n"
                    markdown_content += "\n"
                    
        if self.references:
            if len(self.references) > 0:
                markdown_content += "## References\n\n"
                for reference in self.references:
                    if reference.type == 'website':
                        if reference.name:
                            markdown_content += f"- [{reference.name}]({reference.url})\n"
                        else:
                            markdown_content += f"- [{reference.url}]({reference.url})\n"

        if self.frameworks:
            markdown_content += "## Frameworks\n"

            _frameworks = Framework.load()

            framework_name = "Unknown Framework"
            references = []

            # Get the framework from the list of loaded frameworks using the _id
            for framework in self.frameworks:

                framework_data = next(
                    (f for f in _frameworks if f.id == framework), None)

                if framework_data:
                    framework_name = framework_data.title
                    references = framework_data.external_references

                controls = self.frameworks[framework]
                markdown_content += f"### [{framework_name}]({framework_data.self_url()})\n\n#### Controls\n\n"
                for control in controls:
                    markdown_content += f"- **{control}** \n"
                markdown_content += "\n"

            if references:
                markdown_content += "#### References\n\n"
                for reference in references:
                    if reference.type == 'website':
                        markdown_content += f"- [{reference.name}]({reference.url})\n"
                    else:
                        markdown_content += f"- {reference}\n"
                markdown_content += "\n"

            markdown_content += "\n"

        if self.external_references:
            markdown_content += "## External References\n"
            for ref in self.external_references:
                markdown_content += f"- [{ref.name}]({ref.url})\n"

        return markdown_content.strip()
