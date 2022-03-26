from fastapi import FastAPI
from app.celery_utils import create_celery


def create_app() -> FastAPI:
    app = FastAPI()

    app.celery_app = create_celery()

    @app.get('/')
    async def root():
        return {'message': 'Hello World!'}

    return app
