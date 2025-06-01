from api.v1 import auth
from fastapi import FastAPI

app = FastAPI()

# REF-011-API-VERSIONING
app.include_router(auth.router, prefix="/v1/auth")
