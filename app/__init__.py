from fastapi import FastAPI
from app.celery_utils import create_celery


def create_app() -> FastAPI:
    app = FastAPI()

    app.celery_app = create_celery()

    from app.schools import schools_router
    app.include_router(schools_router)

    @app.get('/')
    async def root():
        return {'message': 'Hello World!'}

    return app
