# Dictionary to store student data
students = {}

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grades = input("Enter student grades (comma-separated): ")
    students[name] = {'age': age, 'grades': grades}
    print(f"Student '{name}' added.\n")

# Function to view a student's data
def view_student():
    name = input("Enter student name to view: ")
    if name in students:
        print(f"Name: {name}, Age: {students[name]['age']}, Grades: {students[name]['grades']}\n")
    else:
        print(f"Student '{name}' not found.\n")

# Function to update a student's data
def update_student():
    name = input("Enter student name to update: ")
    if name in students:
        age = input("Enter new age: ")
        grades = input("Enter new grades (comma-separated): ")
        students[name] = {'age': age, 'grades': grades}
        print(f"Student '{name}' updated.\n")
    else:
        print(f"Student '{name}' not found.\n")

# Function to delete a student's data
def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print(f"Student '{name}' deleted.\n")
    else:
        print(f"Student '{name}' not found.\n")

# Main loop
while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.\n")
