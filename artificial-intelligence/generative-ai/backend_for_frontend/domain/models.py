from pydantic import BaseModel


# REF-011-DATA-MODELING
class LoginRequest(BaseModel):
    username: str
    password: str
