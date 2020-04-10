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

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT, 
  name TEXT NOT NULL, 
  age INT, 
  gender TEXT, 
  nationality TEXT, 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""
execute_query(connection,create_users_table)

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
  id INT AUTO_INCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY fk_user_id (user_id) REFERENCES users(id), 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""
execute_query(connection, create_posts_table)

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INT AUTO_INCREMENT, 
  text TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  FOREIGN KEY fk_user_id(user_id) REFERENCES users (id) FOREIGN KEY fk_post_id(post_id) REFERENCES posts (id),
  PRIMARY KEY (id)
) ENGINE = InnoDB;
"""
execute_query(connection, create_comments_table)

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INT AUTO_INCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id integer NOT NULL, 
  FOREIGN KEY fk_user_id(user_id) REFERENCES users (id) FOREIGN KEY fk_post_id(post_id) REFERENCES posts (id),
  PRIMARY KEY(id)
);
"""
execute_query(connection, create_likes_table)






