from pydantic import BaseModel


class SignInResponseDTO(BaseModel):
    access_token: str
