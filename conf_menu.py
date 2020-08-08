from tkinter import *

class Conf_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        self.barra_FyH = Frame(self.root_frame.main_container, bd=3,
            bg="gray", relief=RIDGE)
        self.barra_FyH.pack(padx=10, pady=10)
        self.FyH_label = Label(self.barra_FyH, text="Fecha y Hora",
            bg="gray", fg="white", font=self.root.myFont)
        self.FyH_label.pack(padx=120, pady=10)
