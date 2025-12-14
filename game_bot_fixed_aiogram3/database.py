
import sqlite3

conn = sqlite3.connect("game.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER,
    chat_id INTEGER,
    balance INTEGER DEFAULT 0,
    last_collect INTEGER DEFAULT 0,
    PRIMARY KEY (user_id, chat_id)
)
""")

conn.commit()
