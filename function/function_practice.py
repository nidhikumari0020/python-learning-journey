# 1️ Simple function - print something
def hello():
    print("HELLO WORLD")
hello()

# 2️ Simple function with custom message
def greet():
    print("Hello Nidhi")  
greet()

# 3️ Function with parameters & return value (Addition)
def add(a, b):
    return a + b
print(add(3,5))

# 4️ Function with parameter & mathematical operation (Square)
def square(a):
    return a*a
print(square(6))

# 5️ Function with conditional logic (Even/Odd check)
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(4))
print(check_even_odd(7))  

# 6️ Function with loop & factorial calculation
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5)) 

# 7️ Function using built-in function (Find largest number in list)
def find_largest(nums):
    return max(nums)
print(find_largest([4, 9, 2, 7]))

# 8️ Function with mathematical operation (Double a number)
def double_number(n):
    return n*2
print(double_number(5))

# 9️ Function with conditional logic (Positive / Negative check)
def check_number(n):
    if n<0:
        return "negative"
    else:
        return "positive"
print(check_number(-3))

# 10 Function using built-in function (String length)
def string_length(text):
    return len(text)
print(string_length("nidhi"))

# 1️1️ Function with loop & sum calculation (1 to n)
def sum_n(n):
    total = 0
    for i in range(1,n+1):
        total+=i
    return total
print(sum_n(15))

# 1️2️ Function with mathematical operation (Square)
def square(n):
    return n*n
print(square(7))

# 1️3️ Function using string method (Convert to uppercase)
def to_upper(text):
    return text.upper()
print(to_upper("python"))

# 1️4️ Function with loop & accumulator (Sum of list elements)
def list_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total
print(list_sum([1, 2, 3, 4]))  

# 1️5️ Function with string indexing (First character)
def first_char(text):
    if not text:
        return ""
    return text[0]
print(first_char("hello"))

# 1️6️ Pythonic version - string slicing (First character)
def first_char(text):
    return text[:1]
print(first_char("hello")) 

# 1️7️ Function with conditional check (Empty string or not)
def check_empty(text):
    if not text:
        return "empty"
    else:
        return "not empty"
print(check_empty(""))

# 1️8️ Alternate version - explicit comparison (Empty string)
def check_empty(text):
    if text == "":
        return "Empty"
    return "Not Empty"
print(check_empty(""))

# 1️9️ Function with mathematical operation (Cube of a number)
def cube(n):
    return n*n*n
print(cube(3))