class Color:
    def __init__(self, color):
        self.__color = color

    def set(self, color):
        self.__color = color

    def get(self):
        return self.__color

    # Такой код позволяет работать с приватным атрибутом __color как через .color, так и через геттер и сеттер.
    # Это дублирование функционала.
    color = property(get, set)


exm = Color("red")
# Атрибут, созданный таким образом будет иметь приоритет при вызове выше, чем у любого другого атрибута с таким же
# именем. То есть при вызове атрибута через экземпляр значение будет искаться не в локальном пространстве имён
# экземпляра, а в пространстве класса.
exm.color = "yellow"
exm.__dict__["color"] = "black"
print(exm.color)
print(exm.__dict__, "\n")


class Color:
    def __init__(self, color):
        self.__color = color

    # Данный декоратор может быть использован для определения методов в классе, которые действуют как атрибуты.
    # Первым обязательно идёт геттер.
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


c = Color("green")
c.color = "pink"
print(c.color)
