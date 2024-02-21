from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, validator

from src.shared.utils.validators import email_validation, full_name_validation


class SignUpParamsDTO(BaseModel):
    name: Annotated[str, StringConstraints(min_length=2)]
    email: str
    password: Annotated[str, StringConstraints(min_length=8)]

    @validator("name")
    def validate_name(cls, value):
        return full_name_validation(value)

    @validator("email")
    def validate_email(cls, value):
        return email_validation(value)
