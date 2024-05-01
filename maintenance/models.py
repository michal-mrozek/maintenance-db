from maintenance import db


class Machine(db.Model):
    # schema for the Machine model
    id = db.Column(db.Integer, primary_key=True)
    machine_name = db.Column(db.String(25), unique=True, nullable=False)
    machine_model = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="machine", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f'{self.machine_name} - {self.machine_model}'


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    task_date = db.Column(db.Date, nullable=False)
    task_due_date = db.Column(db.Date, nullable=False)
    machine_id = db.Column(db.Integer, db.ForeignKey("machine.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f'#{self.id} - Task: {self.task_name} due to: {self.due_date}'