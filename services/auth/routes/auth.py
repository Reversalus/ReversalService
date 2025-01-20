from decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import timedelta, datetime
from database import storeOTP, getOTP, verifyOTP
from models import ResponseModel, UserPayload, OTPPayload, Token
from utils.token_util import create_access_token
from dotenv import  load_dotenv
import os

envpath = os.path.join(os.path.dirname(__file__),'..', '.env')
load_dotenv(dotenv_path=envpath)

router = APIRouter(prefix='/auth', tags=['auth'])

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

# Create new user
@router.post('/register-email',status_code= status.HTTP_201_CREATED)
async def register_user( userPayload: UserPayload):
    return {"data": "user registered"}

# send a otp for a phone number
@router.post('/sendOtp',status_code=status.HTTP_201_CREATED)
async def tigger_otp(userPayload: UserPayload):
    if storeOTP(userPayload.phone_number):
        return ResponseModel(code=200, message="otp sent")
    else:
        return ResponseModel(code=400, message="otp not sent")

# generate new and resend otp
@router.post('/resendOtp',status_code=status.HTTP_201_CREATED)
async def resend_otp(userPayload: UserPayload):
    if storeOTP(userPayload.phone_number):
        return ResponseModel(code=200, message="otp sent")
    else:
        return ResponseModel(code=400, message="otp not sent")

# verify the otp
@router.post('/verifyOtp',status_code=status.HTTP_201_CREATED)
async def verify_otp(otpPayload: OTPPayload):
    if verifyOTP( otpPayload):
        return ResponseModel(code=200, message="otp verified")
    else:
        return ResponseModel(code=400, message="otp not verified")

# bypass otp
@router.post('/bypassOtp',status_code=status.HTTP_201_CREATED)
async def bypass_otp(userPayload: UserPayload):
    print('bypassing otp')
    otp = getOTP(userPayload.phone_number)
    return otp
