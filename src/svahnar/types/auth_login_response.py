# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthLoginResponse", "RequestMetadata"]


class RequestMetadata(BaseModel):
    """Response metadata including timestamp and request ID."""

    request_id: Optional[str] = None
    """Unique request identifier for tracing and support."""


class AuthLoginResponse(BaseModel):
    """Response containing authentication token and user info."""

    email: str
    """Email address of the authenticated user."""

    first_name: str
    """First name of the authenticated user."""

    last_name: str
    """Last name of the authenticated user."""

    request_metadata: Optional[RequestMetadata] = None
    """Response metadata including timestamp and request ID."""
