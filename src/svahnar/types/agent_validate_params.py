# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import FileTypes

__all__ = ["AgentValidateParams"]


class AgentValidateParams(TypedDict, total=False):
    yaml_file: Optional[FileTypes]
    """YAML file to test the agent."""

    yaml_string: Optional[str]
    """YAML string to test the agent."""
