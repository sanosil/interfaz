from tkinter import *
from datetime import datetime, date

class Conf_menu():
    def __init__(self, root, root_frame):
        # variables
        self.root = root
        now = datetime.now()
        self.root_frame = root_frame
        self.primera_mitad = Frame(self.root_frame.main_container, bg="white",
            bd=3, relief=SOLID)
        self.primera_mitad.pack(side=LEFT)
        # Barra de fecha y hora con texto
        self.barra_FyH = Frame(self.primera_mitad, bd=3,
            bg="gray", relief=RIDGE)
        self.barra_FyH.pack(pady=(10,0), side=TOP)
        self.FyH_label = Label(self.barra_FyH, text="Fecha y Hora",
            bg="gray", fg="white", font=self.root.myFont)
        self.FyH_label.pack(padx=120, pady=10)
        # Frame de hora y fecha editable
        self.FyH_frame = Frame(self.primera_mitad, bd=3,
            relief=RIDGE, bg="yellow")
        self.FyH_frame.pack(side=TOP, padx=10, pady=(1,10))
        self.FyH_valores = Label(self.FyH_frame, font=self.root.myFont,
            bg="yellow")
        self.FyH_valores.pack(padx=95, pady=10)
        self.FyH_valores.bind("<Button-1>", self.set_date_time)
        # frame segunda segunda mitad
        self.segunda_mitad = Frame(self.root_frame.main_container, bg="white",
            bd=3, relief=SOLID)
        self.segunda_mitad.pack(fill=BOTH, expand=YES, side=LEFT)
        # Frame de timer
        self.barra_timer = Frame(self.segunda_mitad, bd=3, bg="gray", relief=RIDGE)
        self.barra_timer.pack(side=TOP, padx=10, pady=(10,0))
        self.timer_label = Label(self.barra_timer, bg="gray", fg="white",
            font=self.root.myFont, text="Configurar Timer")
        self.timer_label.pack(padx=95, pady=10)
        # Valore editables del timer
        self.timer_valores_frame = Frame(self.segunda_mitad, bg="white")
        self.timer_valores_frame.pack(side=BOTTOM, padx=10, pady=(6,10))
        for i, bg in self.root_frame.timer_valores:
            self.dias(self.timer_valores_frame, i, bg)

        # Botón de usuario
        self.frame_inferior = Frame(self.root_frame.main_container, bg="white", bd=3,
            relief=SOLID)
        # self.frame_inferior.grid(column=0, row=2, sticky="nw")
        self.frame_inferior.pack(side=BOTTOM, expand=YES, fill=BOTH)
        self.settings = ["USUARIO", "IDIOMA", "WI-FI"]
        for text in self.settings:
            self.settings_buttons(text)

    def settings_buttons(self, text):
        Button(self.frame_inferior, fg="white",
            font=("Verdana", 18), text=text, bg=self.root.color).pack(
            side=LEFT, padx=40, pady=(80, 10))

        self.actualizar_hora()

    def dias(self, frame, text, bg):
        dia = Label(frame, text=text, bg=bg, fg="white", font=("Verdana", 15),
            bd=3, relief=RAISED)
        dia.pack(side=LEFT)
        dia.bind("<Button-1>", self.edit_timer)

    def edit_timer(self, event=None):
        pass

    def set_date_time(self, event=None):
        pass
        # self.root_frame.grid_forget()
        # teclado_fecha.Teclado()

    def actualizar_hora(self):
        if self.root_frame.current_menu == "CONF":
            today = date.today()
            now = datetime.now()
            today_str = today.strftime("%d/%m/%y") + " " + now.strftime("%H:%M:%S")

            self.FyH_valores.config(text=today_str)
            self.root_frame.after(1000, self.actualizar_hora)
