import datetime
from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    with open("static/index.html", "rb") as index_file:
        return Response(content=index_file.read(), media_type="text/html")

@app.get("/api/time")
async def sample():
    return {
        "time": datetime.datetime.now()
    }
