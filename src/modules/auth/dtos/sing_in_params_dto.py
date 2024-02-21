from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, validator

from src.shared.utils.validators import email_validation


class SignInParamsDTO(BaseModel):
    email: str
    password: Annotated[str, StringConstraints(min_length=8)]

    @validator("email")
    def validate_email(cls, value):
        return email_validation(value)
