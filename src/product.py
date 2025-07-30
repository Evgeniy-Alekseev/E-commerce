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


    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None):
        """
        Создает новый продукт из словаря данных
        :param product_data: Словарь с данными продукта
        :param products_list: Список существующих продуктов для проверки дубликатов
        :return: Экземпляр класса Product
        """
        if products_list is None:
            products_list = []

        # Проверка на дубликаты
        for existing_product in products_list:
            if existing_product.name == product_data['name']:
                # Объединяем количество
                existing_product.quantity += product_data['quantity']
                # Выбираем максимальную цену
                if existing_product.price < product_data['price']:
                    existing_product.price = product_data['price']
                return existing_product

        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для цены с проверками"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirm = input(f"Цена снижается с {self.__price} до {new_price}. Подтвердите (y/n): ")
            if confirm.lower() != 'y':
                print("Изменение цены отменено")
                return

        self.__price = new_price

class Category:
    """Класс для представления категорий товаров."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """
        Инициализация категории
        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов в категории
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для списка продуктов в виде строки"""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str.strip()