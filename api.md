# Workbooks

Types:

```python
from grid_api.types import (
    WorkbookListResponse,
    WorkbookCalcResponse,
    WorkbookQueryResponse,
    WorkbookUploadResponse,
    WorkbookValuesResponse,
)
```

Methods:

- <code title="get /v1/workbooks">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">list</a>(\*\*<a href="src/grid_api/types/workbook_list_params.py">params</a>) -> <a href="./src/grid_api/types/workbook_list_response.py">SyncCursorPagination[WorkbookListResponse]</a></code>
- <code title="post /v1/workbooks/{id}/calc">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">calc</a>(id, \*\*<a href="src/grid_api/types/workbook_calc_params.py">params</a>) -> <a href="./src/grid_api/types/workbook_calc_response.py">WorkbookCalcResponse</a></code>
- <code title="post /v1/workbooks/{id}/export">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">export</a>(id, \*\*<a href="src/grid_api/types/workbook_export_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/workbooks/{id}/query">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">query</a>(id, \*\*<a href="src/grid_api/types/workbook_query_params.py">params</a>) -> <a href="./src/grid_api/types/workbook_query_response.py">WorkbookQueryResponse</a></code>
- <code title="post /v1/workbooks/{id}/chart">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">render_chart</a>(id, \*\*<a href="src/grid_api/types/workbook_render_chart_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/workbooks">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">upload</a>(\*\*<a href="src/grid_api/types/workbook_upload_params.py">params</a>) -> <a href="./src/grid_api/types/workbook_upload_response.py">WorkbookUploadResponse</a></code>
- <code title="post /v1/workbooks/{id}/values">client.workbooks.<a href="./src/grid_api/resources/workbooks.py">values</a>(id, \*\*<a href="src/grid_api/types/workbook_values_params.py">params</a>) -> <a href="./src/grid_api/types/workbook_values_response.py">WorkbookValuesResponse</a></code>

# Beta

Types:

```python
from grid_api.types import (
    BetaGetWorkbookLabelsResponse,
    BetaGetWorkbookParametersResponse,
    BetaSearchLabelsResponse,
)
```

Methods:

- <code title="get /v1/workbooks/{id}/labels">client.beta.<a href="./src/grid_api/resources/beta.py">get_workbook_labels</a>(id) -> <a href="./src/grid_api/types/beta_get_workbook_labels_response.py">BetaGetWorkbookLabelsResponse</a></code>
- <code title="get /v1/workbooks/{id}/parameters">client.beta.<a href="./src/grid_api/resources/beta.py">get_workbook_parameters</a>(id) -> <a href="./src/grid_api/types/beta_get_workbook_parameters_response.py">BetaGetWorkbookParametersResponse</a></code>
- <code title="post /v1/workbooks/search/labels">client.beta.<a href="./src/grid_api/resources/beta.py">search_labels</a>(\*\*<a href="src/grid_api/types/beta_search_labels_params.py">params</a>) -> <a href="./src/grid_api/types/beta_search_labels_response.py">BetaSearchLabelsResponse</a></code>
