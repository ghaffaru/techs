from fastapi import FastAPI
from app.celery_utils import create_celery
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.celery_app = create_celery()


    from app.schools.routes import router
    app.include_router(router)

    @app.get('/')
    async def root():
        return {'message': 'Hello World!'}

    return app
