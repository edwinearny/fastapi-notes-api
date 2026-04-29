from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "fastapi-notes-api"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./notes.db"

    class Config:
        env_file = ".env"


settings = Settings()
