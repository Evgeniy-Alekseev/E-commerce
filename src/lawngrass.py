from src.product import Product


class LawnGrass(Product):
    """
    Класс для представления газонной травы, наследуется от Product
    """

    name: str
    description: str
    price: float
    quantity: int
    country: str
    germination_period: str
    color: str


    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """
        Инициализация газонной травы
        :param country: Страна-производитель
        :param germination_period: Срок прорастания (в днях)
        :param color: Цвет травы
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

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