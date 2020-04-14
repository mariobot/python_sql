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
if not exists (select * from sysobjects where name='users' and xtype='U')
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

# script that create rate comments table
reate_comments_table = """
if not exists (select * from sysobjects where name='comments' and xtype='U')
CREATE TABLE comments (
  id INT PRIMARY KEY Identity, 
  text VARCHAR(50) NOT NULL, 
  user_id INT NOT NULL, 
  post_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (post_id) REFERENCES posts (id)   
);
"""

# execute the query for create rate comments table
execute_query(conn, reate_comments_table)

# script that create likes table
create_likes_table = """
if not exists (select * from sysobjects where name='likes' and xtype='U')
CREATE TABLE likes (
  id INT PRIMARY KEY Identity, 
  user_id INT NOT NULL, 
  post_id INT NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (post_id) REFERENCES posts (id)    
);
"""
# execute the query for create likes table
execute_query(conn, create_likes_table)

# script to insert users in the database
create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

#execute_query(conn,create_users) 

create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ('Happy', 'I am feeling very happy today', 1),
  ('Hot Weather', 'The weather is very hot today', 2),
  ('Help', 'I need some help with my work', 2),
  ('Great News', 'I am getting married', 1),
  ('Interesting Game', 'It was a fantastic game of tennis', 5),
  ('Party', 'Anyone up for a late-night party today?', 3);
"""

#execute_query(conn,create_posts) 

create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""

create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""

execute_query(conn, create_comments)
execute_query(conn, create_likes)  

select_users = "SELECT * FROM users"
result = execute_read_query(conn,select_users)   

for u in result:
    print(u)

select_posts = "SELECT * FROM posts"
result_posts = execute_read_query(conn, select_posts)

for p in result_posts:
    print(p)

# executing a JOIN QUERY
select_users_post = """
SELECT 
    users.id,
    users.name,
    posts.description
FROM
    posts
    INNER JOIN users on users.id = posts.user_id
"""

result_up = execute_read_query(conn, select_users_post)

for up in result_up:
    print(up)

# executing a MULTIPLE JOIN QUERY
select_post_comments_users = """
SELECT 
    posts.description as post,
    text as comment,
    name
FROM
    posts
    INNER JOIN users on users.id = posts.user_id 
    INNER JOIN comments on comments.post_id = posts.id
"""
posts_comments_user = execute_read_query(conn, select_post_comments_users)

for pcu in posts_comments_user:
    print(pcu)

select_post_likes = """
SELECT
  description as Post,
  COUNT(likes.id) as Likes
FROM
  likes,
  posts
WHERE
  posts.id = likes.post_id
GROUP BY
  posts.description,
  likes.post_id
"""

post_likes = execute_read_query(conn,select_post_likes)

for pl in post_likes:
    print(pl)

# you can apply UPDATE and DELETE sentences
