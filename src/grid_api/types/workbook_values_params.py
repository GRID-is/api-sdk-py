# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["WorkbookValuesParams"]


class WorkbookValuesParams(TypedDict, total=False):
    read: Required[List[str]]

    apply: Optional[Dict[str, Union[float, str, bool, None]]]
