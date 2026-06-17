import sqlite3

def get_connection():
    conn=sqlite3.connect("app2.db")
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    conn=get_connection()
    c=conn.cursor()

    c.execute(""" 
        CREATE TABLE IF NOT EXISTS tasks(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL
              )
    """)
    conn.commit()
    conn.close()

def create_task(title):
    conn=get_connection()
    c=conn.cursor()
    c.execute("INSERT INTO tasks (title) VALUES (?)",(title,))
    task_id=c.lastrowid
    conn.commit()
    c.execute("SELECT * FROM tasks WHERE id = ? ",(task_id,))
    row=c.fetchone()
    conn.close()
    return dict(row)

def get_all_tasks():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]



    