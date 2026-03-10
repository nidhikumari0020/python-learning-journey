# dictionaries/dict_loop.py

student = {
    "name": "Nidhi",
    "age": 21,
    "course": "BCA"
}

# loop through keys
print("Keys:")
for key in student:
    print(key)

# loop through values
print("\nValues:")
for value in student.values():
    print(value)

# loop through key-value pairs
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")