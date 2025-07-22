class Category:
    """Класс для представления категорий."""
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