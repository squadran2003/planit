from typing import Union

from fastapi import FastAPI, Request, Query, Depends
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlmodel import SQLModel
from .config.settings import create_db_and_tables, get_session
from .models import Todo, Service
import motor.motor_asyncio
import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=str(Path(BASE_DIR, 'static'))), name="static")

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))



session = get_session()

# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get('MONGO_CONSTRING'))
# db = client.get_database(os.environ.get('DB_NAME'))

class Item(BaseModel):
    name: Annotated[str, Query(max_length=20)]
    description:  Annotated[str, None, Query(max_length=20)]
    price: float
    tax: float | None = None

class ServiceModel(BaseModel):
    code: int
    name: str = None
    description: str = None
    stripe_price_id: str = None
    free: bool = True
    cost: int = 0
    video_path: str = None
    poster_path: str = None
    created_at: str = None


# class TodoItem(BaseModel):
#     title: Annotated[str, Query(max_length=20)]
#     description: str


@app.on_event("startup")
async def on_startup():
    create_db_and_tables()


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": 123}
    )


@app.get("/test")
async def test(value: int, q: int | None = None):
    squared = value ** 2
    result = {"original": value, "squared": squared, "message": f"Square of {value} is {squared}"}
    if q:
        result.update({"q": q})
    return result

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/create/service/")
async def create_todo(service_item: ServiceModel, session= Depends(get_session)):
    service = Service(**service_item.dict())
    session.add(service)
    session.commit()
    session.close()
    return service_item

@app.get("/service/")
async def get_todos(session=Depends(get_session)):
    service = session.query(Service).first()
    return service
