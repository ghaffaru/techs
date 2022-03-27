from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import plotly.express as px
from app.database import get_db
from . import models, schemas

router = APIRouter(prefix='/schools', )


def generate_chart(schools,type):
    total_enrollments = []
    ids = []
    for school in schools:
        total_enrollments.append(school.total_enrollment)
        ids.append(school.id)

    fig = px.bar(x=ids, y=total_enrollments)
    file_name = 'static/schools_by_' + str(type) + '.html'
    fig.write_html(file_name)
    return '/static/schools_by_' + str(type) + '.html'


# filter by category
@router.get('/filter-by-category')
async def filter_by_category(category: str, db: Session = Depends(get_db)):
    schools = db.query(models.School).filter(models.School.category == category).all()

    file = generate_chart(schools,'category')

    return {'file': file, 'schools': schools}


# filter by name
@router.get('/filter-by-name')
async def filter_by_name(name: str, db: Session = Depends(get_db)):

    schools_data = db.query(models.School).filter(models.School.name == name).all()

    file = generate_chart(schools_data, 'name')

    return {'file': file, 'schools': schools_data}


# filter by year
@router.get('/filter-by-year')
async def filter_by_name(year: str, db: Session = Depends(get_db)):
    schools = db.query(models.School).filter(models.School.year == year).all()

    file = generate_chart(schools, 'year')

    return {'file': file, 'schools': schools}
