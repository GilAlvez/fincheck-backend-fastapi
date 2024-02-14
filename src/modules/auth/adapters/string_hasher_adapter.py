import base64
import bcrypt


class StringHasherAdapter:
    @staticmethod
    def hash(string: str, rounds: int = 12) -> str:
        value = string.encode()
        salt = bcrypt.gensalt(rounds)
        hashed_string = bcrypt.hashpw(value, salt)

        return base64.b64encode(hashed_string).decode()

    @staticmethod
    def compare(string: str, hashed_string: str) -> bool:
        value = string.encode()
        hashed_value = base64.b64decode(hashed_string.encode())

        return bcrypt.checkpw(value, hashed_value)
