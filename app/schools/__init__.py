from fastapi import APIRouter

schools_router = APIRouter(prefix='/schools', )

from . import models
