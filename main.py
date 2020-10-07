from typing import Optional
import importlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://editor.swagger.io"]
)


@app.get("/request/{hash}")
def route_to_ko(hash: str) -> str:
  try:
    runner = eps[hash]
    result = runner(hash)
  except:
    result = 'What?'
  return result


@app.get("/")
def read_root(name: Optional[str] = 'Bob'):
  return {"Hello": name}


bar = importlib.import_module("shelf.ko42.bar")
eps = dict()

eps['read_root'] = read_root
eps['bar'] = bar.run

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
