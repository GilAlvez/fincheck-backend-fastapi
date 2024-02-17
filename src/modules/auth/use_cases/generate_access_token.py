import jwt
from datetime import datetime, timedelta
from src.modules.auth.entities.user import User


class GenerateAccessToken:
    def __init__(
        self,
        secret_key: str,
        algorithm: str = "HS256",
        expires_in: timedelta = timedelta(days=2),
    ):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expires_in = expires_in

    def execute(self, user: User) -> str:
        payload = {
            "sub": user.id,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + self.expires_in,
        }

        return jwt.encode(
            key=self.secret_key,
            algorithm=self.algorithm,
            payload=payload,
        )
