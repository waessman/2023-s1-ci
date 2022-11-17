from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    """"This is the default view"""
    return {"description": "Please submit a post with a password for validation on validate_password view"}


@app.post("/")
def validate_password(password: str):
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
    return {"Hello": password}
