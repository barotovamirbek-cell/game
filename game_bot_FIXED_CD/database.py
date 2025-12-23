import sqlite3

conn = sqlite3.connect("game.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    money INTEGER DEFAULT 0,
    crystals INTEGER DEFAULT 0,
    last_collect INTEGER DEFAULT 0,
    last_transfer INTEGER DEFAULT 0,
    house_level INTEGER DEFAULT 0,
    car_level INTEGER DEFAULT 0,
    clan_id INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS clans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    owner_id INTEGER,
    level INTEGER DEFAULT 1,
    bonus INTEGER DEFAULT 5
)
""")

conn.commit()
