from modules.auth.models.user import User


class UsersRepository:
    def find_by_email(email: str) -> User:
        return User(
            id=1,
            name="User",
            email="email@email.com",
            password="51sf!$414¨7&8-561",
        )
