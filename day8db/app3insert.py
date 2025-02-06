import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
  user="root",
  password="root",
  port='3306',
  database='pythontraining1'
)
mycursor = mydb.cursor()
sql = """INSERT INTO customer1 (id,name,address) VALUES ( %s, %s, %s)"""
val = ("5","Sadwik", "Hyderabad")
mycursor.execute(sql, val)
val1 =("6","Anirv","Malvern")
mycursor.execute(sql,val1)  # insert into table 
mydb.commit()
print(mycursor.rowcount, "record inserted.")
