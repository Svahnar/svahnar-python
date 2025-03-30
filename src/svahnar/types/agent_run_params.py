# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentRunParams"]


class AgentRunParams(TypedDict, total=False):
    agent_id: Required[str]
    """Unique identifier for the agent"""

    message: Required[str]
    """The message or command to be sent to the agent"""
