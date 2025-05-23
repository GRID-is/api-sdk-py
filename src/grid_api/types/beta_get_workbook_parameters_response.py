# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BetaGetWorkbookParametersResponse", "Parameter", "ParameterLabel"]


class ParameterLabel(BaseModel):
    at: str
    """The cell address/reference which the label applies to"""

    text: str
    """The label string"""


class Parameter(BaseModel):
    labels: List[ParameterLabel]
    """The labels associated with the parameter"""

    ref: str
    """The cell address/reference containing the parameter"""

    type: Literal["blank", "date", "number", "string", "boolean", "error"]
    """The type of value found in the parameter cell"""

    value: Union[str, float, bool, None] = None
    """The value in the parameter cell, type is determined by the type field"""


class BetaGetWorkbookParametersResponse(BaseModel):
    created: datetime
    """The date/time the parameters were detected and stored"""

    parameters: List[Parameter]
    """The parameters associated with the workbook"""

    workbook_id: str
    """The id of the workbook the labels belong to"""

    workbook_version: int
    """The version of the workbook the labels belong to"""
