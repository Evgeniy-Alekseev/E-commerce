from src.product import Product


class LawnGrass(Product):
    """
    Класс для газонной травы, наследуется от Product
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
        Сложение двух продуктов по формуле: цена * количество + цена * количество
        :param other: Другой объект
        :return: Сумма произведений цены на количество
        """
        if type(other) is LawnGrass:
            raise TypeError("Можно складывать только объекты LawnGrass")
        return self.price * self.quantity + other.price * other.quantity