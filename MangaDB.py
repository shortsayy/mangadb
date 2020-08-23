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
 
root.mainloop()
