from customtkinter import *
from PIL import Image
from tkinter import messagebox, PhotoImage
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All fields are required')
    elif usernameEntry.get().lower()=='chandu' and passwordEntry.get().lower()=='1234':
        messagebox.showinfo('Success', 'Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'Wrong credentials')


root = CTk()
root.title("Login")
root.iconbitmap(resource_path("favicon.ico"))
root.geometry("930x478")
root.resizable(False, False)

# Load and display the image
image = CTkImage(Image.open(resource_path("cover.jpg")), size=(930, 478))
imageLabel = CTkLabel(root, image=image, text="")
imageLabel.place(x=0, y=0)

# Heading label
headingLabel = CTkLabel(root, text="Employee Management System", bg_color="#FFFFFF", font=('Goudy Old Style', 20, 'bold'), text_color="dark blue")
headingLabel.place(x=20, y=100)

# Login Inputs
usernameEntry = CTkEntry(root, placeholder_text="Enter Your Username", width=180)
usernameEntry.place(x=50, y=150)

passwordEntry = CTkEntry(root, placeholder_text="Enter Your Password", width=180, show='*')
passwordEntry.place(x=50, y=200)

loginButton = CTkButton(root, text='Login', cursor='hand2', command=login)
loginButton.place(x=70, y=250)

root.mainloop()