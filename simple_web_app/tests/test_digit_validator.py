import pytest
from simple_web_app.string_validators import DigitValidator
from simple_web_app.exceptions import NoDigitException


def test_1_digit_str_should_validate():
    assert None == DigitValidator(content="1").validate()


def test_1_digit_and_1_letter_str_should_validate():
    assert None == DigitValidator(content="1a").validate()


def test_1_letter_and_1_digit_str_should_validate():
    assert None == DigitValidator(content="b1").validate()


def test_1_letter_str_should_raise_http_400_exception():
    with pytest.raises(NoDigitException):
        DigitValidator(content="a").validate()


def test_1_especial_char_str_should_raise_http_400_exception():
    with pytest.raises(NoDigitException):
        DigitValidator(content="@").validate()


def test_empty_str_should_raise_http_400_exception():
    with pytest.raises(NoDigitException):
        DigitValidator(content="").validate()
