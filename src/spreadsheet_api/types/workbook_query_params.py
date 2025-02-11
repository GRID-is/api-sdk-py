# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkbookQueryParams", "Apply", "GoalSeek", "Options"]


class WorkbookQueryParams(TypedDict, total=False):
    read: Required[List[str]]
    """Cell references to read from the workbook and return to the client"""

    apply: Optional[Iterable[Apply]]
    """Cells to update before reading.

    Note that the API has no state and any changes made are cleared after each
    request
    """

    goal_seek: Annotated[Optional[GoalSeek], PropertyInfo(alias="goalSeek")]
    """Goal seek.

    Use this to calculate the required input value for a formula to achieve a
    specified target result. This is particularly useful when the desired outcome is
    known, but the corresponding input is not.
    """

    options: Optional[Options]
    """Defines settings for formatting and structuring query results."""


class Apply(TypedDict, total=False):
    target: Required[str]
    """A1-style reference for the cell to write to"""

    value: Required[Union[float, str, bool, None]]
    """Value to write to the target cell"""


class GoalSeek(TypedDict, total=False):
    control_cell: Required[Annotated[str, PropertyInfo(alias="controlCell")]]
    """Reference for the cell that will contain the solution"""

    target_cell: Required[Annotated[str, PropertyInfo(alias="targetCell")]]
    """Reference for the cell that contains the formula you want to resolve"""

    target_value: Required[Annotated[float, PropertyInfo(alias="targetValue")]]
    """The value you want the formula to return"""


class Options(TypedDict, total=False):
    axis: Optional[Literal["rows", "columns"]]
    """Determines if data is outputted as rows or columns"""

    originals: Optional[Literal["off", "on"]]
    """
    When "originals" option is "on", include original values for cells you apply
    values to
    """

    refs: Optional[Literal["off", "on"]]
    """When "refs" option is "on", include cell addresses (e.g.

    A1) in each cell object as the "r" property
    """

    structure: Optional[Literal["single", "list", "table"]]
    """Specifies if read values are returned as a single value, a list, or a 2D table"""

    values: Optional[Literal["full", "raw", "formatted"]]
    """
    Defines if individual cell values are returned in full (JSON objects), raw (just
    the value), or formatted (with number formatting applied)
    """
