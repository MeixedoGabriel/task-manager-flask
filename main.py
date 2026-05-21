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
    delete_task,
    reset_tasks,
    filter_by_status,
    filter_by_priority,
    filter_by_category,
    search_tasks
)

def mostrar_tasks_bonito(mostar=True):
    tasks = list_tasks()
    if not tasks:
        if mostar:
            print(Fore.RED + "\nNenhuma tarefa encontrada.")
        else:
            return "Nenhuma Tarefa"
    else:
        if mostar:
            print("\n=== TAREFAS ===")
            for task in tasks:
                status_color = Fore.GREEN if task[2] == "Concluída" else Fore.RED

                print(Fore.CYAN + f"\nID: {task[0]}")
                print(f"Tarefa: {task[1]}")
                print(f"Status: {status_color}{task[2]}")
                print(f"Prioridade: {task[3]}")
                print(f"Categoria: {task[4]}")
                print(f"Criada em: {task[5]}")
                print(f"Prazo: {task[6]}")


def display_tasks(tasks):
    if not tasks:
        print(Fore.RED + "\nNenhuma tarefa encontrada.")
        return

    for task in tasks:
        status_color = (
            Fore.GREEN
            if task[2] == "Concluída"
            else Fore.RED
        )

        print(Fore.CYAN + f"\nID: {task[0]}")
        print(f"Tarefa: {task[1]}")
        print(f"Status: {status_color}{task[2]}")
        print(f"Prioridade: {task[3]}")
        print(f"Categoria: {task[4]}")
        print(f"Criada em: {task[5]}")
        print(f"Prazo: {task[6]}")


create_table()

while True:
    clear_screen()

    print(Fore.CYAN + "=== GERENCIADOR DE TAREFAS ===")
    print(Fore.YELLOW + "1 - Adicionar tarefa")
    print(Fore.YELLOW + "2 - Listar tarefas")
    print(Fore.YELLOW + "3 - Concluir tarefa")
    print(Fore.YELLOW + "4 - Deletar tarefa")
    print(Fore.YELLOW + "5 - Filtrar tarefas")
    print(Fore.YELLOW + "6 - Pesquisar tarefa")
    print(Fore.YELLOW + "7 - Resetar banco")
    print(Fore.YELLOW + "8 - Sair")

    option = input("Escolha uma opção: ")

    if option == "1":
        title = input("Digite o nome da tarefa: ").strip()
        print("\nPrioridades:")
        print("1 - Alta")
        print("2 - Média")
        print("3 - Baixa")

        priority_option = input("Escolha a prioridade: ")

        priorities = {
            "1": "Alta",
            "2": "Média",
            "3": "Baixa"
        }

        priority = priorities.get(priority_option)

        if not priority:
            print(Fore.RED + "Prioridade inválida!")
            input("\nPressione ENTER para continuar...")
            continue

        category = input("Digite a categoria: ").strip()

        if not category:
            print(Fore.RED + "Categoria inválida!")
            input("\nPressione ENTER para continuar...")
            continue

        due_date = input(
            "Digite a data de prazo (dd/mm/aaaa): "
        ).strip()
        if not title:
            print(Fore.RED + "A tarefa não pode estar vazia!")
            input("\nPressione ENTER para continuar...")
        else:
            add_task(title, priority, category, due_date)
            print("Tarefa adicionada com sucesso!")
            input("\nPressione ENTER para continuar...")
            continue


    elif option == "2":
        mostrar_tasks_bonito()
        input("\nPressione ENTER para continuar...")


    elif option == "3":
        mostrar_tasks_bonito()
        if "Nenhuma Tarefa" == mostrar_tasks_bonito(mostar=False):
            pass

        else:
            task_id = input("Digite o ID da tarefa: ")

            result = complete_task(task_id)

            if result == "success":
                print(Fore.GREEN + "Tarefa concluída com sucesso!")

            elif result == "already_completed":
                print(Fore.YELLOW + "Essa tarefa já está concluída!")

            else:
                print(Fore.RED + "Tarefa não encontrada!")

        input("\nPressione ENTER para continuar...")


    elif option == "4":
        mostrar_tasks_bonito()
        if "Nenhuma Tarefa" == mostrar_tasks_bonito(mostar=False):
            input("\nPressione ENTER para continuar...")
        else:
            task_id = input("Digite o ID da tarefa: ")

            if not task_id.isdigit():
                print(Fore.RED + "Digite um ID válido!")
                input("\nPressione ENTER para continuar...")
                continue

            success = delete_task(task_id)

            if success:
                print(Fore.GREEN + "Tarefa deletada com sucesso!")
                input("\nPressione ENTER para continuar...")
            else:
                print(Fore.RED + "Tarefa não encontrada!")

    elif option == "5":
        print("\n=== FILTROS ===")
        print("1 - Pendentes")
        print("2 - Concluídas")
        print("3 - Prioridade Alta")
        print("4 - Categoria")

        filter_option = input("Escolha um filtro: ")

        if filter_option == "1":
            tasks = filter_by_status("Pendente")

        elif filter_option == "2":
            tasks = filter_by_status("Concluída")

        elif filter_option == "3":
            tasks = filter_by_priority("Alta")

        elif filter_option == "4":
            category = input("Digite a categoria: ")

            tasks = filter_by_category(category)

        else:
            print(Fore.RED + "Filtro inválido!")
            input("\nPressione ENTER para continuar...")
            continue

        mostrar_tasks_bonito(tasks)

        input("\nPressione ENTER para continuar...")

    elif option == "6":
        keyword = input(
            "Digite um termo para pesquisar: "
        ).strip()

        tasks = search_tasks(keyword)

        print("\n=== RESULTADOS ===")

        mostrar_tasks_bonito(tasks)

        input("\nPressione ENTER para continuar...")
            
        
    elif option == "7":
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


    elif option == "8":
        print(Fore.CYAN + "Saindo...")
        break