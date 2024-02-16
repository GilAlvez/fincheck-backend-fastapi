import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Numeric, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates, relationship
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    active = Column(Boolean, default=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    bank_accounts = relationship(
        "BankAccountModel",
        back_populates="user",
        cascade="all, delete, delete-orphan",
    )

    @validates("email")
    def validate_email(self, key, email):
        assert "@" in email, "Email invalid"
        return email

    @validates("name")
    def validate_name(self, key, name):
        assert len(name) > 0, "Name must not be empty"
        return name


class BankAccountModel(Base):
    __tablename__ = "bank_accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    initial_balance = Column(Numeric(12, 2))
    type = Column(Enum("checking", "cash", "investment"), name="account_type")
    color = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    user = relationship(
        "UserModel",
        back_populates="bank_accounts",
    )
