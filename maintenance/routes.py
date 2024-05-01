from flask import render_template
from maintenance import app, db
from maintenance.models import Machine, Task


@app.route("/")
def home():
    return render_template("tasks.html")