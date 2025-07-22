import pytest
from src.category import Category


def test_category_initialization(sample_category, sample_products):
    assert sample_category.name == "Смартфоны"
    assert "Смартфоны, как средство" in sample_category.description
    assert len(sample_category.products) == 3
    assert sample_category.products[0].name == "Samsung Galaxy S23 Ultra"


def test_empty_category():
    # Проверяем создание категории без продуктов
    empty_category = Category("Пустая", "Нет товаров", [])
    assert len(empty_category.products) == 0
    assert Category.category_count >= 1  # зависит от порядка выполнения тестов
    # product_count не должен увеличиваться для пустой категории