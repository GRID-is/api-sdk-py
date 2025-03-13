# Examples for the GRID python api SDK

This folder contains examples on how to use the GRID python api SDK.
We use uv to manage the project, so make sure to install it before you start.

To run the examples make sure your [API key](https://app.grid.is/account/api-key) is set in the environment variable `GRID_API_TOKEN`.

## Loan calculator

A simple API to calculate the monthly payment for a loan.

You will need to download the [Simple loan calculator and amortization table](https://create.microsoft.com/en-us/template/simple-loan-calculator-and-amortization-table-923c86b5-63f8-42d1-99cb-c6ae4f4b679e) from Microsoft,
upload it to your GRID account and replace the `REPLACE_WITH_YOUR_SPREADSHEET_ID` with its id.

To run execute the following in the `examples` directory:

```uv run loan_calculator.py```
