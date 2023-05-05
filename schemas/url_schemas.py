from pydantic import BaseModel


class CreateUrl(BaseModel):
    target_url: str


class ShowCreateUrl(BaseModel):
    target_url: str
    key: str
    secret_key: str
