# Employee Management System (EmployeeHub)

A beginner-friendly employee management web application built with **Python Flask**, **Microsoft SQL Server**, **pyodbc**, **HTML**, and **CSS**. It provides a dashboard for viewing employee records and performing basic CRUD operations.

## Features

- View employees in a dashboard table
- Add an employee with name, email, and department
- Edit an existing employee's details
- Delete an employee
- Store employee records in Microsoft SQL Server

## Tech Stack

- **Backend:** Python, Flask
- **Database:** Microsoft SQL Server, pyodbc
- **Frontend:** HTML, CSS, Jinja2 templates

## Project Structure

```text
Employee-Management-System/
├── app.py
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
├── static/
│   └── style.css
├── schema.sql
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started (Local Development)

### Prerequisites

- Python 3
- Microsoft SQL Server running locally
- Microsoft ODBC Driver 17 for SQL Server
- Windows Authentication configured for your SQL Server instance

### 1. Create the database and table

Open SQL Server Management Studio, connect to your local SQL Server instance, and execute `schema.sql`.

**Note:** The script creates a database/table if missing; it does not insert employee data.

### 2. Install dependencies

From the project folder, create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Check your database connection

In `app.py`, the connection currently uses:

```text
SERVER=localhost;DATABASE=EmployeeDB;Trusted_Connection=yes;
```

Update `SERVER` to match your local SQL Server instance if needed. The app expects ODBC Driver 17 and Windows Authentication. Never commit database passwords or other secrets.

### 4. Run the application

```powershell
python app.py
```

Open **http://127.0.0.1:5000/** in your browser.

## How It Works

Flask handles routes for listing, adding, editing, and deleting employees. SQL statements executed through pyodbc read and modify records in SQL Server. Flask renders Jinja2 HTML templates styled with CSS.

## Notes

- This is a **learning project**, intended for local development.
- The current application runs with Flask debug mode enabled; do not expose the development server publicly.
- This version uses Flask-rendered HTML templates; **React and REST API endpoints are not yet implemented**.
- Uploading source code to GitHub does not deploy a live website or upload your local SQL Server database.

## Planned Improvements

- REST API endpoints returning JSON
- React frontend
- Form validation and improved error handling
- Production deployment and safer database configuration
