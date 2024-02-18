from datetime import datetime
from pydantic import BaseModel


class JwtPayload(BaseModel):
    sub: str  # user id
    iat: datetime
    exp: datetime
