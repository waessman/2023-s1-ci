import pytest
from string_validators import LengthValidator
from exceptions import MinimumLengthException

def test_length_validator_empty_str_should_raise_http_400_exception():
    with pytest.raises(MinimumLengthException):
        LengthValidator(content="").validate()
