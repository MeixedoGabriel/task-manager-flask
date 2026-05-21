# Biblioteca usada para trabalhar com SQLite
import sqlite3


# Função responsável por conectar no banco
def connect():

    # Cria conexão com o arquivo tasks.db
    conn = sqlite3.connect("tasks.db")

    return conn


# Função que cria a tabela tasks
def create_table():

    conn = connect()

    # Cursor executa comandos SQL
    cursor = conn.cursor()

    # Cria a tabela caso ela não exista
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (

        -- ID único gerado automaticamente
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        -- Nome da tarefa
        title TEXT NOT NULL,

        -- Status da tarefa
        status TEXT NOT NULL,

        -- Prioridade
        priority TEXT NOT NULL,

        -- Categoria
        category TEXT NOT NULL,

        -- Data de criação
        created_at TEXT NOT NULL,

        -- Data limite
        due_date TEXT NOT NULL
    )
    """)

    # Salva alterações no banco
    conn.commit()

    # Fecha conexão
    conn.close()