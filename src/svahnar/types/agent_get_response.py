# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AgentGetResponse", "UploadedBy", "RequestMetadata"]


class UploadedBy(BaseModel):
    """Information about the agent creator."""

    user_email: Optional[str] = None
    """Email of the user who created the agent."""

    user_id: Optional[str] = None
    """ID of the user who created the agent."""


class RequestMetadata(BaseModel):
    """Response metadata including timestamp and request ID."""

    request_id: Optional[str] = None
    """Unique request identifier for tracing and support."""


class AgentGetResponse(BaseModel):
    """
    Agent detail returned by the get-agent endpoint, includes a note about YAML config.
    """

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

    uploaded_by: UploadedBy
    """Information about the agent creator."""

    yaml_configuration: str
    """A note directing the user to the download endpoint for the YAML configuration."""

    request_metadata: Optional[RequestMetadata] = None
    """Response metadata including timestamp and request ID."""
