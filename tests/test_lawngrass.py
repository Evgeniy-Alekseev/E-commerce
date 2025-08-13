import pytest

from src.lawngrass import LawnGrass
from src.product import Category


def test_lawn_grass_initialization(sample_lawn_grass):
    """Тест инициализации газонной травы"""
    assert sample_lawn_grass.name == "Premium Lawn Grass"
    assert sample_lawn_grass.description == "High quality lawn grass seeds"
    assert sample_lawn_grass.price == 5000.0
    assert sample_lawn_grass.quantity == 10
    assert sample_lawn_grass.country == "Netherlands"
    assert sample_lawn_grass.germination_period == "7-14 days"
    assert sample_lawn_grass.color == "Green"


def test_lawn_grass_addition_same_type(sample_lawn_grass, another_lawn_grass):
    """Тест сложения двух видов газонной травы"""
    total = sample_lawn_grass + another_lawn_grass
    expected = (sample_lawn_grass.price * sample_lawn_grass.quantity) + \
               (another_lawn_grass.price * another_lawn_grass.quantity)
    assert total == expected


def test_lawn_grass_addition_different_type_error(sample_lawn_grass, sample_smartphone):
    """Тест сложения газонной травы с другим типом вызывает TypeError"""
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = sample_lawn_grass + sample_smartphone


def test_lawn_grass_inheritance(sample_lawn_grass):
    """Тест проверки наследования от Product"""
    assert isinstance(sample_lawn_grass, LawnGrass)
    assert isinstance(sample_lawn_grass, object) # Все классы наследуются от object
    # Проверяем, что у экземпляра LawnGrass есть все атрибуты Product
    assert hasattr(sample_lawn_grass, 'name')
    assert hasattr(sample_lawn_grass, 'description')
    assert hasattr(sample_lawn_grass, 'price')
    assert hasattr(sample_lawn_grass, 'quantity')


def test_category_add_product_valid_lawn_grass():
    """Тест добавления валидной газонной травы в категорию"""
    category = Category("Garden", "Garden products", [])
    lawn_grass = LawnGrass("Grass Seed", "Premium quality", 50.0, 100, "Netherlands", "7 days", "Green")

    initial_product_count = Category.product_count
    category.add_product(lawn_grass)

    assert len(category._Category__products) == 1
    assert category._Category__products[0] is lawn_grass
    assert Category.product_count == initial_product_count + 1
