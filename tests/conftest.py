import pytest
import json
from src.product import Product, Category


@pytest.fixture
def sample_products():
    """Фикстура для создания списка тестовых продуктов"""
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура для создания тестовой категории"""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        sample_products
    )


@pytest.fixture
def sample_products_json(tmp_path):
    """Фикстура, создающая временный JSON-файл с данными и возвращающая путь к нему"""
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14
                }
            ]
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {
                    "name": "55\" QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]

    # Создаем временный файл
    json_file = tmp_path / "test_products.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return json_file  # Возвращаем путь к файлу


@pytest.fixture
def empty_category():
    """Фикстура для создания пустой категории"""
    return Category("Пустая", "Нет товаров", [])


@pytest.fixture
def sample_product_data():
    """Фикстура для создания данных продукта в виде словаря"""
    return {
        "name": "New Test Product",
        "description": "New Test Description",
        "price": 150.0,
        "quantity": 3
    }


@pytest.fixture
def duplicate_product_data():
    """Фикстура для создания данных дублирующего продукта"""
    return {
        "name": "Samsung Galaxy S23 Ultra",  # Существующее имя
        "description": "Новое описание",
        "price": 190000.0,  # Новая цена
        "quantity": 2  # Добавляемое количество
    }


@pytest.fixture
def price_change_data():
    """Фикстура для тестирования изменения цены"""
    return {
        "positive": 120.0,
        "negative": -50.0,
        "decrease": 90.0
    }
