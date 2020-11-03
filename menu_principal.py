from tkinter import *
import start_menu, conf_menu, diag_menu, log_menu
import sqlite3
# import inicio

class Menu_principal(Frame):
    def __init__(self, root, menu):
        super().__init__(root)
        # Variables
        self.root = root
        self.current_menu  = menu
        self.timer_valores = [
            ["DOM", "blue"], ["LUN", "blue"], ["MAR", "blue"], ["MIE", "blue"],
            ["JUE", "blue"], ["VIE", "blue"], ["SAB", "blue"]
            ]
        self.funcs = [("START/STOP", self.start_menu), ("CONF", self.conf_menu),
            ("DIAG", self.diag_menu), ("LOG", self.log_menu)]
        self.menu_buttons = []
        # Metodos
        self.config(bg="white")
        self.grid(column=0, row=0)

        self.create_widgets(self.current_menu)

    def create_widgets(self, menu):
        data = self.root.database.execute("SELECT * FROM user_settings " \
            f"WHERE username = '{self.root.sesion}';")
        for row in data:
            self.user_data = row
        self.root.timer = self.user_data[7]
        self.current_button_state = self.root.current_button_state
        self.current_program = self.user_data[4]
        self.root.concentracion = self.user_data[6]
        self.root.vol = self.user_data[5]
        self.root.time = (self.root.vol * self.root.concentracion) * 2
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
        if self.current_menu != "START/STOP":
            self.switch_menu("START/STOP")

    def conf_menu(self, event=None):
        if self.current_menu != "CONF":
            self.switch_menu("CONF")

    def diag_menu(self, event=None):
        if self.current_menu != "DIAG":
            self.switch_menu("DIAG")

    def log_menu(self, event=None):
        if self.current_menu != "LOG":
            self.switch_menu("LOG")

    def switch_menu(self, menu):
        self.current_menu = menu
        self.clear(self)
        self.create_widgets(self.current_menu)

    def menu_button_principal(self, text, func):
        if text == self.current_menu:
            self.menu_buttons.append(Button(self.menu,
                activebackground="spring green", width=18, relief=FLAT,
                bg="spring green", font=self.root.myFont_bold, text=text,
                command=func).pack(fill=BOTH, side=LEFT, expand=YES, ipady=10))
        else:
            self.menu_buttons.append(Button(self.menu, text=text,
                activebackground=self.root.selected_color, width=18,
                bg=self.root.color, font=self.root.myFont, fg="white",
                command=func).pack(fill=BOTH, side=LEFT, expand=YES, ipady=10))

    def cambiar_sesion(self):
        if self.root.program_object == None:
            self.clear(self.root)
            self.root.sesion = ""
            inicio.Inicio(self.root).tkraise()

class Root(Tk):
    def __init__(self):
        super().__init__()
        # self.path="/home/pi/Desktop/Interfaz-Sanosil/images/"
        self.path="images/"
        self.timer = 0
        self.sesion = "ADMIN"
        self.database = sqlite3.connect("program_database.db")
        # self.color = "#2ECC71"
        self.fecha_inicio = None
        self.hora_inicio = None
        self.fecha_termino = None
        self.hora_termino = None
        self.color = "green"
        # self.root.selected_color = "#60FEA3"
        self.selected_color = "white"
        self.tanque_lleno = 0
        self.mensaje = "STATUS: LISTO PARA OPERAR"
        self.program_object = None
        self.color_alertas = self.color
        self.bomba_entrada = 0
        self.bomba_salida = 1
        self.current_button_state = 0
        self.current_program = 0
        self.vol = 0
        self.concentracion = 0
        self.time = (self.vol * self.concentracion) * 2
        self.pulsos = 0
        self.ml = 0
        self.temp_dht = 25
        self.temp_dht_inicial = 0
        self.ch3 = 0
        self.humidity_dht = 50
        self.humidity_dht_inicial = 0
        self.config(bg="white")
        self.overrideredirect(1)
        # self.geometry("770x495")
        self.geometry("%dx%d" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        self.myFont = ("Verdana", 12)
        self.myFont_bold = ("Verdana", 12, "bold")
        self.usernames = []
        usernames = self.database.execute("SELECT username FROM user_settings;")
        for row in usernames:
            self.usernames.append(row[0])
        idioma = self.database.execute("SELECT language FROM user_settings " \
            f"WHERE username = '{self.sesion}';")
        for row in idioma:
            self.language = row[0]

        Menu_principal(self, "START/STOP")

    def pin_on(self, ch, s):
        print("channel " + str(ch) + str(s))

Root().mainloop()
