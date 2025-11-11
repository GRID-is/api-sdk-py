# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Mapping, Iterable, Optional, cast

import httpx

from ..types import (
    workbook_calc_params,
    workbook_list_params,
    workbook_query_params,
    workbook_export_params,
    workbook_upload_params,
    workbook_values_params,
    workbook_render_chart_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..pagination import SyncCursorPagination, AsyncCursorPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.workbook_calc_response import WorkbookCalcResponse
from ..types.workbook_list_response import WorkbookListResponse
from ..types.workbook_query_response import WorkbookQueryResponse
from ..types.workbook_upload_response import WorkbookUploadResponse
from ..types.workbook_values_response import WorkbookValuesResponse

__all__ = ["WorkbooksResource", "AsyncWorkbooksResource"]


class WorkbooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkbooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/GRID-is/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return WorkbooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkbooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/GRID-is/api-sdk-py#with_streaming_response
        """
        return WorkbooksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[WorkbookListResponse]:
        """
        List the workbooks linked to an account.

        This endpoint returns a paginated list of workbooks.

        Args:
          cursor: Cursor for the next page of items. If not provided, the first batch of items
              will be returned.

          limit: Number of items to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/workbooks",
            page=SyncCursorPagination[WorkbookListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    workbook_list_params.WorkbookListParams,
                ),
            ),
            model=WorkbookListResponse,
        )

    def calc(
        self,
        id: str,
        *,
        read: SequenceNotStr[str],
        apply: Optional[Dict[str, Union[float, str, bool, None]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkbookCalcResponse:
        """
        Run calculations in a workbook and retrieve cell objects.

        Args:
          apply: Map of cell references to values. The values are written to cells in the
              spreadsheet before performing the read operation. You can write numbers,
              strings, and booleans. Values applied within a request are temporary and affect
              only that specific request. They are not permanently written to the original
              spreadsheet.

              ```json
              {
                "apply": { "A1": 10, "A2": 2.718, "A3": "Total", "A4": true, "A5": null }
                // ...
              }
              ```

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/workbooks/{id}/calc",
            body=maybe_transform(
                {
                    "read": read,
                    "apply": apply,
                },
                workbook_calc_params.WorkbookCalcParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkbookCalcResponse,
        )

    def export(
        self,
        id: str,
        *,
        apply: Optional[Iterable[workbook_export_params.Apply]] | Omit = omit,
        goal_seek: Optional[workbook_export_params.GoalSeek] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Export a workbook as an .xlsx file.

        Cells can be updated before the workbook is
        exported.

        Args:
          apply: Cells to update before exporting.

          goal_seek: Goal seek. Use this to calculate the required input value for a formula to
              achieve a specified target result. This is particularly useful when the desired
              outcome is known, but the corresponding input is not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            **(extra_headers or {}),
        }
        return self._post(
            f"/v1/workbooks/{id}/export",
            body=maybe_transform(
                {
                    "apply": apply,
                    "goal_seek": goal_seek,
                },
                workbook_export_params.WorkbookExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def query(
        self,
        id: str,
        *,
        read: SequenceNotStr[workbook_query_params.Read],
        apply: Optional[Iterable[workbook_query_params.Apply]] | Omit = omit,
        goal_seek: Optional[workbook_query_params.GoalSeek] | Omit = omit,
        options: Optional[workbook_query_params.Options] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          options: Defines settings for configuring query results.

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
        apply: Optional[Iterable[workbook_render_chart_params.Apply]] | Omit = omit,
        matte: Optional[str] | Omit = omit,
        width: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Render a chart using workbook data

        Args:
          chart: Options for rendering a chart from workbook data. Specify the data range, chart
              type, image output format, and title and axis labels.

          apply: Cells to update before rendering the chart.

          matte: Hex color code for the chart's background matte, e.g. '#FFFFFF' for white, if
              not specified, the chart will have a transparent background. Note, this is
              currently only supported for PNG images.

          width: Width of the chart image in pixels. If not given, a width of 764px is used. A
              chart's height cannot be set explicitly because it will differ depending upon
              chart type, title, legend, axis labels, and so on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return self._post(
            f"/v1/workbooks/{id}/chart",
            body=maybe_transform(
                {
                    "chart": chart,
                    "apply": apply,
                    "matte": matte,
                    "width": width,
                },
                workbook_render_chart_params.WorkbookRenderChartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkbookUploadResponse:
        """
        Upload an Excel workbook file and make it available in the API.

        The workbook will be processed in the background. Once it's processed
        successfully it will be available for querying and exporting.

        Args:
          file: Excel (.xlsx) file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/workbooks",
            body=maybe_transform(body, workbook_upload_params.WorkbookUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkbookUploadResponse,
        )

    def values(
        self,
        id: str,
        *,
        read: SequenceNotStr[str],
        apply: Optional[Dict[str, Union[float, str, bool, None]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkbookValuesResponse:
        """
        Run calculations in a workbook and retrieve cell values.

        Args:
          apply: Map of cell references to values. The values are written to cells in the
              spreadsheet before performing the read operation. You can write numbers,
              strings, and booleans. Values applied within a request are temporary and affect
              only that specific request. They are not permanently written to the original
              spreadsheet.

              ```json
              {
                "apply": { "A1": 10, "A2": 2.718, "A3": "Total", "A4": true, "A5": null }
                // ...
              }
              ```

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/workbooks/{id}/values",
            body=maybe_transform(
                {
                    "read": read,
                    "apply": apply,
                },
                workbook_values_params.WorkbookValuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkbookValuesResponse,
        )


class AsyncWorkbooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkbooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/GRID-is/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkbooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkbooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/GRID-is/api-sdk-py#with_streaming_response
        """
        return AsyncWorkbooksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WorkbookListResponse, AsyncCursorPagination[WorkbookListResponse]]:
        """
        List the workbooks linked to an account.

        This endpoint returns a paginated list of workbooks.

        Args:
          cursor: Cursor for the next page of items. If not provided, the first batch of items
              will be returned.

          limit: Number of items to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/workbooks",
            page=AsyncCursorPagination[WorkbookListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    workbook_list_params.WorkbookListParams,
                ),
            ),
            model=WorkbookListResponse,
        )

    async def calc(
        self,
        id: str,
        *,
        read: SequenceNotStr[str],
        apply: Optional[Dict[str, Union[float, str, bool, None]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkbookCalcResponse:
        """
        Run calculations in a workbook and retrieve cell objects.

        Args:
          apply: Map of cell references to values. The values are written to cells in the
              spreadsheet before performing the read operation. You can write numbers,
              strings, and booleans. Values applied within a request are temporary and affect
              only that specific request. They are not permanently written to the original
              spreadsheet.

              ```json
              {
                "apply": { "A1": 10, "A2": 2.718, "A3": "Total", "A4": true, "A5": null }
                // ...
              }
              ```

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/workbooks/{id}/calc",
            body=await async_maybe_transform(
                {
                    "read": read,
                    "apply": apply,
                },
                workbook_calc_params.WorkbookCalcParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkbookCalcResponse,
        )

    async def export(
        self,
        id: str,
        *,
        apply: Optional[Iterable[workbook_export_params.Apply]] | Omit = omit,
        goal_seek: Optional[workbook_export_params.GoalSeek] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Export a workbook as an .xlsx file.

        Cells can be updated before the workbook is
        exported.

        Args:
          apply: Cells to update before exporting.

          goal_seek: Goal seek. Use this to calculate the required input value for a formula to
              achieve a specified target result. This is particularly useful when the desired
              outcome is known, but the corresponding input is not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            **(extra_headers or {}),
        }
        return await self._post(
            f"/v1/workbooks/{id}/export",
            body=await async_maybe_transform(
                {
                    "apply": apply,
                    "goal_seek": goal_seek,
                },
                workbook_export_params.WorkbookExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def query(
        self,
        id: str,
        *,
        read: SequenceNotStr[workbook_query_params.Read],
        apply: Optional[Iterable[workbook_query_params.Apply]] | Omit = omit,
        goal_seek: Optional[workbook_query_params.GoalSeek] | Omit = omit,
        options: Optional[workbook_query_params.Options] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          options: Defines settings for configuring query results.

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
        apply: Optional[Iterable[workbook_render_chart_params.Apply]] | Omit = omit,
        matte: Optional[str] | Omit = omit,
        width: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Render a chart using workbook data

        Args:
          chart: Options for rendering a chart from workbook data. Specify the data range, chart
              type, image output format, and title and axis labels.

          apply: Cells to update before rendering the chart.

          matte: Hex color code for the chart's background matte, e.g. '#FFFFFF' for white, if
              not specified, the chart will have a transparent background. Note, this is
              currently only supported for PNG images.

          width: Width of the chart image in pixels. If not given, a width of 764px is used. A
              chart's height cannot be set explicitly because it will differ depending upon
              chart type, title, legend, axis labels, and so on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return await self._post(
            f"/v1/workbooks/{id}/chart",
            body=await async_maybe_transform(
                {
                    "chart": chart,
                    "apply": apply,
                    "matte": matte,
                    "width": width,
                },
                workbook_render_chart_params.WorkbookRenderChartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkbookUploadResponse:
        """
        Upload an Excel workbook file and make it available in the API.

        The workbook will be processed in the background. Once it's processed
        successfully it will be available for querying and exporting.

        Args:
          file: Excel (.xlsx) file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/workbooks",
            body=await async_maybe_transform(body, workbook_upload_params.WorkbookUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkbookUploadResponse,
        )

    async def values(
        self,
        id: str,
        *,
        read: SequenceNotStr[str],
        apply: Optional[Dict[str, Union[float, str, bool, None]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkbookValuesResponse:
        """
        Run calculations in a workbook and retrieve cell values.

        Args:
          apply: Map of cell references to values. The values are written to cells in the
              spreadsheet before performing the read operation. You can write numbers,
              strings, and booleans. Values applied within a request are temporary and affect
              only that specific request. They are not permanently written to the original
              spreadsheet.

              ```json
              {
                "apply": { "A1": 10, "A2": 2.718, "A3": "Total", "A4": true, "A5": null }
                // ...
              }
              ```

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/workbooks/{id}/values",
            body=await async_maybe_transform(
                {
                    "read": read,
                    "apply": apply,
                },
                workbook_values_params.WorkbookValuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkbookValuesResponse,
        )


class WorkbooksResourceWithRawResponse:
    def __init__(self, workbooks: WorkbooksResource) -> None:
        self._workbooks = workbooks

        self.list = to_raw_response_wrapper(
            workbooks.list,
        )
        self.calc = to_raw_response_wrapper(
            workbooks.calc,
        )
        self.export = to_custom_raw_response_wrapper(
            workbooks.export,
            BinaryAPIResponse,
        )
        self.query = to_raw_response_wrapper(
            workbooks.query,
        )
        self.render_chart = to_custom_raw_response_wrapper(
            workbooks.render_chart,
            BinaryAPIResponse,
        )
        self.upload = to_raw_response_wrapper(
            workbooks.upload,
        )
        self.values = to_raw_response_wrapper(
            workbooks.values,
        )


class AsyncWorkbooksResourceWithRawResponse:
    def __init__(self, workbooks: AsyncWorkbooksResource) -> None:
        self._workbooks = workbooks

        self.list = async_to_raw_response_wrapper(
            workbooks.list,
        )
        self.calc = async_to_raw_response_wrapper(
            workbooks.calc,
        )
        self.export = async_to_custom_raw_response_wrapper(
            workbooks.export,
            AsyncBinaryAPIResponse,
        )
        self.query = async_to_raw_response_wrapper(
            workbooks.query,
        )
        self.render_chart = async_to_custom_raw_response_wrapper(
            workbooks.render_chart,
            AsyncBinaryAPIResponse,
        )
        self.upload = async_to_raw_response_wrapper(
            workbooks.upload,
        )
        self.values = async_to_raw_response_wrapper(
            workbooks.values,
        )


class WorkbooksResourceWithStreamingResponse:
    def __init__(self, workbooks: WorkbooksResource) -> None:
        self._workbooks = workbooks

        self.list = to_streamed_response_wrapper(
            workbooks.list,
        )
        self.calc = to_streamed_response_wrapper(
            workbooks.calc,
        )
        self.export = to_custom_streamed_response_wrapper(
            workbooks.export,
            StreamedBinaryAPIResponse,
        )
        self.query = to_streamed_response_wrapper(
            workbooks.query,
        )
        self.render_chart = to_custom_streamed_response_wrapper(
            workbooks.render_chart,
            StreamedBinaryAPIResponse,
        )
        self.upload = to_streamed_response_wrapper(
            workbooks.upload,
        )
        self.values = to_streamed_response_wrapper(
            workbooks.values,
        )


class AsyncWorkbooksResourceWithStreamingResponse:
    def __init__(self, workbooks: AsyncWorkbooksResource) -> None:
        self._workbooks = workbooks

        self.list = async_to_streamed_response_wrapper(
            workbooks.list,
        )
        self.calc = async_to_streamed_response_wrapper(
            workbooks.calc,
        )
        self.export = async_to_custom_streamed_response_wrapper(
            workbooks.export,
            AsyncStreamedBinaryAPIResponse,
        )
        self.query = async_to_streamed_response_wrapper(
            workbooks.query,
        )
        self.render_chart = async_to_custom_streamed_response_wrapper(
            workbooks.render_chart,
            AsyncStreamedBinaryAPIResponse,
        )
        self.upload = async_to_streamed_response_wrapper(
            workbooks.upload,
        )
        self.values = async_to_streamed_response_wrapper(
            workbooks.values,
        )
