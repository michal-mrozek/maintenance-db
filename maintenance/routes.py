from flask import render_template, request, redirect, url_for
from maintenance import app, db
from maintenance.models import Machine, Task
from datetime import date, timedelta

#Home

@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks = tasks)

#Machines

@app.route("/machines")
def machines():
    machines = list(Machine.query.order_by(Machine.machine_name).all())
    return render_template("machines.html", machines = machines)


@app.route("/add_machine", methods = ["GET", "POST"])
def add_machine():
    if request.method == "POST":
        machine = Machine(
            machine_name = request.form.get("machine_name"),
            machine_model = request.form.get("machine_model"))
        db.session.add(machine)
        db.session.commit()
        return redirect(url_for("machines"))
    return render_template("add_machine.html")


@app.route("/edit_machine/<int:machine_id>", methods = ["GET", "POST"])
def edit_machine(machine_id):
    machine = Machine.query.get_or_404(machine_id)
    if request.method == "POST":
        machine.machine_name = request.form.get("machine_name")
        machine.machine_model = request.form.get("machine_model")
        db.session.add(machine)
        db.session.commit()
        return redirect(url_for("machines"))  
    return render_template("edit_machine.html", machine = machine)


@app.route("/delete_machine/<int:machine_id>")
def delete_machine(machine_id):
    machine = Machine.query.get_or_404(machine_id)
    db.session.delete(machine)
    db.session.commit()
    return redirect(url_for("machines"))

#Tasks

@app.route("/add_task", methods = ["GET", "POST"])
def add_task():
    today = date.today()
    machines = list(Machine.query.order_by(Machine.machine_name).all())
    if request.method == "POST":
        task = Task(
            task_name = request.form.get("task_name"),
            task_description = request.form.get("task_description"),
            task_date = today,
            task_due_date = today + timedelta(days=90),
            machine_id = request.form.get("machine_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", machines = machines)


@app.route("/edit_task/<int:task_id>", methods = ["GET", "POST"])
def edit_task(task_id):
    machines = list(Machine.query.order_by(Machine.machine_name).all())
    task = Task.query.get_or_404(task_id)
    if request.method == "POST":
        
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home"))  
    return render_template("edit_task.html",machines = machines,task = task)


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))

    

