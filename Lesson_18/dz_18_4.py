import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abraham289!",
    database="my_first_db")

mycursor = mydb.cursor()
mycursor.execute('ALTER TABLE student ADD PRIMARY KEY(id)')
