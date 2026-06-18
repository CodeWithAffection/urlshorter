from sqlmodel import create_engine, SQLModel
from sqlalchemy.orm import Session, sessionmaker
from config import settings
from models import Base


sqlalchemy_database_url = settings.sqlalchemy_database_url
engine = create_engine(sqlalchemy_database_url)

SessionLocal = sessionmaker(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)  
    Base.metadata.create_all(engine)      

def get_session():
    with Session(engine) as session:
        yield session
