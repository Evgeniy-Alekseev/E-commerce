import json
from typing import List

from src.product import Product, Category
from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def load_categories_from_json(file_path: str) -> List[Category]:
    """
    Загружает категории и продукты из JSON-файла.
    :param file_path: Путь к JSON-файлу
    :return: Список объектов Category
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    categories = []
    for category_data in data:
        products = []
        for product_data in category_data['products']:
            # Определяем тип продукта на основе наличия специфических полей
            if all(key in product_data for key in ['efficiency', 'model', 'memory', 'color']):
                # Создаем объект Smartphone
                product = Smartphone(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    quantity=product_data['quantity'],
                    efficiency=product_data['efficiency'],
                    model=product_data['model'],
                    memory=product_data['memory'],
                    color=product_data['color']
                )
            elif all(key in product_data for key in ['country', 'germination_period', 'color']):
                # Создаем объект LawnGrass
                product = LawnGrass(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    quantity=product_data['quantity'],
                    country=product_data['country'],
                    germination_period=product_data['germination_period'],
                    color=product_data['color']
                )
            else:
                # Создаем обычный объект Product
                product = Product(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    quantity=product_data['quantity']
                )
            products.append(product)

        categories.append(
            Category(
                name=category_data['name'],
                description=category_data['description'],
                products=products
            )
        )
    return categories
