import sqlite3
from passlib.context import CryptContext

pwd_context= CryptContext(schemes=["bcrypt"],deprecated="auto")
def get_connection():
    conn=sqlite3.connect("app1.db")
    conn.row_factory=sqlite3.Row
    return conn


def init_db():
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL         
        )
    """)

    conn.commit()
    conn.close()


def create_user(user):
    conn=get_connection()
    c=conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?",(user.email,))
    existing_user=c.fetchone()
    if existing_user:
        conn.close()
        return None
    
    hashed_password=pwd_context.hash(user.password)
    c.execute("""
        INSERT INTO users(email,hashed_password) VALUES(?,?)
        """, (user.email,hashed_password)
    )
    user_id=c.lastrowid
    conn.commit()
    c.execute("SELECT * FROM users WHERE id=?",(user_id,))
    row=c.fetchone()
    conn.close()
    return{
        "id":row["id"],
        "email": row["email"]
    }

def get_user_by_email(email):
    conn=get_connection()
    c=conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?",(email,))
    row=c.fetchone()
    conn.close()

    if row:
        return dict(row)
    return None
    