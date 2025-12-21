import sqlite3

conn = sqlite3.connect("game.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    balance INTEGER DEFAULT 0,
    last_collect INTEGER DEFAULT 0,
    house_level INTEGER DEFAULT 1,
    car_level INTEGER DEFAULT 1
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    rarity TEXT,
    bonus INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS equipped (
    user_id INTEGER PRIMARY KEY,
    clothes_rarity TEXT,
    clothes_bonus INTEGER DEFAULT 0
)
""")

conn.commit()
