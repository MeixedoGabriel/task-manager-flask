print("Sistema de tarefas iniciado!")
from database import create_table
from tasks import (
    add_task,
    list_tasks,
    complete_task,
    delete_task
)

create_table()

while True:
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Deletar tarefa")
    print("5 - Sair")

    option = input("Escolha uma opção: ")

    if option == "1":
        title = input("Digite o nome da tarefa: ")
        add_task(title)
        print("Tarefa adicionada com sucesso!")

    elif option == "2":
        tasks = list_tasks()

        print("\n=== TAREFAS ===")

        for task in tasks:
            print(f"{task[0]} - {task[1]} [{task[2]}]")

    elif option == "3":
        task_id = input("Digite o ID da tarefa: ")

        complete_task(task_id)

        print("Tarefa concluída com sucesso!")


    elif option == "4":
        task_id = input("Digite o ID da tarefa: ")

        delete_task(task_id)

        print("Tarefa deletada com sucesso!")


    elif option == "5":
        print("Saindo...")
        break