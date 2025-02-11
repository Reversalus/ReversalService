from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from jose import JWTError, jwt
from dotenv import load_dotenv
import os

# load_dotenv()

# SECRET_KEY = os.getenv("SECRET_KEY")
# print(SECRET_KEY)

