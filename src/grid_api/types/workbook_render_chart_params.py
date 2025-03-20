# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WorkbookRenderChartParams", "Chart", "Apply"]


class WorkbookRenderChartParams(TypedDict, total=False):
    chart: Required[Chart]
    """Options for rendering a chart from workbook data.

    Specify the data range, chart type, image output format, and title and axis
    labels.
    """

    apply: Optional[Iterable[Apply]]
    """Cells to update before rendering the chart.

    Changes are discarded at the end of the request
    """


class Chart(TypedDict, total=False):
    data: Required[Optional[str]]
    """Chart data range, prefixed with an equals sign"""

    format: Literal["png", "svg"]
    """File format to use for the chart image"""

    labels: Optional[str]
    """
    Range of cells to use as the chart's x-axis labels, prefixed with an equals sign
    """

    title: Optional[str]
    """Cell reference to use as the chart's title. Can also be plain text."""

    type: Literal["line", "column"]
    """Type of chart to render"""

    values: Literal["none", "selective", "all"]
    """How to label individual data values on the chart"""


class Apply(TypedDict, total=False):
    target: Required[str]
    """A1-style reference for the cell to write to"""

    value: Required[Union[float, str, bool, None]]
    """Value to write to the target cell"""
