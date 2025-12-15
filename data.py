# for creating and managing database

# data.py
# Database management (PyInstaller-safe)

import sqlite3
import os
import sys



def get_db_path():

    if hasattr(sys, "_MEIPASS"):
        base_path = os.path.dirname(sys.executable)
    else:
  
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, "users_searches.db")



def get_connection():
    return sqlite3.connect(get_db_path())



def create_tables():
    conn = get_connection()
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            city TEXT,
            temperature REAL,
            condition TEXT,
            timestamp TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
    )

    conn.commit()
    conn.close()



def add_user(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (username) VALUES (?)",
        (username,)
    )

    conn.commit()
    conn.close()
    return 1


def get_users():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, username FROM users")
    rows = cur.fetchall()
    conn.close()

    return [{"id": row[0], "username": row[1]} for row in rows]



def save_search(user_id, city, temperature, condition, timestamp):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO searches (user_id, city, temperature, condition, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """,
        (user_id, city, temperature, condition, timestamp)
    )

    conn.commit()
    conn.close()
    return 1


def get_search():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT user_id, city, temperature, condition, timestamp
        FROM searches
        ORDER BY timestamp DESC
        LIMIT 5
        """
    )

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "user_id": row[0],
            "city": row[1],
            "temperature": row[2],
            "condition": row[3],
            "timestamp": row[4],
        }
        for row in rows
    ]
