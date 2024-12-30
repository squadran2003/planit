from sqlmodel import SQLModel, Field
import datetime


class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str = None


class Service(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    code: int
    name: str = None
    description: str = None
    stripe_price_id: str = None
    free: bool = True
    cost: int = 0
    video_path: str = None
    poster_path: str = None
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
    )