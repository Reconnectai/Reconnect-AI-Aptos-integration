import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from blueprints import router
from config import settings


def create_app():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/docs",
        description=settings.DESCRIPTION,
    )

    origins = [settings.FRONTEND_URL, settings.BACKEND_URL]
    if settings.is_dev:
        origins.extend(['http://localhost:3000', 'http://localhost:8080'])
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['GET', 'POST'],
        allow_headers=[
            'User-Agent', 'Cache-Control', 'Content-Type', 'Origin',
            'Access-Control-Allow-Origin', 'Access-Control-Allow-Headers',
            'Content-Length',
        ],
    )
    app.include_router(router)

    return app


if __name__ == '__main__':
    uvicorn.run(
        'app:create_app', host='0.0.0.0', port=8090, reload=True, factory=True)
