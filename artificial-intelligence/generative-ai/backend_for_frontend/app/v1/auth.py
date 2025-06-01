from fastapi import APIRouter
from models import LoginRequest

router = APIRouter()


# REF-011-HTTP-METHOD, REF-011-RESOURCE-NAMING, REF-011-SYNCHRONICITY, REF-011-DATA-DESERIALIZATION
# REF-011-INPUT-VALIDATION
@router.post("/login")  # HINT: @router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    pass
