from flask import render_template, request, redirect, url_for
from maintenance import app, db
from maintenance.models import Machine, Task


@app.route("/")
def home():
    return render_template("tasks.html")

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


