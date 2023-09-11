class Integer:
    """Дескриптор."""

    # self – ссылка на экземпляр, owner – ссылка на класс Point3D, name – имя переменной экземпляра.
    def __set_name__(self, owner, name):
        self.name = "_" + name

    # self – ссылка на экземпляр, instance – ссылка на класс Point3D, owner – ссылка на класс Integer.
    def __get__(self, instance, owner):
        print(f"get {self.name}")
        return getattr(instance, self.name)

    # self – ссылка на экземпляр, instance – ссылка на класс Point3D, value - присваиваемое значение.
    def __set__(self, instance, value):
        print(f"set {self.name} = {value}")
        setattr(instance, self.name, value)


class Point3D:
    # Использование декоратора @property может быть громоздким. Если в классе несколько атрибутов, то для каждого
    # необходимо будет создавать объекты property. Каждому по геттеру, сеттеру и делитеру. Причём функционал для
    # методов будет одинаковым.
    # Для решения этой проблемы можно создать дескриптор.
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt = Point3D(1, 2, 3)
pt.x = 5
pt.z = 88

print()
print(pt.y)  # set _x = 5
print(pt.z)  # set _z = 88

print()
print(pt.__dict__)  # {'_x': 5, '_y': 2, '_z': 88}
