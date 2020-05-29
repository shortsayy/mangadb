from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("MangaDB")
root.geometry("400x400")

#Actual database


#table creation
"""cDB.execute('''CREATE TABLE manga (
        title text,
        author text,
        chapters integer
        )''')"""

#create function to delete record
def delete():
    connectDB = sqlite3.connect('manga_database.db')
    cDB = connectDB.cursor()
#delete records
    cDB.execute("DELETE from manga WHERE oid = " + delBox.get())    





    connectDB.commit()
    #close conn
    connectDB.close()
#functions
def submit():
    #create or connect to database
    connectDB = sqlite3.connect('manga_database.db')
    #cursor instance
    cDB = connectDB.cursor()
    #insert to TABLE
    cDB.execute("INSERT INTO manga VALUES (:Title, :Author, :Chapters)",
            {
                'Title': titleDB.get(),
                'Author': authorDB.get(),
                'Chapters': chaptersDB.get()
            })
    #commit changes to db
    connectDB.commit()
    #close conn
    connectDB.close()
    #clear text boxes
    titleDB.delete(0, END)
    authorDB.delete(0, END)
    chaptersDB.delete(0, END)
#query function
def query():
    #create or connect to database
    connectDB = sqlite3.connect('manga_database.db')
    #cursor instances
    cDB = connectDB.cursor()

    #query db
    cDB.execute("SELECT *, oid FROM manga")
    records = cDB.fetchall()
    #loop thru results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[3]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


    #commit changes to db
    connectDB.commit()
    #close conn
    connectDB.close()


titleDB = Entry(root, width=30)
titleDB.grid(row= 0, column=1, padx=20, pady=(10, 0))

authorDB = Entry(root, width=30)
authorDB.grid(row= 1, column=1)

chaptersDB = Entry(root, width=30)
chaptersDB.grid(row= 2, column=1)

delBox = Entry(root, width=30)
delBox.grid(row=10, column=1)

#text box labels
titleLbl = Label(root, text="Title")
titleLbl.grid(row=0, column=0, pady=(10, 0))

authorLbl = Label(root, text="Author")
authorLbl.grid(row=1, column=0)

chaptersLbl= Label(root, text="Chapters")
chaptersLbl.grid(row=2, column=0)

delBoxLbl = Label(root, text="Delete Number")
delBoxLbl.grid(row=10, column=0, pady=5)

#submit button
submitBtn = Button(root, text="Add manga to database", command=submit)
submitBtn.grid(row=3, columnspan=2, pady=10, padx=10, ipadx=100)

#create query Button
queryBtn = Button(root, text="Check manga", command=query)
queryBtn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#create delete button
delBtn = Button(root, text="Delete manga", command=delete)
delBtn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
root.mainloop()
