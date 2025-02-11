from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field
from typing import Optional, Any
import uuid

Base = declarative_base()


# Response Model:
class ResponseModel(BaseModel):
    code: int
    message: str
    data: Optional[Any] = None

# Define User Pydantic Model:
class UserPayload(BaseModel):
    phone_number: str = Field(..., pattern=r'^[6-9]\d{9}$')

# Define OTP Pydantic Model:
class OTPPayload(BaseModel):
    phone_number: str = Field(..., pattern=r'^[6-9]\d{9}$')
    otp: str = Field(..., pattern=r'^[1-9]\d{5}$')

# Define Token Pydantic Model:
class Token(BaseModel):
    token: str
    token_type: str

# Define User ORM Model:
class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4, server_default=text("uuid_generate_v4()"))
    first_name = Column(String(50), nullable=False)
    middle_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=False)
    email = Column(String(150), unique=True, nullable=True)
    phone = Column(String(20), unique=True, nullable=False)
    profile_image_uri = Column(Text, nullable=True)
    auth_google = Column(Boolean, default=False, server_default=text("false"))
    auth_phone = Column(Boolean, default=False, server_default=text("false"))
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP "))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP "), onupdate=text("CURRENT_TIMESTAMP "))

