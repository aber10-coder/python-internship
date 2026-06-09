class Student:
    def __init__(self, student_id, student_name, marks):
        self.student_id = student_id
        self.student_name = student_name
        self.marks = marks

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.student_name)
        print("Marks:", self.marks)

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"


students = []

n = int(input("Enter the number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    student_id = int(input("Enter Student ID: "))
    student_name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    s = Student(student_id, student_name, marks)

    students.append(s)


print("\nStudent Details")

for student in students:
    student.display_details()
    print("Grade:", student.calculate_grade())
    print()