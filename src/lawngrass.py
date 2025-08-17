from src.product import Product


class LawnGrass(Product):
    """
    Класс для представления газонной травы, наследуется от Product.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """
        Инициализация газонной травы.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество на складе
        :param country: Страна-производитель
        :param germination_period: Срок прорастания
        :param color: Цвет травы
        """
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __add__(self, other):
        """
        Сложение двух видов газонной травы по формуле: цена * количество + цена * количество
        :param other: Другой объект LawnGrass
        :return: Сумма произведений цены на количество
        """
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        # Вызываем метод __add__ родительского класса
        return super().__add__(other)