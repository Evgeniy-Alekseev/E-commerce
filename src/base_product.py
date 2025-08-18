from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.
    Определяет общую интерфейсную функциональность для продуктов.
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация базового продукта.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество на складе
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """
        Возвращает строковое представление продукта.

        :return: Строковое представление продукта
        """
        pass

    @abstractmethod
    def __add__(self, other: object) -> float:
        """
        Сложение продуктов по формуле: цена * количество + цена * количество.

        :param other: Другой продукт для сложения
        :return: Сумма произведений цены на количество
        :raises TypeError: Если сложение происходит между продуктами разных классов
        """
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """
        Создает новый продукт из словаря данных
        :param product_data: Словарь с данными продукта
        :param products_list: Список существующих продуктов для проверки дубликатов
        :return: Экземпляр класса Product или его наследников
        :raises TypeError: Если products_list содержит не только объекты Product или его наследников
        """
        pass
