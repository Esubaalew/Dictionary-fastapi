from fastapi import FastAPI

from dictionary.britannica import get_entries, get_total_entries, get_word_of_the_day, get_parts, get_definitions

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}