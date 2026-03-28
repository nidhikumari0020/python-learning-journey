# student.py

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks  # list of marks

    def get_average(self):
        avg = sum(self.marks) / len(self.marks)
        return avg

    def is_pass(self):
        if self.get_average() >= 40:
            return True
        else:
            return False

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("Average:", self.get_average())
        print("Pass:", self.is_pass())
        print("------")


# creating objects
s1 = Student("Nidhi", 18, [80, 75, 90])
s2 = Student("Rahul", 19, [30, 35, 25])

# using methods
s1.display()
s2.display()