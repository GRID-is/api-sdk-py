# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["WorkbookUploadParams"]


class WorkbookUploadParams(TypedDict, total=False):
    body: Required[FileTypes]

    x_uploaded_filename: Required[Annotated[str, PropertyInfo(alias="X-Uploaded-Filename")]]
    """The name of the workbook file"""
