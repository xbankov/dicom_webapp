from pydantic import BaseSettings


class Settings(BaseSettings):
    threshold: float = 0.5
