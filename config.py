from functools import cached_property

from aptos_sdk.async_client import RestClient
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str = 'development'
    PROJECT_NAME: str = f"Reconnect AI Auth (Aptos) API - {ENV.capitalize()}"
    DESCRIPTION: str = "A Reconnect AI Auth"
    VERSION: str = "0.1"

    APTOS_URL: str
    SECRET_KEY: str
    BACKEND_URL: str = ''
    FRONTEND_URL: str = ''
    RECONNECT_WALLET: str

    @property
    def is_dev(self) -> bool:
        return self.ENV == 'development'

    @cached_property
    def aptos_client(self) -> RestClient:
        return RestClient(self.APTOS_URL)

    class Config:
        case_sensitive = True
        keep_untouched = (cached_property,)


settings = Settings()
