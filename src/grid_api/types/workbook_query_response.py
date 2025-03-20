# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "WorkbookQueryResponse",
    "Apply",
    "Read",
    "ReadDataTable",
    "ReadDataTableData",
    "ReadDataTableDataValueCell",
    "ReadDataTableDataErrorCell",
    "ReadDataTableDataEmptyCell",
    "ReadDataList",
    "ReadDataListData",
    "ReadDataListDataValueCell",
    "ReadDataListDataErrorCell",
    "ReadDataListDataEmptyCell",
    "ReadDataCell",
    "ReadDataCellData",
    "ReadDataCellDataValueCell",
    "ReadDataCellDataErrorCell",
    "ReadDataCellDataEmptyCell",
    "ReadValueTable",
    "ReadValueList",
    "ReadValue",
    "ReadFormattedValueTable",
    "ReadFormattedValueList",
    "ReadFormattedValue",
    "GoalSeek",
]


class Apply(BaseModel):
    target: str
    """A1-style reference for the cell that was updated"""

    value: Union[float, str, bool, None] = None
    """New value of the cell"""

    original_value: Union[float, str, bool, None] = FieldInfo(alias="originalValue", default=None)
    """Original value of the cell before applying the new value"""


class ReadDataTableDataValueCell(BaseModel):
    t: Literal["b", "n", "d", "s"]
    """Data type of the cell value (e.g. boolean, number, text)"""

    v: Union[float, str, bool, None] = None
    """Underlying cell value"""

    r: Optional[str] = None
    """Relative A1-based cell reference"""

    w: Optional[str] = None
    """Formatted cell value"""

    z: Optional[str] = None
    """Number format associated with the cell"""


class ReadDataTableDataErrorCell(BaseModel):
    t: Literal["e"]
    """Data type of the cell value (always 'e' for 'error')"""

    v: str
    """Underlying cell value"""

    e: Optional[str] = None
    """Description of the error"""

    r: Optional[str] = None
    """Relative A1-based cell reference"""


class ReadDataTableDataEmptyCell(BaseModel):
    t: Literal["z"]
    """Data type of the cell value (always 'z' for 'empty cell')"""


ReadDataTableData: TypeAlias = Union[ReadDataTableDataValueCell, ReadDataTableDataErrorCell, ReadDataTableDataEmptyCell]


class ReadDataTable(BaseModel):
    data: List[List[ReadDataTableData]]

    source: str
    """A1-style reference for the cell or cells that were updated"""

    type: Literal["dataTable"]


class ReadDataListDataValueCell(BaseModel):
    t: Literal["b", "n", "d", "s"]
    """Data type of the cell value (e.g. boolean, number, text)"""

    v: Union[float, str, bool, None] = None
    """Underlying cell value"""

    r: Optional[str] = None
    """Relative A1-based cell reference"""

    w: Optional[str] = None
    """Formatted cell value"""

    z: Optional[str] = None
    """Number format associated with the cell"""


class ReadDataListDataErrorCell(BaseModel):
    t: Literal["e"]
    """Data type of the cell value (always 'e' for 'error')"""

    v: str
    """Underlying cell value"""

    e: Optional[str] = None
    """Description of the error"""

    r: Optional[str] = None
    """Relative A1-based cell reference"""


class ReadDataListDataEmptyCell(BaseModel):
    t: Literal["z"]
    """Data type of the cell value (always 'z' for 'empty cell')"""


ReadDataListData: TypeAlias = Union[ReadDataListDataValueCell, ReadDataListDataErrorCell, ReadDataListDataEmptyCell]


class ReadDataList(BaseModel):
    data: List[ReadDataListData]

    source: str
    """A1-style reference for the cell or cells that were updated"""

    type: Literal["dataList"]


class ReadDataCellDataValueCell(BaseModel):
    t: Literal["b", "n", "d", "s"]
    """Data type of the cell value (e.g. boolean, number, text)"""

    v: Union[float, str, bool, None] = None
    """Underlying cell value"""

    r: Optional[str] = None
    """Relative A1-based cell reference"""

    w: Optional[str] = None
    """Formatted cell value"""

    z: Optional[str] = None
    """Number format associated with the cell"""


class ReadDataCellDataErrorCell(BaseModel):
    t: Literal["e"]
    """Data type of the cell value (always 'e' for 'error')"""

    v: str
    """Underlying cell value"""

    e: Optional[str] = None
    """Description of the error"""

    r: Optional[str] = None
    """Relative A1-based cell reference"""


class ReadDataCellDataEmptyCell(BaseModel):
    t: Literal["z"]
    """Data type of the cell value (always 'z' for 'empty cell')"""


ReadDataCellData: TypeAlias = Union[ReadDataCellDataValueCell, ReadDataCellDataErrorCell, ReadDataCellDataEmptyCell]


class ReadDataCell(BaseModel):
    data: ReadDataCellData
    """
    Represents a single workbook cell, including its value (`v`), cell reference
    (`r`), type (`t`), number format (`z`), and formatted text (`w`).
    """

    source: str
    """A1-style reference for the cell or cells that were updated"""

    type: Literal["cell"]


class ReadValueTable(BaseModel):
    data: List[List[Union[float, str, bool, None]]]

    source: str
    """A1-style reference for the cell or cells that were updated"""

    type: Literal["valueTable"]


class ReadValueList(BaseModel):
    data: List[Union[float, str, bool, None]]

    source: str
    """A1-style reference for the cell or cells that were updated"""

    type: Literal["valueList"]


class ReadValue(BaseModel):
    data: Union[float, str, bool, None] = None

    source: str
    """A1-style reference for the cell or cells that were updated"""

    type: Literal["value"]


class ReadFormattedValueTable(BaseModel):
    data: List[List[str]]

    source: str
    """A1-style reference for the cell or cells that were updated"""

    type: Literal["formattedValueTable"]


class ReadFormattedValueList(BaseModel):
    data: List[str]

    source: str
    """A1-style reference for the cell or cells that were updated"""

    type: Literal["formattedValueList"]


class ReadFormattedValue(BaseModel):
    data: str

    source: str
    """A1-style reference for the cell or cells that were updated"""

    type: Literal["formattedValue"]


Read: TypeAlias = Annotated[
    Union[
        ReadDataTable,
        ReadDataList,
        ReadDataCell,
        ReadValueTable,
        ReadValueList,
        ReadValue,
        ReadFormattedValueTable,
        ReadFormattedValueList,
        ReadFormattedValue,
    ],
    PropertyInfo(discriminator="type"),
]


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
