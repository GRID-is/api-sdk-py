# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WorkbookCalcParams"]


class WorkbookCalcParams(TypedDict, total=False):
    read: Required[SequenceNotStr[str]]

    apply: Optional[Dict[str, Union[float, str, bool, None]]]
    """Map of cell references to values.

    The values are written to cells in the spreadsheet before performing the read
    operation. You can write numbers, strings, and booleans. Values applied within a
    request are temporary and affect only that specific request. They are not
    permanently written to the original spreadsheet.

    ```json
    {
      "apply": { "A1": 10, "A2": 2.718, "A3": "Total", "A4": true, "A5": null }
      // ...
    }
    ```
    """
