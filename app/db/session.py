from functools import lru_cache

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import PyMongoError

from app.core.config import get_settings


@lru_cache
def get_mongo_client() -> MongoClient:
    settings = get_settings()

    try:
        client = MongoClient(
            settings.mongodb_uri,
            appname=settings.mongodb_app_name,
            serverSelectionTimeoutMS=settings.mongodb_server_selection_timeout_ms,
        )
        client.admin.command("ping")
        return client
    except PyMongoError as exc:
        raise RuntimeError(
            "No se pudo conectar a MongoDB Atlas usando las credenciales del .env."
        ) from exc


def get_database_session() -> Database:
    settings = get_settings()
    return get_mongo_client()[settings.mongodb_db_name]