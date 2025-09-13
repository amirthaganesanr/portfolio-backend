from fastapi import FastAPI
from app.config.config import settings
from app.api.routes import router as api_router
from app.services.service import load_instruments

def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)
    load_instruments()
    app.include_router(api_router, prefix="/api")
    return app

app = create_app()
