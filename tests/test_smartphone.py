import pytest

from src.product import Category
from src.smartphone import Smartphone


def test_smartphone_initialization(sample_smartphone):
    """Тест инициализации смартфона"""
    assert sample_smartphone.name == "iPhone 15 Pro"
    assert sample_smartphone.description == "Latest model from Apple"
    assert sample_smartphone.price == 120000.0
    assert sample_smartphone.quantity == 3
    assert sample_smartphone.efficiency == "A17 Bionic"
    assert sample_smartphone.model == "iPhone 15 Pro"
    assert sample_smartphone.memory == "256GB"
    assert sample_smartphone.color == "Titanium"


def test_smartphone_addition_same_type(sample_smartphone, another_smartphone):
    """Тест сложения двух смартфонов"""
    total = sample_smartphone + another_smartphone
    expected = (sample_smartphone.price * sample_smartphone.quantity) + \
               (another_smartphone.price * another_smartphone.quantity)
    assert total == expected


def test_smartphone_addition_different_type_error(sample_smartphone, sample_lawn_grass):
    """Тест сложения смартфона с другим типом вызывает TypeError"""
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = sample_smartphone + sample_lawn_grass


def test_smartphone_inheritance(sample_smartphone):
    """Тест проверки наследования от Product"""
    assert isinstance(sample_smartphone, Smartphone)
    assert isinstance(sample_smartphone, object) # Все классы наследуются от object
    # Проверяем, что у экземпляра Smartphone есть все атрибуты Product
    assert hasattr(sample_smartphone, 'name')
    assert hasattr(sample_smartphone, 'description')
    assert hasattr(sample_smartphone, 'price')
    assert hasattr(sample_smartphone, 'quantity')


def test_category_add_product_valid_smartphone():
    """Тест добавления валидного смартфона в категорию"""
    category = Category("Electronics", "Electronic devices", [])
    smartphone = Smartphone("iPhone", "Latest model", 999.0, 10, "A15", "13 Pro", "256GB", "Black")

    initial_product_count = Category.product_count
    category.add_product(smartphone)

    assert len(category._Category__products) == 1
    assert category._Category__products[0] is smartphone
    assert Category.product_count == initial_product_count + 1
