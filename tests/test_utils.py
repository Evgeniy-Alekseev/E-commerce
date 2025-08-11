import pytest
import json
import tempfile
from pathlib import Path
from src.product import Product, Category
from src.utils import load_categories_from_json


def test_load_categories_from_json_returns_list(sample_products_json):
    """Тест проверяет, что функция возвращает список категорий"""
    categories = load_categories_from_json(sample_products_json)
    assert isinstance(categories, list)
    assert len(categories) == 2


def test_load_categories_from_json_correct_structure(sample_products_json):
    """Тест проверяет корректность структуры загруженных данных"""
    categories = load_categories_from_json(sample_products_json)
    
    # Проверяем первую категорию (Смартфоны)
    assert categories[0].name == "Смартфоны"
    assert "коммуникации" in categories[0].description
    assert len(categories[0].products) == 3
    
    # Проверяем продукты в первой категории
    assert categories[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[0].products[0].price == 180000.0
    assert categories[0].products[0].quantity == 5
    
    assert categories[0].products[1].name == "Iphone 15"
    assert categories[0].products[1].description == "512GB, Gray space"
    
    # Проверяем вторую категорию (Телевизоры)
    assert categories[1].name == "Телевизоры"
    assert len(categories[1].products) == 1
    assert categories[1].products[0].name == "55\" QLED 4K"


def test_load_categories_from_json_product_attributes(sample_products_json):
    """Тест проверяет корректность атрибутов продуктов"""
    categories = load_categories_from_json(sample_products_json)
    
    # Проверяем атрибуты первого продукта
    product = categories[0].products[0]
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
    
    # Проверяем атрибуты последнего продукта
    product = categories[1].products[0]
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_load_categories_from_json_updates_class_counters(sample_products_json):
    """Тест проверяет обновление счетчиков категорий и продуктов"""
    # Сбросим счетчики перед тестом
    Category.category_count = 0
    Category.product_count = 0
    
    categories = load_categories_from_json(sample_products_json)
    
    assert Category.category_count == 2
    assert Category.product_count == 4  # 3 смартфона + 1 телевизор


def test_load_categories_from_json_file_not_found():
    """Тест проверяет обработку случая с отсутствующим файлом"""
    with pytest.raises(FileNotFoundError):
        load_categories_from_json("nonexistent_file.json")


def test_load_categories_from_json_invalid_json(tmp_path):
    """Тест проверяет обработку невалидного JSON"""
    invalid_json = tmp_path / "invalid.json"
    invalid_json.write_text("{ это: невалидный, json: }", encoding='utf-8')
    
    with pytest.raises(json.JSONDecodeError):
        load_categories_from_json(invalid_json)
