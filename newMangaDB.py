#
# =========================
# |             MANGA DATABASE             |
# =========================

# programmer: Kyle Santos
# FEATURES:  Does a Treeview Database to store data
# Has a key ID for the search bar
# Can delete data from treeview
# has the option whether to make the  Manga title dropped/complete/On Hold
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

# functions
def search():
    q = schVar.get()
    query = "SELECT ID FROM Author, Title, Chapter, Status WHERE Author LIKE '%" + q + "%' OR Title LIKE '%" + q + "%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def update(rows):
    DB.delete(*DB.get_children())  # gets
    for i in rows:
        DB.insert('', 'end', values=i)

def add_mangadb():
    au = t2.get()#author
    ttl = t3.get()#title
    chp = t4.get()#chapter
    sts = t5.get()#status
    add = "INSERT INTO mangatable(ID, Author, Title, Chapter, Status) VALUES(NULL, %s, %s, %s, %s)"
    cursor.execute(add, (au, ttl, chp, sts))
    clear()

def clear():
    query = "SELECT ID, Author, Title, Chapter, Status FROM mangatable"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)


def fetch(event):
    rowid = DB.identify_row(event.y)
    item = DB.item(DB.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])

def update_mangadb():
    return True

def delete_mangadb(): #THIS NEEDS FIXING
    #prompt to ask if user is sure to delete database
    try:
        confirm = tk.messagebox.askquestion('Delete manga', 'are you sure to delete manga?')
        if confirm == 'yes':
            authordata = t2.get()
            query = "DELETE FROM mangatable WHERE Author = %s"
            data = (authordata,)
            cursor.execute(query, authordata)
            tk.messagebox.showinfo('Delete manga', "Deleted: %d" % cursor.rowcount)
            clear()
            root.destroy()
        else:
            tk.messagebox.showinfo('Return','Deletion cancelled.')
    except mysql.connector.Error as err: #done this to error check what happens if data fails to delete
        print("Error:", err.message)

# These frames are created for the Database
root = Tk()
schVar = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar() #This is stringint because this is the chapter one, where you need numbers to input data
t5 = StringVar()
# wrapper and frames
wrapperDB = LabelFrame(root, text="Manga Database")
wrapperDB.pack(fill="both")
frmSch = Frame(root)
frmSch.pack()
frmEntries = Frame(root)
frmEntries.pack()

# Actual treeview
DB = ttk.Treeview(wrapperDB, columns=(1, 2, 3, 4, 5), show="headings",
                  height="6")  # done to create basic treeview functions

# treeview heading, they' are for the columns
DB.heading(1, text="ID")
DB.heading(2, text="Author")
DB.heading(3, text="Title")
DB.heading(4, text="Chapter")
DB.heading(5, text="Status")
DB.bind('<Double 1>', fetch)
DB.pack()

query= "SELECT ID, Author, Title, Chapter, Status FROM mangatable"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

# search bar section etc
lblSearch = Label(frmSch, text="Search")
lblSearch.pack(side=tk.LEFT, padx=10)
schEnt = Entry(frmSch,
               textvariable=schVar)  # textvariable is where a text associates with a StringVar to the contents of an
# Entry field.
schEnt.pack(side=tk.LEFT, padx=6)
schBtn = Button(frmSch, text="Search Manga", command=search)
schBtn.pack(side=tk.LEFT, padx=6)
clsBtn = Button(frmSch, text="Clear", command= clear)
clsBtn.pack(side=tk.LEFT, padx=6)

# Manga field Labels, Entries, and Buttons
lblID = Label(frmEntries, text="ID") #Needed primary key to be able to count manga
lblID.grid(column=0, row=0, padx=5, pady=3)
entID = Entry(frmEntries, textvariable=t1)
entID.grid(column=1, row=0, padx=5, pady=3)

lblAuth = Label(frmEntries, text="Author")
lblAuth.grid(column=0, row=1, padx=5, pady=3)
entAuth = Entry(frmEntries, textvariable=t2)
entAuth.grid(column=1, row=1, padx=5, pady=3)

lblTitle = Label(frmEntries, text="Title")
lblTitle.grid(column=0, row=2, padx=5, pady=3)
entTitle = Entry(frmEntries, textvariable=t3)
entTitle.grid(column=1, row=2, padx=5, pady=3)

lblChp = Label(frmEntries, text="Chapters")
lblChp.grid(column=0, row=3, padx=5, pady=3)
entChp = Entry(frmEntries, textvariable=t4)
entChp.grid(column=1, row=3, padx=5, pady=3)

lblSts = Label(frmEntries, text="Status")
lblSts.grid(column=0, row=4, padx=5, pady=3)
cbSts = ttk.Combobox(frmEntries, values=[
    "",
    "Completed",
    "On Hold",
    "Dropped"
], textvariable=t5)
cbSts.grid(column=1, row=4, padx=5, pady=3)

btnUpdate = Button(frmEntries, text="Update Database", command= update_mangadb)
btnUpdate.grid(row=2, column=3, padx=5, pady=3)

btnAdd = Button(frmEntries, text="Add to Database", command= add_mangadb)
btnAdd.grid(row=3, column=3, padx=5, pady=3)

btnDel = Button(frmEntries, text="Delete Data", command= delete_mangadb)
btnDel.grid(row=4, column=3, padx=5, pady=3)

root.title("Manga DB")
root.geometry('800x800')  # Starting size/position: width x height + leftDistance + topDistance
root.minsize(200, 200)  # Minimum size: width, height

root.mainloop()
