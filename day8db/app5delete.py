import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
  user="root",
  password="root",
  port='3306',
  database='pythontraining1'
)

mycursor = mydb.cursor()

sql = "DELETE FROM customer1 WHERE id=5"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")