import pymysql

mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='Vikki19@'
)

mycursor=mydb.cursor()
mycursor.execute("show databases")

for i in mycursor:
    print(i)

