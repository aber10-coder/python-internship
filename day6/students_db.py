import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

students = [
    ("Aber", 95),
    ("John", 88),
    ("Alice", 91),
    ("Mike", 76),
    ("Sarah", 89)
]

for student in students:
    cursor.execute(
        "INSERT INTO students VALUES (?, ?)",
        student
    )

conn.commit()
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.close()