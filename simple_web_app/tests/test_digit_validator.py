from simple_web_app.string_validators import DigitValidator


def test_1_digit_str_should_validate():
    assert None == DigitValidator(content="1").validate()
