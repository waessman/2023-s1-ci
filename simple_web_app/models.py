from pydantic import BaseModel
from string_validators import Validator, LengthValidator, DigitValidator


class PasswordSchema(BaseModel):
    content: str


class ValidationResponse(BaseModel):
    message: str


class PasswordValidator(BaseModel):
    content: str
    response: ValidationResponse | None = None

    def get_validators(self):
        validators = [
            LengthValidator(),
            DigitValidator(),
        ]
        return validators

    def password_validate(self) -> ValidationResponse:
        validators: list[Validator] = self.get_validators()
        for validator in validators:
            validator.validate(self.content)
        self.response = ValidationResponse(message="OK")
        return self.response
