from fastapi import APIRouter, FastAPI, status, Depends
import asyncio
from models import GetUrl, CreateShort, urls
from database import sessionmaker, get_db
from algorithm import get_short


router = APIRouter(prefix="/shorturl", tags=["urls"])

@router.post("/short", response_model=GetUrl, status_code=status.HTTP_201_CREATED)
async def short_create(url : str, session : sessionmaker = Depends(get_db)) -> GetUrl:
    shorted_url = get_short(url)
    link = urls(url = url, shortcode=shorted_url)
    session.add(link)
    session.commit()
    session.refresh(link)
    from sqlmodel import select
    result = session.execute(select(urls)).all()
    print(result)
    return link


    
