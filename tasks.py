from database import connect
from datetime import datetime

def add_task(title, priority, category, due_date):
    conn = connect()
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%d/%m/%Y")

    cursor.execute(
        """
        INSERT INTO tasks (
            title,
            status,
            priority,
            category,
            created_at,
            due_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            title,
            "Pendente",
            priority,
            category,
            created_at,
            due_date
        )
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

    # Busca a tarefa
    cursor.execute(
        "SELECT status FROM tasks WHERE id = ?",
        (task_id,)
    )

    task = cursor.fetchone()

    # Verifica se tarefa existe
    if not task:
        conn.close()
        return "not_found"

    # Verifica se já está concluída
    if task[0] == "Concluída":
        conn.close()
        return "already_completed"

    # Atualiza status
    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        ("Concluída", task_id)
    )

    conn.commit()
    conn.close()

    return "success"


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


def filter_by_status(status):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE status = ?",
        (status,)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def filter_by_priority(priority):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE priority = ?",
        (priority,)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def filter_by_category(category):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE category = ?",
        (category,)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def search_tasks(keyword):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE title LIKE ?",
        (f"%{keyword}%",)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


from datetime import datetime


def get_dashboard_data():
    conn = connect()
    cursor = conn.cursor()

    # Total de tarefas
    cursor.execute("SELECT COUNT(*) FROM tasks")
    total_tasks = cursor.fetchone()[0]

    # Pendentes
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Pendente'"
    )
    pending_tasks = cursor.fetchone()[0]

    # Concluídas
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Concluída'"
    )
    completed_tasks = cursor.fetchone()[0]

    # Alta prioridade
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE priority = 'Alta'"
    )
    high_priority_tasks = cursor.fetchone()[0]

    # Tarefas vencidas
    today = datetime.now().strftime("%d/%m/%Y")

    cursor.execute(
        """
        SELECT COUNT(*) FROM tasks
        WHERE due_date < ?
        AND status = 'Pendente'
        """,
        (today,)
    )

    overdue_tasks = cursor.fetchone()[0]

    conn.close()

    return {
        "total": total_tasks,
        "pending": pending_tasks,
        "completed": completed_tasks,
        "high_priority": high_priority_tasks,
        "overdue": overdue_tasks
    }