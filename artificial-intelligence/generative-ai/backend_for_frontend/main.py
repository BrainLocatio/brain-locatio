import os

from api.v1 import auth
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# REF-API-SECURITY-CORS
frontend_url: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
app.add_middleware(
    CORSMiddleware, allow_origins=frontend_url, allow_credentials=False, allow_methods=["POST"], allow_headers=["*"]
)

# REF-011-API-VERSIONING
app.include_router(auth.router, prefix="/v1/auth")
