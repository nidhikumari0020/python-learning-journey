# lists/remove_duplicates.py

numbers = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", numbers)

# convert to set and back to list
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)