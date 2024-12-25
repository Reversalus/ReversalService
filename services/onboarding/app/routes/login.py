from fastapi import APIRouter
from ..models.user import EmailLogin

loginRouter = APIRouter()

# for normal login using email and password
@loginRouter.post("/login")
def email_login(emailLogin: EmailLogin):
    return {"message": "OTP login successful"}

#  for login using google account
@loginRouter.post("/")
def google_login(emailLogin: EmailLogin):
    return {"message": "Google login successful"}