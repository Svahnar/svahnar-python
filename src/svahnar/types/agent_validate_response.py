# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AgentValidateResponse"]


class AgentValidateResponse(BaseModel):
    message: str
    """Detailed message about the validation outcome."""

    status: str
    """The result status of the validation."""

    suggestion: Optional[str] = None
    """Optional suggestion if any errors were found."""
