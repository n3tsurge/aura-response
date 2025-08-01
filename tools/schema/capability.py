from typing import Optional, Any, Union
from pydantic import BaseModel, Field
from schema.external_reference import ExternalReference
from schema.framework import Framework
from schema.base import BaseComponent

phase_order = [
            "preparation", "identification", "containment", "eradication", "recovery", "lessons-learned", "operations"]

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


class Requirement(BaseModel):
    id: str = Field(
        ...,
        description="The unique identifier for the requirement."
    )
    description: str = Field(
        ...,
        description="A detailed description of the requirement."
    )
    type: Optional[str] = Field(
        default=None,
        description="The category of the requirement, if applicable."
    )

class Capability(BaseComponent):
    documentation: Optional[dict[str, list[Union[DocumentationElement,Requirement]]]] = Field(
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
    category: str = Field(
        default="",
        description="The category of the capability, e.g., 'Security', 'Compliance', etc."
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
    staff: Optional[list[str]] = Field(
        default_factory=list,
        description="A list of staff associated with the capability."
    )
    references: Optional[list[ExternalReference]] = Field(
        default_factory=list,
        description="A list of references related to the capability."
    )
    mitre_defend: Optional[str] = Field(
        default=None,
        description="The MITRE defend tactic associated with the capability, if applicable."
    )

    @classmethod
    def generate_index_md(cls, items: list['Capability']) -> str:
        """Generates a Table of Contents for the tools."""
        toc = "# Capabilities\n\n"
        toc += "This document provides an overview of all capabilities broken down by response phase.\n\n"

        phases = {}
        for capability in items:
            phase = capability.phase_friendly_name if capability.phase_friendly_name else "Unknown"
            if phase not in phases:
                phases[phase] = []
            phases[phase].append(capability)
            
        # Sort the phases by the predefined order
        phases = {phase: phases[phase] for phase in phase_order if phase in phases}
        
        for phase, capabilities in phases.items():
            toc += f"## {phase.capitalize()} Phase\n\n"
            toc += "| Capability | ID | Phase | Description |\n"
            toc += "|------------|----|-------|-------------|\n"
            for capability in capabilities:
                toc += f"| [{capability.title}]({capability.phase_friendly_name}/{capability.id}.md) | {capability.id} | {capability.phase_friendly_name.capitalize()} | {capability.description} |\n"
            toc += "\n"

        return toc.strip()

    @classmethod
    def generate_phase_matrix(cls) -> str:
        """Generates an HTML table of all the capabilities grouped by their
        phase which each phase as a column and the associated capabilities as rows. 
        When a phase cell is empty the cell show have no bottom border."""
        markdown_content = "# Capability Phase Matrix\n\n"
        markdown_content += "This matrix shows the capabilities grouped by their response phase.\n\n"
        
        

        _phases = {}
        for capability in cls.load():
            phase = capability.phase_friendly_name if capability.phase_friendly_name else "Unknown"
            if phase not in _phases:
                _phases[phase] = []
            _phases[phase].append(capability)
            
        # Sort the phases by the predefined order
        _phases = {phase: _phases[phase] for phase in phase_order if phase in _phases}

        markdown_content += " | ".join([p.capitalize()
                                       for p in _phases.keys()]) + " |\n"
        markdown_content += "| :--- " * len(_phases) + "|\n"
        max_length = max(len(capabilities)
                         for capabilities in _phases.values())
        for i in range(max_length):
            row = []
            for phase, capabilities in _phases.items():
                if i < len(capabilities):
                    capability = capabilities[i]
                    row.append(
                        f"[{capability.title} ({capability.id})]({phase}/{capability.id}.md)")
                else:
                    row.append("")
            markdown_content += "| " + " | ".join(row) + " |\n"
        markdown_content += "\n"

        return markdown_content.strip()

    @classmethod
    def generate_tool_matrix(cls) -> str:
        """Generates a Markdown table of all capabilities and their associated tools with
        each tool as a column and the associated capabilities as rows with the covered
        controls listed in the cells."""
        from schema.tool import Tool
        tools = Tool.load()

        markdown_content = "# Tool Coverage Matrix\n\n"
        markdown_content += "This matrix shows the coverage of capabilities across different tools. "
        markdown_content += "A CSV representation of this matrix can be found here [tool_coverage.csv](../../files/tool_coverage.csv).\n\n"
        markdown_content += "| Capability | Phase | " + \
            " | ".join(f"[{t.title}]({t.self_url()})" for t in tools) + " |\n"
        markdown_content += "| :--- | :--- | " + \
            " | ".join(":---:" for _ in tools) + " |\n"
            
        _phases = {}
        
        for capability in cls.load():
            # Group capabilities by their phase
            phase = capability.phase_friendly_name if capability.phase_friendly_name else "Unknown"
            if phase not in _phases:
                _phases[phase] = []
            _phases[phase].append(capability)
            
        # Sort the phases by the predefined order
        _phases = {phase: _phases[phase] for phase in phase_order if phase in _phases}
        
        for phase, capabilities in _phases.items():

            for capability in capabilities:
                markdown_content += f"| [{capability.title} ({capability.id})]({capability.phase_friendly_name}/{capability.id}.md) | {capability.phase_friendly_name.capitalize()} | "
                tool_coverage = []
                for tool in tools:
                    if capability.id in tool.capability:
                        tool_coverage.append(
                            f"[:white_check_mark:](../tool/{tool.friendly_name}/{capability.id}.md)")
                    else:
                        tool_coverage.append("")

                markdown_content += " | ".join(tool_coverage) + " |\n"

        markdown_content += "\n"
        return markdown_content.strip()

    @classmethod
    def generate_tool_matrix_csv(cls) -> str:
        """Generates a CSV representation of the tool coverage matrix."""
        from schema.tool import Tool
        tools = Tool.load()

        csv_content = "Capability,Phase," + \
            ",".join(t.title for t in tools) + "\n"
            
        _phases = {}
        
        for capability in cls.load():
            # Group capabilities by their phase
            phase = capability.phase_friendly_name if capability.phase_friendly_name else "Unknown"
            if phase not in _phases:
                _phases[phase] = []
            _phases[phase].append(capability)
            
        # Sort the phases by the predefined order
        _phases = {phase: _phases[phase] for phase in phase_order if phase in _phases}
        
        for phase, capabilities in _phases.items():
            for capability in capabilities:           
                csv_content += f"{capability.title} ({capability.id}),{capability.phase_friendly_name.capitalize()},"
                tool_coverage = []
                for tool in tools:
                    if capability.id in tool.capability:
                        tool_coverage.append("x")
                    else:
                        tool_coverage.append("")
                csv_content += ",".join(tool_coverage) + "\n"

        return csv_content.strip()

    @classmethod
    def generate_framework_matrix(cls, items: list[Any]) -> str:
        """Generates a Markdown table of all capabilities and their associated frameworks with
        each framework as a column and the associated capabilities as rows with the covered
        controls listed in the cells."""
        markdown_content = "# Framework Coverage Matrix\n\n"
        markdown_content += "This matrix shows the coverage of capabilities across different frameworks by phases.\n\n"
        
        _phases = {}
        for capability in items:
            phase = capability.phase_friendly_name if capability.phase_friendly_name else "Unknown"
            if phase not in _phases:
                _phases[phase] = []
            _phases[phase].append(capability)
            
        for phase, capabilities in _phases.items():
            markdown_content += f"## {phase.capitalize()} Phase\n\n"
            markdown_content += "| Capability | " + \
                " | ".join(f"[{f.title}]({f.self_url()})" for f in Framework.load()) + " |\n"
            markdown_content += "| :--- | " + \
                " | ".join(":---" for _ in Framework.load()) + " |\n"

            for capability in capabilities:
                markdown_content += f"| [{capability.title} ({capability.id})]({capability.phase_friendly_name}/{capability.id}.md) | "
                framework_coverage = []
                for framework in Framework.load():
                    if framework.id in capability.frameworks:
                        controls = capability.frameworks[framework.id]
                        framework_coverage.append(", ".join(controls))
                    else:
                        framework_coverage.append("")

                markdown_content += " | ".join(framework_coverage) + " |\n"
            markdown_content += "\n"
            
        markdown_content += "\n"

        return markdown_content.strip()

    @classmethod
    def load(cls) -> dict['Capability', str]:
        """Loads all capabilities from the JSON files in the 'capabilities' directory."""
        return super().load()
    
    def self_url(self, base_dir: str = None) -> str:
        """Returns the URL to the component's self-reference."""
        if base_dir is None:
            return f"../{self.__class__.__name__.lower()}/{self.phase_friendly_name}/{self.id}.md"
        return f"{base_dir}/{self.__class__.__name__.lower()}/{self.phase_friendly_name}/{self.id}.md"

    def generate_markdown(self) -> str:
        """Generates a Markdown representation of the capability."""
        markdown_content = f"# {self.title}\n"

        if self.phase:
            markdown_content += f"&nbsp;![](https://img.shields.io/badge/ID-{self.id}-blue)&nbsp;![](https://img.shields.io/badge/Phase-{self.phase_friendly_name.capitalize().replace('-','%20')}_%28{self.phase}%29-blue)&nbsp;![](https://img.shields.io/badge/Category-{self.category.capitalize()}-blue)\n"

        markdown_content += f"## Overview\n{self.description}\n\n"

        if self.stakeholders:
            markdown_content += "## Stakeholders\n"
            markdown_content += "Stakeholders are individuals or groups who have an interest in the capability.\n\n"
            for stakeholder in self.stakeholders:
                markdown_content += f"- {stakeholder}\n"
            markdown_content += "\n"

        if self.staff:
            markdown_content += "## Staff\n"
            markdown_content += "Staff are individuals or systems that interact with and execute a capability.\n\n"
            for staff in self.staff:
                markdown_content += f"- {staff}\n"
            markdown_content += "\n"

        if self.documentation:
            for key in self.documentation.keys():
                doc_part = self.documentation[key]
                if len(doc_part) > 0:
                    markdown_content += f"## {key.title().capitalize()}\n"
                    
                    
                    if key == "requirements":
                        markdown_content += "For a tool, system or staff perform this capability, the following requirements should be considered:\n\n"
                        markdown_content += "| Requirement ID | Description | Type |\n"
                        markdown_content += "| :--- | :--- | :--- |\n"
                        
                        # Sort the requirements by type
                        doc_part.sort(key=lambda x: (x.type or "N/A", x.id))
                        for item in doc_part:
                            markdown_content += f"| {self.id}-{item.id.upper()} | {item.description} | {item.type.capitalize() }|\n"
                            
                    elif key == "automation":
                        markdown_content += "This section provides information on how the capability can be automated.\n\n"
                        markdown_content += "| Automation ID | Description | Type |\n"
                        markdown_content += "| :--- | :--- | :--- |\n"
                        for item in doc_part:
                            markdown_content += f"| {self.id}-{item.id.upper()} | {item.description} | {item.type.capitalize() if item.type else 'N/A'} |\n"
                    elif key in ["enrichment", "hunting"]:
                        # These sections can use either Requirement or DocumentationElement structure
                        # Check the first item to determine which structure is used
                        if doc_part and hasattr(doc_part[0], 'id') and not hasattr(doc_part[0], 'title'):
                            # Requirement structure with id, description, type
                            markdown_content += f"| {key.title()} ID | Description | Type |\n"
                            markdown_content += "| :--- | :--- | :--- |\n"
                            for item in doc_part:
                                markdown_content += f"| {self.id}-{item.id.upper()} | {item.description} | {item.type.capitalize() if item.type else 'N/A'} |\n"
                        else:
                            # DocumentationElement structure with title, type, description
                            for item in doc_part:
                                if hasattr(item, 'title'):
                                    if item.type == "list-item":
                                        markdown_content += f"- **{item.title}**: {item.description}\n"
                                    else:
                                        markdown_content += f"### {item.title}\n\n{item.description}\n\n"
                                else:
                                    # Fallback for malformed data
                                    markdown_content += f"- {item.description}\n"
                    elif key == "fields":
                        # Fields section can have either structure - check first item
                        if doc_part and hasattr(doc_part[0], 'id') and not hasattr(doc_part[0], 'title'):
                            # Extended Requirement structure with id, name, description, type
                            markdown_content += "| Field ID | Name | Description | Type |\n"
                            markdown_content += "| :--- | :--- | :--- | :--- |\n"
                            for item in doc_part:
                                name = getattr(item, 'name', item.id)  # Fallback to id if no name
                                markdown_content += f"| {item.id} | {name} | {item.description} | {item.type} |\n"
                        else:
                            # DocumentationElement structure with title, type, description
                            markdown_content += "| Field | Description |\n"
                            markdown_content += "| :--- | :--- |\n"
                            for item in doc_part:
                                if hasattr(item, 'title'):
                                    markdown_content += f"| {item.title} | {item.description} |\n"
                                else:
                                    # Fallback for malformed data
                                    markdown_content += f"| {getattr(item, 'name', 'Unknown')} | {item.description} |\n"
                    else:
                        # These sections use DocumentationElement structure with title
                        for item in doc_part:
                            if hasattr(item, 'title'):
                                if item.type == "list-item":
                                    markdown_content += f"- **{item.title}**: {item.description}\n"
                                else:
                                    markdown_content += f"### {item.title}\n\n{item.description}\n\n"
                            else:
                                # Fallback for items without title (shouldn't happen with proper schema)
                                markdown_content += f"- {item.description}\n"
                    markdown_content += "\n"

        if self.references or self.mitre_defend:
            markdown_content += "## References\n\n"
            if self.mitre_defend:
                markdown_content += f"- [MITRE D3FEND: {self.mitre_defend}](https://d3fend.mitre.org/technique/{self.mitre_defend}/)\n"
                
            for reference in self.references:
                if reference.type == 'website':
                    if reference.name:
                        markdown_content += f"- [{reference.name}]({reference.url})\n"
                    else:
                        markdown_content += f"- [{reference.url}]({reference.url})\n"

        if self.external_references:
            markdown_content += "## External References\n"
            for ref in self.external_references:
                markdown_content += f"- [{ref.name}]({ref.url})\n"

        # Generate the tools section by loading all the tools
        # and finding all the tools that reference this capability
        from schema.tool import Tool
        tools = Tool.load()
        tools_using_capability = [
            tool for tool in tools if self.id in tool.capability]
        if tools_using_capability:
            markdown_content += "## Tools\n"
            markdown_content += "The following tools provide this capability:\n\n"
            for tool in tools_using_capability:
                markdown_content += f"- [{tool.title}](../tool/{tool.friendly_name}/{self.id}.md)\n"
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

                controls = self.frameworks[framework]
                markdown_content += f"### [{framework_name}]({framework_data.self_url()})\n\n#### Controls\n\n"
                for control in controls:
                    markdown_content += f"- {control} \n"
                markdown_content += "\n"

            if references or self.mitre_defend:
                markdown_content += "#### References\n\n"
                for reference in references:
                    if reference.type == 'website':
                        markdown_content += f"- [{reference.name}]({reference.url})\n"
                    else:
                        markdown_content += f"- {reference}\n"
                markdown_content += "\n"

            markdown_content += "\n"

        return markdown_content.strip()
