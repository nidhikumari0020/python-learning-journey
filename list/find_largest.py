# lists/find_largest.py

numbers = [5, 12, 7, 18, 3]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)