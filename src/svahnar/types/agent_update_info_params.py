# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentUpdateInfoParams"]


class AgentUpdateInfoParams(TypedDict, total=False):
    agent_id: Required[str]

    deploy_to: str

    description: str

    name: str
