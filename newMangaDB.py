#
#=========================
#|             MANGA DATABASE             |
#=========================

#programmer: Kyle Santos
#FEATURES:  Does a Treeview Database to store data
#Has a key ID for the search bar
#Can delete data from treeview
#has the option whether to make the  Manga title dropedd/complete/On Hold
#3rd revision due to pygubu (my fault)  wasting my time, so compromises must be made




#main window for the  database
from tkinter import  *
import tkinter as tk
from tkinter import  ttk
from tkinter import  messagebox
import mysql.connector




root = Tk()
root.title("Manga DB")
root.geometry('400x400+100+20') # Starting size/position: width x height + leftDistance + topDistance
root.minsize(200,200) #Minimum size: width, height

#Frame mainwindow for the heading to be done.
root.config()


#mainwindow Label (the title on the top of the program)
#mainLbl = tk.Label(root ,anchor='center' , background="#607D8B", compound='top', font=('Segoe UI Semibold', 16 ), foreground="#ffffff", justify='center' , text= 'MangaDB')
#mainLbl.pack(fill='x')

#local mySQL creation for database
mdb = mysql.connector.connect(host="localhost",
                              user="shorts",
                              password="shorts",
                              port=3306
)
cursor = mdb.cursor()
cursor.execute("SHOW DATABASES")
cc = print(cursor.execute())

cDB = input("Would you like to create a database?: (y/n)")
if cDB == 'y':
    cursor.execute("SHOW DATABASES")
    cursor
#function to ask user to create a database
def create():

#These frames are created for  the Database
wrapperDB = LabelFrame(root, text="Manga Database")
wrapperDB.pack(fill="both", expand= "yes")
frmSch = Frame(root, text="Search")
frmSch.pack()
frmEntries = Frame(root)
frmEntries.pack()

#Actual treeview
DB =  ttk.Treeview(wrapperDB,  columns=(1,2,3,4), show="headings", height="6") #done to create basic treeview functions
DB.column(0, width=270, minwidth=270, stretch=Tk.NO)
DB.column(1, width=150, minwidth=150, stretch=Tk.NO)
DB.column(2, width=400, minwidth=200)
DB.column(3, width=80, minwidth=50, stretch=Tk.NO)
DB.column(4, width=80, minwidth=50, stretch=Tk.NO)

#treeview heading, they' are for the columns
DB.heading(0, text="ID", anchor=Tk.W)
DB.heading(1, text="Author", anchor=Tk.W)
DB.heading(2, text="Title", anchor=Tk.W)
DB.heading(3, text="Chapter", anchor=Tk.W)
DB.heading(4, text="Status", anchor=Tk.W)

#functions
def  update():
    for i in rows:
        DB.insert(' ', 'end', values=i)

#query for  mySQL
query= "SELECT id, manga_author, manga_title, manga_chapter, manga_status"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)



root.mainloop()
