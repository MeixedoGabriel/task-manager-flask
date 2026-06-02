from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)
from tasks import (
    list_tasks,
    get_dashboard_data,
    add_task,
    complete_task,
    delete_task,
    filter_tasks,
    reset_tasks,
    get_task,
    update_task
)

from database import create_table

from auth import (
    register_user,
    login_user,
    get_username
)

app = Flask(__name__)

app.secret_key = "minha_chave_super_secreta"

create_table()

# =========================
# PÁGINA PRINCIPAL
# =========================
@app.route("/")
def home():

    if "user_id" not in session:
        return redirect(url_for("login"))

    search = request.args.get("search", "")
    status = request.args.get("status", "")
    priority = request.args.get("priority", "")
    order = request.args.get("order", "")

    tasks = filter_tasks(
        session["user_id"],
        search,
        status,
        priority,
        order
    )

    dashboard = get_dashboard_data(
        session["user_id"]
    )
    
    username = get_username(
        session["user_id"]
    )

    return render_template(
        "index.html",
        tasks=tasks,
        dashboard=dashboard,
        search=search,
        status=status,
        priority=priority,
        order=order,
        username=username
    )


# =========================
# ADICIONAR TAREFA
# =========================
@app.route("/add", methods=["POST"])
def add_new_task():

    title = request.form["title"]
    priority = request.form["priority"]
    category = request.form["category"]
    due_date = request.form["due_date"]

    add_task(
        title,
        priority,
        category,
        due_date,
        session["user_id"]
    )

    return redirect(url_for("home"))


# =========================
# CONCLUIR TAREFA
# =========================
@app.route("/complete/<int:task_id>") # /complete/ seguido de um número inteiro, que será passado para a função complete como argumento task_id
def complete(task_id):

    complete_task(task_id)

    return redirect(url_for("home"))


# =========================
# DELETAR TAREFA
# =========================
@app.route("/delete/<int:task_id>") # /delete/ seguido de um número inteiro, que será passado para a função delete como argumento task_id
def delete(task_id):

    delete_task(task_id)

    return redirect(url_for("home"))


@app.route(
    "/edit/<int:task_id>",
    methods=["GET", "POST"]
)
def edit(task_id):

    if request.method == "POST":

        title = request.form["title"]
        priority = request.form["priority"]
        category = request.form["category"]
        due_date = request.form["due_date"]

        update_task(
            task_id,
            title,
            priority,
            category,
            due_date
        )

        return redirect(url_for("home"))

    task = get_task(task_id)

    return render_template(
        "edit_task.html",
        task=task
    )


# =========================
# RESETAR BANCO
# =========================
@app.route("/reset", methods=["POST"])
def reset():

    reset_tasks(
        session["user_id"]
    )

    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        result = register_user(
            username,
            password
        )

        if result is True:
            return redirect(url_for("login"))

        if result == "weak_password":

            return render_template(
                "register.html",
                error="""
        A senha deve possuir pelo menos 6 caracteres,
        1 letra e 1 número.
        """
            )

        return render_template(
            "register.html",
            error="Usuário já existe."
        )

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user_id = login_user(
            username,
            password
        )

        if user_id:

            session["user_id"] = user_id

            return redirect(url_for("home"))

        return render_template(
            "login.html",
            error="Usuário ou senha inválidos."
        )

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)