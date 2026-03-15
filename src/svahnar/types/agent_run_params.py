# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AgentRunParams"]


class AgentRunParams(TypedDict, total=False):
    agent_id: Required[str]
    """Unique identifier for the agent."""

    message: Required[Union[str, Dict[str, object], None]]
    """The message or command to be sent to the agent."""

    agent_history: Optional[Iterable[object]]
    """List of prior messages; defaults to empty list."""

    hitl_decision: Optional[Literal["approve", "edit", "reject"]]
    """Human-in-the-loop decision for the agent."""

    thread_id: Optional[str]
    """Unique identifier for the chat session."""
