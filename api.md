# Workbooks

Types:

```python
from grid_api.types import WorkbookListResponse, WorkbookQueryResponse, WorkbookUploadResponse
```

Methods:

- <code title="get /v1/workbooks">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">list</a>(\*\*<a href="src/grid_api/types/workbook_list_params.py">params</a>) -> <a href="./src/grid_api/types/workbook_list_response.py">SyncCursorPagination[WorkbookListResponse]</a></code>
- <code title="post /v1/workbooks/{id}/export">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">export</a>(id, \*\*<a href="src/grid_api/types/workbook_export_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/workbooks/{id}/query">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">query</a>(id, \*\*<a href="src/grid_api/types/workbook_query_params.py">params</a>) -> <a href="./src/grid_api/types/workbook_query_response.py">WorkbookQueryResponse</a></code>
- <code title="post /v1/workbooks/{id}/chart">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">render_chart</a>(id, \*\*<a href="src/grid_api/types/workbook_render_chart_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/workbooks">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">upload</a>(\*\*<a href="src/grid_api/types/workbook_upload_params.py">params</a>) -> <a href="./src/grid_api/types/workbook_upload_response.py">WorkbookUploadResponse</a></code>
