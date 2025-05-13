# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WorkbookQueryResponse",
    "Apply",
    "Read",
    "ReadData",
    "ReadDataValueCell",
    "ReadDataErrorCell",
    "ReadDataEmptyCell",
    "GoalSeek",
]


class Apply(BaseModel):
    original_value: Union[float, str, bool, None] = FieldInfo(alias="originalValue", default=None)
    """Original value of the cell before applying the new value"""

    target: str
    """A1-style reference for the cell that was updated"""

    value: Union[float, str, bool, None] = None
    """New value of the cell"""


class ReadDataValueCell(BaseModel):
    t: Literal["b", "n", "d", "s"]
    """Data type of the cell value (e.g. boolean, number, text)"""

    v: Union[float, str, bool, None] = None
    """Underlying cell value"""

    r: Optional[str] = None
    """Relative A1-based cell reference.

    This property only appears when there's a real cell behind the value
    """

    w: Optional[str] = None
    """Formatted cell value"""

    z: Optional[str] = None
    """Number format associated with the cell"""


class ReadDataErrorCell(BaseModel):
    t: Literal["e"]
    """Data type of the cell value (always 'e' for 'error')"""

    v: str
    """Underlying cell value"""

    e: Optional[str] = None
    """Description of the error"""

    r: Optional[str] = None
    """Relative A1-based cell reference.

    This property only appears when there's a real cell behind the value
    """


class ReadDataEmptyCell(BaseModel):
    t: Literal["z"]
    """Data type of the cell value (always 'z' for 'empty cell')"""

    r: Optional[str] = None
    """Relative A1-based cell reference.

    This property only appears when there's a real cell behind the value
    """


ReadData: TypeAlias = Union[ReadDataValueCell, ReadDataErrorCell, ReadDataEmptyCell]


class Read(BaseModel):
    data: List[List[ReadData]]

    source: str
    """A1-style reference for the cell or cells that were updated"""

    type: Literal["dataTable"]


class GoalSeek(BaseModel):
    control_cell: str = FieldInfo(alias="controlCell")
    """Reference for the cell that contains the solution"""

    target_cell: str = FieldInfo(alias="targetCell")
    """Reference for the cell that contains the formula you wanted to resolve"""

    target_value: float = FieldInfo(alias="targetValue")
    """The value you wanted the formula to return"""

    solution: Optional[float] = None
    """The result of the formula"""


class WorkbookQueryResponse(BaseModel):
    apply: Optional[List[Apply]] = None
    """Confirmation of the changes that were applied to the spreadsheet.

    Note that the API has no state and any changes made are cleared after each
    request
    """

    read: List[Read]
    """Details on the values that were read from the workbook cells"""

    goal_seek: Optional[GoalSeek] = FieldInfo(alias="goalSeek", default=None)
    """Results of a goal seek operation."""
