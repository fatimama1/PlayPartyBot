import json

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    USERS: list[int]
    DATABASE_URL: str
    EVENT_NAME: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )

    def __init__(self, **values):
        for field in ("USERS",):
            if field in values and isinstance(values[field], str):
                values[field] = json.loads(values[field])
        super().__init__(**values)


settings = Settings()
