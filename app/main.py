from typing import Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import motor.motor_asyncio
import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=str(Path(BASE_DIR, 'static'))), name="static")

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get('MONGO_CONSTRING'))
# db = client.get_database(os.environ.get('DB_NAME'))

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": 123}
    )

@app.get("/test")
def test():
    return {"message": "Hello World- Test"}