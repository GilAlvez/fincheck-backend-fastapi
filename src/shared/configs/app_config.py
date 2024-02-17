from datetime import timedelta
from pydantic import BaseModel


class AppConfig(BaseModel):
    jwt_expires_in: timedelta = timedelta(days=2)
