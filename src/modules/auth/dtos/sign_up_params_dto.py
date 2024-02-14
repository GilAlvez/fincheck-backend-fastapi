from typing_extensions import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints


class SignUpParamsDTO(BaseModel):
    name: Annotated[str, StringConstraints(min_length=2)]
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8)]
