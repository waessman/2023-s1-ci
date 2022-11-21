from string import ascii_lowercase, punctuation
from abc import ABC, abstractmethod
from exceptions import (
    MinimumLengthException,
    NoDigitException,
    NoLowerCaseException,
    EspecialCharacterException,
)


class Validator(ABC):
    @abstractmethod
    def validate(self, content) -> None:
        """
        This is the interface of the validation interface.
        :param content: the text to be validated
        :return: None if the text is valid or raise an Exception otherwise.
        """


class LengthValidator(Validator):
    def __init__(self):
        self.minimum_length = 8

    def validate(self, content):
        if self.minimum_length > len(content):
            msg = f"Passwords must have at least {self.minimum_length} characters!"
            raise MinimumLengthException(detail=msg)


class DigitValidator(Validator):
    def __init__(self):
        self.digit_set = set("0123456789")

    def validate(self, content):
        content_set = set(content)
        if self.digit_set.isdisjoint(content_set):
            msg = "Passwords must have at least 1 digit!"
            raise NoDigitException(detail=msg)


class LowerCaseValidator(Validator):
    def __init__(self):
        self.lower_case_set = set(ascii_lowercase)

    def validate(self, content):
        content_set = set(content)
        if self.lower_case_set.isdisjoint(content_set):
            msg = "Passwords must have at least 1 lower case letter!"
            raise NoLowerCaseException(detail=msg)


class EspecialCharacterValidator(Validator):
    def __init__(self):
        self.especial_set = set(punctuation)

    def validate(self, content):
        content_set = set(content)
        if self.especial_set.isdisjoint(content_set):
            msg = "Passwords must have at least 1 especial character!"
            raise EspecialCharacterException(detail=msg)
