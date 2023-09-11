class Point:
    x = 0
    y = 0

    def func():
        print("method without self parameter")

    def func2(self):
        print("method with self parameter")


# Point.__dict__ : {'__module__': '__main__', 'x': 0, 'y': 0, 'func': <function Point.func at 0x0000025D0443FE20>,
# 'func2': <function Point.func2 at 0x0000025D0443FEB0>, '__dict__': <attribute '__dict__' of 'Point' objects>,
# '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None}
print(f"Point.__dict__ : {Point.__dict__}")

a = Point()
print(f"\na.__dict__ : {a.__dict__}")  # a.__dict__ : {}
print(f"a.x = {a.x}, a.y = {a.y}")  # a.x = 0, a.y = 0

a.x = 10
print(f"\na.__dict__ : {a.__dict__}")  # a.__dict__ : {'x': 10}
print(f"a.x = {a.x}, a.y = {a.y}")  # a.x = 10, a.y = 0


Point.new_attr = 5
print(f"\na.new_attr = {a.new_attr}\n")  # a.new_attr = 5

Point.func()
try:
    a.func()
except TypeError as e:
    print(f"{e.__class__}: {e}")

print()

try:
    Point.func2()
except TypeError as e:
    print(f"{e.__class__}: {e}")
a.func2()

Point.func2(Point())
