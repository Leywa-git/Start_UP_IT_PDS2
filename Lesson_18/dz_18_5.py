import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abraham289!",
    database="my_first_db")

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO student (id, name) VALUES (01, 'John')")
mycursor.execute("INSERT INTO employee (id, name, salary) VALUES (01, 'John', 10000)")
mydb.commit()
