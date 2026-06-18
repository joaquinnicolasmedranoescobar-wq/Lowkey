from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

API_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = API_ROOT / ".env"


class Settings(BaseSettings):
	api_v1_prefix: str = "/api/v1"
	allowed_origins: list[str] = ["*"]
	api_title: str = "Lowkey API"
	api_description: str = "Base API for vehicle maintenance, expenses, and statistics."
	api_version: str = "0.1.0"

	mongodb_uri: str = Field(..., env="MONGODB_URI")
	mongodb_db_name: str = Field("lowkey", env="MONGODB_DB_NAME")
	mongodb_app_name: str = Field("LowkeyAPI", env="MONGODB_APP_NAME")
	mongodb_server_selection_timeout_ms: int = Field(
		5000,
		env="MONGODB_SERVER_SELECTION_TIMEOUT_MS",
	)

	class Config:
		env_file = ENV_FILE
		env_file_encoding = "utf-8"
		case_sensitive = False


@lru_cache
def get_settings() -> Settings:
	return Settings()