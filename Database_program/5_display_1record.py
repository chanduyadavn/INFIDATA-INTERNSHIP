import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="company")

cur=myconn.cursor()
try:

    cur.execute("select* from employee where eid=102 ")

    #fetching the rows from the cursor object
    result=cur.fetchone()
    #printing the result
    for x in result:
        print(x)
except Exception as e:
    print("can not process",result)

myconn.close()