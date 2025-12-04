import sqlite3

# Create a connection to a database called database.db
conn = sqlite3.connect('database.db')

# Create a cursor to perform database operations
cursor = conn.cursor()

def add_task(name, description):
  cursor.execute("INSERT INTO tasks (task_name, task_description, state) VALUES (?, ?, ?)",
  (name, description, 0))
  conn.commit()
  print("Task added")

# add_task('Homework', 'Complete assignments for this week')

def list_tasks():
  cursor.execute("SELECT task_number, task_name, task_description, state FROM tasks")
  rows = cursor.fetchall()

  print("\n------ Task List ------")
  for t in rows:
    status = "Completed" if t[3] == 1 else "Incomplete"
    print(f"{t[0]}. [{status}] {t[1]} — {t[2]}")
  print()

# print(list_tasks())

def complete_task(task_number):
  cursor.execute("UPDATE tasks SET state = 1 WHERE task_number = ?", (task_number,))
  conn.commit()
  print("Task marked as completed")

# complete_task(1)

def delete_task(task_number):
  cursor.execute("DELETE FROM tasks WHERE task_number = ?", (task_number,))
  conn.commit()
  print("Task deleted")

# delete_task(4)