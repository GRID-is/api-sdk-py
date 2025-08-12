# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from grid_api import Grid, AsyncGrid
from tests.utils import assert_matches_type
from grid_api.types import (
    BetaSearchLabelsResponse,
    BetaGetWorkbookLabelsResponse,
    BetaGetWorkbookParametersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBeta:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_workbook_labels(self, client: Grid) -> None:
        beta = client.beta.get_workbook_labels(
            "id",
        )
        assert_matches_type(BetaGetWorkbookLabelsResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_workbook_labels(self, client: Grid) -> None:
        response = client.beta.with_raw_response.get_workbook_labels(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(BetaGetWorkbookLabelsResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_workbook_labels(self, client: Grid) -> None:
        with client.beta.with_streaming_response.get_workbook_labels(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(BetaGetWorkbookLabelsResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_workbook_labels(self, client: Grid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.beta.with_raw_response.get_workbook_labels(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_workbook_parameters(self, client: Grid) -> None:
        beta = client.beta.get_workbook_parameters(
            "id",
        )
        assert_matches_type(BetaGetWorkbookParametersResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_workbook_parameters(self, client: Grid) -> None:
        response = client.beta.with_raw_response.get_workbook_parameters(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(BetaGetWorkbookParametersResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_workbook_parameters(self, client: Grid) -> None:
        with client.beta.with_streaming_response.get_workbook_parameters(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(BetaGetWorkbookParametersResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_workbook_parameters(self, client: Grid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.beta.with_raw_response.get_workbook_parameters(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_labels(self, client: Grid) -> None:
        beta = client.beta.search_labels(
            query="profit",
        )
        assert_matches_type(BetaSearchLabelsResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_labels_with_all_params(self, client: Grid) -> None:
        beta = client.beta.search_labels(
            query="profit",
            max_labels=20,
            max_results=10,
        )
        assert_matches_type(BetaSearchLabelsResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search_labels(self, client: Grid) -> None:
        response = client.beta.with_raw_response.search_labels(
            query="profit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(BetaSearchLabelsResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search_labels(self, client: Grid) -> None:
        with client.beta.with_streaming_response.search_labels(
            query="profit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(BetaSearchLabelsResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBeta:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_workbook_labels(self, async_client: AsyncGrid) -> None:
        beta = await async_client.beta.get_workbook_labels(
            "id",
        )
        assert_matches_type(BetaGetWorkbookLabelsResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_workbook_labels(self, async_client: AsyncGrid) -> None:
        response = await async_client.beta.with_raw_response.get_workbook_labels(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = await response.parse()
        assert_matches_type(BetaGetWorkbookLabelsResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_workbook_labels(self, async_client: AsyncGrid) -> None:
        async with async_client.beta.with_streaming_response.get_workbook_labels(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(BetaGetWorkbookLabelsResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_workbook_labels(self, async_client: AsyncGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.beta.with_raw_response.get_workbook_labels(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_workbook_parameters(self, async_client: AsyncGrid) -> None:
        beta = await async_client.beta.get_workbook_parameters(
            "id",
        )
        assert_matches_type(BetaGetWorkbookParametersResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_workbook_parameters(self, async_client: AsyncGrid) -> None:
        response = await async_client.beta.with_raw_response.get_workbook_parameters(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = await response.parse()
        assert_matches_type(BetaGetWorkbookParametersResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_workbook_parameters(self, async_client: AsyncGrid) -> None:
        async with async_client.beta.with_streaming_response.get_workbook_parameters(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(BetaGetWorkbookParametersResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_workbook_parameters(self, async_client: AsyncGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.beta.with_raw_response.get_workbook_parameters(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_labels(self, async_client: AsyncGrid) -> None:
        beta = await async_client.beta.search_labels(
            query="profit",
        )
        assert_matches_type(BetaSearchLabelsResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_labels_with_all_params(self, async_client: AsyncGrid) -> None:
        beta = await async_client.beta.search_labels(
            query="profit",
            max_labels=20,
            max_results=10,
        )
        assert_matches_type(BetaSearchLabelsResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search_labels(self, async_client: AsyncGrid) -> None:
        response = await async_client.beta.with_raw_response.search_labels(
            query="profit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = await response.parse()
        assert_matches_type(BetaSearchLabelsResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search_labels(self, async_client: AsyncGrid) -> None:
        async with async_client.beta.with_streaming_response.search_labels(
            query="profit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(BetaSearchLabelsResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True
