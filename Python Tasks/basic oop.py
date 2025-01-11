class Student:
    def __init__(self, name, age, *grades):
        # Initializing student attributes
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        # Display the student name, age, and grades
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {', '.join(map(str, self.grades))}")

    def calculate_average(self):
        # Calculate the average grade
        if len(self.grades) == 0:
            return 0
        average = sum(self.grades) / len(self.grades)
        return average

# Create a Student object
student1 = Student("Alice", 20, 90, 85, 88, 92)

# Call the methods
student1.display_details()

# Calculate and print the average grade
average_grade = student1.calculate_average()
print(f"Average Grade: {average_grade:.2f}")
