from src.modules.users.data_sources.users_data_source import UsersDataSource
from src.modules.auth.entities.user import User


class UsersRepository:
    def __init__(self, users_data_source: UsersDataSource) -> None:
        self.users_data_source = users_data_source

    def find_unique(
        self,
        *,
        by_id: str | None = None,
        by_email: str | None = None,
    ) -> User | None:

        if by_id:
            unique_user = self.users_data_source.find_by_id(by_id)
        elif by_email:
            unique_user = self.users_data_source.find_by_email(by_email)
        else:
            unique_user = None

        if not unique_user:
            return None
        else:
            return User(**unique_user)
