# basic.py

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi, I am", self.name)


# creating objects
s1 = Student("Nidhi", 18)
s2 = Student("Rahul", 20)

# accessing attributes
print(s1.name)
print(s2.age)

# calling method
s1.greet()
s2.greet()