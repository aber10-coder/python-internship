import sqlite3

def create_table():

    conn=sqlite3.connect("main6.db")
    c=conn.cursor()
    c.execute(""" 
        CREATE TABLE main_stud(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              marks REAL
              )
    """)

    conn.commit()
    conn.close()

def insert_student(name,marks):
    conn=sqlite3.connect("main6.db")
    c=conn.cursor()
    c.execute("INSERT INTO main_stud(name,marks) VALUES(?,?)",(name,marks))
    
    conn.commit()
    conn.close()
    print("Student added succesfully!")

def  get_all_students():
    conn=sqlite3.connect("main6.db")
    c=conn.cursor()

    c.execute("SELECT * FROM main_stud")
    students=c.fetchall()
    conn.close()
    if students:
        print("ALL STUDENTS:\n")
        for student in students:
            print(
                f"ID: {student[0]},"
                f"Name: {student[1]},"
                f"Marks: {student[2]},"
            )
    else:
        print("No students found!\n")


def get_student_by_id(student_id):
    conn = sqlite3.connect("main6.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM main_stud WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    if student:
        print(
            f"ID: {student[0]}, "
            f"Name: {student[1]}, "
            f"Marks: {student[2]}"
        )
    else:
        print("Student not found.")


def update_marks(student_id, new_marks):
    conn = sqlite3.connect("main6.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE main_stud SET marks = ? WHERE id = ?",
        (new_marks, student_id)
    )

    conn.commit()
    conn.close()

    print("Marks updated successfully.")


def delete_student(student_id):
    conn = sqlite3.connect("main6.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM main_stud WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    print("Student deleted successfully.")


def get_students_above(threshold):
    conn = sqlite3.connect("main6.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM main_stud WHERE marks > ?",
        (threshold,)
    )

    students = cursor.fetchall()

    conn.close()

    if students:
        print(f"\nStudents with marks above {threshold}:")
        for student in students:
            print(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Marks: {student[2]}"
            )
    else:
        print("No matching students found.")


def main():
    create_table()

    while True:
        print("\n===== Student Database System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Get Student by ID")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Students Above Marks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))

            insert_student(name, marks)

        elif choice == "2":
            get_all_students()

        elif choice == "3":
            student_id = int(input("Enter student ID: "))

            get_student_by_id(student_id)

        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            new_marks = int(input("Enter new marks: "))

            update_marks(student_id, new_marks)

        elif choice == "5":
            student_id = int(input("Enter student ID: "))

            delete_student(student_id)

        elif choice == "6":
            threshold = int(input("Enter threshold marks: "))

            get_students_above(threshold)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

main()
