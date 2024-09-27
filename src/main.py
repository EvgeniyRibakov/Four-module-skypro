class Product:
    __price = float

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> float:
        """Геттер атрибута price"""
        return self.__price

    @price.setter
    def price(self, price: int) -> None:
        """Сеттер атрибута price"""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    @classmethod
    def new_product(cls, params: dict) -> "Product":
        """Создаёт новый объект класса Product"""
        new_prod = cls(params["name"], params["description"], params["price"], params["quantity"])
        return new_prod


class Category:
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет новый объект в список атрибута __products"""
        self.__products.append(product)
        self.product_count += 1

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    @property
    def products(self) -> list:
        """Публичная версия атрибута __products, выдающая список строк"""
        product_list = []
        for product in self.__products:
            product_list.append(str(product))
        return product_list


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(Category.category_count)
    print(Category.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и "
                         "помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)
    print(Category.category_count)
    print(Category.product_count)
