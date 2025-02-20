# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkbookExportParams", "Apply", "GoalSeek"]


class WorkbookExportParams(TypedDict, total=False):
    apply: Optional[Iterable[Apply]]
    """Cells to update before exporting"""

    goal_seek: Annotated[Optional[GoalSeek], PropertyInfo(alias="goalSeek")]
    """Goal seek.

    Use this to calculate the required input value for a formula to achieve a
    specified target result. This is particularly useful when the desired outcome is
    known, but the corresponding input is not.
    """


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
