import tkinter as tk
from tkinter import messagebox, filedialog
import pyfiglet
import os

class app():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ASCII TEXT")
        self.window.geometry("1180x718")

        self.current_dir = tk.StringVar()
        self.current_dir.set(os.getcwd())
        
        self.entryDir = tk.Entry(self.window,width=196,textvariable=self.current_dir)
        self.entryDir.place(x=0,y=0)

        self.window.mainloop()

if __name__=="__main__":
    app()

