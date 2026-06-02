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

    #tabela de usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL
    )
    """)

    # Cria a tabela caso ela não exista - tabela de tarefas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT NOT NULL,

        status TEXT NOT NULL,

        priority TEXT NOT NULL,

        category TEXT NOT NULL,

        created_at TEXT NOT NULL,

        due_date TEXT NOT NULL,

        user_id INTEGER,

        FOREIGN KEY (user_id)
        REFERENCES users(id)
    )
    """)

    # Salva alterações no banco
    conn.commit()

    # Fecha conexão
    conn.close()