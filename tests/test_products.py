import pytest
from product import Product, Category


def test_product_initialization(sample_products):
    p1, p2, p3 = sample_products

    assert p1.name == "Samsung Galaxy S23 Ultra"
    assert p1.description == "256GB, Серый цвет, 200MP камера"
    assert p1.price == 180000.0
    assert p1.quantity == 5

    assert p2.name == "Iphone 15"
    assert p3.description == "1024GB, Синий"
