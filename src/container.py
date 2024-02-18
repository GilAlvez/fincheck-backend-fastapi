from dependency_injector import containers, providers
from src.shared.configs.settings import Settings
from src.modules.auth.use_cases.validate_access_token import ValidateAccessToken
from src.modules.auth.adapters.string_hasher_adapter import StringHasherAdapter
from src.modules.users.data_sources.users_data_source import UsersDataSource
from src.modules.users.repositories.users_repository import UsersRepository
from src.modules.auth.use_cases.generate_access_token import GenerateAccessToken
from src.modules.auth.use_cases.sign_in_with_email import SignInWithEmail


class Container(containers.DeclarativeContainer):
    settings = providers.Singleton(Settings)

    # Adapters
    string_hasher_adapter = providers.Singleton(StringHasherAdapter)

    # Data Sources
    users_data_source = providers.Singleton(UsersDataSource)

    # Repositories
    users_repository = providers.Singleton(
        UsersRepository,
        users_data_source=users_data_source,
    )

    # Use Cases
    generate_access_token = providers.Singleton(
        GenerateAccessToken,
        secret_key=settings().JWT_SECRET_KEY,
        algorithm=settings().app_config.jwt_algorithm,
        expires_in=settings().app_config.jwt_expires_in,
    )
    validate_access_token = providers.Singleton(
        ValidateAccessToken,
        secret_key=settings().JWT_SECRET_KEY,
        algorithm=settings().app_config.jwt_algorithm,
    )
    sing_in_with_email = providers.Singleton(
        SignInWithEmail,
        users_repository=users_repository,
        generate_access_token=generate_access_token,
        string_hasher_adapter=string_hasher_adapter,
    )


container = Container()
