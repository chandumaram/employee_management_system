# Employee Management System 
Created Using Python, Custom-Tkinter and MySQL

## Setup Application
- Download/get code from github 
    `https://github.com/chandumaram/employee_management_system#`

- (Optional) If you want create virtual environment the run the following command 
    `virtualenv venv`
    - Then activate virtual environment for that run 
        `venv\Scripts\activate` 

- Install all required python packages 
    `pip install -r .\requirements.txt`

- In this project we are using MySQL and SQLite databases
    - If you want to use MySQL as database, so you need to download and setup MySQL in your system
        - After installed MySQL, Open `mysql_database.py` file and replace your password in line 11
        - Open `ems.py` file, un-comment the line `import mysql_database as database` and comment the line `import sqlite_database as database`

    - If you want to use SQLite as database, noneed to install anything
        - Just open `ems.py` file, un-comment the line `import sqlite_database as database` and comment the line `import mysql_database as database`

- Then run `login.py` file to up the project


## To convert this application as .exe file
- Run the following command 
    - if you use MySQL database
    `pyinstaller --onefile --noconsole --icon="C:\path\to\favicon.ico" --add-data "cover.jpg;." --add-data "bg.jpg;." --add-data "favicon.ico;." login.py
    `
    - if you use SQLite database
    `pyinstaller --onefile --noconsole --icon="C:\path\to\favicon.ico" --add-data "cover.jpg;." --add-data "bg.jpg;." --add-data "favicon.ico;." --add-data "sqlite_ems.db;." login.py
    `

- Then it will create build and dist folders and login.spec file

- Our `login.exe` file is placed inside the dist folder

