import sqlite3
conn = sqlite3.connect("school.db")
cursor = conn.cursor()
name = "John"


cursor.execute(
    "DELETE FROM students WHERE name = ?",
    (name,)
)

conn.commit()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

print("Remaining students:")

for row in rows:
    print(f"Student: {row[0]}, Marks: {row[1]}")

conn.close()