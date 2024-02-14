from typing_extensions import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints


class SignInParamsDTO(BaseModel):
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8)]
