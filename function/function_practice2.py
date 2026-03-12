# 1️⃣ Count even numbers in a list
# Type: Loop + Conditional + List processing
def count_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count
print(count_even([1,2,3,4,5,6]))


# 2️⃣ Find smallest number using built-in function
# Type: List + Built-in function (min)
def find_smallest(nums):
    if not nums: 
        return None
    return min(nums)

print(find_smallest([8, 3, 10, 2])) 


# 3️⃣ Find smallest number using loop
# Type: Loop + Comparison + List traversal
def find_smallest(nums):
    if not nums:
        return None
    
    smallest = nums[0]

    for n in nums:
        if n < smallest:
            smallest = n
    return smallest        

print(find_smallest([8, 3, 10, 2]))


# 4️⃣ Reverse a string
# Type: String slicing
def reverse_string(text):
    reversed_s = text[::-1]
    return reversed_s
print(reverse_string("python"))


# 5️⃣ Check palindrome
# Type: String comparison + slicing
def is_palindrome(text):
     return text == text[::-1]
print(is_palindrome("121"))


# 6️⃣ Multiply all numbers in a list
# Type: Loop + accumulator pattern
def multiply_list(nums):
    result = 1
    for n in nums:
        result *= n
    return result

print(multiply_list([1,2,3,4])) 


# 7️⃣ Count vowels in a string
# Type: Loop + Conditional + String membership
def count_vowels(text):
    result = 0 
    vowels = "aeiou"
    for char in text:
        if char.lower() in vowels:
            result += 1
    return result
print(count_vowels("education"))


# 8️⃣ Find average of numbers in list
# Type: Mathematical operation + Built-in functions
def find_average(nums):
    if not nums:
        return 0
    avg = sum(nums) / len(nums)
    return avg
print(find_average([10,20,30]))


# 9️⃣ Count odd numbers in a list
# Type: Loop + Conditional + List processing
def count_odd(nums):
    count = 0
    for n in nums:
        if n % 2 != 0:
            count += 1
    return count
    
print(count_odd([1,2,3,4,5]))


# 🔟 Find largest number in list
# Type: Loop + Comparison
def find_largest(nums):
    if not nums:
        return None
    largest = nums[0]

    for n in nums:
        if n > largest:
            largest = n
    return largest
print(find_largest([4,9,2,7]))


# 1️⃣1️⃣ Sum of digits of a number
# Type: While loop + Mathematical logic
def sum_of_digits(n):
    total = 0 
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total
print(sum_of_digits(1234))


# 1️⃣2️⃣ Count words in a sentence
# Type: String method (split) + length calculation
def count_words(sentence):
    word = sentence.split()
    return len(word)
print(count_words(" i love python"))