# Importa cores para deixar o terminal mais bonito
from colorama import Fore, Style, init

# Importa funções do sistema operacional
import os

# Inicia o colorama
# autoreset=True faz a cor voltar ao normal automaticamente
init(autoreset=True)


# Função para limpar o terminal
def clear_screen():
    os.system("cls")  # "cls" funciona no Windows


print("Sistema de tarefas iniciado!")


# Importa a função que cria a tabela do banco
from database import create_table

# Importa todas as funções do arquivo tasks.py
from tasks import (
    add_task,
    list_tasks,
    complete_task,
    delete_task,
    reset_tasks,
    filter_by_status,
    filter_by_priority,
    filter_by_category,
    search_tasks,
    get_dashboard_data
)


# Função responsável por mostrar as tarefas na tela
def display_tasks(tasks):

    # Verifica se a lista está vazia
    if not tasks:
        print(Fore.RED + "\nNenhuma tarefa encontrada.")
        return "Nenhuma Tarefa"

    # Percorre cada tarefa da lista
    for task in tasks:

        # Define a cor do status
        # Verde = concluída
        # Vermelho = pendente
        status_color = (
            Fore.GREEN
            if task[2] == "Concluída"
            else Fore.RED
        )

        # Exibe os dados da tarefa
        print(Fore.CYAN + f"\nID: {task[0]}")
        print(f"Tarefa: {task[1]}")
        print(f"Status: {status_color}{task[2]}")
        print(f"Prioridade: {task[3]}")
        print(f"Categoria: {task[4]}")
        print(f"Criada em: {task[5]}")
        print(f"Prazo: {task[6]}")


# Cria a tabela do banco caso ela não exista
create_table()


