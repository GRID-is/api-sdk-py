# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import beta_search_labels_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.beta_search_labels_response import BetaSearchLabelsResponse
from ..types.beta_get_workbook_labels_response import BetaGetWorkbookLabelsResponse
from ..types.beta_get_workbook_parameters_response import BetaGetWorkbookParametersResponse

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/GRID-is/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/GRID-is/api-sdk-py#with_streaming_response
        """
        return BetaResourceWithStreamingResponse(self)

    def get_workbook_labels(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BetaGetWorkbookLabelsResponse:
        """
        Retrieve labels automatically detected for cells and ranges in the workbook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/workbooks/{id}/labels",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaGetWorkbookLabelsResponse,
        )

    def get_workbook_parameters(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BetaGetWorkbookParametersResponse:
        """
        Retrieve labels automatically detected for cells and ranges in the workbook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/workbooks/{id}/parameters",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaGetWorkbookParametersResponse,
        )

    def search_labels(
        self,
        *,
        query: str,
        max_labels: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BetaSearchLabelsResponse:
        """
        Search data labels across all spreadsheets uploaded to an account

        Args:
          max_labels: Maximum number of labels to return per workbook

          max_results: Maximum number of workbooks to return results for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/workbooks/search/labels",
            body=maybe_transform(
                {
                    "query": query,
                    "max_labels": max_labels,
                    "max_results": max_results,
                },
                beta_search_labels_params.BetaSearchLabelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaSearchLabelsResponse,
        )


class AsyncBetaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/GRID-is/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/GRID-is/api-sdk-py#with_streaming_response
        """
        return AsyncBetaResourceWithStreamingResponse(self)

    async def get_workbook_labels(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BetaGetWorkbookLabelsResponse:
        """
        Retrieve labels automatically detected for cells and ranges in the workbook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/workbooks/{id}/labels",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaGetWorkbookLabelsResponse,
        )

    async def get_workbook_parameters(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BetaGetWorkbookParametersResponse:
        """
        Retrieve labels automatically detected for cells and ranges in the workbook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/workbooks/{id}/parameters",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaGetWorkbookParametersResponse,
        )

    async def search_labels(
        self,
        *,
        query: str,
        max_labels: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BetaSearchLabelsResponse:
        """
        Search data labels across all spreadsheets uploaded to an account

        Args:
          max_labels: Maximum number of labels to return per workbook

          max_results: Maximum number of workbooks to return results for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/workbooks/search/labels",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "max_labels": max_labels,
                    "max_results": max_results,
                },
                beta_search_labels_params.BetaSearchLabelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaSearchLabelsResponse,
        )


class BetaResourceWithRawResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

        self.get_workbook_labels = to_raw_response_wrapper(
            beta.get_workbook_labels,
        )
        self.get_workbook_parameters = to_raw_response_wrapper(
            beta.get_workbook_parameters,
        )
        self.search_labels = to_raw_response_wrapper(
            beta.search_labels,
        )


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.get_workbook_labels = async_to_raw_response_wrapper(
            beta.get_workbook_labels,
        )
        self.get_workbook_parameters = async_to_raw_response_wrapper(
            beta.get_workbook_parameters,
        )
        self.search_labels = async_to_raw_response_wrapper(
            beta.search_labels,
        )


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

        self.get_workbook_labels = to_streamed_response_wrapper(
            beta.get_workbook_labels,
        )
        self.get_workbook_parameters = to_streamed_response_wrapper(
            beta.get_workbook_parameters,
        )
        self.search_labels = to_streamed_response_wrapper(
            beta.search_labels,
        )


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.get_workbook_labels = async_to_streamed_response_wrapper(
            beta.get_workbook_labels,
        )
        self.get_workbook_parameters = async_to_streamed_response_wrapper(
            beta.get_workbook_parameters,
        )
        self.search_labels = async_to_streamed_response_wrapper(
            beta.search_labels,
        )
