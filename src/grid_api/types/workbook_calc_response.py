# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "WorkbookCalcResponse",
    "WorkbookCalcResponseItem",
    "WorkbookCalcResponseItemReadValue",
    "WorkbookCalcResponseItemUnionMember1",
]


class WorkbookCalcResponseItemReadValue(BaseModel):
    formatted: str
    """Formatted cell value"""

    offset: List[object]
    """Cell position in the spreadsheet, using 0-indexed x/y coordinates.

    Origin [0, 0] is at the top-left
    """

    type: Literal["blank", "boolean", "number", "string", "date", "error"]
    """Type of the cell value"""

    value: Union[float, str, bool, None] = None
    """Cell value"""

    error: Optional[str] = None


class WorkbookCalcResponseItemUnionMember1(BaseModel):
    formatted: str
    """Formatted cell value"""

    offset: List[object]
    """Cell position in the spreadsheet, using 0-indexed x/y coordinates.

    Origin [0, 0] is at the top-left
    """

    type: Literal["blank", "boolean", "number", "string", "date", "error"]
    """Type of the cell value"""

    value: Union[float, str, bool, None] = None
    """Cell value"""

    error: Optional[str] = None


WorkbookCalcResponseItem: TypeAlias = Union[
    WorkbookCalcResponseItemReadValue, List[WorkbookCalcResponseItemUnionMember1]
]

WorkbookCalcResponse: TypeAlias = Dict[str, WorkbookCalcResponseItem]
