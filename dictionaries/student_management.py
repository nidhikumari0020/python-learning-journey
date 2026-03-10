# dictionaries/student_management.py

students = {}  # empty dictionary to store student info

while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        students[roll] = {"name": name, "age": age}
        print(f"Student {name} added successfully!")
        
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for roll, info in students.items():
                print(f"Roll: {roll}, Name: {info['name']}, Age: {info['age']}")
                
    elif choice == "3":
        roll = input("Enter roll number to remove: ")
        if roll in students:
            removed = students.pop(roll)
            print(f"Removed student {removed['name']}")
        else:
            print("Student not found.")
            
    elif choice == "4":
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice, try again.")