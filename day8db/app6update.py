import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
  user="root",
  password="root",
  port='3306',
  database='pythontraining1'
)

mycursor = mydb.cursor()
sql = "UPDATE customer1 SET address = 'Jercycity' WHERE id=3"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) affected")