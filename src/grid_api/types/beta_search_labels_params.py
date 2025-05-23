# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BetaSearchLabelsParams"]


class BetaSearchLabelsParams(TypedDict, total=False):
    query: Required[str]

    max_labels: Optional[int]
    """Maximum number of labels to return per workbook"""

    max_results: Optional[int]
    """Maximum number of workbooks to return results for"""
