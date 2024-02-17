from fastapi import APIRouter

from src.container import Container

container = Container()
router = APIRouter(prefix="/api")


@router.get("/v1/auth/sign-in")
async def sign_in(): ...
