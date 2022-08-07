import sqlite3

try:
    conn = sqlite3.connect('test.db')
except Exception as e:
    print("Error in connecting",str(e))

c = conn.cursor()
c.execute("create table student(sname varchar(20), stuid number(10))")

c.execute("insert into student values('srivatsan',2011003010555)")
c.execute("insert into student values('harish',2011003010492)")
c.execute("insert into student values('subesh',2011003010516)")
c.execute("insert into student values('arvind',2011003010552)")

conn.commit()

for row in c.execute("select * from student"):
    print(row)

conn.close()
