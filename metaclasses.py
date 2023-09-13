# Метакласс - объект, который позволяет создавать пользовательские типы.
# Метакласс нельзя порождать динамически, он является вершиной, отправной точкой для создания других классов.
# В python метаклассом является объект type.
# В данном примере класс B и класс A идентичны.
class B:
    var = 100


# type(obj) / type(name, bases, dict) – основополагающий тип, конструктор для динамических пользовательских типов.
# obj – объект, тип которого требуется определить.
# name – имя для создаваемого типа, становится атрибутом __name__.
# bases – кортеж с родительскими классами, становится атрибутом __bases__.
# dict – словарь, который будет являться пространством имён для тела класса, становится атрибутом __dict__.
A = type("B", (), {"var": 100})

a = A()
b = B()
print(f"{A.var}, {B.var}\n")  # 100, 100


# Можно использовать функции в качестве метаклассов.
def create_class_point(name, base, attrs):
    attrs.update({"MIN_COORD": 0, "MAX_COORD": 25})
    return type(name, base, attrs)


# При отработке метода create_class_point интерпретатор автоматически передаст аргументы:
# name = "Point", base = () и attrs – содержимое класса Point.
class Point(metaclass=create_class_point):
    def get_coords(self):
        return self.MIN_COORD, self.MAX_COORD


pt = Point()
print(pt.MAX_COORD)  # 25
print(pt.get_coords(), "\n")  # (0, 25)


# Лучше использовать классы в качестве метакласса.
class Meta(type):
    # Используется cls, поскольку на момент вызова инициализатора Meta класс Point уже существует.
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.MIN_COORD = -5
        cls.MAX_COORD = 5

    # # Вместо __init__ можно использовать __new__.
    # def __new__(cls, name, base, attrs):
    #     attrs.update({"MIN_COORD": -5, "MAX_COORD": 5})
    #     return type(name, base, attrs)


class Point(metaclass=Meta):
    def get_coords(self):
        return self.MIN_COORD, self.MAX_COORD


pt = Point()
print(pt.MAX_COORD)  # 5
print(pt.get_coords(), "\n")  # (-5, 5)


# С помощью метаклассов можно упрощать функционал.
class Meta(type):
    def __init__(cls, name, base, attrs):
        cls.class_attrs = attrs
        # Добавление инициализатора в класс Woman.
        cls.__init__ = Meta.create_local_attrs

    def create_local_attrs(self, *args, **kwargs):  # self - ссылка на экземпляр класса Woman.
        """Инициализатор класса Woman."""
        for key, val in self.class_attrs.items():
            self.__dict__[key] = val


class Woman(metaclass=Meta):
    title = "Заголовок"
    content = "Контент"
    photo = "Путь к фото"


w = Woman()
print(w.__dict__)  # {'__module__': '__main__', '__qualname__': 'Woman', 'title': 'Заголовок', 'content': 'Контент', 'photo': 'Путь к фото'}
