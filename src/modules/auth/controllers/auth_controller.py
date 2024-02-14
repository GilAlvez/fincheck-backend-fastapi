from modules.auth.dtos.sign_in_response_dto import SignInResponseDTO
from modules.auth.dtos.sing_in_params_dto import SignInParamsDTO
from modules.auth.use_cases.sign_in_with_email import SignInWithEmail


class AuthController:
    def __init__(self, sing_in_with_email: SignInWithEmail):
        self.sing_in_with_email = sing_in_with_email

    def sign_in(self, params: SignInParamsDTO) -> SignInResponseDTO:
        token = self.sing_in_with_email.execute(params.email, params.password)
        return SignInResponseDTO(access_token=token)
