from tkinter import *
import start_menu, conf_menu, diag_menu, log_menu

import inicio

class Menu_principal(Frame):
    def __init__(self, root, menu):
        super().__init__(root)
        # Variables
        self.root = root
        self.timer = self.root.timer
        self.mensaje = "STATUS: LISTO PARA OPERAR"
        self.current_menu  = menu
        self.current_button_state = self.root.current_button_state
        self.current_program = self.root.current_program
        self.vol = self.root.vol
        self.tiempo_sanitizacion = 0
        self.state = ("Normal", "Step", "Testing", "Manual")
        self.timer_valores = [
            ["DOM", "blue"], ["LUN", "blue"], ["MAR", "blue"], ["MIE", "blue"],
            ["JUE", "blue"], ["VIE", "blue"], ["SAB", "blue"]
            ]
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
        self.main_container.grid(column=0, row=1, sticky="w")
        # --------------------------- Menu START/STOP ------------------------
        if menu == "START/STOP":
            start_menu.Start_menu(self.root, self)
        # --------------------------- Menu CONF -------------------------------
        elif menu == "CONF":
            conf_menu.Conf_menu(self.root, self)
        # --------------------------- Menu DIAG -------------------------------
        elif menu == "DIAG":
            diag_menu.Diag_menu(self.root, self)
        # --------------------------- Menu Log --------------------------------
        elif menu == "LOG":
            log_menu.Log_menu(self.root, self)

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
            self.menu_buttons.append(Button(self.menu,
                activebackground="#60FEA3", fg="white", width=18,
                bg="#60FEA3", font=self.root.myFont, text=text, relief=FLAT,
                command=func).pack(fill=BOTH, side=LEFT, expand=YES, ipady=10))
        else:
            self.menu_buttons.append(Button(self.menu, fg="white",
                activebackground="#60FEA3", width=18,
                bg=self.root.color, font=self.root.myFont, text=text,
                command=func).pack(fill=BOTH, side=LEFT, expand=YES, ipady=10))

    def cambiar_sesion(self):
        self.grid_forget()
        self.root.sesion = ""
        inicio.Inicio(self.root).tkraise()

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.temp_dht = 25
        self.ch3 = 0
        self.humidity_dht = 50
        self.config(bg="white")
        self.overrideredirect(1)
        self.geometry("770x495")
        self.sesion = "Admin"
        self.myFont = ("Verdana", 12)
        self.color = "#2ECC71"
        Menu_principal(self, "START/STOP")

    def pin_on(self, ch, s):
        pass

# Root().mainloop()
