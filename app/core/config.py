from pathlib import PurePath, Path

from pydantic import PostgresDsn, AnyHttpUrl, ConfigDict, BaseModel, BaseConfig
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool
    sentry_dsn: AnyHttpUrl

    database_url: PostgresDsn
    upload_folder: PurePath = PurePath(f'{PurePath(Path(__file__)).parents[2]}/tmp')
    minio_host: str
    bucket_access_token: str
    bucket_secret_key: str
    bucket_name: str
