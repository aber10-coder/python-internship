import sqlite3
conn=sqlite3.connect('pract.db')
c=conn.cursor()

#c.execute("INSERT INTO emp VALUES('aber','nashid',50000)")
#c.execute("DELETE FROM emp WHERE rowid=2")
c.execute("SELECT * FROM emp")
print(c.fetchall())
conn.commit()

conn.close()