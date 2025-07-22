import pytest
from src.product import Product


def test_category_count(sample_category):
    # Создаем еще одну категорию для теста
    tv = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром",
        [tv]
    )

    assert Category.category_count == 2
    assert Category.product_count == 4  # 3 из sample_category + 1 из category2


def test_product_initialization(sample_products):
    p1, p2, p3 = sample_products

    assert p1.name == "Samsung Galaxy S23 Ultra"
    assert p1.description == "256GB, Серый цвет, 200MP камера"
    assert p1.price == 180000.0
    assert p1.quantity == 5

    assert p2.name == "Iphone 15"
    assert p3.description == "1024GB, Синий"
