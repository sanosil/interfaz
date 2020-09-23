from tkinter import *

class User_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        self.current = 0

        self.create_widgets()

    def create_widgets(self):
        self.main_container = Frame(self.root_frame, bg="white")
        self.main_container.grid(column=0, row=1)
        path = "images/"
        # self.path="/home/pi/Desktop/Interfaz-Sanosil/images/"

        self.images = {
            "admin": PhotoImage(file=path+"Admin.png"),
            "operador": PhotoImage(file=path+"User.png"),
            "service": PhotoImage(file=path+"Service.png")
            }

        self.rowa = Frame(self.main_container, bg="white")
        self.rowa.grid(column=0, row=0)

        self.frm_title = Frame(self.rowa, bg="white", relief=RIDGE,
            bd=5)
        self.frm_title.pack(pady=40)

        self.title = Label(self.frm_title, bg="white",
            font=("Verdana", 15, "bold"),
            text="Cambiar nombre de usuario y contraseña")
        self.title.pack(padx=20, pady=10)
