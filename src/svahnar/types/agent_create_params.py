# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    deploy_to: Required[str]
    """Where to deploy the agent. Options: 'AgentStore' or 'Organization'."""

    description: Required[str]
    """A brief description of the agent."""

    name: Required[str]
    """The agent's name. Supports Unicode characters."""

    yaml_file: Required[FileTypes]
    """The YAML configuration for the agent."""

    agent_icon: Optional[FileTypes]
