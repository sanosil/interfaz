from tkinter import *

class Program_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame

        self.create_widgets()

    def create_widgets(self):
        self.main = Frame(self.root_frame, bg="white")
        self.main.grid(sticky=W, column=0, row=1)

        self.frame_programa = Frame(self.main, bg="white")
        self.frame_programa.grid(column=0, row=0, sticky=W, padx=20, pady=10)

        self.frame_titulo_programa = Frame(self.frame_programa, bg="white",
            relief=RIDGE, bd=3)
        self.frame_titulo_programa.grid(column=0, row=0, sticky=W)
        self.titulo = Label(self.frame_titulo_programa, bg="white",
            text="Programa", font=("Verdana", 15, "bold"))
        self.titulo.pack(padx=30, pady=5)
        
