from pydantic import BaseSettings


class Settings(BaseSettings):
    project_url: str
    service_role_secret: str

    class Config:
        env_file = ".env"


settings = Settings()
