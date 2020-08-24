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

root = Tk()
root.title("Manga DB")
root.geometry('400x400+100+20') # Starting size/position: width x height + leftDistance + topDistance
root.minsize(200,200) #Minimum size: width, height

#Frame mainwindow for the heading to be done.
root.config(background='#CFD8DC', container='true', height='200', highlightbackground='#cfcfcf')
root.config(highlightcolor='#cfcfcf', relief='raised', width='200')
root.pack(side='top')

#mainwindow Label (the title on the top of the program)
#mainLbl = tk.Label(root ,anchor='center' , background="#607D8B", compound='top', font=('Segoe UI Semibold', 16 ), foreground="#ffffff", justify='center' , text= 'MangaDB')
#mainLbl.pack(fill='x')

#treeview Frame
treeviewFrm= Frame(root, bg='gray')
treeviewFrm.pack()

#Actual treeview
DB =  ttk.Treeview.master() #done to create basic treeview functions



root.mainloop()
