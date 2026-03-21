# Write a function to print numbers from 1 to n

# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i)
# print(print_numbers(10))

# Write a function to sum numbers from 1 to n

# def sum_num(n):
#     total = 0
#     for i in range(1,n+1):
#         total+=i
#     return total
# print(sum_num(10))

# Write a function to find factorial of a number

# def factorial_num(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result
# print(factorial_num(5))

# Write a function to check even or odd

# def check_num(n):
#      if n%2==0:
#           return "EVEN"
#      else:
#           return "ODD"
# print(check_num(10))


# Write a function to find largest of 3 numbers    

# def find_largest(a, b, c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
# print(find_largest(3,6,9))


# list in single line

# def list_number(list):
#     for item in list:
#         print(item, end=" ")
# list_number([1,24,45,67])

# convert usd to inr

# def covert(usd_value):
#     result = usd_value * 91
#     return result
# print(covert(3))

# Count number of digits in a number

# Reverse a number

# Check palindrome number

# Find sum of digits

# Find product of digits
    
# def calc_sum(n):
#     if (n==0):
#         return 0
#     print(n)
#     return calc_sum(n - 1) + n
# print(calc_sum(5))

def print_list(list, idx=0):
    if(idx==len(list)):
        return
    
    print(list[idx])
    print_list(list,idx+1)

fruit = ["mango","orange","apple"]
print_list(fruit)

# print(print_list([1,2,3,4,5]))  