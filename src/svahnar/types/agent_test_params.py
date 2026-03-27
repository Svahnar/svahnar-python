# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypedDict

from .._types import FileTypes

__all__ = ["AgentTestParams"]


class AgentTestParams(TypedDict, total=False):
    agent_history: str
    """List of prior messages; defaults to empty list."""

    hitl_decision: Optional[Literal["approve", "edit", "reject"]]
    """Human-in-the-loop decision."""

    message: Union[str, Dict[str, object], None]
    """The message or command to be sent to the agent."""

    thread_id: Optional[str]
    """Unique identifier for the chat session."""

    yaml_file: Optional[FileTypes]
    """YAML file to test the agent."""

    yaml_string: Optional[str]
    """YAML string to test the agent."""
