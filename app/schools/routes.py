from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from . import models, schemas

router = APIRouter(prefix='/schools', )


# filter by category
@router.get('/filter-by-category',response_model=list[schemas.School])
async def filter_by_category(category: str, db: Session = Depends(get_db)):

    return db.query(models.School).filter(models.School.category == category).all()


# filter by name
@router.get('/filter-by-name', response_model=list[schemas.School])
async def filter_by_name(name: str, db: Session = Depends(get_db)):

    return db.query(models.School).filter(models.School.name == name).all()


# filter by year
@router.get('/filter-by-year', response_model=list[schemas.School])
async def filter_by_name(year: str, db: Session = Depends(get_db)):

    return db.query(models.School).filter(models.School.year == year).all()