# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentUpdateInfoParams"]


class AgentUpdateInfoParams(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent to update."""

    deploy_to: str
    """Change deployment to 'AgentStore' or 'Organization'."""

    description: str
    """The new description of the agent."""

    name: str
    """The new name of the agent."""
