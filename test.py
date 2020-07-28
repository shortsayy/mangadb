import tkinter as  tk
import pygubu


class pp:
    def __init__(self):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('test2.ui')
        self.mainwindow = builder.get_object('mainWindow')

    def run (self):
        self.mainwindow.mainloop()

    def quit1 (self):
        self.mainwindow.quit()

if __name__ == '__main__':
    app = pp()
    app.run()
