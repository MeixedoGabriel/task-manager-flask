from colorama import Fore, Style, init
import os

init(autoreset=True)

def clear_screen():
    os.system("cls")

print("Sistema de tarefas iniciado!")
from database import create_table
from tasks import (
    add_task,
    list_tasks,
    complete_task,
    delete_task
    reset_tasks
)

def mostrar_tasks_bonito():
    tasks = list_tasks()
    print("\n=== TAREFAS ===")
    for task in tasks:
        status_color = Fore.GREEN if task[2] == "Concluída" else Fore.RED

        print(
            f"{Fore.CYAN}{task[0]} "
            f"- {task[1]} "
             f"{status_color}[{task[2]}]"
            )

create_table()

while True:
    clear_screen()

    print(Fore.CYAN + "=== GERENCIADOR DE TAREFAS ===")
    print(Fore.YELLOW + "1 - Adicionar tarefa")
    print(Fore.YELLOW + "2 - Listar tarefas")
    print(Fore.YELLOW + "3 - Concluir tarefa")
    print(Fore.YELLOW + "4 - Deletar tarefa")
    print(Fore.YELLOW + "5 - Resetar banco de dados")
    print(Fore.YELLOW + "6 - Sair")

    option = input("Escolha uma opção: ")

    if option == "1":
        title = input("Digite o nome da tarefa: ").strip()
        if not title:
            print(Fore.RED + "A tarefa não pode estar vazia!")
        else:
            add_task(title)
            print("Tarefa adicionada com sucesso!")
            input("\nPressione ENTER para continuar...")
            continue

    elif option == "2":
        mostrar_tasks_bonito()
        input("\nPressione Enter para continuar...")

    elif option == "3":
        mostrar_tasks_bonito()
        task_id = input("Digite o ID da tarefa: ")

        if not task_id.isdigit():
            print(Fore.RED + "Digite um ID válido!")
            input("\nPressione ENTER para continuar...")
            continue

        complete_task(task_id)

        print("Tarefa concluída com sucesso!")
        input("\nPressione ENTER para continuar...")


    elif option == "4":
        mostrar_tasks_bonito()
        task_id = input("Digite o ID da tarefa: ")

        if not task_id.isdigit():
            print(Fore.RED + "Digite um ID válido!")
            input("\nPressione ENTER para continuar...")
            continue

        delete_task(task_id)

        print("Tarefa deletada com sucesso!")
        input("\nPressione ENTER para continuar...")

    elif option == "5":
        confirm = " "
        while confirm not in "sn":
            confirm = input(
                Fore.RED +
                "Tem certeza que deseja apagar TODAS as tarefas? (s/n): "
            ).lower()[0]
            
        if confirm == "s":
            reset_tasks()
            print(Fore.GREEN + "Banco resetado com sucesso!")

        elif confirm == "n":
            print(Fore.YELLOW + "Operação cancelada.")

        input("\nPressione ENTER para continuar...")


    elif option == "6":
        print(Fore.CYAN + "Saindo...")
        break