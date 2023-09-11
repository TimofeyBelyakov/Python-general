numbers = [1, 2, 3]

# Формирование генератора.
# По сути, сейчас генератор можно воспринимать как обычный итератор.
gen = (number for number in numbers)
print(type(gen))  # <class 'generator'>
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
try:
    print(next(gen))
except StopIteration as e:
    print(f"{e.__class__}\n")  # Error: <class 'StopIteration'>


def func_gen():
    """Функция генератор."""

    global numbers
    for x in numbers:
        yield x
        print("after yield")


gen = func_gen()
print(next(gen))  # 1
print(next(gen))  # after yield \n 2
print(next(gen))  # after yield \n 3
try:
    print(next(gen))
except StopIteration as e:
    print(f"{e.__class__}")  # after yield \n <class 'StopIteration'>
