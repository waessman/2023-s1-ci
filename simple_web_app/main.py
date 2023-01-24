from fastapi import FastAPI

from .models import PasswordSchema, PasswordValidator, ValidationResponse

app = FastAPI()


@app.get("/")
def read_root():
    """ "This is the default view"""
    return {"description": "This is just a dummy response. Your API is up and running!"}


@app.post("/", response_model=ValidationResponse, status_code=201)
def validate_password(password: PasswordSchema):
    """
    # Please, submit a post with the password to validate
    ## Passwords must comply to:

    1. 8 characters minimum<br>
    2. At least 1 number<br>
    3. At least 1 especial character<br>
    4. At least 1 upper case letter<br>
    5. At least 1 lower case letter<br>
    6. Especial characters can not be / ^ ~

    :param password: this is the password to be validated<br>
    :return: validation result in terms of OK, or VALIDATION ERROR<br>
    """
    validator = PasswordValidator(content=password.content)
    result = validator.password_validate()
    return result
