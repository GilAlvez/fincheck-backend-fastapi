from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    active: bool
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime
