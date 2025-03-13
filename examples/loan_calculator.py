from fastapi import FastAPI
from grid_api import Grid, APIConnectionError, APIStatusError, RateLimitError

app = FastAPI()

@app.get("/")
async def get_loan_calculations(loan_amount: float = 100000.0, years: int = 25, interest_rate: float = 2.5):
    client = Grid()

    first_row_to_read = 14
    end_row_to_read = years * 12 + first_row_to_read - 1

    try:
        response = client.workbooks.query(
            id="82012e4a-a2bf-4d4a-97e6-93ebf31704d5",
            apply=[
                {"target": "'Loan calculator'!D3", "value": loan_amount},
                {"target": "'Loan calculator'!D4", "value": interest_rate / 100},
                {"target": "'Loan calculator'!D5", "value": years}
            ],
            read=["'Loan calculator'!D8", f"'Loan calculator'!B{first_row_to_read}:'Loan calculator'!H{end_row_to_read}"]
        )
    except APIConnectionError as e:
        return {"error": "The server could not be reached."}
    except RateLimitError as e:
        return {"error", "A 429 status code was received; we should back off a bit."}
    except APIStatusError as e:
        return {"error": e.message}


    monthly_payments = response.read[0].data[0][0].v
    rows = [[cell.v for cell in row] for row in response.read[1].data]

    return {"monthly_payments": monthly_payments, "payment_schedule": rows}