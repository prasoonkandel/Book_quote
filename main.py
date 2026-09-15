from tkinter.constants import PAGES

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "welcome to home page <3"}


@app.get("/text/{text}")
async def getTxt(text: str):
    return {"text": text}
