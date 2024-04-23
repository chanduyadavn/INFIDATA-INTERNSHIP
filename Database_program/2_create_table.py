import mysql.connector

myconn=mysql.connector.connect(
    host='localhost',user='root',database='company'
)
cur=myconn.cursor()

try:
    cur.execute('create table employee(ename varchar(30),eid int(4) primary key,dept varchar(20),designation varchar(20),mobile varchar(10),place varchar(15))')
    print("your table created")

except Exception as e:
#myconn.rollback
    print('can not process:',e)

myconn.close()