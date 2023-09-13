from dataclasses import dataclass, field, InitVar, make_dataclass
from typing import Any


class Thing:
    # Присваивать значение по умолчанию dims=[] опасно, так как атрибут будет ссылаться на одну и ту же область памяти
    # для каждого экземпляра.
    def __init__(self, name, weight, price, calc=True, dims=None):
        self.name = name
        self.weight = weight
        self.price = price
        self.price_per_gram = price / weight if calc else 0  # какой-то вычисляемый атрибут
        self.dims = dims if dims is not None else []

    def __repr__(self):
        return f"Thing: {self.__dict__}"


@dataclass  # может принимать параметры
class ThingData:
    """Класс данных."""
    name: str
    weight: int
    price: float
    # InitVar позволяет передать атрибут в качестве аргумента в __post_init__.
    calc: InitVar[bool] = True
    # Атрибут не будет добавлен в инициализатор, так как его значение вычисляемое.
    price_per_gram: float = field(init=False, default=0)
    # Создание атрибута со значением по умолчанию с изменяемым типом.
    dims: list = field(default_factory=list)

    # При создании экземпляра этот метод вызывается последним.
    # Используется для вычисляемого атрибута.
    def __post_init__(self, calc):
        if calc:
            self.price_per_gram = self.price / self.weight


# Классы Thing и ThingData практически идентичны.
t = Thing("php", 1, 1, False)
td1 = ThingData("python", 2, 2, False)

print(t)  # Thing: {'name': 'php', 'weight': 1, 'price': 1, 'price_per_gram': 0, 'dims': []}
print(td1, "\n")  # ThingData(name='python', weight=2, price=2, price_per_gram=0, dims=[])

td2 = ThingData("java", 3, 3)
td3 = ThingData("java", 3, 3)

# Экземпляры классов данных равны, если равны их атрибуты.
# Это происходит благодаря тому, что декоратор @dataclass переопределил магический метод __eq__.
# @dataclass переопределяет некоторые магические методы, если это не устраивает, то можно эти методы переопределить.
print(td1 == td2)  # False
print(td2 == td3, "\n")  # True


class GoodsMethodsFactory:
    """Вспомогательный класс."""
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    current_uid = 0  # неаннотированный атрибут будет пропускаться @dataclass
    uid: int = field(init=False)  # автоматически увеличивается в __post_init__
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    # Эти атрибуты просто переопределятся.
    price: float = 0
    weight: int | float = 0
    # Атрибут, который формируется методом.
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    def __post_init__(self):
        # Без вызова __post_init__ базового класса атрибут uid не сформируется.
        # Для __init__ вызов базового метода не нужен, так как @dataclass сделает это автоматически.
        super().__post_init__()


b = Book()
print(b, "\n")  # Book(uid=1, price=0, weight=0, title='', author='', measure=[0, 0, 0])


class Car:
    def __init__(self, model: str, max_speed, price: float = 0):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed

    def __repr__(self):
        return f"Car: {self.__dict__}"


# Создание класса данных с помощью make_dataclass().
# Классы Car и CarData практически идентичны.
CarData = make_dataclass(
    cls_name="CarData",
    fields=[("model", str), "max_speed", ("price", float, field(default=0))],
    namespace={"get_max_speed": lambda self: self.max_speed}
)


c = Car("BMW", 256, 4096)
cd = CarData("BMW", 256, 4096)

print(c)  # Car: {'model': 'BMW', 'max_speed': 256, 'price': 4096}
print(cd)  # CarData(model='BMW', max_speed=256, price=4096)
print(cd.get_max_speed())  # 256
