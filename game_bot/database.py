
import sqlite3
conn = sqlite3.connect("game.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER,
    chat_id INTEGER,
    balance INTEGER DEFAULT 0,
    total_earned INTEGER DEFAULT 0,
    last_collect INTEGER DEFAULT 0,
    PRIMARY KEY (user_id, chat_id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    user_id INTEGER,
    chat_id INTEGER,
    item TEXT,
    level INTEGER DEFAULT 1,
    PRIMARY KEY (user_id, chat_id, item)
)
""")

conn.commit()
