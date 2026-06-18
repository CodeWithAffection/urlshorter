from datetime import datetime,timezone
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, TIMESTAMP, text
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

class urls(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, nullable=False)
    url = Column(String, primary_key=False, nullable=False)
    shortcode = Column(String, primary_key=False, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=True, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=True, server_default=text("now()"))

class CreateShort(BaseModel):
    url : str
    shorted_url : str

class GetUrl(BaseModel):
    id : int
    url : str
    shortcode : str
    created_at : Optional[datetime] = None
    updated_at : Optional[datetime] = None

class DelUrl(BaseModel):
    id : int
    url : str
    shortcode : str
    created_at : datetime
    updated_at : datetime
    count : int

