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
