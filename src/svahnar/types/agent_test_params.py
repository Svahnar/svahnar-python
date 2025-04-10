# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["AgentTestParams"]


class AgentTestParams(TypedDict, total=False):
    message: Required[str]

    yaml_file: Optional[FileTypes]

    yaml_string: Optional[str]
    """YAML string to validate."""
