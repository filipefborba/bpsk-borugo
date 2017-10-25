from tkinter import *
import tkinter as tk

class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x200")
        self.window.title("BPSK - Borugo")
        self.window.resizable(True, True)
        self.window.configure(bg = 'light gray')
        for i in range(4):
            self.window.rowconfigure(i, minsize=50)
        self.window.columnconfigure(0, minsize=300)

    def mainloop(self):
        self.window.mainloop()


#Loop do codigo
app = Interface()
app.mainloop()
