from typing import List

from src.abstract_entity import AbstractEntity
from src.base_product import BaseProduct
from src.creatable_mixin import CreatableMixin
from src.custom_exceptions import ZeroQuantityError
from typing import List, Optional, TypeVar, Type

T = TypeVar('T', bound='Product')

class Product(CreatableMixin, BaseProduct):
    """Класс для представления продукта."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
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
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float:
        """
        Сложение двух продуктов по формуле: цена * количество + цена * количество
        :param other: Другой объект Product
        :return: Сумма произведений цены на количество
        """
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        total_price = (self.price * self.quantity) + (other.price * other.quantity)
        return total_price

    @classmethod
    def new_product(cls: Type[T], product_data: dict, products_list: Optional[List['Product']] = None) -> T:
        """
        Создает новый продукт из словаря данных
        :param product_data: Словарь с данными продукта
        :param products_list: Список существующих продуктов для проверки дубликатов
        :return: Экземпляр класса Product или его наследников
        :raises TypeError: Если products_list содержит не только объекты Product или его наследников
        """
        if products_list is None:
            products_list = []

        # Проверка, что все элементы в products_list являются Product или его наследниками
        for product in products_list:
            if not isinstance(product, Product):
                raise TypeError("products_list может содержать только объекты Product или его наследников")

        # Проверка на дубликаты
        for existing_product in products_list:
            if existing_product.name == product_data["name"]:
                # Объединяем количество
                existing_product.quantity += product_data["quantity"]
                # Выбираем максимальную цену
                if existing_product.price < product_data["price"]:
                    existing_product.price = product_data["price"]
                return existing_product

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверками"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        # Проверяем, существует ли уже атрибут __price (для инициализации)
        if hasattr(self, "_Product__price") and new_price < self.__price:
            confirm = input(
                f"Цена снижается с {self.__price} до {new_price}. Подтвердите (y/n): "
            )
            if confirm.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price


class Category(AbstractEntity):
    """Класс для представления категорий товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        """
        Инициализация категории
        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов в категории
        """
        self.__products: List[Product] = products
        super().__init__(name, description)
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        """Возвращает итератор для продуктов категории."""
        return CategoryIterator(self)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию.
        :param product: Продукт для добавления
        :raises TypeError: Если передан не объект Product или его наследник
        :raises ZeroQuantityError: Если количество товара равно нулю
        """
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только объекты Product или его наследников")

            if product.quantity <= 0:
                raise ValueError("Товар с нулевым количеством не может быть добавлен")

            self.__products.append(product)
            Category.product_count += 1
            print("Товар добавлен")

        except (TypeError, ZeroQuantityError) as e:
            print(f"Ошибка добавления товара: {e}")
            raise  # Пробрасываем исключение дальше для обработки в тестах
        finally:
            print("Обработка добавления товара завершена")

    def middle_price(self) -> float:
        """
        Подсчитывает средний ценник всех товаров в категории.
        :return: Средняя цена товаров в категории, или 0 если категория пуста
        """
        try:
            if not self.__products:
                raise ZeroDivisionError("В категории нет товаров")

            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)

        except ZeroDivisionError:
            return 0.0

    @property
    def products(self) -> str:
        """Геттер для списка продуктов в виде строки."""
        return "\n".join(str(product) for product in self.__products)


class CategoryIterator:
    """Класс для итерации по товарам категории"""

    def __init__(self, category: Category):
        """
        Инициализация итератора
        :param category: Объект Category для итерации
        """
        self.category = category
        self.index = 0

    def __iter__(self):
        """Возвращает сам объект как итератор"""
        return self

    def __next__(self):
        """Возвращает следующий продукт в категории"""
        if self.index < len(self.category._Category__products):
            product = self.category._Category__products[self.index]
            self.index += 1
            return product
        raise StopIteration
