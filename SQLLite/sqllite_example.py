import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("You are connecto to SQL Lite database")
    except Error as e:
        print(f"Error {e} when try to coonect SQL Lite database")
    return connection

connection = create_connection("C:\\Desarrollo\\Python_SQL\\SQLLite\\sm_app.sqllite")
    
