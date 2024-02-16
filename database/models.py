import enum
import re
import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Numeric, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates, relationship
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class TransactionType(enum.Enum):
    income = "income"
    expende = "expense"


class BankAccountType(enum.Enum):
    checking = "checking"
    cash = "cash"
    investment = "investment"


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    active = Column(Boolean, default=True)
    name = Column(String(100))
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    bank_accounts = relationship(
        "BankAccountModel",
        back_populates="user",
        cascade="all, delete, delete-orphan",
    )
    categories = relationship(
        "CategoryModel",
        back_populates="user",
        cascade="all, delete, delete-orphan",
    )
    transactions = relationship(
        "TransactionModel",
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
    name = Column(String(100))
    initial_balance = Column(Numeric(12, 2))
    type = Column(Enum(BankAccountType), name="bank_account_type")
    color = Column(String(7))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    user = relationship(
        "UserModel",
        back_populates="bank_accounts",
    )
    transactions = relationship(
        "TransactionModel",
        back_populates="bank_account",
        cascade="all, delete, delete-orphan",
    )

    @validates("color")
    def validate_color(self, key, color):
        if not re.match(r"^#(?:[0-9a-fA-F]{3}){1,2}$", color):
            raise ValueError("Invalid HEX for color")
        return color


class CategoryModel(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100))
    icon = Column(String)
    type = Column(Enum(TransactionType), name="transaction_type")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    user = relationship("UserModel", back_populates="categories")
    transactions = relationship("TransactionModel", back_populates="category")

    @validates("icon")
    def validate_icon(self, key, icon):
        if not re.match(r"^https?:\/\/", icon):
            raise ValueError("Invalid URL for icon")
        return icon


class TransactionModel(Base):
    __tablename__ = "transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100))
    value = Column(Numeric(12, 2))
    type = Column(Enum(TransactionType), name="transaction_type")
    date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
    )
    user = relationship("UserModel", back_populates="transactions")
    bank_account_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "bank_accounts.id",
            ondelete="CASCADE",
        ),
    )
    bank_account = relationship("BankAccountModel", back_populates="transactions")
    category_id = Column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="SET NULL"),
        nullable=True,
    )
    category = relationship("CategoryModel", back_populates="transactions")
