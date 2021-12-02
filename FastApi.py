
import io
from typing import Dict, Optional
from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from fastapi.responses import ORJSONResponse, UJSONResponse, HTMLResponse, StreamingResponse

app = FastAPI()

class RoleName(str, Enum):
    admin = 'Admin'
    writer = 'Writer'
    reader = 'Reader'

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class Operations(BaseModel):
    Number1: float
    Number2: float


@app.get('/')
def root():
    return {'message' : 'Hello world, from galileo master, section V'}