# Loop principal do sistema
while True:

    # Limpa o terminal sempre que o menu aparece
    clear_screen()

    # Menu principal
    print(Fore.CYAN + "=== GERENCIADOR DE TAREFAS ===")
    print(Fore.YELLOW + "1 - Adicionar tarefa")
    print(Fore.YELLOW + "2 - Listar tarefas")
    print(Fore.YELLOW + "3 - Concluir tarefa")
    print(Fore.YELLOW + "4 - Deletar tarefa")
    print(Fore.YELLOW + "5 - Dashboard")
    print(Fore.YELLOW + "6 - Filtrar tarefas")
    print(Fore.YELLOW + "7 - Pesquisar tarefa")
    print(Fore.YELLOW + "8 - Resetar banco")
    print(Fore.YELLOW + "9 - Sair")

    # Recebe a opção escolhida pelo usuário
    option = input("Escolha uma opção: ")

    # =========================
    # ADICIONAR TAREFA
    # =========================
    if option == "1":

        # Remove espaços extras com strip()
        title = input("Digite o nome da tarefa: ").strip()

        print("\nPrioridades:")
        print("1 - Alta")
        print("2 - Média")
        print("3 - Baixa")

        priority_option = input("Escolha a prioridade: ")

        # Dicionário que transforma número em texto
        priorities = {
            "1": "Alta",
            "2": "Média",
            "3": "Baixa"
        }

        # Busca a prioridade escolhida
        priority = priorities.get(priority_option)

        # Verifica se a prioridade existe
        if not priority:
            print(Fore.RED + "Prioridade inválida!")
            input("\nPressione ENTER para continuar...")
            continue

        category = input("Digite a categoria: ").strip()

        # Verifica se categoria foi preenchida
        if not category:
            print(Fore.RED + "Categoria inválida!")
            input("\nPressione ENTER para continuar...")
            continue

        due_date = input(
            "Digite a data de prazo (dd/mm/aaaa): "
        ).strip()

        # Verifica se o título está vazio
        if not title:
            print(Fore.RED + "A tarefa não pode estar vazia!")
            input("\nPressione ENTER para continuar...")

        else:
            # Adiciona a tarefa no banco
            add_task(title, priority, category, due_date)

            print("Tarefa adicionada com sucesso!")

            input("\nPressione ENTER para continuar...")
            continue

    # =========================
    # LISTAR TAREFAS
    # =========================
    elif option == "2":

        # Busca todas as tarefas
        tasks = list_tasks()

        # Mostra as tarefas
        display_tasks(tasks)

        input("\nPressione ENTER para continuar...")

    # =========================
    # CONCLUIR TAREFA
    # =========================
    elif option == "3":

        tasks = list_tasks()

        display_tasks(tasks)

        # Verifica se existem tarefas
        if "Nenhuma Tarefa" == display_tasks(tasks):
            pass

        else:
            task_id = input("Digite o ID da tarefa: ")

            # Tenta concluir a tarefa
            result = complete_task(task_id)

            # Verifica o resultado retornado
            if result == "success":
                print(Fore.GREEN + "Tarefa concluída com sucesso!")

            elif result == "already_completed":
                print(Fore.YELLOW + "Essa tarefa já está concluída!")

            else:
                print(Fore.RED + "Tarefa não encontrada!")

        input("\nPressione ENTER para continuar...")

    # =========================
    # DELETAR TAREFA
    # =========================
    elif option == "4":

        tasks = list_tasks()

        display_tasks(tasks)

        if "Nenhuma Tarefa" == display_tasks(tasks):
            input("\nPressione ENTER para continuar...")

        else:
            task_id = input("Digite o ID da tarefa: ")

            # Verifica se o usuário digitou apenas números
            if not task_id.isdigit():
                print(Fore.RED + "Digite um ID válido!")
                input("\nPressione ENTER para continuar...")
                continue

            # Deleta a tarefa
            success = delete_task(task_id)

            if success:
                print(Fore.GREEN + "Tarefa deletada com sucesso!")
                input("\nPressione ENTER para continuar...")

            else:
                print(Fore.RED + "Tarefa não encontrada!")

    # =========================
    # DASHBOARD
    # =========================
    elif option == "5":

        # Busca os dados do dashboard
        data = get_dashboard_data()

        print(Fore.CYAN + "\n=== DASHBOARD ===\n")

        # Exibe estatísticas
        print(f"Total de tarefas: {data['total']}")
        print(Fore.RED + f"Pendentes: {data['pending']}")
        print(Fore.GREEN + f"Concluídas: {data['completed']}")
        print(Fore.YELLOW + f"Alta prioridade: {data['high_priority']}")
        print(Fore.MAGENTA + f"Tarefas vencidas: {data['overdue']}")

        input("\nPressione ENTER para continuar...")

    # =========================
    # FILTROS
    # =========================
    elif option == "6":

        print("\n=== FILTROS ===")
        print("1 - Pendentes")
        print("2 - Concluídas")
        print("3 - Prioridade Alta")
        print("4 - Categoria")

        filter_option = input("Escolha um filtro: ")

        # Filtra pelo status pendente
        if filter_option == "1":
            tasks = filter_by_status("Pendente")

        # Filtra concluídas
        elif filter_option == "2":
            tasks = filter_by_status("Concluída")

        # Filtra alta prioridade
        elif filter_option == "3":
            tasks = filter_by_priority("Alta")

        # Filtra por categoria
        elif filter_option == "4":
            category = input("Digite a categoria: ")
            tasks = filter_by_category(category)

        else:
            print(Fore.RED + "Filtro inválido!")
            input("\nPressione ENTER para continuar...")
            continue

        display_tasks(tasks)

        input("\nPressione ENTER para continuar...")

    # =========================
    # PESQUISAR TAREFA
    # =========================
    elif option == "7":

        keyword = input(
            "Digite um termo para pesquisar: "
        ).strip()

        # Pesquisa tarefas contendo a palavra
        tasks = search_tasks(keyword)

        print("\n=== RESULTADOS ===")

        display_tasks(tasks)

        input("\nPressione ENTER para continuar...")

    # =========================
    # RESETAR BANCO
    # =========================
    elif option == "8":

        confirm = " "

        # Loop até o usuário digitar s ou n
        while confirm not in "sn":

            confirm = input(
                Fore.RED +
                "Tem certeza que deseja apagar TODAS as tarefas? (s/n): "
            ).lower()[0]

        if confirm == "s":

            # Apaga todas as tarefas
            reset_tasks()

            print(Fore.GREEN + "Banco resetado com sucesso!")

        elif confirm == "n":
            print(Fore.YELLOW + "Operação cancelada.")

        input("\nPressione ENTER para continuar...")

    # =========================
    # SAIR
    # =========================
    elif option == "9":

        print(Fore.CYAN + "Saindo...")
        break