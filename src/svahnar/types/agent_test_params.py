# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["AgentTestParams"]


class AgentTestParams(TypedDict, total=False):
    message: Required[str]
    """The message or command to be sent to the agent."""

    agent_history: str
    """List of prior messages; defaults to empty list."""

    hitl_decision: Optional[Literal["approve", "edit", "reject"]]
    """Human-in-the-loop decision."""

    thread_id: Optional[str]
    """Unique identifier for the chat session."""

    yaml_file: Optional[FileTypes]
    """YAML file to test the agent."""

    yaml_string: Optional[str]
    """YAML string to test the agent."""
