# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["AgentReconfigureParams"]


class AgentReconfigureParams(TypedDict, total=False):
    agent_id: Required[str]

    yaml_file: Required[FileTypes]
