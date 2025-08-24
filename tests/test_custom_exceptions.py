import pytest
from src.custom_exceptions import ZeroQuantityError

def test_zero_quantity_error_default_message():
    """Тест исключения ZeroQuantityError с сообщением по умолчанию"""
    with pytest.raises(ZeroQuantityError) as exc_info:
        raise ZeroQuantityError()
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"

def test_zero_quantity_error_custom_message():
    """Тест исключения ZeroQuantityError с пользовательским сообщением"""
    custom_message = "Пользовательское сообщение об ошибке"
    with pytest.raises(ZeroQuantityError) as exc_info:
        raise ZeroQuantityError(custom_message)
    assert str(exc_info.value) == custom_message
    assert exc_info.value.message == custom_message
