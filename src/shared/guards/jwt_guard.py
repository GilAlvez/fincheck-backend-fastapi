from fastapi import Security, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.container import container
from src.shared.exceptions.invalid_jwt_exception import InvalidJwtException
from src.modules.auth.entities.jwt_payload import JwtPayload


bearer = HTTPBearer()


def jwt_guard(
    authorization: HTTPAuthorizationCredentials = Security(bearer),
) -> JwtPayload:
    try:
        token = authorization.credentials
        payload = container.validate_access_token().execute(token)
        return payload
    except InvalidJwtException:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
