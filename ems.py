from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
# import mysql_database as database
import sqlite_database as database
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Functions
def treeview_data():
    # fetch all employees from database
    employees = database.fetch_emps()
    # delete all data from tree
    tree.delete(*tree.get_children())
    # loop the all employees and add into tree
    for emp in employees:
        tree.insert('',END,values=emp)

def select_emp(event):
    selected_emp = tree.selection()
    if selected_emp:
        row = tree.item(selected_emp)['values']
        # first clear the data
        clear()
        # insert data into entries/fields
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    roleBox.set(role_options[0])
    genderBox.set(gender_options[0])
    salaryEntry.delete(0, END)

def add_emp():
    emp_id = idEntry.get()
    name = nameEntry.get()
    phone = phoneEntry.get()
    role = roleBox.get()
    gender = genderBox.get()
    salary = salaryEntry.get()
    if emp_id=='' or name=='' or phone=='' or role=='' or gender=='' or salary=='':
        messagebox.showerror('Error', "All fields are required.")
    elif database.id_exists(emp_id):
        messagebox.showerror('Error', "Id already exists.")
    else:
        database.insert(emp_id, name, phone, role, gender, salary)
        treeview_data()
        clear()
        messagebox.showinfo('Success', f'{emp_id} data is added.')

def update_emp():
    selected_emp = tree.selection()
    if not selected_emp:
        messagebox.showerror('Error', "No data is selected to update")
    else:
        emp_id = idEntry.get()
        name = nameEntry.get()
        phone = phoneEntry.get()
        role = roleBox.get()
        gender = genderBox.get()
        salary = salaryEntry.get()
        database.update(emp_id, name, phone, role, gender, salary)
        messagebox.showinfo('Success', f'{emp_id} data is updated.')
        treeview_data()
        clear()


def delete_emp():
    selected_emp = tree.selection()
    if not selected_emp:
        messagebox.showerror('Error', 'No data is selected to delete.')
    else:
        emp_id = idEntry.get()
        is_delete = messagebox.askyesno('Confirm', f'Are you sure you want to delete the employee {emp_id}?')
        if is_delete:
            database.delete(emp_id)
            treeview_data()
            clear()
            messagebox.showinfo("Success", f"{emp_id} data is deleted.")

def search_emp():
    search_option = searchBox.get()
    search_value = searchEntry.get()
    if search_option=="Search By" or search_option=='':
        messagebox.showerror('Error', 'Please select search option.')
    elif search_value=='':
        messagebox.showerror('Error', 'Please enter search value.')
    else:
        searched_employees = database.search(search_option, search_value)
        # delete all data from tree
        tree.delete(*tree.get_children())
        # loop the all employees and add into tree
        for emp in searched_employees:
            tree.insert('', END, values=emp)

def show_all():
    searchBox.set(search_options[0])
    searchEntry.delete(0, END)
    treeview_data()

def delete_all():
    is_delete_all = messagebox.askyesno('Confirm', 'Are you sure you want to delete all the records?')
    if is_delete_all:
        database.delete_all()
        treeview_data()
        clear()
        messagebox.showinfo("Success", f"All data deleted.")

# GUI Part
window = CTk()
window.geometry('930x580+100+75') # we fix the window display so added +100+100
window.resizable(False, False)
window.title('Employee Management System')
window.iconbitmap(resource_path("favicon.ico"))
window.configure(fg_color='#161C30')

logo = CTkImage(Image.open(resource_path('bg.jpg')), size=(930, 158))
logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0, column=0, columnspan=2)

# Right Frame Configuration
leftFrame = CTkFrame(window, fg_color='#161C30')
leftFrame.grid(row=1, column=0)

idLabel = CTkLabel(leftFrame, text='Id', font=('arial', 18, 'bold'), text_color='white')
idLabel.grid(row=0, column=0, padx=20, pady=10, sticky='w')
idEntry = CTkEntry(leftFrame, font=('arial', 15), width=180)
idEntry.grid(row=0, column=1)

nameLabel = CTkLabel(leftFrame, text='Name', font=('arial', 18, 'bold'), text_color='white')
nameLabel.grid(row=1, column=0, padx=20, pady=10, sticky='w')
nameEntry = CTkEntry(leftFrame, font=('arial', 15), width=180)
nameEntry.grid(row=1, column=1)

