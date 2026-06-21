from fastapi import APIRouter, FastAPI, status, Depends, HTTPException
import asyncio
from models import GetUrl, CreateShort, urls, DelUrl, deletes
from database import sessionmaker, get_db
from algorithm import get_short
from sqlalchemy import select, delete


router = APIRouter(prefix="/shorten", tags=["urls"])

counter = 0

@router.post("/", response_model=GetUrl, status_code=status.HTTP_201_CREATED)
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


@router.get("/{id}", response_model=GetUrl, status_code=status.HTTP_200_OK)
async def short_get(id : int, session : sessionmaker = Depends(get_db)) -> GetUrl:
    u = session.get(urls, id)
    return u

@router.delete("/{id}", response_model=DelUrl, status_code=status.HTTP_202_ACCEPTED)
async def short_del(id : int, session : sessionmaker = Depends(get_db)) -> DelUrl:
    u = session.get(urls, id)
    d = session.get(deletes, 1)
    if d is None:
        d = deletes(id = 1, count = 0)
        session.add(d)
        session.commit()
        session.refresh(d)
    num = d.count
    delu = DelUrl(id = id, url = u.url, shortcode=u.shortcode, created_at = u.created_at, updated_at = u.updated_at, count = num)
    d.count+=1
    session.delete(u)
    session.commit()
    return delu

    
