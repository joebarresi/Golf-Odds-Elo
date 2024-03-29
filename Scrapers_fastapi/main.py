from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from pydantic import BaseModel
from mangum import Mangum
import get_minimum_odds as gmo
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient

app = FastAPI()
handler = Mangum(app)
EVENT = "The Players Championship"

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the internal API for generating best Golf Odds"}


@app.get("/get-pga-best-odds")
async def best_pga_odds():
    data = gmo.get_minimum_odds(EVENT)
    print(type(data))
    obj = {"info": data}
    return obj

client = TestClient(app)

def test_odds():
    print(client.get("/get-pga-best-odds").json())
