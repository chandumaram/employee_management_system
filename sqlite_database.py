"""
SQLite version of the Employee Management System database.
This replaces MySQL and allows the app to be fully portable.
"""

import sqlite3
import os
from tkinter import messagebox

# Database file (will be created in the same folder as the .exe)
DB_FILE = os.path.join(os.path.abspath("."), "sqlite_ems.db")

# Function to get connection
def get_connection():
    return sqlite3.connect(DB_FILE)

# Initialize database and table
def init_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data (
                Id TEXT PRIMARY KEY,
                Name TEXT,
                Phone TEXT,
                Role TEXT,
                Gender TEXT,
                Salary REAL
            )
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror('Error', f'Something went wrong while initializing the database: {e}')

# Fetch all employees
def fetch_emps():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data")
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        messagebox.showerror('Error', f'Failed to fetch data: {e}')
        return []

# Check if ID exists
def id_exists(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM data WHERE Id=?", (emp_id,))
        exists = cursor.fetchone()[0] > 0
        conn.close()
        return exists
    except Exception as e:
        messagebox.showerror('Error', f'Failed to check ID: {e}')
        return False

# Insert employee
def insert(emp_id, name, phone, role, gender, salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO data (Id, Name, Phone, Role, Gender, Salary) VALUES (?, ?, ?, ?, ?, ?)",
                       (emp_id, name, phone, role, gender, salary))
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror('Error', f'Failed to insert data: {e}')

# Update employee
def update(emp_id, name, phone, role, gender, salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE data
            SET Name=?, Phone=?, Role=?, Gender=?, Salary=?
            WHERE Id=?
        """, (name, phone, role, gender, salary, emp_id))
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror('Error', f'Failed to update data: {e}')

# Delete employee
def delete(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM data WHERE Id=?", (emp_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror('Error', f'Failed to delete data: {e}')

# Search employee
def search(search_column, search_value):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM data WHERE {search_column} LIKE ?"
        cursor.execute(query, ('%' + search_value + '%',))
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        messagebox.showerror('Error', f'Failed to search data: {e}')
        return []

# Delete all employees
def delete_all():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM data")
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror('Error', f'Failed to delete all data: {e}')


# Call initialization at import
init_db()