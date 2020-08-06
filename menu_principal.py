from tkinter import *
import inicio, start_menu, conf_menu, diag_menu, log_menu

class Menu_principal(Frame):
    def __init__(self, root, menu):
        super().__init__(root)
        # Variables
        self.root = root
        self.current_menu  = menu
        self.current_state = 0
        self.state = ("Normal", "Step", "Testing", "Manual")
        self.funcs = [("START/STOP", self.start_menu), ("CONF", self.conf_menu), ("DIAG", self.diag_menu), ("LOG", self.log_menu)]
        self.menu_buttons = []
        # Metodos
        self.config(bg="white")
        self.grid(column=0, row=0)

        self.create_widgets(self.current_menu)

    def create_widgets(self, menu):
        # Barra de menús
        self.menu = Frame(self, bg="white")
        self.menu.grid(column=0, row=0)
        # Se crean los botones de menús
        for func, command in self.funcs:
            self.menu_button_principal(func, command)
        # Contenedor principal del menú seleccionado
        self.main_container = Frame(self, bg="white")
        self.main_container.grid(column=0, row=1)
        # --------------------------- Menu START/STOP ------------------------
        if menu == "START/STOP":
            start_menu.Start_menu(self.root, self)
        # --------------------------- Menu CONF -------------------------------
        elif menu == "CONF":
            pass
        # ------------------ Termina menu CONF -------------------------------
        elif menu == "DIAG":
            pass
        elif menu == "LOG":
            pass

    def clear(self, frame):
        for l in frame.grid_slaves():
            l.destroy()

    def start_menu(self, event=None):
        self.switch_menu("START/STOP")

    def conf_menu(self, event=None):
        self.switch_menu("CONF")

    def diag_menu(self, event=None):
        self.switch_menu("DIAG")

    def log_menu(self, event=None):
        self.switch_menu("LOG")

    def switch_menu(self, menu):
        self.current_menu = menu
        self.clear(self)
        self.create_widgets(self.current_menu)

    def menu_button_principal(self, text, func):
        if text == self.current_menu:
            self.menu_buttons.append(Button(self.menu, fg="white", width=18,
                bg="#60FEA3", font=self.root.myFont, text=text, relief=FLAT,
                command=func).pack(fill=BOTH, side=LEFT, expand=YES, ipady=10))
        else:
            self.menu_buttons.append(Button(self.menu, fg="white", width=18,
                bg=self.root.color, font=self.root.myFont, text=text,
                command=func).pack(fill=BOTH, side=LEFT, expand=YES, ipady=10))

    def menu_button(self, text):
        pass

    def cambiar_sesion(self):
        self.grid_forget()
        self.root.sesion = ""
        inicio.Inicio(self.root).tkraise()

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.config(bg="white")
        self.overrideredirect(1)
        self.geometry("800x480")
        self.sesion = "Admin"
        self.myFont = ("Verdana", 12)
        self.color = "#2ECC71"
        Menu_principal(self, "START/STOP").tkraise()

Root().mainloop()
