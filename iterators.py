numbers = [1, 2, 3]

i = iter(numbers)  # итератор
print(type(i))  # <class 'list_iterator'>
print(next(i))  # 1
print(next(i))  # 2
print(next(i))  # 3
try:
    print(next(i))
except StopIteration as err:
    print(f"Error: {err.__class__}\n")  # Error: <class 'StopIteration'>

# То же самое происходит при переборе итерируемых объектов в цикле.
for item in numbers:
    print(item)
