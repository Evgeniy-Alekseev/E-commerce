from unittest.mock import patch

import pytest

from src.product import Product, Category
from src.smartphone import Smartphone
from src.custom_exceptions import ZeroQuantityError


def test_category_count(sample_category):
    """Тестирование счетчиков категорий и продуктов"""
    # Сохраняем текущие значения счетчиков
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    # Создаем еще одну категорию для теста
    tv = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром",
        [tv]
    )

    # Проверяем, что счетчики увеличились на правильное значение
    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + 1


def test_product_initialization(sample_products):
    """Тест инициализации продукта"""
    p1, p2, p3 = sample_products

    assert p1.name == "Samsung Galaxy S23 Ultra"
    assert p1.description == "256GB, Серый цвет, 200MP камера"
    assert p1.price == 180000.0
    assert p1.quantity == 5

    assert p2.name == "Iphone 15"
    assert p2.price == 210000.0
    assert p2.quantity == 8

    assert p3.name == "Xiaomi Redmi Note 11"
    assert p3.description == "1024GB, Синий"
    assert p3.price == 31000.0
    assert p3.quantity == 14


def test_category_initialization(sample_category):
    """Тест инициализации категории"""
    assert sample_category.name == "Смартфоны"
    assert "Смартфоны, как средство" in sample_category.description
    # Проверяем через геттер products, который возвращает строку
    products_str = sample_category.products
    assert "Samsung Galaxy S23 Ultra" in products_str
    assert "Iphone 15" in products_str
    assert "Xiaomi Redmi Note 11" in products_str


def test_empty_category():
    """Тест создания пустой категории"""
    empty_category = Category("Пустая", "Нет товаров", [])
    assert empty_category.products == ""  # Геттер возвращает пустую строку
    # Проверяем счетчики (они могут зависеть от порядка выполнения других тестов)
    assert Category.category_count >= 1


def test_product_price_getter(sample_products):
    """Тест геттера цены"""
    product = sample_products[0]
    assert product.price == 180000.0


def test_product_price_setter_positive(sample_products):
    """Тест сеттера цены с положительным значением"""
    product = sample_products[0]
    old_price = product.price
    product.price = 200000.0
    assert product.price == 200000.0


def test_product_price_setter_negative(sample_products):
    """Тест сеттера цены с отрицательным значением"""
    product = sample_products[0]
    old_price = product.price
    product.price = -1000.0
    # Цена не должна измениться
    assert product.price == old_price


def test_product_price_setter_zero(sample_products):
    """Тест сеттера цены с нулевым значением"""
    product = sample_products[0]
    old_price = product.price
    product.price = 0.0
    # Цена не должна измениться
    assert product.price == old_price  # Цена не должна измениться


@patch('builtins.input', return_value='y')
def test_product_price_setter_decrease_confirmed(mock_input, sample_products):
    """Тест сеттера цены со снижением цены (подтверждено)"""
    product = sample_products[0]
    old_price = product.price
    new_price = old_price - 10000.0
    product.price = new_price
    assert product.price == new_price


@patch('builtins.input', return_value='n')
def test_product_price_setter_decrease_cancelled(mock_input, sample_products):
    """Тест сеттера цены со снижением цены (отменено)"""
    product = sample_products[0]
    old_price = product.price
    new_price = old_price - 10000.0
    product.price = new_price
    # Цена не должна измениться, так как отменено
    assert product.price == old_price  # Цена не должна измениться


def test_new_product_creation():
    """Тест создания нового продукта через классметод"""
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 10000.0,
        "quantity": 5
    }

    product = Product.new_product(product_data)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 10000.0
    assert product.quantity == 5


def test_new_product_duplicate_merge():
    """Тест объединения дубликатов при создании продукта"""
    existing_product = Product("Test Product", "Existing Description", 10000.0, 3)
    existing_products = [existing_product]

    new_product_data = {
        "name": "Test Product",
        "description": "New Description",  # Это поле игнорируется при объединении
        "price": 15000.0,  # Большая цена - должна обновиться
        "quantity": 2  # Должна добавиться к существующему количеству
    }

    result = Product.new_product(new_product_data, existing_products)

    # Должен вернуться тот же объект
    assert result is existing_product
    assert result.quantity == 5  # 3 + 2
    assert result.price == 15000.0  # Максимальная цена


