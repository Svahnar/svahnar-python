# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = [
    "AgentTestResponse",
    "AdditionalMetadata",
    "ResponseResponseItem",
    "ResponseResponseItemToolcall",
    "Usage",
    "UsageCreditsCharged",
    "RequestMetadata",
]


class AdditionalMetadata(BaseModel):
    thread_id: Optional[str] = None


class ResponseResponseItemToolcall(BaseModel):
    name: str

    id: Optional[str] = None

    arguments: Optional[Dict[str, object]] = None


class ResponseResponseItem(BaseModel):
    hitl: Union[str, Dict[str, object], None] = None

    llmresponse: Optional[str] = None

    reasoning: Optional[str] = None

    toolcalls: Optional[List[ResponseResponseItemToolcall]] = None

    toolresponse: Optional[List[object]] = None


class UsageCreditsCharged(BaseModel):
    agent_name: str

    credit_consumed: int

    number_of_runs: int


class Usage(BaseModel):
    credits_charged: Optional[List[UsageCreditsCharged]] = None

    total_credits_charged: Optional[int] = None


class RequestMetadata(BaseModel):
    """Response metadata including timestamp and request ID."""

    request_id: Optional[str] = None
    """Unique request identifier for tracing and support."""


class AgentTestResponse(BaseModel):
    additional_metadata: AdditionalMetadata

    response: List[Dict[str, ResponseResponseItem]]

    usage: Usage

    request_metadata: Optional[RequestMetadata] = None
    """Response metadata including timestamp and request ID."""
