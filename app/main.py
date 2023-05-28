from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

item_master = {1 : "Description for item 1",
               2 : "Description for item 2",
               3 : "Description for item 3",
               4 : "Description for item 4",
               5 : "Description for item 5"
                }


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/")
async def root():
    return {"message": "Hello World"}

#creating another endpoint in terms of fastapi
#creating another url in simple terms
@app.get("/items")
async def items():
    return {"items": item_master}


@app.get("/items/{item_id}")
async def get_item(item_id : int, short : bool):
    if(short == True):
        return {"item": item_master[item_id] }
    else:
        return {"item":"This is a long description"}

@app.post("/items")
async def create_item(item : Item):
    return item