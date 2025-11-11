# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "WorkbookRenderChartParams",
    "Chart",
    "ChartAxisDim",
    "ChartAxisValue",
    "Apply",
    "ApplyTarget",
    "ApplyTargetReferenceObject",
]


class WorkbookRenderChartParams(TypedDict, total=False):
    chart: Required[Chart]
    """Options for rendering a chart from workbook data.

    Specify the data range, chart type, image output format, and title and axis
    labels.
    """

    apply: Optional[Iterable[Apply]]
    """Cells to update before rendering the chart."""

    matte: Optional[str]
    """Hex color code for the chart's background matte, e.g.

    '#FFFFFF' for white, if not specified, the chart will have a transparent
    background. Note, this is currently only supported for PNG images.
    """

    width: Optional[int]
    """Width of the chart image in pixels.

    If not given, a width of 764px is used. A chart's height cannot be set
    explicitly because it will differ depending upon chart type, title, legend, axis
    labels, and so on.
    """


class ChartAxisDim(TypedDict, total=False):
    number_format: Annotated[Optional[str], PropertyInfo(alias="numberFormat")]
    """Number format pattern used for formatting the axis labels."""

    reverse: Optional[Literal["false", "true"]]
    """If true, invert the scale of the axis. If false, keep the order untouched."""

    title: Optional[str]
    """Cell reference to use as the axis title. Can also be plain text."""


class ChartAxisValue(TypedDict, total=False):
    clip: Optional[Literal["false", "true"]]
    """
    If true, any graphics outside the min or max boundaries of the axes are
    truncated.
    """

    max: Optional[float]
    """A maximum value for the axis."""

    min: Optional[float]
    """A minimum value for the axis."""

    number_format: Annotated[Optional[str], PropertyInfo(alias="numberFormat")]
    """Number format pattern used for formatting the axis labels."""

    reverse: Optional[Literal["false", "true"]]
    """Draw the axis in ascending or descending order."""

    title: Optional[str]
    """Cell reference to use as the axis title. Can also be plain text."""

    type: Optional[Literal["linear", "log"]]
    """Types of scales that can be used by an axis."""


class Chart(TypedDict, total=False):
    axis_dim: Annotated[Optional[ChartAxisDim], PropertyInfo(alias="axisDim")]
    """How an axis representing dimensional categories is presented."""

    axis_value: Annotated[Optional[ChartAxisValue], PropertyInfo(alias="axisValue")]
    """How an axis representing value magnitudes is presented."""

    blanks: Optional[Literal["gap", "zero", "span"]]
    """
    Enum representing the supported strategies for handling blank or missing data
    points.
    """

    chart_colors: Annotated[Optional[str], PropertyInfo(alias="chartColors")]
    """
    An Excel array expression that returns a 1-dimensional list of HTML color
    strings
    """

    color_by_point: Annotated[Optional[str], PropertyInfo(alias="colorByPoint")]
    """Vary colors by point rather than series."""

    data: Optional[str]
    """Chart data range, prefixed with an equals sign"""

    data_lines: Annotated[Optional[str], PropertyInfo(alias="dataLines")]
    """Chart data range, prefixed with an equals sign, used for lines in a combo chart"""

    dir: Optional[Literal["", "col", "row"]]
    """Enum representing the supported read orientations for data directions."""

    footnote: Optional[str]
    """Cell reference to use as the chart's footnote text. Can also be plain text."""

    format: Optional[Literal["png", "svg"]]
    """Supported image types for rendering charts from workbook data."""

    interpolate: Optional[Literal["linear", "step", "step-after", "step-before", "monotone", "basis"]]
    """
    Enum representing the supported interpolation types for data visualization or
    curve fitting.
    """

    labels: Optional[str]
    """
    Range of cells to use as the chart's x-axis labels, prefixed with an equals sign
    """

    legend: Optional[str]
    """
    Range of cells to use as the chart's legend labels, prefixed with an equals sign
    """

    legend_lines: Annotated[Optional[str], PropertyInfo(alias="legendLines")]
    """
    Range of cells to use as the chart's line labels in the legend, prefixed with an
    equals sign
    """

    legend_visible: Annotated[Optional[Literal["false", "true"]], PropertyInfo(alias="legendVisible")]
    """Whether to display a chart legend"""

    number_format: Annotated[Optional[str], PropertyInfo(alias="numberFormat")]
    """Number format pattern used for formatting labels on the chart."""

    sort_by: Annotated[Optional[int], PropertyInfo(alias="sortBy")]
    """The number of which series the data should be sorted by (e.g.

    1 for the first series).
    """

    sort_order: Annotated[Optional[Literal["", "ascending", "descending"]], PropertyInfo(alias="sortOrder")]
    """The sorting direction when the sortBy property is set."""

    stacked: Optional[Literal["false", "true"]]
    """Whether to display series stacked or grouped"""

    subtitle: Optional[str]
    """Cell reference to use as the chart's subtitle. Can also be plain text."""

    title: Optional[str]
    """Cell reference to use as the chart's title. Can also be plain text."""

    type: Optional[Literal["area", "bar", "column", "combo", "line", "pie", "scatterplot", "waterfall"]]
    """Types of charts that can be rendered using workbook data."""

    values: Optional[Literal["none", "selective", "all"]]
    """Options for labelling individual data values on a chart.

    If "none" (the default) then no data labels are shown. If "selective", data
    labels are shown when they fit without overlap. If "all", all values are
    labelled.
    """


class ApplyTargetReferenceObject(TypedDict, total=False):
    cells: Required[str]
    """Unprefixed A1-style range, id, or name"""

    sheet: Required[Optional[str]]
    """Name of the sheet to reference"""


ApplyTarget: TypeAlias = Union[str, ApplyTargetReferenceObject]


class Apply(TypedDict, total=False):
    target: Required[ApplyTarget]
    """Reference for the cell to write to"""

    value: Required[Union[float, str, bool, None]]
    """Value to write to the target cell"""
