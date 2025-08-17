from src.product import Product


class Smartphone(Product):
    """
    Класс для представления смартфона, наследуется от Product.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: str, color: str):
        """
        Инициализация смартфона.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество на складе
        :param efficiency: Производительность
        :param model: Модель смартфона
        :param memory: Объем встроенной памяти
        :param color: Цвет смартфона
        """
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __add__(self, other):
        """
        Сложение двух смартфонов по формуле: цена * количество + цена * количество
        :param other: Другой объект Smartphone
        :return: Сумма произведений цены на количество
        """
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        # Вызываем метод __add__ родительского класса
        return super().__add__(other)