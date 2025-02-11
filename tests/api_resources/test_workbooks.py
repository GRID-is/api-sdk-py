# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from grid_api import GRID, AsyncGRID
from tests.utils import assert_matches_type
from grid_api.types import WorkbookQueryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkbooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_query(self, client: GRID) -> None:
        workbook = client.workbooks.query(
            id="id",
            read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
        )
        assert_matches_type(WorkbookQueryResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_query_with_all_params(self, client: GRID) -> None:
        workbook = client.workbooks.query(
            id="id",
            read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
            apply=[
                {
                    "target": "A2",
                    "value": 1234,
                }
            ],
            goal_seek={
                "control_cell": "controlCell",
                "target_cell": "targetCell",
                "target_value": 0,
            },
            options={
                "axis": "rows",
                "originals": "off",
                "refs": "off",
                "structure": "single",
                "values": "full",
            },
        )
        assert_matches_type(WorkbookQueryResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_query(self, client: GRID) -> None:
        response = client.workbooks.with_raw_response.query(
            id="id",
            read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workbook = response.parse()
        assert_matches_type(WorkbookQueryResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_query(self, client: GRID) -> None:
        with client.workbooks.with_streaming_response.query(
            id="id",
            read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workbook = response.parse()
            assert_matches_type(WorkbookQueryResponse, workbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_query(self, client: GRID) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workbooks.with_raw_response.query(
                id="",
                read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_render_chart(self, client: GRID) -> None:
        workbook = client.workbooks.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        )
        assert_matches_type(object, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_render_chart_with_all_params(self, client: GRID) -> None:
        workbook = client.workbooks.render_chart(
            id="id",
            chart={
                "data": "=C2:C142",
                "format": "png",
                "labels": "=B2:B142",
                "title": "=A1",
                "type": "line",
            },
            apply=[
                {
                    "target": "A2",
                    "value": 1234,
                }
            ],
        )
        assert_matches_type(object, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_render_chart(self, client: GRID) -> None:
        response = client.workbooks.with_raw_response.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workbook = response.parse()
        assert_matches_type(object, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_render_chart(self, client: GRID) -> None:
        with client.workbooks.with_streaming_response.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workbook = response.parse()
            assert_matches_type(object, workbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_render_chart(self, client: GRID) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workbooks.with_raw_response.render_chart(
                id="",
                chart={"data": "=C2:C142"},
            )


class TestAsyncWorkbooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_query(self, async_client: AsyncGRID) -> None:
        workbook = await async_client.workbooks.query(
            id="id",
            read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
        )
        assert_matches_type(WorkbookQueryResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncGRID) -> None:
        workbook = await async_client.workbooks.query(
            id="id",
            read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
            apply=[
                {
                    "target": "A2",
                    "value": 1234,
                }
            ],
            goal_seek={
                "control_cell": "controlCell",
                "target_cell": "targetCell",
                "target_value": 0,
            },
            options={
                "axis": "rows",
                "originals": "off",
                "refs": "off",
                "structure": "single",
                "values": "full",
            },
        )
        assert_matches_type(WorkbookQueryResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncGRID) -> None:
        response = await async_client.workbooks.with_raw_response.query(
            id="id",
            read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workbook = await response.parse()
        assert_matches_type(WorkbookQueryResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncGRID) -> None:
        async with async_client.workbooks.with_streaming_response.query(
            id="id",
            read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workbook = await response.parse()
            assert_matches_type(WorkbookQueryResponse, workbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_query(self, async_client: AsyncGRID) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workbooks.with_raw_response.query(
                id="",
                read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_render_chart(self, async_client: AsyncGRID) -> None:
        workbook = await async_client.workbooks.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        )
        assert_matches_type(object, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_render_chart_with_all_params(self, async_client: AsyncGRID) -> None:
        workbook = await async_client.workbooks.render_chart(
            id="id",
            chart={
                "data": "=C2:C142",
                "format": "png",
                "labels": "=B2:B142",
                "title": "=A1",
                "type": "line",
            },
            apply=[
                {
                    "target": "A2",
                    "value": 1234,
                }
            ],
        )
        assert_matches_type(object, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_render_chart(self, async_client: AsyncGRID) -> None:
        response = await async_client.workbooks.with_raw_response.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workbook = await response.parse()
        assert_matches_type(object, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_render_chart(self, async_client: AsyncGRID) -> None:
        async with async_client.workbooks.with_streaming_response.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workbook = await response.parse()
            assert_matches_type(object, workbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_render_chart(self, async_client: AsyncGRID) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workbooks.with_raw_response.render_chart(
                id="",
                chart={"data": "=C2:C142"},
            )
