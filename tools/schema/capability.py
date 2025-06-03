from typing import Optional
from pydantic import Field
from schema.external_reference import ExternalReference
from schema.framework import Framework
from schema.base import BaseComponent


class Capability(BaseComponent):
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
    stakeholders: Optional[list[str]] = Field(
        default_factory=list,
        description="A list of stakeholders associated with the capability."
    )
    actors: Optional[list[str]] = Field(
        default_factory=list,
        description="A list of actors associated with the capability."
    )
    
    @classmethod
    def load(cls) -> dict['Capability', str]:
        """Loads all capabilities from the JSON files in the 'capabilities' directory."""
        return super().load()

    def generate_markdown(self) -> str:
        """Generates a Markdown representation of the capability."""
        markdown_content = f"# {self.title}\n\n"
        markdown_content += f"## Overview\n\n{self.description}\n\n"

        if self.phase:
            markdown_content += f"**Phase:** {self.phase}\n\n"

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

                controls = self.frameworks
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
