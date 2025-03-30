# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AgentBulkDeleteParams"]


class AgentBulkDeleteParams(TypedDict, total=False):
    agent_ids: Required[List[str]]
    """The list of agent IDs to delete"""
