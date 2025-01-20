
from datetime import timedelta, datetime
from jose import JWTError, jwt

from dotenv import load_dotenv
import os

envpath = os.path.join(os.path.dirname(__file__),'..','.env')
load_dotenv(dotenv_path=envpath)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


