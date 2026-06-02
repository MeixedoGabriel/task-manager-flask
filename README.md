# Task Manager Flask

Sistema web de gerenciamento de tarefas desenvolvido com Python, Flask e SQLite.

## Sobre o Projeto

O Task Manager Flask é uma aplicação web que permite criar, organizar e acompanhar tarefas de forma simples e eficiente.

O sistema possui autenticação de usuários, garantindo que cada usuário tenha acesso apenas às suas próprias tarefas, além de recursos de produtividade como dashboard, filtros e ordenação personalizada.

## Funcionalidades

* Cadastro de usuários
* Login e logout
* Senhas criptografadas com hash
* Sistema multiusuário
* CRUD completo de tarefas
* Dashboard de produtividade
* Pesquisa de tarefas
* Filtros por status
* Filtros por prioridade
* Ordenação personalizada
* Edição de tarefas
* Exclusão de tarefas
* Deploy em produção

## Tecnologias Utilizadas

### Backend

* Python
* Flask
* SQLite

### Frontend

* HTML5
* CSS3
* Jinja2

### Ferramentas

* Git
* GitHub
* Render

## Demonstração

Aplicação online:

https://task-manager-flask-ocxx.onrender.com

## Instalação

Clone o repositório:

```bash
git clone https://github.com/MeixedoGabriel/task-manager-flask.git
```

Entre na pasta:

```bash
cd task-manager-flask
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python app.py
```

## Estrutura do Projeto

```text
task-manager-flask
│
├── static/
├── templates/
├── app.py
├── auth.py
├── database.py
├── tasks.py
├── requirements.txt
├── Procfile
├── README.md
└── .gitignore
```

## Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

* Desenvolvimento web com Flask
* Banco de dados SQLite
* SQL (CRUD)
* Autenticação e sessões
* Hash de senhas
* Organização de código em módulos
* Deploy em produção
* Controle de versão com Git e GitHub

## Autor

Gabriel Meixedo

Estudante de Ciência da Computação com foco em desenvolvimento Back-End utilizando Python.

