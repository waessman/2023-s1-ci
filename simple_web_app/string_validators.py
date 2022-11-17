from exceptions import MinimumLengthException

class LengthValidator:
    def __init__(self, content: str):
        self.minimum_length = 8
        self.content = content

    def validate(self):
        if self.minimum_length > len(self.content):
            msg = f"Passwords must have at least {self.minimum_length} characters!"
            raise MinimumLengthException(detail=msg)
