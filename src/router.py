from fastapi import APIRouter
from pydantic import BaseModel


class IndexResponseDTO(BaseModel):
    message: str


router = APIRouter(prefix="/api")


@router.get("/v1/", response_model=IndexResponseDTO)
async def index():
    return {"message": "hello world"}


@router.websocket("/ws")
async def open_connection():
    pass
