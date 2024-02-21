from src.modules.auth.dtos.sign_up_params_dto import SignUpParamsDTO
from src.shared.exceptions.invalid_user_mutation_exception import (
    InvalidUserMutationException,
)
from src.modules.auth.adapters.string_hasher_adapter import StringHasherAdapter
from src.modules.auth.use_cases.generate_access_token import GenerateAccessToken
from src.modules.users.repositories.users_repository import UsersRepository
from src.shared.exceptions.conflict_exception import ConflictException


class SignUpWithEmail:
    def __init__(
        self,
        users_repository: UsersRepository,
        generate_access_token: GenerateAccessToken,
        string_hasher_adapter: StringHasherAdapter,
    ):
        self.users_repository = users_repository
        self.generate_access_token = generate_access_token
        self.string_hasher_adapter = string_hasher_adapter

    def execute(
        self,
        params: SignUpParamsDTO,
    ) -> str:
        user = self.users_repository.find_unique(by_email=params.email)
        if user:
            raise ConflictException("Email already exists")

        hashed_password = self.string_hasher_adapter.hash(params.password)
        created_user = self.users_repository.create(
            params.name, params.email, hashed_password
        )
        if not created_user:
            raise InvalidUserMutationException(
                "User not created, check sign up credentials"
            )

        token = self.generate_access_token.execute(created_user)

        return token
