class Point:
    attr = 5

    @classmethod
    def func(cls, x):
        return cls.attr + x

    @staticmethod
    def func2(x):
        # Внутри статического метода можно обращаться к атрибутам класса через его имя Point.attr, однако так делать не
        # рекомендуется.
        return Point.attr + x


print(Point.func(1))
print(Point.func2(2))

a = Point()
print(a.func(3))
print(a.func2(4))
