from src.modules.auth.entities.user import User


class GenerateAccessToken:
    def execute(self, user: User) -> str:
        return "token"
