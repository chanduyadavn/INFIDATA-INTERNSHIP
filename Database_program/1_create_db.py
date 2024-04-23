import mysql.connector
myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor=myconn.cursor()

try:
    mycursor.execute('CREATE DATABASE company')
    print('database created succesfully')
except Exception as e:
    print('cant not process:',e)

myconn.close()