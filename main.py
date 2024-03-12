from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum
import get_minimum_odds as gmo

app = FastAPI()
handler = Mangum(app)
EVENT = "The Players Championship"


@app.get("/")
async def root():
    return {"message": "Welcome to the internal API for generating best Golf Odds"}


@app.get("/get-pga-best-odds")
async def best_pga_odds():
    return gmo.get_minimum_odds(EVENT)
