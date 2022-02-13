import uvicorn
from fastapi import FastAPI

from app.functions import parse_json

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/anime-girls/{pr_lang}")
def get_anime_girl(pr_lang: str):
    result = parse_json(pr_lang)
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)
