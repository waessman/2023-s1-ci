from pydantic import BaseModel
from string_validators import LengthValidator, DigitValidator


class PasswordSchema(BaseModel):
    content: str


class ValidationResponse(BaseModel):
    message: str


class PasswordValidator(BaseModel):
    content: str
    response: ValidationResponse | None = None

    def password_validate(self) -> ValidationResponse:
        LengthValidator(content=self.content).validate()
        DigitValidator(content=self.content).validate()
        self.response = ValidationResponse(message="OK")
        return self.response
