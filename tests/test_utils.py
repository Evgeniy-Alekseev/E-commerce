import json

import pytest

from src.lawngrass import LawnGrass
from src.product import Category, Product
from src.smartphone import Smartphone
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

    # Используем приватный атрибут для доступа к списку продуктов
    assert len(categories[0]._Category__products) == 3

    # Проверяем продукты в первой категории
    assert categories[0]._Category__products[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[0]._Category__products[0].price == 180000.0
    assert categories[0]._Category__products[0].quantity == 5
    assert categories[0]._Category__products[1].name == "Iphone 15"
    assert categories[0]._Category__products[1].description == "512GB, Gray space"

    # Проверяем вторую категорию (Телевизоры)
    assert categories[1].name == "Телевизоры"
    assert len(categories[1]._Category__products) == 1
    assert categories[1]._Category__products[0].name == "55\" QLED 4K"


def test_load_categories_from_json_product_attributes(sample_products_json):
    """Тест проверяет корректность атрибутов продуктов"""
    categories = load_categories_from_json(sample_products_json)

    # Проверяем атрибуты первого продукта
    product = categories[0]._Category__products[0]
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

    # Проверяем атрибуты последнего продукта
    product = categories[1]._Category__products[0]
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


def test_load_categories_from_json_returns_list_extended(tmp_path):
    """Тест проверяет, что функция возвращает список категорий с расширенными данными"""
    # Создаем JSON с данными для новых классов
    data = [
        {
            "name": "Электроника",
            "description": "Электронные устройства",
            "products": [
                {
                    "name": "iPhone 15 Pro",
                    "description": "Latest Apple smartphone",
                    "price": 99900.0,
                    "quantity": 5,
                    "efficiency": "A17 Pro",
                    "model": "iPhone 15 Pro",
                    "memory": "256GB",
                    "color": "Titanium"
                }
            ]
        },
        {
            "name": "Сад и огород",
            "description": "Товары для сада",
            "products": [
                {
                    "name": "Газонная трава Премиум",
                    "description": "Высококачественные семена",
                    "price": 2500.0,
                    "quantity": 50,
                    "country": "Нидерланды",
                    "germination_period": "7-14 дней",
                    "color": "Зеленый"
                }
            ]
        }
    ]

    json_file = tmp_path / "extended_test_products.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    categories = load_categories_from_json(json_file)
    assert isinstance(categories, list)
    assert len(categories) == 2


def test_load_categories_from_json_smartphone_type(tmp_path):
    """Тест проверяет, что смартфоны создаются как объекты Smartphone"""
    data = [
        {
            "name": "Смартфоны",
            "description": "Мобильные телефоны",
            "products": [
                {
                    "name": "Samsung Galaxy S24",
                    "description": "Флагманский смартфон",
                    "price": 89990.0,
                    "quantity": 3,
                    "efficiency": "Snapdragon 8 Gen 3",
                    "model": "Galaxy S24",
                    "memory": "512GB",
                    "color": "Phantom Black"
                }
            ]
        }
    ]

    json_file = tmp_path / "smartphone_test.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    categories = load_categories_from_json(json_file)
    category = categories[0]
    # Используем приватный атрибут для доступа к списку продуктов
    product = category._Category__products[0]

    # Проверяем, что продукт является экземпляром Smartphone
    assert isinstance(product, Smartphone)
    # Проверяем атрибуты Smartphone
    assert product.efficiency == "Snapdragon 8 Gen 3"
    assert product.model == "Galaxy S24"
    assert product.memory == "512GB"
    assert product.color == "Phantom Black"


def test_load_categories_from_json_lawn_grass_type(tmp_path):
    """Тест проверяет, что газонная трава создается как объекты LawnGrass"""
    data = [
        {
            "name": "Садовые товары",
            "description": "Все для сада",
            "products": [
                {
                    "name": "Газонная трава Эконом",
                    "description": "Эконом-вариант семян",
                    "price": 1200.0,
                    "quantity": 100,
                    "country": "Россия",
                    "germination_period": "10-20 дней",
                    "color": "Темно-зеленый"
                }
            ]
        }
    ]

    json_file = tmp_path / "lawn_grass_test.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    categories = load_categories_from_json(json_file)
    category = categories[0]
    # Используем приватный атрибут для доступа к списку продуктов
    product = category._Category__products[0]

    # Проверяем, что продукт является экземпляром LawnGrass
    assert isinstance(product, LawnGrass)
    # Проверяем атрибуты LawnGrass
    assert product.country == "Россия"
    assert product.germination_period == "10-20 дней"
    assert product.color == "Темно-зеленый"


def test_load_categories_from_json_mixed_types(tmp_path):
    """Тест проверяет загрузку смешанных типов продуктов"""
    data = [
        {
            "name": "Смешанная категория",
            "description": "Разные типы товаров",
            "products": [
                {
                    "name": "Обычный продукт",
                    "description": "Стандартное описание",
                    "price": 1000.0,
                    "quantity": 10
                },
                {
                    "name": "Xiaomi Phone",
                    "description": "Китайский смартфон",
                    "price": 25000.0,
                    "quantity": 7,
                    "efficiency": "Snapdragon 7 Gen 2",
                    "model": "Redmi Note 12",
                    "memory": "128GB",
                    "color": "Синий"
                },
                {
                    "name": "Трава для клумб",
                    "description": "Семена для клумб",
                    "price": 800.0,
                    "quantity": 30,
                    "country": "Германия",
                    "germination_period": "5-10 дней",
                    "color": "Разноцветная"
                }
            ]
        }
    ]

    json_file = tmp_path / "mixed_test.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    categories = load_categories_from_json(json_file)
    category = categories[0]
    # Используем приватный атрибут для доступа к списку продуктов
    products = category._Category__products

    # Проверяем количество продуктов
    assert len(products) == 3

    # Проверяем типы продуктов
    assert isinstance(products[0], Product)  # Обычный продукт
    assert not isinstance(products[0], Smartphone)  # Не смартфон
    assert not isinstance(products[0], LawnGrass)  # Не газонная трава

    assert isinstance(products[1], Smartphone)  # Смартфон
    assert products[1].model == "Redmi Note 12"

    assert isinstance(products[2], LawnGrass)  # Газонная трава
    assert products[2].country == "Германия"
