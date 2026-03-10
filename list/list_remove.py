# lists/list_remove.py

fruits = ["apple", "banana", "mango", "orange"]
print("Original list:", fruits)

# remove an item
fruits.remove("banana")
print("After removing 'banana':", fruits)

# remove last item
fruits.pop()
print("After popping last item:", fruits)

# remove all items
fruits.clear()
print("After clearing list:", fruits)