from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)
from tasks import (
    list_tasks,
    get_dashboard_data,
    add_task,
    complete_task,
    delete_task,
    filter_tasks,
    reset_tasks
)

app = Flask(__name__)

# =========================
# PÁGINA PRINCIPAL
# =========================
@app.route("/")
def home():

    search = request.args.get("search", "")
    status = request.args.get("status", "")
    priority = request.args.get("priority", "")
    order = request.args.get("order", "")

    tasks = filter_tasks(
        search,
        status,
        priority,
        order
    )

    dashboard = get_dashboard_data()

    return render_template(
        "index.html",
        tasks=tasks,
        dashboard=dashboard,
        search=search,
        status=status,
        priority=priority,
        order=order
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
        due_date
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


# =========================
# RESETAR BANCO
# =========================
@app.route("/reset", methods=["POST"])
def reset():

    reset_tasks()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)