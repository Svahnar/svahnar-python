# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AgentDeleteResponse", "RequestMetadata"]


class RequestMetadata(BaseModel):
    """Response metadata including timestamp and request ID."""

    request_id: Optional[str] = None
    """Unique request identifier for tracing and support."""


class AgentDeleteResponse(BaseModel):
    """Response after deleting a single agent."""

    deleted_id: str
    """ID of the agent that was successfully deleted."""

    message: str
    """Summary of the deletion operation."""

    request_metadata: Optional[RequestMetadata] = None
    """Response metadata including timestamp and request ID."""
