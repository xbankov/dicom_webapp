from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    threshold: float = 0.5
