from exceptions import MinimumLengthException, NoDigitException


class LengthValidator:
    def __init__(self, content: str):
        self.minimum_length = 8
        self.content = content

    def validate(self):
        if self.minimum_length > len(self.content):
            msg = f"Passwords must have at least {self.minimum_length} characters!"
            raise MinimumLengthException(detail=msg)
        return None


class DigitValidator:
    def __init__(self, content: str):
        self.content = content
        self.digit_set = {digit for digit in "0123456789"}
        self.content_set = {character for character in content}

    def validate(self):
        if self.digit_set.isdisjoint(self.content_set):
            msg = "Passwords must have at least 1 digit!"
            raise NoDigitException(detail=msg)
        return None
