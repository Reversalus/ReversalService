from fastapi import APIRouter
from ..models.user import EmailLogin

loginRouter = APIRouter()

# for normal login using email and password
@loginRouter.post("/register")
def email_register(emailLogin: EmailLogin):
    return {"message": "OTP login successful"}

#  for login using google account
@loginRouter.post("/register/google")
def google_register(emailLogin: EmailLogin):
    return {"message": "Google login successful"}