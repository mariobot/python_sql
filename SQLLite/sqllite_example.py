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

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query excecuted successfully")
    except Error as e:
        print(f"Error {e}")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error {e}")        

connection = create_connection("C:\\Desarrollo\\Python_SQL\\SQLLite\\sm_app.sqllite")

# script to create users table
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""
# execute the query for create users table
execute_query(connection,create_users_table)

# script to create posts table
create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

# execute the query for create the posts table
execute_query(connection, create_posts_table)

# script that create rate comments table
reate_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  text TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

# execute the query for create rate comments table
execute_query(connection, reate_comments_table)

# script that create likes table
create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id integer NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""
# execute the query for create likes table
execute_query(connection, create_likes_table)

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

execute_query(connection,create_users)

create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""

execute_query(connection,create_posts)

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

execute_query(connection, create_comments)
execute_query(connection, create_likes)  

select_users = "SELECT * FROM users"
result = execute_read_query(connection,select_users)   

for u in result:
    print(u)

select_posts = "SELECT * FROM posts"
result_posts = execute_read_query(connection, select_posts)

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

result_up = execute_read_query(connection, select_users_post)

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
    INNER JOIN users on users.id = comments.user_id
    INNER JOIN comments on posts.id = comments.post_id
"""
posts_comments_user = execute_read_query(connection, select_post_comments_users)

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
  likes.post_id
"""

post_likes = execute_read_query(connection,select_post_likes)

for pl in post_likes:
    print(pl)

# updating records

select_post_description = "SELECT description FROM posts where id = 2"
post_description = execute_read_query(connection,select_post_description)
print(post_description)

update_sentence = """
UPDATE
  posts
SET
  description = "The weather has become so could in this quarantine"
WHERE
  id = 2
"""
# Execute the update command
execute_query(connection, update_sentence)

post_description = execute_read_query(connection,select_post_description)
print(post_description)

delete_sentence = "DELETE FROM comments where id = 5"
#execute_query(connection,delete_sentence)