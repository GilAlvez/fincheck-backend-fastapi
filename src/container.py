from dependency_injector import containers, providers

from src.shared.configs.settings import Settings
from src.modules.auth.use_cases.generate_access_token import GenerateAccessToken


class Container(containers.DeclarativeContainer):
    _settings_singleton = providers.Singleton(Settings)
    settings = _settings_singleton()

    # Use Cases
    generate_access_token = providers.Singleton(
        GenerateAccessToken,
        secret_key=settings.JWT_SECRET_KEY,
        algorithm=settings.app_config.jwt_algorithm,
        expires_in=settings.app_config.jwt_expires_in,
    )
