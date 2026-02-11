# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["AgentUpdateInfoParams"]


class AgentUpdateInfoParams(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent to update."""

    agent_icon: Optional[FileTypes]
    """New agent icon (512x512 pixels)."""

    deploy_to: Optional[str]
    """New deployment target: 'AgentStore' or 'Organization'."""

    description: Optional[str]
    """New description for the agent."""

    name: Optional[str]
    """New name for the agent."""
