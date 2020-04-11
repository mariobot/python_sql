# install pyodbc

import pyodbc

def create_connection(server_name,db_name,user,password):
    connection = None
    try:
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server_name+';DATABASE='+db_name+';UID='+user+';PWD='+ password)
        print("Conection to SQL Server Successfully")
    except pyodbc.Error as e:
        print(f"Error {e}")
    return connection

conn = create_connection("MBOTERO\\JWSQLSERVER","python_test","pyuser","123456")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()        
        print("Command executed successfully")        
    except pyodbc.Error as e:
        print(f"Error {e}")    
    
def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Command executed successfully")
        return result
    except pyodbc.Error as e:
        print(f"Error {e}")    

# script to create users table
create_users_table = """
if not exists (select * from sysobjects where name='users' and xtype='TABLE')
    CREATE TABLE users (
    id INT PRIMARY KEY Identity,
    name VARCHAR(50) NOT NULL,
    age INT,
    gender VARCHAR(50),
    nationality VARCHAR(50)
);
"""

# executing creation of users table
execute_query(conn, create_users_table)

# script to create posts table
create_posts_table = """
if not exists (select * from sysobjects where name='posts' and xtype='U')
CREATE TABLE posts(
  id INT PRIMARY KEY Identity, 
  title VARCHAR(50) NOT NULL, 
  description VARCHAR(50) NOT NULL, 
  user_id INT NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""
# executing creation of posts table
execute_query(conn, create_posts_table)