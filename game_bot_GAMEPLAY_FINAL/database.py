
import sqlite3, time
conn = sqlite3.connect("game.db")
cursor = conn.cursor()

def init_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        balance INTEGER DEFAULT 0,
        income INTEGER DEFAULT 10,
        last_collect INTEGER DEFAULT 0
    )""")
    conn.commit()

def get_user(uid):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (uid,))
    return cursor.fetchone()

def create_user(uid):
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (uid,))
    conn.commit()

def collect(uid):
    cursor.execute("UPDATE users SET balance = balance + income, last_collect=? WHERE user_id=?",
                   (int(time.time()), uid))
    conn.commit()