phoneLabel = CTkLabel(leftFrame, text='Phone', font=('arial', 18, 'bold'), text_color='white')
phoneLabel.grid(row=2, column=0, padx=20, pady=10, sticky='w')
phoneEntry = CTkEntry(leftFrame, font=('arial', 15), width=180)
phoneEntry.grid(row=2, column=1)

roleLabel = CTkLabel(leftFrame, text='Role', font=('arial', 18, 'bold'), text_color='white')
roleLabel.grid(row=3, column=0, padx=20, pady=10, sticky='w')
role_options = ['Web Developer', 'Data Scientist', 'Business Analytics', 'UX/UI Designer']
roleBox = CTkComboBox(leftFrame, values=role_options, font=('arial', 15), width=180, state='readonly')
roleBox.grid(row=3, column=1)
roleBox.set(role_options[0])

genderLabel = CTkLabel(leftFrame, text='Gender', font=('arial', 18, 'bold'), text_color='white')
genderLabel.grid(row=4, column=0, padx=20, pady=10, sticky='w')
gender_options = ['Male', 'Female']
genderBox = CTkComboBox(leftFrame, values=gender_options, font=('arial', 15), width=180, state='readonly')
genderBox.grid(row=4, column=1)
genderBox.set(gender_options[0])

salaryLabel = CTkLabel(leftFrame, text='Salary', font=('arial', 18, 'bold'), text_color='white')
salaryLabel.grid(row=5, column=0, padx=20, pady=10, sticky='w')
salaryEntry = CTkEntry(leftFrame, font=('arial', 15), width=180)
salaryEntry.grid(row=5, column=1)

# Right Frame Configuration
rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1)

search_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
searchBox = CTkComboBox(rightFrame, values=search_options, state='readonly')
searchBox.grid(row=0, column=0)
# searchBox.set('Search By')
searchBox.set(search_options[0])

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1)

searchButton = CTkButton(rightFrame, text='Search', width=100, command=search_emp)
searchButton.grid(row=0, column=2)

showallButton = CTkButton(rightFrame, text='Show All', width=100, command=show_all)
showallButton.grid(row=0, column=3, pady=5)

tree = ttk.Treeview(rightFrame, height=13)
tree.grid(row=1, column=0, columnspan=4)

tree['columns']= ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')
tree.heading('Id', text='Id')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Salary', text='Salary')

tree.config(show='headings')

tree.column('Id', width=100)
tree.column('Name', width=160)
tree.column('Phone', width=160)
tree.column('Role', width=200)
tree.column('Gender', width=100)
tree.column('Salary', width=140)

style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 18, 'bold'))
style.configure("Treeview", font=('arial', 15), rowheight=30, background='#161C30', foreground='white')

rightFrameScrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL, command=tree.yview)
rightFrameScrollbar.grid(row=1, column=4, sticky='ns')

tree.config(yscrollcommand=rightFrameScrollbar.set)


# Button Frame Configuration
buttonFrame = CTkFrame(window, fg_color='#161C30')
buttonFrame.grid(row=2, column=0, columnspan=2, pady=25)

newButton = CTkButton(buttonFrame, text='New Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command=lambda : clear(True))
newButton.grid(row=0, column=0, pady=5, padx=5)

addButton = CTkButton(buttonFrame, text='Add Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command=add_emp)
addButton.grid(row=0, column=1, pady=5, padx=5)

updateButton = CTkButton(buttonFrame, text='Update Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command=update_emp)
updateButton.grid(row=0, column=2, pady=5, padx=5)

deleteButton = CTkButton(buttonFrame, text='Delete Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command=delete_emp)
deleteButton.grid(row=0, column=3, pady=5, padx=5)

deleteAllButton = CTkButton(buttonFrame, text='Delete All', font=('arial', 15, 'bold'), width=160, corner_radius=15, command=delete_all)
deleteAllButton.grid(row=0, column=4, pady=5, padx=5)

# default load employees data
treeview_data()

# select employee for update
window.bind("<ButtonRelease>", select_emp)

window.mainloop()

