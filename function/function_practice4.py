# Even or Odd Checker

def check_even_odd(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(3))
print(check_even_odd(2))

# Sum of Two Numbers

def sum_numbers(a,b):
    return a + b
print(sum_numbers(5,7))

# Find the Largest Number

def find_largest(a,b):
    if a>b:
        return a
    elif a==b:
        return "equal"
    else:
        return b
print(find_largest(4,6))
print(find_largest(4,4))

# Square of a Number

def square(n):
    return n*n
print(square(5))

# Factorial Calculator

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result
print(factorial(5))

# Count Characters in a String

def count_chars(text):
    return len(text)
print(count_chars("hello"))

# Palindrome Checker

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
print(is_palindrome("madam"))

# Average of Three Numbers

def average(a,b,c):
    result = (a+b+c)/3
    return result
print(average(3,6,9))

# Positive, Negative, or Zero

def check_number(n):
    if n>0:
        return "Positive"
    elif n==0:
        return "Zero"
    else:
        return "Negative"

print(check_number(-3))
print(check_number(6))
print(check_number(0))

# Sum of Numbers from 1 to N

def sum_to_n(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
print(sum_to_n(5))

# Reverse a Number

def reverse_number(n):
    num = str(n)
    rev = num[::-1]
    return int(rev)
print(reverse_number(1234))


