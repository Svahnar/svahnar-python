# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AgentCreateResponse", "RequestMetadata"]


class RequestMetadata(BaseModel):
    """Response metadata including timestamp and request ID."""

    request_id: Optional[str] = None
    """Unique request identifier for tracing and support."""


class AgentCreateResponse(BaseModel):
    """Response after creating a new agent."""

    agent_id: str
    """Unique identifier of the created agent."""

    message: str
    """Human-readable result message."""

    request_metadata: Optional[RequestMetadata] = None
    """Response metadata including timestamp and request ID."""
