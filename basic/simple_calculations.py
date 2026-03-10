# basics/simple_calculations.py

# take two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# addition
add = num1 + num2
print("Sum:", add)

# subtraction
sub = num1 - num2
print("Difference:", sub)

# multiplication
mul = num1 * num2
print("Product:", mul)

# division
if num2 != 0:
    div = num1 / num2
    print("Quotient:", div)
else:
    print("Cannot divide by zero!")