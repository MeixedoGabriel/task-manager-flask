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