def test_new_product_duplicate_merge_lower_price():
    """Тест объединения дубликатов с меньшей ценой"""
    existing_product = Product("Test Product", "Existing Description", 20000.0, 3)
    existing_products = [existing_product]

    new_product_data = {
        "name": "Test Product",
        "description": "New Description",
        "price": 15000.0,  # Меньшая цена - не должна обновиться
        "quantity": 2
    }

    result = Product.new_product(new_product_data, existing_products)

    assert result is existing_product
    assert result.quantity == 5  # 3 + 2
    assert result.price == 20000.0  # Остается старая цена (максимальная)


def test_category_add_product(sample_category, sample_products):
    """Тест добавления продукта в категорию"""
    initial_product_count = Category.product_count

    new_product = Product("New Product", "New Description", 50000.0, 10)
    sample_category.add_product(new_product)

    # Проверяем, что продукт добавился
    products_str = sample_category.products
    assert "New Product" in products_str
    # Проверяем, что счетчик продуктов увеличился
    assert Category.product_count == initial_product_count + 1


def test_category_products_property(sample_category):
    """Тест геттера продуктов категории"""
    products_str = sample_category.products
    expected_lines = [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    ]

    for line in expected_lines:
        assert line in products_str


def test_category_counters():
    """Тест счетчиков категорий и продуктов"""
    # Сохраняем текущие значения
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    # Создаем новую категорию
    products = [
        Product("Product 1", "Description 1", 10000.0, 5),
        Product("Product 2", "Description 2", 20000.0, 3)
    ]

    category = Category("Test Category", "Test Description", products)

    # Проверяем, что счетчики увеличились
    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + 2


def test_new_product_with_none_products_list():
    """Тест создания продукта с None вместо списка продуктов"""
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 10000.0,
        "quantity": 5
    }

    product = Product.new_product(product_data, None)
    assert product.name == "Test Product"


def test_category_products_getter_empty():
    """Тест геттера продуктов для пустой категории"""
    empty_category = Category("Empty", "No products", [])
    assert empty_category.products == ""


def test_product_str_representation(sample_products):
    """Тест строкового представления продукта"""
    product = sample_products[0]
    expected_str = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product) == expected_str


def test_category_str_representation(sample_category):
    """Тест строкового представления категории"""
    expected_str = "Смартфоны, количество продуктов: 27 шт."  # 5 + 8 + 14
    assert str(sample_category) == expected_str


def test_product_addition(sample_products):
    """Тест сложения продуктов"""
    p1, p2, _ = sample_products
    total = p1 + p2
    expected = p1.price * p1.quantity + p2.price * p2.quantity
    assert total == expected


def test_product_addition_with_wrong_type(sample_products):
    """Тест сложения продукта с неправильным типом"""
    p1 = sample_products[0]
    with pytest.raises(TypeError):
        _ = p1 + "not a product"


def test_category_iteration(sample_category):
    """Тест итерации по категории"""
    product_names = [product.name for product in sample_category]
    expected_names = [
        "Samsung Galaxy S23 Ultra",
        "Iphone 15",
        "Xiaomi Redmi Note 11"
    ]
    assert product_names == expected_names


def test_category_empty_iteration(empty_category):
    """Тест итерации по пустой категории"""
    products = list(empty_category)  # Преобразуем итератор в список
    assert products == []


def test_category_multiple_iterations(sample_category):
    """Тест нескольких итераций по одной категории"""
    # Первая итерация
    first_iter = [p.name for p in sample_category]
    # Вторая итерация
    second_iter = [p.name for p in sample_category]
    assert first_iter == second_iter


def test_category_products_property_after_str(sample_category):
    """Тест, что геттер products работает корректно после добавления __str__"""
    products_str = sample_category.products
    expected_lines = [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    ]
    for line in expected_lines:
        assert line in products_str


def test_product_addition_same_type():
    """Тест сложения продуктов одного типа"""
    p1 = Product("Product 1", "Description 1", 100.0, 2)
    p2 = Product("Product 2", "Description 2", 50.0, 3)
    result = p1 + p2
    expected = (100.0 * 2) + (50.0 * 3)  # 200 + 150 = 350
    assert result == expected


def test_product_addition_different_types_error():
    """Тест сложения продуктов разных типов вызывает TypeError"""
    p1 = Product("Product 1", "Description 1", 100.0, 2)
    s1 = Smartphone("Smartphone 1", "Description", 50000.0, 1, "High", "Model X", "128GB", "Black")

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = p1 + s1


def test_category_add_product_valid_product():
    """Тест добавления валидного продукта в категорию"""
    category = Category("Test Category", "Test Description", [])
    product = Product("Test Product", "Test Description", 100.0, 5)

    initial_product_count = Category.product_count
    category.add_product(product)

    assert len(category._Category__products) == 1
    assert category._Category__products[0] is product
    assert Category.product_count == initial_product_count + 1

