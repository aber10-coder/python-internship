import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Retrieve students with marks above 70
cursor.execute(
    "SELECT * FROM students WHERE marks > ?",
    (70,)
)

# Get all matching rows
rows = cursor.fetchall()

# Print each row using f-strings
for row in rows:
    print(f"Student: {row[0]}, Marks: {row[1]}")

conn.close()