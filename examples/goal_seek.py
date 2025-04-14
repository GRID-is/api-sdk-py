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


@app.get("/seek_interests")
async def seek_interests(target_amount: float):
    client = AsyncGrid()

    try:
        response = await client.workbooks.query(
            id="REPLACE_WITH_YOUR_SPREADSHEET_ID",
            goal_seek={
                "targetCell": "Sheet1!C7",
                "targetValue": target_amount,
                "controlCell": "Sheet1!C5",
            },
            read=[]
        )
    except APIConnectionError as e:
        return {"error": "The server could not be reached."}
    except RateLimitError as e:
        return {"error", "A 429 status code was received; we should back off a bit."}
    except APIStatusError as e:
        return {"error": e.message}

    solution = response.goalSeek["solution"]

    return {"interest_rate": solution}


@app.get("/seek_years")
async def seek_years(target_amount: float):
    client = AsyncGrid()

    try:
        response = await client.workbooks.query(
            id="REPLACE_WITH_YOUR_SPREADSHEET_ID",
            goal_seek={
                "targetCell": "Sheet1!C7",
                "targetValue": target_amount,
                "controlCell": "Sheet1!C4",
            },
            read=[]
        )
    except APIConnectionError as e:
        return {"error": "The server could not be reached."}
    except RateLimitError as e:
        return {"error": "A 429 status code was received; we should back off a bit."}
    except APIStatusError as e:
        return {"error": e.message}

    solution = response.goalSeek["solution"]

    return {"years": solution}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)