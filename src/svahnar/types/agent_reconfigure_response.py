# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AgentReconfigureResponse", "RequestMetadata"]


class RequestMetadata(BaseModel):
    """Response metadata including timestamp and request ID."""

    request_id: Optional[str] = None
    """Unique request identifier for tracing and support."""


class AgentReconfigureResponse(BaseModel):
    """Simple response containing a message string."""

    message: str
    """Human-readable result message."""

    request_metadata: Optional[RequestMetadata] = None
    """Response metadata including timestamp and request ID."""
