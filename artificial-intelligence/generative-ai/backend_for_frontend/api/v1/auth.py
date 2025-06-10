"""
REF-007-API-ENDPOINT-TESTING
Request example to test the endpoint:
POST http://127.0.0.1:8000/v1/auth/login
Payload
{
    "username": "test-username",
    "password": "test-password"
}
"""

from domain.models import LoginRequest, TokenResponse
from fastapi import APIRouter

router = APIRouter()


# REF-011-HTTP-METHOD, REF-011-RESOURCE-NAMING, REF-011-SYNCHRONICITY, REF-011-DATA-DESERIALIZATION
# REF-011-INPUT-VALIDATION, REF-011-RESPONSE-VALIDATION
@router.post("/login", response_model=TokenResponse)  # TODO status_code=
def login(data: LoginRequest) -> TokenResponse:
    # REF-008-SPHINX-DOCSTRING
    """
    Authentication endpoint using Username & password with JWT.

    :param data: LoginRequest with username and password
    :type data: LoginRequest
    :return: JWT token response
    :rtype: TokenResponse
    """
    # REF-011-DATA-SERIALIZATION
    return TokenResponse(access_token="token123", token_type="bearer", expires_in=3600)
