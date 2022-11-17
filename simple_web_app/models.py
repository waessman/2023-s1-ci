from pydantic import BaseModel


class PasswordSchema(BaseModel):
    content: str


class ValidationResponse(BaseModel):
    messages: list[str]
