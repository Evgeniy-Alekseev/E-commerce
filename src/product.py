class Product:
    """Класс для представления продукта."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """
        Инициализация продукта
        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество на складе
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категорий товаров."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """
        Инициализация категории
        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов в категории
        """
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
