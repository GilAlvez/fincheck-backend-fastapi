from fastapi import APIRouter


router = APIRouter(prefix="/api")


@router.get("/v1/auth/sign-in")
async def sign_in(): ...
