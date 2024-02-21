from src.modules.auth.dtos.sing_in_params_dto import SignInParamsDTO
from src.shared.exceptions.invalid_password_exception import InvalidPasswordException
from src.shared.exceptions.user_not_found_exception import UserNotFoundException
from src.modules.users.repositories.users_repository import UsersRepository
from src.modules.auth.adapters.string_hasher_adapter import StringHasherAdapter
from src.modules.auth.use_cases.generate_access_token import GenerateAccessToken


class SignInWithEmail:
    def __init__(
        self,
        users_repository: UsersRepository,
        generate_access_token: GenerateAccessToken,
        string_hasher_adapter: StringHasherAdapter,
    ):
        self.users_repository = users_repository
        self.generate_access_token = generate_access_token
        self.string_hasher_adapter = string_hasher_adapter

    def execute(self, params: SignInParamsDTO) -> str:
        user = self.users_repository.find_unique(by_email=params.email)
        if not user:
            raise UserNotFoundException("Email is not registered")

        is_valid_password = self.string_hasher_adapter.compare(
            params.password, user.password
        )

        if not is_valid_password:
            raise InvalidPasswordException()

        token = self.generate_access_token.execute(user)

        return token
