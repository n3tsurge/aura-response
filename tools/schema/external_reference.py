from typing import Optional
from pydantic import BaseModel, Field

class ExternalReference(BaseModel):
    """Model representing an external reference with a name and URL."""
    name: Optional[str] = Field(default=None, description="The name of the external reference.")
    url: str = Field(..., description="The URL of the external reference.")
    type: str = Field(default='website', description="The type of the external reference.", validators=[
                      lambda v: v in ['website', 'document', 'other']])

    def __str__(self):
        return f"{self.name} ({self.url})"