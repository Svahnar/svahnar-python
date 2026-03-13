# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["AgentBulkDeleteResponse", "RequestMetadata"]


class RequestMetadata(BaseModel):
    """Response metadata including timestamp and request ID."""

    request_id: Optional[str] = None
    """Unique request identifier for tracing and support."""


class AgentBulkDeleteResponse(BaseModel):
    """Response after deleting multiple agents."""

    message: str
    """Summary of the deletion operation."""

    deleted_ids: Optional[List[str]] = None
    """IDs of the agents that were successfully deleted."""

    error_details: Optional[List[Dict[str, str]]] = None
    """Details of agents that failed to be deleted."""

    request_metadata: Optional[RequestMetadata] = None
    """Response metadata including timestamp and request ID."""
