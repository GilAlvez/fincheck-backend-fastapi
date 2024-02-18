from fastapi import APIRouter, Depends

from src.modules.auth.entities.jwt_payload import JwtPayload
from src.shared.guards.jwt_guard import jwt_guard

router = APIRouter(prefix="/api")


@router.get("/v1/auth/sign-in")
async def sign_in(): ...


@router.get("/v1/protected/example")
async def protected_example(jwt_payload: JwtPayload = Depends(jwt_guard)): ...
