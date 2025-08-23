from src.abstract_entity import AbstractEntity
from src.product import Product
from src.custom_exceptions import ZeroQuantityError


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
        try:
            if quantity <= 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен в заказ")

            self.product = product
            self.quantity = quantity
            self.total_cost = product.price * quantity
            super().__init__(f"Заказ {product.name}", f"Заказ товара {product.name}")
            print("Товар добавлен")
        except ZeroQuantityError as e:
            print(f"Ошибка добавления товара: {e}")
        finally:
            print("Обработка добавления товара завершена")
