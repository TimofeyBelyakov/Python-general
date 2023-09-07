numbers = [1, 2, 3]

i = iter(numbers)  # итератор
print(type(i))
print(next(i))
print(next(i))
print(next(i))
try:
    print(next(i))
except StopIteration as err:
    print(f"Error: {err.__class__}")

# То же самое происходит при переборе итерируемых объектов в цикле.
for item in numbers:
    print(item)
