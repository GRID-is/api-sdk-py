# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from grid_api import Grid, AsyncGrid
from tests.utils import assert_matches_type
from grid_api.types import (
    WorkbookListResponse,
    WorkbookQueryResponse,
    WorkbookUploadResponse,
)
from grid_api._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from grid_api.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkbooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Grid) -> None:
        workbook = client.workbooks.list()
        assert_matches_type(SyncCursorPagination[WorkbookListResponse], workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Grid) -> None:
        workbook = client.workbooks.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(SyncCursorPagination[WorkbookListResponse], workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Grid) -> None:
        response = client.workbooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workbook = response.parse()
        assert_matches_type(SyncCursorPagination[WorkbookListResponse], workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Grid) -> None:
        with client.workbooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workbook = response.parse()
            assert_matches_type(SyncCursorPagination[WorkbookListResponse], workbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export(self, client: Grid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        workbook = client.workbooks.export(
            id="id",
        )
        assert workbook.is_closed
        assert workbook.json() == {"foo": "bar"}
        assert cast(Any, workbook.is_closed) is True
        assert isinstance(workbook, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_with_all_params(self, client: Grid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        workbook = client.workbooks.export(
            id="id",
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
        )
        assert workbook.is_closed
        assert workbook.json() == {"foo": "bar"}
        assert cast(Any, workbook.is_closed) is True
        assert isinstance(workbook, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export(self, client: Grid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        workbook = client.workbooks.with_raw_response.export(
            id="id",
        )

        assert workbook.is_closed is True
        assert workbook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert workbook.json() == {"foo": "bar"}
        assert isinstance(workbook, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export(self, client: Grid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.workbooks.with_streaming_response.export(
            id="id",
        ) as workbook:
            assert not workbook.is_closed
            assert workbook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert workbook.json() == {"foo": "bar"}
            assert cast(Any, workbook.is_closed) is True
            assert isinstance(workbook, StreamedBinaryAPIResponse)

        assert cast(Any, workbook.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_export(self, client: Grid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workbooks.with_raw_response.export(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_query(self, client: Grid) -> None:
        workbook = client.workbooks.query(
            id="id",
            read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
        )
        assert_matches_type(WorkbookQueryResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_query_with_all_params(self, client: Grid) -> None:
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
    def test_raw_response_query(self, client: Grid) -> None:
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
    def test_streaming_response_query(self, client: Grid) -> None:
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
    def test_path_params_query(self, client: Grid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workbooks.with_raw_response.query(
                id="",
                read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
            )

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_render_chart(self, client: Grid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/chart").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        workbook = client.workbooks.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        )
        assert workbook.is_closed
        assert workbook.json() == {"foo": "bar"}
        assert cast(Any, workbook.is_closed) is True
        assert isinstance(workbook, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_render_chart_with_all_params(self, client: Grid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/chart").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        workbook = client.workbooks.render_chart(
            id="id",
            chart={
                "data": "=C2:C142",
                "format": "png",
                "labels": "=B2:B142",
                "title": "=A1",
                "type": "line",
                "values": "none",
            },
            apply=[
                {
                    "target": "A2",
                    "value": 1234,
                }
            ],
        )
        assert workbook.is_closed
        assert workbook.json() == {"foo": "bar"}
        assert cast(Any, workbook.is_closed) is True
        assert isinstance(workbook, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_render_chart(self, client: Grid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/chart").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        workbook = client.workbooks.with_raw_response.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        )

        assert workbook.is_closed is True
        assert workbook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert workbook.json() == {"foo": "bar"}
        assert isinstance(workbook, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_render_chart(self, client: Grid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/chart").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.workbooks.with_streaming_response.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        ) as workbook:
            assert not workbook.is_closed
            assert workbook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert workbook.json() == {"foo": "bar"}
            assert cast(Any, workbook.is_closed) is True
            assert isinstance(workbook, StreamedBinaryAPIResponse)

        assert cast(Any, workbook.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_render_chart(self, client: Grid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workbooks.with_raw_response.render_chart(
                id="",
                chart={"data": "=C2:C142"},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_upload(self, client: Grid) -> None:
        workbook = client.workbooks.upload(
            file=b"raw file contents",
        )
        assert_matches_type(WorkbookUploadResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload(self, client: Grid) -> None:
        response = client.workbooks.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workbook = response.parse()
        assert_matches_type(WorkbookUploadResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload(self, client: Grid) -> None:
        with client.workbooks.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workbook = response.parse()
            assert_matches_type(WorkbookUploadResponse, workbook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkbooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGrid) -> None:
        workbook = await async_client.workbooks.list()
        assert_matches_type(AsyncCursorPagination[WorkbookListResponse], workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGrid) -> None:
        workbook = await async_client.workbooks.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AsyncCursorPagination[WorkbookListResponse], workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGrid) -> None:
        response = await async_client.workbooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workbook = await response.parse()
        assert_matches_type(AsyncCursorPagination[WorkbookListResponse], workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGrid) -> None:
        async with async_client.workbooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workbook = await response.parse()
            assert_matches_type(AsyncCursorPagination[WorkbookListResponse], workbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export(self, async_client: AsyncGrid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        workbook = await async_client.workbooks.export(
            id="id",
        )
        assert workbook.is_closed
        assert await workbook.json() == {"foo": "bar"}
        assert cast(Any, workbook.is_closed) is True
        assert isinstance(workbook, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_with_all_params(self, async_client: AsyncGrid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        workbook = await async_client.workbooks.export(
            id="id",
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
        )
        assert workbook.is_closed
        assert await workbook.json() == {"foo": "bar"}
        assert cast(Any, workbook.is_closed) is True
        assert isinstance(workbook, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export(self, async_client: AsyncGrid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        workbook = await async_client.workbooks.with_raw_response.export(
            id="id",
        )

        assert workbook.is_closed is True
        assert workbook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await workbook.json() == {"foo": "bar"}
        assert isinstance(workbook, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export(self, async_client: AsyncGrid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.workbooks.with_streaming_response.export(
            id="id",
        ) as workbook:
            assert not workbook.is_closed
            assert workbook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await workbook.json() == {"foo": "bar"}
            assert cast(Any, workbook.is_closed) is True
            assert isinstance(workbook, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, workbook.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_export(self, async_client: AsyncGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workbooks.with_raw_response.export(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_query(self, async_client: AsyncGrid) -> None:
        workbook = await async_client.workbooks.query(
            id="id",
            read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
        )
        assert_matches_type(WorkbookQueryResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncGrid) -> None:
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
    async def test_raw_response_query(self, async_client: AsyncGrid) -> None:
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
    async def test_streaming_response_query(self, async_client: AsyncGrid) -> None:
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
    async def test_path_params_query(self, async_client: AsyncGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workbooks.with_raw_response.query(
                id="",
                read=["A1", "Sheet2!B3", "=SUM(A1:A4)"],
            )

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_render_chart(self, async_client: AsyncGrid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/chart").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        workbook = await async_client.workbooks.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        )
        assert workbook.is_closed
        assert await workbook.json() == {"foo": "bar"}
        assert cast(Any, workbook.is_closed) is True
        assert isinstance(workbook, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_render_chart_with_all_params(self, async_client: AsyncGrid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/chart").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        workbook = await async_client.workbooks.render_chart(
            id="id",
            chart={
                "data": "=C2:C142",
                "format": "png",
                "labels": "=B2:B142",
                "title": "=A1",
                "type": "line",
                "values": "none",
            },
            apply=[
                {
                    "target": "A2",
                    "value": 1234,
                }
            ],
        )
        assert workbook.is_closed
        assert await workbook.json() == {"foo": "bar"}
        assert cast(Any, workbook.is_closed) is True
        assert isinstance(workbook, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_render_chart(self, async_client: AsyncGrid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/chart").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        workbook = await async_client.workbooks.with_raw_response.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        )

        assert workbook.is_closed is True
        assert workbook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await workbook.json() == {"foo": "bar"}
        assert isinstance(workbook, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_render_chart(self, async_client: AsyncGrid, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/workbooks/id/chart").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.workbooks.with_streaming_response.render_chart(
            id="id",
            chart={"data": "=C2:C142"},
        ) as workbook:
            assert not workbook.is_closed
            assert workbook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await workbook.json() == {"foo": "bar"}
            assert cast(Any, workbook.is_closed) is True
            assert isinstance(workbook, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, workbook.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_render_chart(self, async_client: AsyncGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workbooks.with_raw_response.render_chart(
                id="",
                chart={"data": "=C2:C142"},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload(self, async_client: AsyncGrid) -> None:
        workbook = await async_client.workbooks.upload(
            file=b"raw file contents",
        )
        assert_matches_type(WorkbookUploadResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncGrid) -> None:
        response = await async_client.workbooks.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workbook = await response.parse()
        assert_matches_type(WorkbookUploadResponse, workbook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncGrid) -> None:
        async with async_client.workbooks.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workbook = await response.parse()
            assert_matches_type(WorkbookUploadResponse, workbook, path=["response"])

        assert cast(Any, response.is_closed) is True
