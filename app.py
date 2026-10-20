
from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=EmployeeDB;"
    "Trusted_Connection=yes;"
)


# HOME PAGE - Display employees
@app.route('/')
def index():
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()

    return render_template('index.html', employees=employees)


# ADD EMPLOYEE
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']

        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO Employees (name, email, department) VALUES (?, ?, ?)",
            (name, email, department)
        )

        conn.commit()

        return redirect(url_for('index'))

    return render_template('add.html')


# EDIT EMPLOYEE
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']

        cursor.execute(
            "UPDATE Employees SET name=?, email=?, department=? WHERE id=?",
            (name, email, department, id)
        )

        conn.commit()

        return redirect(url_for('index'))

    cursor.execute(
        "SELECT * FROM Employees WHERE id=?",
        (id,)
    )

    employee = cursor.fetchone()

    return render_template('edit.html', employee=employee)


# DELETE EMPLOYEE
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM Employees WHERE id=?",
        (id,)
    )

    conn.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
