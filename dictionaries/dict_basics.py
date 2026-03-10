# dictionaries/dict_basics.py

# creating a dictionary
student = {
    "name": "Nidhi",
    "age": 21,
    "course": "BCA"
}

print("Original dictionary:", student)

# accessing elements
print("Name:", student["name"])
print("Age:", student.get("age"))

# updating values
student["age"] = 22
student["city"] = "Mumbai"  # adding new key
print("Updated dictionary:", student)

# removing a key
student.pop("course")
print("After removing 'course':", student)