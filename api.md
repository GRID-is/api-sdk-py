# Workbooks

Types:

```python
from spreadsheet_api.types import WorkbookQueryResponse, WorkbookRenderChartResponse
```

Methods:

- <code title="post /v1/workbooks/{id}/query">client.workbooks.<a href="./src/spreadsheet_api/resources/workbooks.py">query</a>(id, \*\*<a href="src/spreadsheet_api/types/workbook_query_params.py">params</a>) -> <a href="./src/spreadsheet_api/types/workbook_query_response.py">WorkbookQueryResponse</a></code>
- <code title="post /v1/workbooks/{id}/chart">client.workbooks.<a href="./src/spreadsheet_api/resources/workbooks.py">render_chart</a>(id, \*\*<a href="src/spreadsheet_api/types/workbook_render_chart_params.py">params</a>) -> <a href="./src/spreadsheet_api/types/workbook_render_chart_response.py">object</a></code>
