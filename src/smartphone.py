from src.product import Product


class Smartphone(Product):
    """
    Класс для смартфонов, наследуется от Product
    """

    name: str
    description: str
    price: float
    quantity: int
    efficiency: str
    model: str
    memory: int
    color: str


    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """
        Инициализация смартфона
        :param efficiency: Производительность (в условных единицах)
        :param model: Модель смартфона
        :param memory: Объем встроенной памяти (в ГБ)
        :param color: Цвет смартфона
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """
        Сложение двух продуктов по формуле: цена * количество + цена * количество
        :param other: Другой объект
        :return: Сумма произведений цены на количество
        """
        if type(other) is Smartphone:
            raise TypeError("Можно складывать только объекты Smartphone")
        return self.price * self.quantity + other.price * other.quantity