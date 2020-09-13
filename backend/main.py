import datetime
from fastapi import FastAPI

app = FastAPI()

app.get("/api/time")
async def sample():
    return {
        "time": datetime.datetime.now()
    }
