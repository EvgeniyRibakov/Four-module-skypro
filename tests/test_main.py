import pytest

from src.main import Category, Product


@pytest.fixture()
def product_1():
    return Product(
        name="Samsung Galaxy S22 Snapdragon 8 gen 1",
        price=35000.0,
        description="amaled display, 8/256Gb , 50,24,12MP ,Color-Black",
        quantity=3,
    )


def test_product_1(product_1):
    assert product_1.name == "Samsung Galaxy S22 Snapdragon 8 gen 1"
    assert product_1.price == 35000.0
    assert product_1.description == "amaled display, 8/256Gb , 50,24,12MP ,Color-Black"
    assert product_1.quantity == 3


@pytest.fixture()
def product_2():
    return Product(
        name="Honor 200 lite",
        price=30000.0,
        description="amaled display, 8/256Gb , 200MP ,Color-white",
        quantity=6,
    )


def test_product_2(product_2):
    assert product_2.name == "Honor 200 lite"
    assert product_2.price == 30000.0
    assert product_2.description == "amaled display, 8/256Gb , 200MP ,Color-white"
    assert product_2.quantity == 6


@pytest.fixture()
def product_3():
    return Product(
        name="Iphone 14 pro max",
        price=35000.0,
        description="amaled display, 8/512Gb , 50Mp ,Color-Purple",
        quantity=5,
    )


def test_product_3(product_3):
    assert product_3.name == "Iphone 14 pro max"
    assert product_3.price == 35000.0
    assert product_3.description == "amaled display, 8/512Gb , 50Mp ,Color-Purple"
    assert product_3.quantity == 5


@pytest.fixture()
def category_1():
    return Category(
        name="Телефоны",
        description="Самые топовые делефоны до 35000",
        products=("Iphone 14 pro max", "Iphone 14 pro max", "Honor 200 lite"),
    )


def test_category_1(category_1):
    assert category_1.name == "Телефоны"
    assert category_1.description == "Самые топовые делефоны до 35000"
    assert category_1.products == (
        "Iphone 14 pro max",
        "Iphone 14 pro max",
        "Honor 200 lite",
    )
