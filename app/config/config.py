from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI App"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()
