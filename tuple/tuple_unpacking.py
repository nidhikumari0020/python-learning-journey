# tuples/tuple_unpacking.py

fruits = ("apple", "banana", "mango")

# unpacking tuple
a, b, c = fruits
print("a:", a)
print("b:", b)
print("c:", c)

# ignoring values with _
a, _, c = fruits
print("\nIgnoring second element:")
print("a:", a)
print("c:", c)