import jwt
from src.modules.auth.entities.jwt_payload import JwtPayload
from src.shared.exceptions.invalid_jwt_exception import InvalidJwtException


class ValidateAccessToken:
    def __init__(self, secret_key: str, algorithm: str) -> None:
        self.secret_key = secret_key
        self.algorithm = algorithm

    def execute(self, token: str) -> JwtPayload:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return JwtPayload(**payload)
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, jwt.PyJWTError):
            raise InvalidJwtException()
