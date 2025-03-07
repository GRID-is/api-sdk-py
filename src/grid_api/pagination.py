# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["CursorPaginationPagination", "SyncCursorPagination", "AsyncCursorPagination"]

_T = TypeVar("_T")


class CursorPaginationPagination(BaseModel):
    next_cursor: Optional[str] = None


class SyncCursorPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    pagination: Optional[CursorPaginationPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.pagination is not None:
            if self.pagination.next_cursor is not None:
                next_cursor = self.pagination.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncCursorPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    pagination: Optional[CursorPaginationPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.pagination is not None:
            if self.pagination.next_cursor is not None:
                next_cursor = self.pagination.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})
