from modules.users.repositories.users_repository import UsersRepository
from modules.auth.adapters.string_hasher_adapter import StringHasherAdapter
from modules.auth.use_cases.generate_access_token import GenerateAccessToken


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

    def execute(self, email: str, password: str) -> str:
        user = self.users_repository.find_by_email(email)

        if not user:
            return "InvalidCred"

        is_valid_password = self.string_hasher_adapter.compare(password, user.password)

        if not is_valid_password:
            return "InvalidCred"

        token: str = self.generate_access_token.execute(user)

        return token
