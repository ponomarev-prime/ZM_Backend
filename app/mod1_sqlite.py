import sqlite3
from datetime import datetime

# Создаем базу данных
conn = sqlite3.connect('Profile.db')

# Создаем таблицу Cookie Profile
conn.execute('''CREATE TABLE IF NOT EXISTS Cookie_Profile 
                (id INTEGER PRIMARY KEY NOT NULL, 
                created_at TEXT NOT NULL, 
                cookie TEXT, 
                last_run TEXT, 
                run_count INTEGER);''')

# Добавляем 15 записей
for i in range(15):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute(f"INSERT INTO Cookie_Profile (created_at) VALUES ('{now}')")

conn.commit()
conn.close()
