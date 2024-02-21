from fastapi import APIRouter, Depends, HTTPException
from src.shared.exceptions.invalid_password_exception import InvalidPasswordException
from src.shared.exceptions.user_not_found_exception import UserNotFoundException
from src.shared.exceptions.invalid_user_mutation_exception import (
    InvalidUserMutationException,
)
from src.shared.exceptions.conflict_exception import ConflictException
from src.modules.auth.dtos.sing_in_params_dto import SignInParamsDTO
from src.container import container
from src.modules.auth.dtos.sign_up_params_dto import SignUpParamsDTO
from src.modules.auth.entities.jwt_payload import JwtPayload
from src.shared.guards.jwt_guard import jwt_guard

router = APIRouter(prefix="/api")


@router.post("/v1/auth/sign-in")
async def sign_in(params: SignInParamsDTO):
    try:
        return container.auth_controller().sign_in(params)
    except (UserNotFoundException, InvalidPasswordException):
        raise HTTPException(status_code=400, detail="Invalid Credentials")


@router.post("/v1/auth/sign-up")
async def sign_up(params: SignUpParamsDTO):
    try:
        return container.auth_controller().sign_up(params)
    except (ConflictException, InvalidUserMutationException):
        raise HTTPException(status_code=400, detail="Invalid Credentials")


@router.get("/v1/protected/example")
async def protected_example(jwt_payload: JwtPayload = Depends(jwt_guard)): ...
