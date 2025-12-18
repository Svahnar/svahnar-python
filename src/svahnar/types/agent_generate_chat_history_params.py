# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AgentGenerateChatHistoryParams"]


class AgentGenerateChatHistoryParams(TypedDict, total=False):
    query: Required[str]
    """The user's query"""

    response: Required[Union[str, object]]
    """The raw response from the agent service"""

    chat_history: Optional[Iterable[object]]
    """Existing chat history"""
