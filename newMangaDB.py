#
# =========================
# |             MANGA DATABASE             |
# =========================

# programmer: Kyle Santos
# FEATURES:  Does a Treeview Database to store data
# Has a key ID for the search bar
# Can delete data from treeview
# has the option whether to make the  Manga title dropedd/complete/On Hold
# 3rd revision due to pygubu (my fault)  wasting my time, so compromises must be made


# main window for the  database
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


# mainwindow Label (the title on the top of the program)
# mainLbl = tk.Label(root ,anchor='center' , background="#607D8B", compound='top', font=('Segoe UI Semibold', 16 ), foreground="#ffffff", justify='center' , text= 'MangaDB')
# mainLbl.pack(fill='x')

# functions
def update(rows):
    DB.delete(*DB.get_children())  # gets
    for i in rows:
        DB.insert(' ', 'end', values=i)


def search():
    q = schVar.get()
    query = "SELECT id FROM Author, Title, Chapter, Status WHERE Author LIKE '%" + q + "%' OR Title LIKE '%" + q + "%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def clear():
    query = "SELECT ID, Author, Title, Chapter, Status"
    cursor.execute(query)
    rows = cursor.fetchall(rows)
    update(rows)


# local mySQL creation for database
mdb = mysql.connector.connect(host="localhost",
                              user="shorts",
                              password="shorts",
                              port=3306,
                              database="mangadatabase",
                              auth_plugin="mysql_native_password"
                              )
cursor = mdb.cursor(buffered=True)  # buffered cursor means that the database will fetch all rows
cursor.execute("SHOW DATABASES")

# cursor.execute("CREATE DATABASE mangadatabase")
# cc = print(cursor.execute())


# if else statement for a function below(incomplete, prototype)
# cDB = input("Would you like to create a database?: (y/n)")
# if cDB == 'y':
# cursor.execute("SHOW DATABASES")
# cursor

# function to ask user to create a database
# def create():

# These frames are created for  the Database
root = Tk()
schVar = StringVar()
wrapperDB = LabelFrame(root, text="Manga Database")
wrapperDB.pack(fill="both", expand="yes")
frmSch = Frame(root)
frmSch.pack()
frmEntries = Frame(root)
frmEntries.pack()

# Actual treeview
DB = ttk.Treeview(wrapperDB, columns=(1, 2, 3, 4, 5), show="headings",
                  height="6")  # done to create basic treeview functions
#treeview heading, they' are for the columns
DB.heading(1, text="ID")
DB.heading(2, text="Author")
DB.heading(3, text="Title")
DB.heading(4, text="Chapter")
DB.heading(5, text="Status")
DB.pack()


# search bar section etc
lblSearch = Label(frmSch, text="Search")
lblSearch.pack(side=tk.LEFT, padx=10)
schEnt = Entry(frmSch,
               textvariable=schVar)  # textvariable is where a text associates with a StringVar to the contents of an Entry field.
schEnt.pack(side=tk.LEFT, padx=6)
schBtn = Button(frmSch, text="Search Manga", command=search)
schBtn.pack(side=tk.LEFT, padx=6)
clsBtn = Button(frmSch, text="Clear", command=clear)
clsBtn.pack(side=tk.LEFT, padx=6)

root.title("Manga DB")
root.geometry('400x400+100+20')  # Starting size/position: width x height + leftDistance + topDistance
root.minsize(200, 200)  # Minimum size: width, height

root.mainloop()
