# Maintenance DB Web Application

---


The website is live, can be found [Click](https://maintenance-db-mm-87fcc874b709.herokuapp.com/)

![Site view across devices](/maintenance/static/media/responsiveness.png)

---

## Overview
This README provides an overview of the Maintenance Database (DB) Web Application, detailing its features, installation instructions, and usage guidelines.

---

**User Story:**
As a *maintenance* engineer, I want to *efficiently manage tasks* for our facility's equipment, ensuring *optimal functioning* and *minimizing downtime*.

**Acceptance Criteria:**
1. **Dashboard Overview:**
   - I should see a *dashboard* displaying key metrics such as *upcoming tasks*, and *overdue tasks*.
   - The dashboard should provide a *clear summary* of maintenance activities to help me *prioritize tasks* effectively.

2. **Maintenance Records Management:**
   - I should be able to *add* new maintenance tasks, specifying details such as *equipment type*, *description*, and *scheduled date*.
   - I should be able to *view* a list of existing maintenance tasks, with options to *edit* or *delete tasks* as needed.
   - Changes made to maintenance records should be *immediately reflected* in the system.

3. **Access Control:**
   - As a supervisor, I should have *full access* to all features of the application, including *adding, editing, and deleting* maintenance records.

---

## Features

1. **Navbar** Provides an easy reference to navigate between the 'Home', 'list of the Machines'and 'form to add task'.

![Navbar](/maintenance/static/media/navbar.png)

2. **Dashboard:** User-friendly display of key metrics.

![Dashboard with list of tasks](/maintenance/static/media/tasks.png)

3. **Machine Records:** CRUD functionality for tasks.
   *ADD*
   
![Form to add machine](/maintenance/static/media/add-machine-form.png)

   *READ, UPDATE & DELETE*

![Dashboard with list of machines](/maintenance/static/media/machines.png)

4. **Maintenance Task Records:** CRUD functionality for tasks, behave in same manner as machine's CRUD.

![Dashboard with list of tasks](/maintenance/static/media/tasks.png)

![form to add task](/maintenance/static/media/add-task-form.png)


5. **Upcoming and overdue tasks** Overdue tasks are marked in red, upcoming task in 2 week time are marked in yellow. (printscreen made on 05/05/2024)

![Upcoming and overdue](/maintenance/static/media/overdue.png)

---

## Manual Testing

1. **Dashboard:**
- Check if the dashboard displays accurate and updated information.
- Test responsiveness across different devices and screen sizes.

2. **Maintenance Records Management:**
- Add a new maintenance task and verify it appears correctly.
- Edit an existing task and ensure changes are saved.
- Delete a task and confirm it is removed from the database.
- Test edge cases (e.g., adding tasks with missing information).

---

## Installation

1. **Clone Repository:** `git clone https://github.com/michal-mrozek/maintenance-db.git`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Database Setup:** Configure and run migrations.
4. **Environment Variables:** Set up `.env` file.
5. **Start Application:** `python app.py`
6. **Access Application:** http://localhost:5000

---

## Credit

Project inspired by a project I made while studying with codeinstitute [task manager]
The application utilize Bootstrap's grid system for responsive design, ensuring compatibility with various devices and screen sizes.

---

## Contributing

Contributions welcome! Submit bug reports or suggestions via the pull request.

---

## License

Licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## Contact

For support, email [maintenance@example.com](mailto:maintenance@example.com).

---

## Authors

- [Author Name](https://github.com/michal-mrozek)

---


