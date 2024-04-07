import sqlite3

#____________query str____________
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS tbl_user(user_id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT DEFAULT 'unknown' , lastname TEXT NOT NULL , age INTEGER , country TEXT)"
SELECT_ALL_USERS = "SELECT * FROM tbl_user"
INSERT_INTO = "INSERT INTO tbl_user(name, lastname, age, country) VALUES(?,?,?,?)"
DELETE_USER = "DELETE FROM tbl_user WHERE name = ?"

#____________connect method____________
def check_connection():
    return sqlite3.connect("balle.db")
    
#____________query method____________

def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE)

def select_all_users(connection):
    with connection:
        return connection.execute(SELECT_ALL_USERS).fetchall()

def insert_into(connection, name, lastname, age, country):
    with connection:
        return connection.execute(INSERT_INTO, (name, lastname, age, country))
    
def delete_user(connection, name):
    with connection:
        connection.execute(DELETE_USER, (name,))
