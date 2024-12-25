from pydantic import BaseModel
from datetime import datetime

class EmailLogin(BaseModel):
    email: str
    password: str
