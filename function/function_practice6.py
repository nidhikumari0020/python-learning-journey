# sum of any number of arguement

def sum_all(*number):
  return sum(number)
print(sum_all(1,2,3,4,5))

# altrenate 
def sum_of_digits(n):
    total = 0 
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total
print(sum_of_digits(1234))

# Build profile

def build_profile(**info):
   for key , value in info.items():
      print(f"{key.capitalize()} : {value}")

build_profile(name = "nidhi", age = 20, city = "delhi" )     

# factorial recursive

def factorial(n):
   if(n==1 or n==0):
      return 1
   else:
      return factorial(n-1) * n
print(factorial(5))

# fabonacci series - recursive

def fibonacci(n):
   if n==0:
      return 0
   if n==1:
      return 1
   
   return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))

# Filter Even Numbers — Lambda

def filter_even_num(num):
   even_number = list(filter(lambda n: n%2==0 , num))
   return even_number
print(filter_even_num([1,2,5,7,3,2,4,6]))

# apply discount

def apply_discount(price, discount=10):
   price_discount = map(lambda p: p *(1 - discount/100),price)
   return list(price_discount)

print(apply_discount([20,50]))

#  Grade Classifier - A (90+), B (80–89), C (70–79), D (60–69), F (below 60).

def grade(marks):
   if marks >= 90:
      return "A"
   elif marks >= 80:
      return "B"
   elif marks >= 70:
      return "C"
   elif marks >= 60:
      return "D"
   else:
      return "F"
print(grade(95))
print(grade(15))
print(grade(85))
print(grade(67))
print(grade(77))
print(grade(113))

#  Nested: Power Function

def make_power(exp):
   def power(number):
      return number ** exp
   return power

square = make_power(2)
print(square(4))

cube = make_power(3)
print(cube(3))
