from settings import settings
from sqlalchemy import create_engine

# REF-009-DB-CONNECTION-CONFIG
engine = create_engine(settings.database_url)

db = ""
