import pytest
from string_validators import LengthValidator
from exceptions import MinimumLengthException


def test_length_validator_empty_str_should_raise_http_400_exception():
    with pytest.raises(MinimumLengthException):
        LengthValidator(content="").validate()


def test_length_validator_7_chars_str_should_raise_http_400_exception():
    with pytest.raises(MinimumLengthException):
        LengthValidator(content="1234567").validate()


def test_length_validator_8_chars_str_should_validate():
    assert None == LengthValidator(content="12345678").validate()


def test_length_validator_9_chars_str_should_validate():
    assert None == LengthValidator(content="123456789").validate()
