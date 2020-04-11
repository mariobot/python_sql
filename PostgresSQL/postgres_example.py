import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name,db_user,db_password,db_host,db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port
        )
        print("You are contected to PostgresSQL")
    except OperationalError as e:
        print(f"Error {e}")
    return connection

connection = create_connection(
    "postgres", "postgres", "abc123", "127.0.0.1", "5432"
)

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:    
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"Error {e}")

create_database = "CREATE DATABASE sm_app"
execute_query(connection, create_database)

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL, 
  age INTEGER,
  gender TEXT,
  nationality TEXT
)
"""


# You can replicate the same logic at sqllite_example 
# Only need to have present the correct sintax for PostgresSQL



    