def test_category_add_product_invalid_type():
    """Тест добавления невалидного объекта в категорию вызывает TypeError"""
    category = Category("Test Category", "Test Description", [])

    initial_product_count = Category.product_count
    with pytest.raises(TypeError, match="Можно добавлять только объекты Product или его наследников"):
        category.add_product("Not a product")

    # Убедиться, что продукт не был добавлен
    assert len(category._Category__products) == 0
    assert Category.product_count == initial_product_count


def test_category_add_product_invalid_type_number():
    """Тест добавления числа в категорию вызывает TypeError"""
    category = Category("Test Category", "Test Description", [])

    initial_product_count = Category.product_count
    with pytest.raises(TypeError, match="Можно добавлять только объекты Product или его наследников"):
        category.add_product(123)

    # Убедиться, что продукт не был добавлен
    assert len(category._Category__products) == 0
    assert Category.product_count == initial_product_count

def test_category_add_product_invalid_type_none():
    """Тест добавления None в категорию вызывает TypeError"""
    category = Category("Test Category", "Test Description", [])

    initial_product_count = Category.product_count
    with pytest.raises(TypeError, match="Можно добавлять только объекты Product или его наследников"):
        category.add_product(None)

    # Убедиться, что продукт не был добавлен
    assert len(category._Category__products) == 0
    assert Category.product_count == initial_product_count

    def test_product_init_zero_quantity():
        """Тест инициализации продукта с нулевым количеством вызывает ValueError"""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("Test Product", "Test Description", 100.0, 0)

    def test_product_init_negative_quantity():
        """Тест инициализации продукта с отрицательным количеством вызывает ValueError"""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("Test Product", "Test Description", 100.0, -5)

    def test_category_add_product_zero_quantity(monkeypatch):
        """Тест добавления продукта с нулевым количеством в категорию"""
        # Перехватываем вывод в stdout
        captured_output = []

        def mock_print(*args):
            captured_output.append(" ".join(map(str, args)))

        monkeypatch.setattr('builtins.print', mock_print)

        category = Category("Test Category", "Test Description", [])

        # Создаем фиктивный продукт с нулевым количеством для теста add_product
        class MockProduct:
            def __init__(self, name, description, price, quantity):
                self.name = name
                self.description = description
                self.price = price
                self.quantity = quantity

        mock_product = MockProduct("Mock Product", "Mock Description", 50.0, 0)

        # Вызываем метод add_product
        category.add_product(mock_product)

        # Проверяем вывод
        output = " ".join(captured_output)
        assert "Ошибка добавления товара: Товар с нулевым количеством не может быть добавлен" in output
        assert "Обработка добавления товара завершена" in output
        # Проверяем, что продукт не был добавлен
        assert len(category._Category__products) == 0

    def test_category_add_product_valid_product(monkeypatch):
        """Тест добавления валидного продукта в категорию"""
        # Перехватываем вывод в stdout
        captured_output = []

        def mock_print(*args):
            captured_output.append(" ".join(map(str, args)))

        monkeypatch.setattr('builtins.print', mock_print)

        category = Category("Test Category", "Test Description", [])
        product = Product("Valid Product", "Valid Description", 150.0, 3)

        # Вызываем метод add_product
        category.add_product(product)

        # Проверяем вывод
        output = " ".join(captured_output)
        assert "Товар добавлен" in output
        assert "Обработка добавления товара завершена" in output
        # Проверяем, что продукт был добавлен
        assert len(category._Category__products) == 1
        assert category._Category__products[0] is product

    def test_category_average_price_empty():
        """Тест метода average_price для пустой категории"""
        empty_category = Category("Empty Category", "No products", [])
        avg_price = empty_category.middle_price()
        assert avg_price == 0.0

    def test_category_average_price_non_empty():
        """Тест метода average_price для категории с продуктами"""
        products = [
            Product("Product 1", "Description 1", 100.0, 5),
            Product("Product 2", "Description 2", 200.0, 3),
            Product("Product 3", "Description 3", 150.0, 2)
        ]
        category = Category("Test Category", "Test Description", products)
        avg_price = category.middle_price()
        expected_avg = (100.0 + 200.0 + 150.0) / 3  # 150.0
        assert avg_price == expected_avg

    def test_category_average_price_single_product():
        """Тест метода average_price для категории с одним продуктом"""
        product = Product("Single Product", "Single Description", 75.5, 10)
        category = Category("Single Product Category", "One product", [product])
        avg_price = category.middle_price()
        assert avg_price == 75.5