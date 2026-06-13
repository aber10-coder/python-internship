def get_marks(num_subjects: int) -> list[int]:
    marks: list[int] = []

    for j in range(num_subjects):
        mark: int = int(input(f"Enter mark for subject {j + 1}: "))
        marks.append(mark)

    return marks


def calculate_average(marks: list[int]) -> float:
    total: int = sum(marks)
    return total / len(marks)


def calculate_grade(avg: float) -> str:
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def main() -> None:
    num_students: int = int(input("Enter the number of students: "))
    num_subjects: int = 5

    students: list[list[int]] = []

    for i in range(num_students):
        print(f"\nMarks of student {i + 1}")
        marks: list[int] = get_marks(num_subjects)
        students.append(marks)

    print("\nStudent Grades:")

    for i, marks in enumerate(students, start=1):
        avg: float = calculate_average(marks)
        grade: str = calculate_grade(avg)

        print(f"Student {i}")
        print(f"Average: {avg:.2f}")
        print(f"Grade: {grade}\n")


main()