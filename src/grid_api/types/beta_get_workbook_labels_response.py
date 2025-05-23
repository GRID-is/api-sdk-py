# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BetaGetWorkbookLabelsResponse", "Label"]


class Label(BaseModel):
    at: str
    """The cell address/reference which the label applies to"""

    for_: str = FieldInfo(alias="for")
    """The cell address/reference which the label applies to"""

    text: str
    """The label string"""

    type: Optional[str] = None
    """The type of the label, almost always text, not to be confused with cell type"""


class BetaGetWorkbookLabelsResponse(BaseModel):
    created: datetime
    """The date/time the labels were detected and stored"""

    labels: List[Label]
    """The labels associated with the workbook"""

    workbook_id: str
    """The id of the workbook the labels belong to"""

    workbook_version: int
    """The version of the workbook the labels belong to"""
