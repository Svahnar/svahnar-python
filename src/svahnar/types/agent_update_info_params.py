# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["AgentUpdateInfoParams"]


class AgentUpdateInfoParams(TypedDict, total=False):
    agent_id: Required[str]

    deploy_to: Optional[str]

    description: Optional[str]

    name: Optional[str]

    agent_icon: Optional[FileTypes]
