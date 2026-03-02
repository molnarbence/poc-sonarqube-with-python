from fastapi import FastAPI

from app.utils import add

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    return {"item_id": item_id}


@app.post("/add")
async def add_numbers(a: int, b: int) -> dict:
    return {"result": add(a, b)}
