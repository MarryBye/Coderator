from core.models.base import BaseModel
from core.models.guild import GuildModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from core.config import Config

DATABASE_URL = f"{Config.DATABASE_DRIVER}://{Config.DATABASE_USER}:{Config.DATABASE_PASSWORD}@{Config.DATABASE_HOST}:{Config.DATABASE_PORT}/{Config.DATABASE_NAME}"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(bind=engine)

def get_database_session() -> Session:
    return session_local()

BaseModel.metadata.create_all(bind=engine)