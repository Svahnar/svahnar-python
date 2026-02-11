# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = [
    "AgentRunResponse",
    "AdditionalMetadata",
    "ResponseResponseItem",
    "ResponseResponseItemToolcall",
    "Usage",
    "UsageCreditsCharged",
    "RequestMetadata",
]


class AdditionalMetadata(BaseModel):
    thread_id: str


class ResponseResponseItemToolcall(BaseModel):
    args: Dict[str, object]

    name: str


class ResponseResponseItem(BaseModel):
    llmresponse: str

    reasoning: str

    toolcalls: List[ResponseResponseItemToolcall]

    toolresponse: List[str]


class UsageCreditsCharged(BaseModel):
    agent_name: str

    credit_consumed: int

    number_of_runs: int


class Usage(BaseModel):
    credits_charged: List[UsageCreditsCharged]

    total_credits_charged: int


class RequestMetadata(BaseModel):
    """Response metadata including timestamp and request ID."""

    request_id: Optional[str] = None
    """Unique request identifier for tracing and support."""


class AgentRunResponse(BaseModel):
    additional_metadata: AdditionalMetadata

    response: List[Dict[str, ResponseResponseItem]]

    usage: Usage

    request_metadata: Optional[RequestMetadata] = None
    """Response metadata including timestamp and request ID."""
