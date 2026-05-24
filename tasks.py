# Importa a conexão com o banco
from database import connect

# Importa funções de data
from datetime import datetime


# =========================
# ADICIONAR TAREFA
# =========================
def add_task(title, priority, category, due_date):

    conn = connect()
    cursor = conn.cursor()

    # Pega a data atual
    created_at = datetime.now().strftime("%d/%m/%Y")
    try:
        due_date = datetime.strptime(
            due_date,
            "%Y-%m-%d"
        ).strftime("%d/%m/%Y")

    except ValueError:
        pass

    # Insere a tarefa no banco
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

        # Valores que serão inseridos
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


# =========================
# LISTAR TAREFAS
# =========================
def list_tasks():

    conn = connect()
    cursor = conn.cursor()

    # Busca todas as tarefas
    cursor.execute("SELECT * FROM tasks")

    # fetchall pega todos os resultados
    tasks = cursor.fetchall()

    conn.close()

    return tasks


# =========================
# CONCLUIR TAREFA
# =========================
def complete_task(task_id):

    conn = connect()
    cursor = conn.cursor()

    # Busca o status da tarefa
    cursor.execute(
        "SELECT status FROM tasks WHERE id = ?",
        (task_id,)
    )

    # fetchone pega apenas um resultado
    task = cursor.fetchone()

    # Verifica se a tarefa existe
    if not task:
        conn.close()
        return "not_found"

    # Verifica se já foi concluída
    if task[0] == "Concluída":
        conn.close()
        return "already_completed"

    # Atualiza o status
    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        ("Concluída", task_id)
    )

    conn.commit()
    conn.close()

    return "success"


# =========================
# DELETAR TAREFA
# =========================
def delete_task(task_id):

    conn = connect()
    cursor = conn.cursor()

    # Deleta a tarefa pelo ID
    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()

    # rowcount mostra quantas linhas foram afetadas
    deleted_rows = cursor.rowcount

    conn.close()

    # Retorna True se deletou alguma linha
    return deleted_rows > 0


# =========================
# RESETAR BANCO
# =========================
def reset_tasks():

    conn = connect()
    cursor = conn.cursor()

    # Apaga todas as tarefas
    cursor.execute("DELETE FROM tasks")

    # Reinicia os IDs do banco
    cursor.execute(
        "DELETE FROM sqlite_sequence WHERE name='tasks'"
    )

    conn.commit()
    conn.close()


# =========================
# FILTRAR POR STATUS
# =========================
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


# =========================
# FILTRAR POR PRIORIDADE
# =========================
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


# =========================
# FILTRAR POR CATEGORIA
# =========================
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


# =========================
# PESQUISAR TAREFAS
# =========================
def search_tasks(keyword):

    conn = connect()
    cursor = conn.cursor()

    # LIKE permite procurar palavras parecidas
    cursor.execute(
        "SELECT * FROM tasks WHERE title LIKE ?",
        (f"%{keyword}%",)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


# =========================
# DASHBOARD
# =========================
def get_dashboard_data():

    conn = connect()
    cursor = conn.cursor()

    # Conta total de tarefas
    cursor.execute("SELECT COUNT(*) FROM tasks")
    total_tasks = cursor.fetchone()[0]

    # Conta pendentes
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Pendente'"
    )
    pending_tasks = cursor.fetchone()[0]

    # Conta concluídas
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Concluída'"
    )
    completed_tasks = cursor.fetchone()[0]

    # Conta alta prioridade
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE priority = 'Alta'"
    )
    high_priority_tasks = cursor.fetchone()[0]

    # Data atual
    today = datetime.now().strftime("%d/%m/%Y")

    # Conta tarefas vencidas
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

    # Retorna os dados em formato de dicionário
    return {
        "total": total_tasks,
        "pending": pending_tasks,
        "completed": completed_tasks,
        "high_priority": high_priority_tasks,
        "overdue": overdue_tasks
    }