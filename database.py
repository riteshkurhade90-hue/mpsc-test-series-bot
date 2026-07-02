import sqlite3

DB_NAME = "quiz.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS results (
        user_id INTEGER PRIMARY KEY,
        correct INTEGER,
        wrong INTEGER,
        percentage REAL,
        submitted_at TEXT
    )
    """)

    conn.commit()
    conn.close()
