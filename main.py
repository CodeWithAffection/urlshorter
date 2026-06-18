from fastapi import FastAPI
from routers import create_short
from database import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(create_short.router)

