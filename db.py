import sqlite3

def get_connection():
    return sqlite3.connect("employees.db")

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER,
                        department TEXT,
                        salary REAL
                    )''')
    conn.commit()
    conn.close()
