class InvalidPasswordException(Exception):

    def __init__(self, message: str | None = None):
        self.message = message
