# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AgentListResponse", "Agent", "AgentUploadedBy", "RequestMetadata"]


class AgentUploadedBy(BaseModel):
    """Information about the agent creator."""

    user_email: Optional[str] = None
    """Email of the user who created the agent."""

    user_id: Optional[str] = None
    """ID of the user who created the agent."""


class Agent(BaseModel):
    """Single agent detail response with tracing metadata."""

    agent_id: str
    """Unique identifier of the agent."""

    description: str
    """Description of the agent."""

    hosted_to: str
    """Deployment target: 'AgentStore' or 'Organization'."""

    is_creator: bool
    """Whether the requesting user is the creator of this agent."""

    name: str
    """Name of the agent."""

    uploaded_by: AgentUploadedBy
    """Information about the agent creator."""


class RequestMetadata(BaseModel):
    """Response metadata including timestamp and request ID."""

    request_id: Optional[str] = None
    """Unique request identifier for tracing and support."""


class AgentListResponse(BaseModel):
    agents: Optional[List[Agent]] = None
    """List of agents the user has access to."""

    request_metadata: Optional[RequestMetadata] = None
    """Response metadata including timestamp and request ID."""
