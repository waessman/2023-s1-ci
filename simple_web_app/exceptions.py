from fastapi import HTTPException


class MinimumLengthException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)


class NoDigitException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)
