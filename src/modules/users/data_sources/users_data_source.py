from sqlalchemy import select
from src.external.database.connection import db
from src.external.database.models import UserModel


class UsersDataSource:
    def find_by_email(self, email: str) -> dict | None:
        result = db.scalars(select(UserModel).where(UserModel.email == email)).first()

        if result is not None:
            return result.__dict__
        return None

    def find_by_id(self, email: str) -> dict | None:
        return {}

    def create_user(self, name: str, email: str, password: str) -> dict | None:
        new_user = UserModel(name=name, email=email, password=password)
        db.add(new_user)
        db.commit()

        if new_user:
            return new_user.__dict__
        return None
