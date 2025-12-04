import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                  task_number INTEGER PRIMARY KEY,
                  task_name TEXT,
                  task_description TEXT,
                  state INTEGER,
                  total REAL)''')
conn.commit()