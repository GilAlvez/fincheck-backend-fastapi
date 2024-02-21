from src.modules.auth.dtos.sign_up_params_dto import SignUpParamsDTO
from src.modules.auth.use_cases.sign_up_with_email import SignUpWithEmail
from src.modules.auth.dtos.sign_in_response_dto import SignInResponseDTO
from src.modules.auth.dtos.sing_in_params_dto import SignInParamsDTO
from src.modules.auth.use_cases.sign_in_with_email import SignInWithEmail


class AuthController:
    def __init__(
        self,
        sign_in_with_email: SignInWithEmail,
        sign_up_with_email: SignUpWithEmail,
    ):
        self.sign_in_with_email = sign_in_with_email
        self.sign_up_with_email = sign_up_with_email

    def sign_in(self, params: SignInParamsDTO) -> SignInResponseDTO:
        # try
        token = self.sign_in_with_email.execute(params)
        # catch
        return SignInResponseDTO(access_token=token)

    def sign_up(self, params: SignUpParamsDTO) -> SignInResponseDTO:
        token = self.sign_up_with_email.execute(params)
        return SignInResponseDTO(access_token=token)
