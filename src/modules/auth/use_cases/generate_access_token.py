from modules.auth.use_cases.sign_in_with_email import User


class GenerateAccessToken:
    def execute(user: User) -> str:
        return "token"
