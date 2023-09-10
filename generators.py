numbers = [1, 2, 3]

# Формирование генератора.
# По сути, сейчас генератор можно воспринимать как обычный итератор.
gen = (number for number in numbers)
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
try:
    print(next(gen))
except StopIteration as err:
    print(f"Error: {err.__class__}")


def func_gen():
    """Функция генератор."""

    global numbers
    for x in numbers:
        yield x
        print("after yield")


gen = func_gen()
print(next(gen))
print(next(gen))
print(next(gen))
try:
    print(next(gen))
except StopIteration as err:
    print(f"Error: {err.__class__}")
