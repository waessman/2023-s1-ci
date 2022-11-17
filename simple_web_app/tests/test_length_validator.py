import pytest
from simple_web_app.string_validators import LengthValidator
from simple_web_app.exceptions import MinimumLengthException


def test_empty_str_should_raise_http_400_exception():
    with pytest.raises(MinimumLengthException):
        LengthValidator(content="").validate()


def test_7_chars_str_should_raise_http_400_exception():
    with pytest.raises(MinimumLengthException):
        LengthValidator(content="1234567").validate()


def test_8_chars_str_should_validate():
    assert None == LengthValidator(content="12345678").validate()


def test_9_chars_str_should_validate():
    assert None == LengthValidator(content="123456789").validate()
