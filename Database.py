import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.create_connection()

    def create_connection(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            print(f"Connected to SQLite database: {self.db_file}")
        except Error as e:
            print(f"Error connecting to SQLite database: {e}")

    def create_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palname TEXT,
            instagram TEXT,
            twitter TEXT,
            discord TEXT,
            steam TEXT,
            telegram TEXT
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            self.connection.commit()
            print("Table 'users' created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def insert_user(self, palname, instagram, twitter, discord, steam, telegram):
        insert_sql = """
        INSERT INTO users (palname, instagram, twitter, discord, steam, telegram)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (palname, instagram, twitter, discord, steam, telegram))
            self.connection.commit()
            print("User inserted successfully.")
        except Error as e:
            print(f"Error inserting user: {e}")

    def update_user(self, user_id, palname, instagram, twitter, discord, steam, telegram):
        update_sql = """
        UPDATE users
        SET palname = ?,
            instagram = ?,
            twitter = ?,
            discord = ?,
            steam = ?,
            telegram = ?
        WHERE id = ?
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_sql, (palname, instagram, twitter, discord, steam, telegram, user_id))
            self.connection.commit()
            print("User updated successfully.")
        except Error as e:
            print(f"Error updating user: {e}")

    def delete_user(self, user_id):
        delete_sql = "DELETE FROM users WHERE id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_sql, (user_id,))
            self.connection.commit()
            print("User deleted successfully.")
        except Error as e:
            print(f"Error deleting user: {e}")

    def fetch_all_users(self):
        select_sql = "SELECT id, palname, instagram, twitter, discord, steam, telegram FROM users"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error fetching users: {e}")
            return []

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection to SQLite database closed.")
