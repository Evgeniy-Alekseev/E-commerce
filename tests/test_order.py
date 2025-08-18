from src.product import Product
from src.order import Order


def test_order_initialization():
    """Тест инициализации заказа"""
    product = Product("Test Product", "Test Description", 100.0, 5)
    order = Order(product, 3)

    assert order.product == product
    assert order.quantity == 3
    assert order.total_cost == 300.0  # 100.0 * 3
    assert "Заказ" in order.name
    assert "Заказ товара" in order.description


def test_order_with_different_quantities():
    """Тест заказа с разными количествами"""
    product = Product("Expensive Product", "Test Description", 500.0, 10)

    # Заказ 1 единицы
    order1 = Order(product, 1)
    assert order1.quantity == 1
    assert order1.total_cost == 500.0

    # Заказ 5 единиц
    order5 = Order(product, 5)
    assert order5.quantity == 5
    assert order5.total_cost == 2500.0


def test_order_attributes():
    """Тест атрибутов заказа"""
    product = Product("Test Product", "Test Description", 75.5, 20)
    order = Order(product, 2)

    # Проверяем, что все атрибуты присутствуют
    assert hasattr(order, 'product')
    assert hasattr(order, 'quantity')
    assert hasattr(order, 'total_cost')
    assert hasattr(order, 'name')  # Унаследовано от AbstractEntity
    assert hasattr(order, 'description')  # Унаследовано от AbstractEntity