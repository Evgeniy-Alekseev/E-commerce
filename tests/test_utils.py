import pytest
from src.utils import load_data_from_json

def test_load_from_json(tmp_path):
    # Создаем временный JSON файл
    json_data = [
        {
            "name": "Тестовая категория",
            "description": "Описание тестовой категории",
            "products": [
                {
                    "name": "Тестовый продукт",
                    "description": "Описание тестового продукта",
                    "price": 100.0,
                    "quantity": 10
                }
            ]
        }
    ]

    file_path = tmp_path / "test_products.json"
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file)

    categories = load_data_from_json(file_path)
    assert len(categories) == 1
    assert categories[0].name == "Тестовая категория"
    assert len(categories[0].products) == 1
    assert categories[0].products[0].name == "Тестовый продукт"
