import mysql.connector
from mysql.connector import Error

def create_connection(host_name,user_name,user_password,database):
    connection = None
    try:
        if database is "":            
            connection = mysql.connector.connect(
                host = host_name,
                user = user_name,
                passwd = user_password
            )
        else:
            connection = mysql.connector.connect(
                host = host_name,
                database = database,
                user = user_name,
                passwd = user_password
            )
        print("Connection to MySQL DB Successful")
    except Error as e:
        print(f"Error {e} when try to connect MySQL")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("SQL Command executed")
    except Error as e:
        print(f"Error {e} when try to excecute a query")

connection = create_connection("","","","")

# to create a database
new_database = "CREATE DATABASE sm_app"
execute_query(connection, new_database)

connection = create_connection("","","","")





