# Celsius to Fahrenheit

def celsius_to_fahrenheit(c):
    celsius = (c * 9/5) + 32
    return celsius
print(celsius_to_fahrenheit(25))

#  Simple Calculator

def calculator(a, b, op,):

    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a/b
    else:
        return "invalid operation"
print(calculator(10,5,"+"))
print(calculator(10,5,"-"))
print(calculator(10,5,"*"))
print(calculator(10,5,"/"))
print(calculator(10,5,"="))    

