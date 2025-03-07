# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkbookListResponse"]


class WorkbookListResponse(BaseModel):
    id: str
    """A workbook's unique identifier"""

    created: datetime
    """The date/time the workbook was created"""

    defect: Literal[
        "",
        "too_big",
        "converted_workbook_too_big",
        "unrecognized_format",
        "cannot_fetch_from_remote",
        "processing_timeout",
        "conversion_error",
    ]
    """The defect that was found in the most recent version of the workbook, if any"""

    filename: str
    """The original filename of the uploaded workbook"""

    modified: datetime
    """The date/time the workbook was last modified"""

    state: Literal["processing", "ready", "error"]
    """The current state of the most recent version of the workbook"""

    version: int
    """The most recent version of the workbook"""

    latest_ready_version: Optional[int] = None
    """The latest version of the workbook that has a 'ready' state"""
