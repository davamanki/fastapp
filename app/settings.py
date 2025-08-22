from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = BASE_DIR / ".env"
load_dotenv(ENV_PATH)

class Settings(BaseSettings):
    run_in_docker: bool = Field(False, alias="RUN_IN_DOCKER")
    pg_user: str = Field(..., alias="POSTGRES_USER")
    pg_password: str = Field(..., alias="POSTGRES_PASSWORD")
    pg_db: str = Field(..., alias="POSTGRES_DB")
    pg_port: int = Field(5432, alias="POSTGRES_PORT")
    app_port: int = Field(8000, alias="APP_PORT")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def pg_host(self) -> str:
        return "db" if self.run_in_docker else "127.0.0.1"

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.pg_user}:{self.pg_password}@{self.pg_host}:{self.pg_port}/{self.pg_db}"


settings = Settings()
print(settings.database_url)