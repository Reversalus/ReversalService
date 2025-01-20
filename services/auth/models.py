from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field
from typing import Optional, Any

# Define User ORM Model:
# class Users(Base):
#     __tablename__ = 'users'

#     phone_number = Column(Integer, primary_key=True, index=True)

#     class Config:
#         orm_mode = True


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
