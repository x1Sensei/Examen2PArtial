from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas inicial
tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Agregar nueva tarea
        task = request.form.get("task")
        if task:
            tasks.append({"task": task, "done": False})
        return redirect(url_for("home"))
    return render_template("index.html", tasks=tasks)

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    # Marcar tarea como completada
    tasks[task_id]["done"] = True
    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    # Eliminar tarea
    tasks.pop(task_id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

