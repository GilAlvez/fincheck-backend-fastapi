class StringHasherAdapter:
    def hash(value: str, salt: int) -> str:
        return "HashedPassword"

    def compare(value: str, hash: str) -> bool:
        return True
