# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WorkbookUploadResponse"]


class WorkbookUploadResponse(BaseModel):
    id: str
    """The id of the newly uploaded workbook"""
