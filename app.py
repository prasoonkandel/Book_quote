from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.types import Json

app = FastAPI()


class Quote(BaseModel):
    query: str
    count: int


@app.get("/")
def read_root():
    return {"message": "Welcome to Book Quote"}
