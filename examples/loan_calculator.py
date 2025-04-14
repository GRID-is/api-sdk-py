# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "fastapi[standard]",
#     "grid-api",
#     "uvicorn",
# ]
# ///
import uvicorn
from fastapi import FastAPI

from grid_api import AsyncGrid, APIStatusError, RateLimitError, APIConnectionError

app = FastAPI()


@app.get("/")
async def get_loan_calculations(loan_amount: float = 100000.0, years: int = 25, interest_rate: float = 2.5):
    client = AsyncGrid()

    loan_calculator_spreadsheet_id = "REPLACE_WITH_YOUR_SPREADSHEET_ID"
    first_row_to_read = 14
    end_row_to_read = years * 12 + first_row_to_read - 1

    try:
        response = await client.workbooks.query(
            id=loan_calculator_spreadsheet_id,
            apply=[
                {"target": "'Loan calculator'!D3", "value": loan_amount},
                {"target": "'Loan calculator'!D4", "value": interest_rate / 100},
                {"target": "'Loan calculator'!D5", "value": years},
            ],
            read=[
                "'Loan calculator'!D8",
                f"'Loan calculator'!B{first_row_to_read}:'Loan calculator'!H{end_row_to_read}",
            ],
        )
    except APIConnectionError:
        return {"error": "The server could not be reached."}
    except RateLimitError:
        return {"error": "A 429 status code was received; we should back off a bit."}
    except APIStatusError as e:
        return {"error": e.message}

    monthly_payments = response.read[0].data[0][0].v
    rows = [[cell.v for cell in row] for row in response.read[1].data]

    return {"monthly_payments": monthly_payments, "payment_schedule": rows}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
