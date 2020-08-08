from tkinter import *
from datetime import datetime, date

class Conf_menu():
    def __init__(self, root, root_frame):
        # variables
        self.root = root
        now = datetime.now()
        self.root_frame = root_frame
        self.primera_mitad = Frame(self.root_frame.main_container, bg="white")
        self.primera_mitad.pack(fill=BOTH, side=LEFT, expand=YES)
        # Barra de fecha y hora con texto
        self.barra_FyH = Frame(self.primera_mitad, bd=3,
            bg="gray", relief=RIDGE)
        self.barra_FyH.pack(padx=10, pady=(10,0), side=TOP)
        self.FyH_label = Label(self.barra_FyH, text="Fecha y Hora",
            bg="gray", fg="white", font=self.root.myFont)
        self.FyH_label.pack(padx=120, pady=10)
        # Frame de hora y fecha editable
        self.FyH_frame = Frame(self.primera_mitad, bd=3,
            relief=SOLID, bg="yellow")
        self.FyH_frame.pack(side=TOP, padx=10, pady=(1,10))
        self.FyH_valores = Label(self.FyH_frame, font=self.root.myFont, bg="yellow")
        self.FyH_valores.pack(padx=110, pady=10)
        self.FyH_valores.bind("<Button-1>", self.set_date_time)
        self.actualizar_hora()

    def set_date_time(self, event):
        self.root_frame.grid_forget()
        # teclado_fecha.Teclado()

    def actualizar_hora(self):
        if self.root_frame.current_menu == "CONF":
            today = date.today()
            now = datetime.now()
            today_str = today.strftime("%d/%m/%y") + " " + now.strftime("%H:%M:%S")

            self.FyH_valores.config(text=today_str)
            self.root_frame.after(1000, self.actualizar_hora)
