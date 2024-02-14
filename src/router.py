from fastapi import APIRouter

from modules.auth.controllers.auth_controller import AuthController
from modules.auth.dtos.sign_in_response_dto import SignInResponseDTO


router = APIRouter(prefix="/api")


@router.get("/v1/auth/sign-in", response_model=SignInResponseDTO)
async def sign_in():
    response = AuthController.sign_in()
    return response
