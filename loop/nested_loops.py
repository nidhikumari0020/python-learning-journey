# Print a pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Iterating a 2D list
matrix = [[1,2,3], [4,5,6]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()