from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from getter import ingredient_getter


app = FastAPI()


class Item(BaseModel):
    word: str


@app.post("/populate/{word}")
async def feature(item: Item):
    item = jsonable_encoder(item)
    word_string = item['word']
    results_json = ingredient_getter(word_string)
    return results_json
