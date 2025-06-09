# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["AgentTestParams"]


class AgentTestParams(TypedDict, total=False):
    message: Required[str]
    """The message or command to be sent to the agent"""

    agent_history: Optional[Iterable[object]]
    """List of prior messages; defaults to empty list"""

    yaml_file: Optional[FileTypes]
    """YAML file to test the agent."""

    yaml_string: Optional[str]
    """YAML string to test the agent."""
