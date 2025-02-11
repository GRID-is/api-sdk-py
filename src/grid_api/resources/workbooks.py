# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ..types import workbook_query_params, workbook_render_chart_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.workbook_query_response import WorkbookQueryResponse

__all__ = ["WorkbooksResource", "AsyncWorkbooksResource"]


class WorkbooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkbooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/spreadsheet-api-python#accessing-raw-response-data-eg-headers
        """
        return WorkbooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkbooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/spreadsheet-api-python#with_streaming_response
        """
        return WorkbooksResourceWithStreamingResponse(self)

    def query(
        self,
        id: str,
        *,
        read: List[str],
        apply: Optional[Iterable[workbook_query_params.Apply]] | NotGiven = NOT_GIVEN,
        goal_seek: Optional[workbook_query_params.GoalSeek] | NotGiven = NOT_GIVEN,
        options: Optional[workbook_query_params.Options] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkbookQueryResponse:
        """
        Read cell data or apply temporary changes.

        Send a JSON object with a `read` key to read values from cells and formulas.
        Optionally, use the `apply` key to update cells before reading.

        Args:
          read: Cell references to read from the workbook and return to the client

          apply: Cells to update before reading. Note that the API has no state and any changes
              made are cleared after each request

          goal_seek: Goal seek. Use this to calculate the required input value for a formula to
              achieve a specified target result. This is particularly useful when the desired
              outcome is known, but the corresponding input is not.

          options: Defines settings for formatting and structuring query results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/workbooks/{id}/query",
            body=maybe_transform(
                {
                    "read": read,
                    "apply": apply,
                    "goal_seek": goal_seek,
                    "options": options,
                },
                workbook_query_params.WorkbookQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkbookQueryResponse,
        )

    def render_chart(
        self,
        id: str,
        *,
        chart: workbook_render_chart_params.Chart,
        apply: Optional[Iterable[workbook_render_chart_params.Apply]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Render a chart using workbook data

        Args:
          chart: Options for rendering a chart from workbook data. Specify the data range, chart
              type, image output format, and title and axis labels.

          apply: Cells to update before rendering the chart. Changes are discarded at the end of
              the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/workbooks/{id}/chart",
            body=maybe_transform(
                {
                    "chart": chart,
                    "apply": apply,
                },
                workbook_render_chart_params.WorkbookRenderChartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncWorkbooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkbooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/spreadsheet-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkbooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkbooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/spreadsheet-api-python#with_streaming_response
        """
        return AsyncWorkbooksResourceWithStreamingResponse(self)

    async def query(
        self,
        id: str,
        *,
        read: List[str],
        apply: Optional[Iterable[workbook_query_params.Apply]] | NotGiven = NOT_GIVEN,
        goal_seek: Optional[workbook_query_params.GoalSeek] | NotGiven = NOT_GIVEN,
        options: Optional[workbook_query_params.Options] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkbookQueryResponse:
        """
        Read cell data or apply temporary changes.

        Send a JSON object with a `read` key to read values from cells and formulas.
        Optionally, use the `apply` key to update cells before reading.

        Args:
          read: Cell references to read from the workbook and return to the client

          apply: Cells to update before reading. Note that the API has no state and any changes
              made are cleared after each request

          goal_seek: Goal seek. Use this to calculate the required input value for a formula to
              achieve a specified target result. This is particularly useful when the desired
              outcome is known, but the corresponding input is not.

          options: Defines settings for formatting and structuring query results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/workbooks/{id}/query",
            body=await async_maybe_transform(
                {
                    "read": read,
                    "apply": apply,
                    "goal_seek": goal_seek,
                    "options": options,
                },
                workbook_query_params.WorkbookQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkbookQueryResponse,
        )

    async def render_chart(
        self,
        id: str,
        *,
        chart: workbook_render_chart_params.Chart,
        apply: Optional[Iterable[workbook_render_chart_params.Apply]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Render a chart using workbook data

        Args:
          chart: Options for rendering a chart from workbook data. Specify the data range, chart
              type, image output format, and title and axis labels.

          apply: Cells to update before rendering the chart. Changes are discarded at the end of
              the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/workbooks/{id}/chart",
            body=await async_maybe_transform(
                {
                    "chart": chart,
                    "apply": apply,
                },
                workbook_render_chart_params.WorkbookRenderChartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class WorkbooksResourceWithRawResponse:
    def __init__(self, workbooks: WorkbooksResource) -> None:
        self._workbooks = workbooks

        self.query = to_raw_response_wrapper(
            workbooks.query,
        )
        self.render_chart = to_raw_response_wrapper(
            workbooks.render_chart,
        )


class AsyncWorkbooksResourceWithRawResponse:
    def __init__(self, workbooks: AsyncWorkbooksResource) -> None:
        self._workbooks = workbooks

        self.query = async_to_raw_response_wrapper(
            workbooks.query,
        )
        self.render_chart = async_to_raw_response_wrapper(
            workbooks.render_chart,
        )


class WorkbooksResourceWithStreamingResponse:
    def __init__(self, workbooks: WorkbooksResource) -> None:
        self._workbooks = workbooks

        self.query = to_streamed_response_wrapper(
            workbooks.query,
        )
        self.render_chart = to_streamed_response_wrapper(
            workbooks.render_chart,
        )


class AsyncWorkbooksResourceWithStreamingResponse:
    def __init__(self, workbooks: AsyncWorkbooksResource) -> None:
        self._workbooks = workbooks

        self.query = async_to_streamed_response_wrapper(
            workbooks.query,
        )
        self.render_chart = async_to_streamed_response_wrapper(
            workbooks.render_chart,
        )
