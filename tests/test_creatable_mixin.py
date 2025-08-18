import pytest
from io import StringIO
from src.creatable_mixin import CreatableMixin
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_creatable_mixin_prints_on_creation_product(monkeypatch):
    """Тест, что CreatableMixin печатает информацию при создании Product"""
    # Перехватываем вывод в stdout
    captured_output = StringIO()
    monkeypatch.setattr('sys.stdout', captured_output)

    # Создаем продукт
    product = Product("Test Product", "Test Description", 100.0, 5)

    # Проверяем, что информация была напечатана
    output = captured_output.getvalue()
    assert "Product('Test Product', 'Test Description', 100.0, 5)" in output


def test_creatable_mixin_prints_on_creation_smartphone(monkeypatch):
    """Тест, что CreatableMixin печатает информацию при создании Smartphone"""
    # Перехватываем вывод в stdout
    captured_output = StringIO()
    monkeypatch.setattr('sys.stdout', captured_output)

    # Создаем смартфон
    smartphone = Smartphone(
        "iPhone", "Latest model", 999.0, 10,
        "A15", "13 Pro", "256GB", "Black"
    )

    # Проверяем, что информация была напечатана
    output = captured_output.getvalue()
    assert "Smartphone('iPhone', 'Latest model', 999.0, 10" in output
    assert "'A15'" in output
    assert "'13 Pro'" in output
    assert "'256GB'" in output
    assert "'Black'" in output


def test_creatable_mixin_prints_on_creation_lawn_grass(monkeypatch):
    """Тест, что CreatableMixin печатает информацию при создании LawnGrass"""
    # Перехватываем вывод в stdout
    captured_output = StringIO()
    monkeypatch.setattr('sys.stdout', captured_output)

    # Создаем газонную траву
    lawn_grass = LawnGrass(
        "Grass Seed", "Premium quality", 50.0, 100,
        "Netherlands", "7 days", "Green"
    )

    # Проверяем, что информация была напечатана
    output = captured_output.getvalue()
    assert "LawnGrass('Grass Seed', 'Premium quality', 50.0, 100" in output
    assert "'Netherlands'" in output
    assert "'7 days'" in output
    assert "'Green'" in output

def test_creatable_mixin_repr_method():
    """Тест метода __repr__ у CreatableMixin"""
    product = Product("Test Product", "Test Description", 100.0, 5)
    repr_str = repr(product)
    assert repr_str == "Product('Test Product', 'Test Description', 100.0, 5)"
