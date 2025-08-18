import pytest
from abc import ABC, abstractmethod
from src.abstract_entity import AbstractEntity
from src.product import Category
from src.order import Order

def test_abstract_entity_is_abstract():
    """Тест, что AbstractEntity является абстрактным классом"""
    # Попытка создать экземпляр абстрактного класса должна вызвать TypeError
    with pytest.raises(TypeError):
        AbstractEntity("name", "description")

def test_category_inherits_from_abstract_entity():
    """Тест, что Category наследуется от AbstractEntity"""
    category = Category("Test Category", "Test Description", [])
    assert isinstance(category, AbstractEntity)
    assert isinstance(category, Category)

def test_order_inherits_from_abstract_entity():
    """Тест, что Order наследуется от AbstractEntity"""
    from src.product import Product
    product = Product("Test Product", "Test Description", 100.0, 5)
    order = Order(product, 3)
    assert isinstance(order, AbstractEntity)
    assert isinstance(order, Order)

def test_category_implements_abstract_methods():
    """Тест, что Category реализует все абстрактные методы AbstractEntity"""
    # Создание экземпляра Category не должно вызывать ошибок
    category = Category("Test Category", "Test Description", [])
    assert category.name == "Test Category"
    assert category.description == "Test Description"

def test_order_implements_abstract_methods():
    """Тест, что Order реализует все абстрактные методы AbstractEntity"""
    from src.product import Product
    product = Product("Test Product", "Test Description", 100.0, 5)
    order = Order(product, 3)
    assert order.name is not None  # У Order есть имя, унаследованное от AbstractEntity
    assert order.description is not None  # У Order есть описание, унаследованное от AbstractEntity
    assert order.product == product
    assert order.quantity == 3
    assert order.total_cost == 300.0