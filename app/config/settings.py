from sqlmodel import SQLModel, create_engine, Session
import os

# Database URL
DATABASE_URL = os.environ.get("DB_STRING", None)
if DATABASE_URL is None:
    raise ValueError("DB_STRING environment variable not set")
print(f"DATABASE_URL: {DATABASE_URL}")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=False to reduce logging


# Dependency for getting a session
def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
