import math
from functools import wraps


def func_decorator(func):
    # Функция обёртка.
    def wrapper(*args, **kwargs):
        print("----before----")
        res = func(*args, **kwargs)
        print("----after----")
        return res
    return wrapper


def some_func(title):
    res = "title: " + str(title)
    print(res)
    return res


# Благодаря декоратору можно расширить возможности функции.
# В основе декораторов лежит замыкание.
f = func_decorator(some_func)
res = f("python")
print()


# Декорировать функцию можно проще.
@func_decorator
def some_func2(title):
    res = "title: " + str(title)
    print(res)
    return res


res2 = some_func2("java")
print()


# В декоратор можно передавать параметры.
def decorator(dx=0.01):
    def diff(func):
        # Данный декоратор нужен для того, чтобы имя и описание брались у передаваемой функции func.
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            # Расчёт производной в точке.
            return (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
        return wrapper
    return diff


@decorator(dx=0.00001)
def sin_x(x):
    """Функция для вычисления производной синуса."""
    return math.sin(x)


print(sin_x(4))
# Теперь при вызове имени и описании функции значения будут взяты у sin_x. Иначе были бы взяты у wrapper.
print(f"Имя функции: {sin_x.__name__}")
print(f"Описание функции: {sin_x.__doc__}")