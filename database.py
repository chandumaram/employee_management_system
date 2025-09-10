"""
To connect python to MySql database, install pymysql package
"""

import pymysql
from tkinter import messagebox

def connect_database():
    global  mycursor, conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='Maram01ApR!')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error', 'Something went wrong')
        return

    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (Id VARCHAR(20), Name VARCHAR(50), Phone VARCHAR(15), Role VARCHAR(50), Gender VARCHAR(20), Salary DECIMAL(10,2))')

def fetch_emps():
    sql_selectall_query = "SELECT * FROM data"
    mycursor.execute(sql_selectall_query)
    result = mycursor.fetchall()
    return result

def id_exists(emp_id):
    sql_exists_query = "SELECT COUNT(*) FROM data WHERE Id=%s"
    mycursor.execute(sql_exists_query, emp_id)
    exists_result = mycursor.fetchone()
    return exists_result[0]>0

def insert(emp_id, name, phone, role, gender, salary):
    sql_insert_query = "INSERT INTO data (Id, Name, Phone, Role, Gender, Salary) VALUES (%s, %s, %s, %s, %s, %s)"
    insert_values = (emp_id, name, phone, role, gender, salary)
    mycursor.execute(sql_insert_query, insert_values)
    conn.commit()

def update(emp_id, name, phone, role, gender, salary):
    sql_update_query = "UPDATE data SET Name=%s, Phone=%s, Role=%s, Gender=%s, Salary=%s WHERE Id=%s"
    update_values = (name, phone, role, gender, salary, emp_id)
    mycursor.execute(sql_update_query, update_values)
    conn.commit()

def delete(emp_id):
    sql_delete_query = "DELETE FROM data WHERE Id=%s"
    mycursor.execute(sql_delete_query, emp_id)
    conn.commit()

def search(search_column, search_value):
    sql_search_query = f"SELECT * FROM employee_data.data where {search_column} LIKE '%{search_value}%'"
    mycursor.execute(sql_search_query)
    search_result = mycursor.fetchall()
    return search_result

def delete_all():
    sql_delete_all_query = "TRUNCATE TABLE data"
    # sql_delete_all_query = "DELETE TABLE data"
    mycursor.execute(sql_delete_all_query)
    conn.commit()



connect_database()