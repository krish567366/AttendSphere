from pydantic import BaseSettings # Corrected from pydantic_settings for broader compatibility

class Settings(BaseSettings):
    PROJECT_NAME: str = "Auth Service"
    DATABASE_URL: str = "postgresql://user:password@localhost/auth_db"
    SECRET_KEY: str = "your-secret-key"  # CHANGE THIS!
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env" # This will load from .env file in the service's root if present

settings = Settings()
