import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="telusko")
cursor = mydb.cursor()

cursor.execute("select * from student")
for i in cursor:
    print(i)
