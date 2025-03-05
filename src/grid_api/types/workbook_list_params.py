# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkbookListParams"]


class WorkbookListParams(TypedDict, total=False):
    cursor: str
    """Cursor for the next page of items.

    If not provided, the first batch of items will be returned.
    """

    limit: int
    """Number of items to return per page"""
