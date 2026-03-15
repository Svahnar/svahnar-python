# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CreditGetResponse", "RequestMetadata"]


class RequestMetadata(BaseModel):
    """Response metadata including timestamp and request ID."""

    request_id: Optional[str] = None
    """Unique request identifier for tracing and support."""


class CreditGetResponse(BaseModel):
    """Response containing remaining credits."""

    credits_remaining: int
    """Number of credits remaining for the organization."""

    request_metadata: Optional[RequestMetadata] = None
    """Response metadata including timestamp and request ID."""
