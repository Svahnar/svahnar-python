# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AgentRunResponse",
    "ReplyReplyItem",
    "ReplyReplyItemMessage",
    "ReplyReplyItemMessageContent",
    "ReplyReplyItemMessageContentMessage",
    "ReplyReplyItemMessageContentMessageInvalidToolCall",
    "ReplyReplyItemMessageContentMessageResponseMetadata",
    "ReplyReplyItemMessageContentMessageToolCall",
]


class ReplyReplyItemMessageContentMessageInvalidToolCall(BaseModel):
    id: str
    """Unique identifier for the tool call"""

    function: object
    """Details of the function call including its name and arguments"""

    type: str
    """The type of the tool call"""


class ReplyReplyItemMessageContentMessageResponseMetadata(BaseModel):
    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)


class ReplyReplyItemMessageContentMessageToolCall(BaseModel):
    id: str
    """Unique identifier for the tool call"""

    function: object
    """Details of the function call including its name and arguments"""

    type: str
    """The type of the tool call"""


class ReplyReplyItemMessageContentMessage(BaseModel):
    id: str
    """Unique identifier for the message"""

    content: str
    """The actual message content"""

    example: bool
    """Flag indicating if the message is an example"""

    type: str
    """Indicates whether the message is from a human or AI"""

    additional_kwargs: Optional[object] = None
    """Additional keyword arguments"""

    invalid_tool_calls: Optional[List[ReplyReplyItemMessageContentMessageInvalidToolCall]] = None
    """List of invalid tool calls (if any)"""

    name: Optional[str] = None
    """Optional name of the sender"""

    response_metadata: Optional[ReplyReplyItemMessageContentMessageResponseMetadata] = None
    """Metadata about the response including token usage and model details"""

    tool_calls: Optional[List[ReplyReplyItemMessageContentMessageToolCall]] = None
    """List of tool calls (if any)"""


class ReplyReplyItemMessageContent(BaseModel):
    messages: List[ReplyReplyItemMessageContentMessage]
    """A group of messages exchanged during the conversation"""


class ReplyReplyItemMessage(BaseModel):
    id: str
    """Unique identifier for the container"""

    content: List[ReplyReplyItemMessageContent]
    """A list of message groups"""

    example: bool
    """Flag indicating if this is an example container"""

    type: str
    """The type of the container message"""

    additional_kwargs: Optional[object] = None
    """Additional keyword arguments for the container"""

    name: Optional[str] = None
    """Optional name for the container"""

    response_metadata: Optional[object] = None
    """Response metadata at the container level"""


class ReplyReplyItem(BaseModel):
    messages: List[ReplyReplyItemMessage]
    """List of message containers for an agent"""


class AgentRunResponse(BaseModel):
    reply: List[Dict[str, Optional[ReplyReplyItem]]]
    """List of agent items in the response"""
