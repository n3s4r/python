class Student:
    def __init__(self, name, major, age, cgpa):
        self.name = name
        self.major = major
        self.age = age
        self.cgpa = cgpa

# Creating the instance
student1 = Student("Tashin Mahmud", "Computer Science", 25, 2.75)

# Printing the details
print(f"{student1.name}  {student1.major}  {student1.age}  {student1.cgpa:.2f}")
