import tkinter as tk
from tkinter import messagebox, filedialog
import pyfiglet
import os

class app():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ASCII TEXT")
        self.window.geometry("1178x718")


        self.window.mainloop()

if __name__=="__main__":
    app()
