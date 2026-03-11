def factorial_with_steps(n):
    if n < 0:
        return "Please enter a positive number."
    if n == 0 or n == 1:
        print(f"{n}! = 1")
        return 1
    
    # Numbers ki list banana (e.g., [5, 4, 3, 2, 1])
    steps = [str(i) for i in range(n, 0, -1)]
    
    # Saare numbers ko ' × ' ke saath jodna
    sequence = " × ".join(steps)
    
    # Result calculate karna
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    print(f"{n}! = {sequence} = {result}")
    return result

# Function call
factorial_with_steps(5)