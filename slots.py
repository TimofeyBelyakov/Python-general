class Point:
    # Коллекция __slots__ необходима для задания фиксированного количества атрибутов класса.
    # Как правило, коллекция __slots__ задаётся в виде кортежа. Внутри самого класса можно создавать атрибуты, даже если
    # их нет в __slots__, потому что __slots__ накладывает ограничения только на локальные атрибуты, а не на атрибуты
    # класса.
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(10, 20)
try:
    pt.z = 30
except AttributeError as e:
    print(f"{e.__class__}: {e}\n")  # <class 'AttributeError'>: 'Point' object has no attribute 'z'

pt2 = Point2(-10, -20)

# __slots__ способен снизить занимаемую экземплярами память. Если задан __slots__, то коллекция __dict__ не формируется.
print(f"size pt: {pt.__sizeof__()}")  # size pt: 32
print(f"size pt2: {pt2.__sizeof__() + pt2.__dict__.__sizeof__()}\n")  # size pt2: 120


class Point:
    __slots__ = ("x", "y", "__len")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__len = (x * x + y * y) ** 0.5

    @property  # __slots__ можно использовать с @property
    def len(self):
        return self.__len

    @len.setter
    def len(self, other):
        self.__len = other


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


pt = Point(100, 200)
print(pt.len)  # 223.60679774997897
pt.len = 10
print(pt.len, "\n")  # 10

pt3D = Point3D(1, 2, 3)
# Если в родительском классе задан __slots__, то при наследовании его свойства не передаются.
# То есть, в экземпляры дочернего класса можно добавлять новые локальные атрибуты.
pt3D.new_attr = "text"
print(pt3D.new_attr, "\n")  # text

# Однако атрибуты родительского класса из __slots__ в коллекцию __dict__ экземпляра дочернего класса добавляться не
# будут, даже если вручную создать атрибут с таким же именем.
pt3D.x = 100
print(pt3D.x)  # 100
print(f"dict pt3D: {pt3D.__dict__}\n")  # dict pt3D: {'z': 3, 'new_attr': 'text'}


class Point:
    __slots__ = ("x", "y", "__len")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point):
    # Если в дочернем классе создать собственную коллекцию __slots__, то она расширит родительскую.
    __slots__ = "z",

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


pt3D = Point3D(10, 11, 12)
print(f"{pt3D.x}, {pt3D.y}, {pt3D.z}")  # 10, 11, 12
print(pt3D.__slots__)  # ('z',)
