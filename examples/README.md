# Examples for the GRID API Python SDK

This folder contains examples on how to use the GRID API Python SDK. We use [uv](https://docs.astral.sh/uv) to manage the code, so make sure to [install uv before you start](https://docs.astral.sh/uv/getting-started/installation/).

Before you run any of the examples, make sure your [API key](https://app.grid.is/account/api-key) is set in the environment variable `GRID_API_TOKEN`.

## Loan calculator

A simple HTTP API to calculate the monthly payment for a loan.

You will need to download the [simple loan calculator and amortization table](https://create.microsoft.com/en-us/template/simple-loan-calculator-and-amortization-table-923c86b5-63f8-42d1-99cb-c6ae4f4b679e) from Microsoft,
upload it to your GRID account and replace `REPLACE_WITH_YOUR_SPREADSHEET_ID` with its workbook id. See our [quick start guide](https://docs.grid.is/api-reference/getting-started) for more details.

To start the loan calculator server, run the following in this `examples` directory:

```term
uv run loan_calculator.py
```

This starts a server on <http://localhost:8000/>.


## Goal seek

A simple HTTP API to calculate interest rates and years to save up a target amount. Showcases how to use the `goal_seek` method.

You will need to upload the `goal_seek_example.xlsx`, found in this folder, to your GRID account and replace `REPLACE_WITH_YOUR_SPREADSHEET_ID` with its workbook id. 
See our [quick start guide](https://docs.grid.is/api-reference/getting-started) for more details.

To start the goal seek server, run the following in this `examples` directory:

```term
uv run goal_seek.py
```

This starts a server on <http://localhost:8000/>.
