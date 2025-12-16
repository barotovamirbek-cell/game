
import sqlite3, time

COLLECT_CD = 3600  # 1 hour

conn = sqlite3.connect("game.db")
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        balance INTEGER DEFAULT 0,
        income INTEGER DEFAULT 10,
        last_collect INTEGER DEFAULT 0
    )
    """)
    conn.commit()

def get_user(uid):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (uid,))
    return cursor.fetchone()

def create_user(uid):
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (uid,))
    conn.commit()

def can_collect(uid):
    u = get_user(uid)
    return int(time.time()) - u[3] >= COLLECT_CD

def collect(uid):
    u = get_user(uid)
    income = u[2]
    cursor.execute("""
        UPDATE users
        SET balance = balance + ?,
            last_collect = ?
        WHERE user_id = ?
    """, (income, int(time.time()), uid))
    conn.commit()
    return income

def time_left(uid):
    u = get_user(uid)
    passed = int(time.time()) - u[3]
    return max(COLLECT_CD - passed, 0)
