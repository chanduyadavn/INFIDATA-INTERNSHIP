import mysql.connector
#create the connection object
myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="company")
#creating the cursor object
cur=myconn.cursor()
try:
    #reading the employee data
    cur.execute("select* from employee ")

    #fetching the rows from the cursor object
    result=cur.fetchone()
    #printing the result
    for x in result:
        print(x)
except Exception as e:
    print("can not process",result)

myconn.close()