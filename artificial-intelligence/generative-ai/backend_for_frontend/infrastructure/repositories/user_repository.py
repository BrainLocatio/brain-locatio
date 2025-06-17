from typing import Optional

from infrastructure.db import db
from infrastructure.models import User


# REF-011-API-CRUD-OPERATIONS, REF-009-DB-ORM
def get_user_by_username(username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()  # type: ignore
