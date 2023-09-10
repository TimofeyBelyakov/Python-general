class Point:
    x = 0
    y = 0

    def func():
        print("method without self parameter")

    def func2(self):
        print("method with self parameter")


print(f"Point.__dict__ : {Point.__dict__}")

a = Point()
print(f"\na.__dict__ : {a.__dict__}")
print(f"a.x = {a.x}, a.y = {a.y}")

a.x = 10
print(f"\na.__dict__ : {a.__dict__}")
print(f"a.x = {a.x}, a.y = {a.y}")


Point.new_attr = 5
print(f"\na.new_attr = {a.new_attr}\n")

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
