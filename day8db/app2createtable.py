import mysql.connector # type: ignore
#pip install mysql-connector-python
con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  port='3306',
  database='pythontraining1'
)
mycursor = con.cursor()
mycursor.execute("CREATE TABLE customer1 (id int primary key,name VARCHAR(10), address VARCHAR(20))")
'''
use pythontraining1;
show tables;
desc customer;
select * from customer;

'''