import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senha_db',
    database='Carros'
)
