# tasks.py

from database import get_db_connection


def show_tasks(user):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Tasks WHERE user_id = (SELECT id FROM Users WHERE username = %s)", (user,))
    tasks = cursor.fetchall()

    for task in tasks:
        print(f"Task ID: {task[0]} | Task: {task[2]} | Status: {task[3]}")

    cursor.close()
    conn.close()


def add_task(user, task_name):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM Users WHERE username = %s", (user,))
    user_id = cursor.fetchone()[0]

    cursor.execute("INSERT INTO Tasks (user_id, task_name) VALUES (%s, %s)", (user_id, task_name))
    conn.commit()

    cursor.close()
    conn.close()


def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Tasks WHERE id = %s", (task_id,))
    conn.commit()

    cursor.close()
    conn.close()
