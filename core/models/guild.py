from core.models.base import BaseModel
from sqlalchemy import Column, BigInteger, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class GuildModel(BaseModel):
    __tablename__ = "guilds"
    
    id = Column(BigInteger, primary_key=True, autoincrement=False)
    joined_at = Column(DateTime, nullable=False)