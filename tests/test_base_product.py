import pytest
from abc import ABC, abstractmethod
from src.base_product import BaseProduct
from src.product import Product


def test_base_product_is_abstract():
    """Тест, что BaseProduct является абстрактным классом"""
    # Попытка создать экземпляр абстрактного класса должна вызвать TypeError
    with pytest.raises(TypeError):
        BaseProduct("name", "description", 100.0, 10)


def test_product_inherits_from_base_product():
    """Тест, что Product наследуется от BaseProduct"""
    product = Product("Test Product", "Test Description", 100.0, 5)
    assert isinstance(product, BaseProduct)
    assert isinstance(product, Product)


def test_product_implements_abstract_methods():
    """Тест, что Product реализует все абстрактные методы BaseProduct"""
    # Создание экземпляра Product не должно вызывать ошибок
    product = Product("Test Product", "Test Description", 100.0, 5)

    # Проверка наличия абстрактных методов
    assert hasattr(product, '__str__')
    assert hasattr(product, '__add__')

    # Проверка, что методы работают
    assert str(product) == "Test Product, 100.0 руб. Остаток: 5 шт."

    # Проверка сложения
    product2 = Product("Test Product 2", "Test Description 2", 200.0, 3)
    result = product + product2
    assert result == (100.0 * 5) + (200.0 * 3)
