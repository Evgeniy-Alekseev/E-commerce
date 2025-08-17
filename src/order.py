from src.abstract_entity import AbstractEntity
from src.product import Product


class Order(AbstractEntity):
    """
    Класс для представления заказа.
    """

    def __init__(self, product: Product, quantity: int):
        """
        Инициализация заказа.

        :param product: Товар в заказе
        :param quantity: Количество купленного товара
        """
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity
        super().__init__(f"Заказ {product.name}", f"Заказ товара {product.name}")
