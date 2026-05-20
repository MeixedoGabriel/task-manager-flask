from database import connect

def add_task(title):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, status) VALUES (?, ?)",
        (title, "Pendente")
    )

    conn.commit()
    conn.close()


def list_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()

    return tasks


def complete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        ("Concluída", task_id)
    )

    conn.commit()

    updated_rows = cursor.rowcount

    conn.close()

    return updated_rows > 0


def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()

    deleted_rows = cursor.rowcount

    conn.close()

    return deleted_rows > 0

def reset_tasks():
    conn = connect()
    cursor = conn.cursor()

    # Deleta todas as tarefas
    cursor.execute("DELETE FROM tasks")

    # Reseta contador de IDs
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='tasks'")

    conn.commit()
    conn.close()