from db import get_cursor

def get_all_tasks():
    cur = get_cursor()
    cur.execute("SELECT * FROM tasks")
    return cur.fetchall()


def get_incomplete_tasks():
    cur = get_cursor()
    cur.execute("SELECT * FROM tasks WHERE is_complete=false")
    return cur.fetchall()


def add_task(title):
    cur = get_cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    cur.connection.commit()   # 🔥 ВОТ ЭТО НУЖНО


def update_task(task_id):
    cur = get_cursor()
    cur.execute(
        "UPDATE tasks SET is_complete = NOT is_complete WHERE id=%s",
        (task_id,)
    )
    cur.connection.commit()   # 🔥


def delete_task(task_id):
    cur = get_cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    cur.connection.commit()   # 🔥