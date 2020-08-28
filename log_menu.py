from tkinter import *
from datetime import datetime, date

class Log_menu():
    def __init__(self, root, root_frame):
        # Variables root
        self.root = root
        self.root_frame = root_frame
        self.current_log = 1
        self.create_widgets()

    def create_widgets(self):
        self.rowa = Frame(self.root_frame.main_container, bg="white")
        self.rowa.grid(column=0, row=0)
        # Título
        self.frame_titulo = Frame(self.rowa, bg="white", bd=3, relief=RIDGE)
        self.label_titulo = Label(self.frame_titulo, text="EVENTOS LOG",
            font=("Verdana", 15, "bold"), bg="white")
        self.frame_titulo.pack(pady=20)
        self.label_titulo.pack(padx=80)

        self.rowb = Frame(self.root_frame.main_container, bg="white")
        self.rowb.grid(column=0, row=1, sticky=W)
        # ID
        self.frame_id = Frame(self.rowb, bg="yellow", bd=3, relief=RIDGE)
        self.label_id = Label(self.frame_id, bg="yellow", text="LOG ID",
            font=self.root.myFont)
        self.frame_id.pack(side=LEFT, padx=(50,30), pady=5)
        self.label_id.pack(padx=20)
        # Fecha
        self.frame_fecha = Frame(self.rowb, bg="yellow", bd=3, relief=RIDGE)
        self.label_fecha = Label(self.frame_fecha, bg="yellow", text="FECHA INICIO",
            font=self.root.myFont)
        self.frame_fecha.pack(side=LEFT, padx=(60, 10), pady=5)
        self.label_fecha.pack(padx=50)

        # Hora
        self.frame_hora = Frame(self.rowb, bg="yellow", bd=3, relief=RIDGE)
        self.label_hora = Label(self.frame_hora, bg="yellow", text="HORA INICIO",
            font=self.root.myFont)
        self.frame_hora.pack(side=LEFT, padx=10, pady=5)
        self.label_hora.pack(padx=45)

        self.rowc = Frame(self.root_frame.main_container, bg="white")
        self.rowc.grid(column=0, row=2, sticky=W)

        # Valor ID
        self.frame_valor_id = Frame(self.rowc, bg="lightgray", bd=3, relief=SUNKEN)
        self.label_valor_id = Label(self.frame_valor_id, font=self.root.myFont,
            text=self.current_log, bg="lightgray")
        self.frame_valor_id.pack(side=LEFT, padx=(50,30), pady=(5, 20))
        if self.current_log < 10:
            self.label_valor_id.pack(padx=45)
        else:
            self.label_valor_id.pack(padx=40)
        # Valor FECHA
        self.frame_valor_fecha = Frame(self.rowc, bg="lightgray", bd=3, relief=SUNKEN)
        self.label_valor_fecha = Label(self.frame_valor_fecha, font=self.root.myFont,
            text=self.root.fecha_inicio, bg="lightgray")
        self.frame_valor_fecha.pack(side=LEFT, padx=(60, 10), pady=(5, 20))
        if self.root.fecha_inicio != None:
            self.label_valor_fecha.pack(padx=110-(len(str(self.root.fecha_inicio))*5))
        else:
            self.label_valor_fecha.pack(padx=107)
        # Valor HORA
        self.frame_valor_hora = Frame(self.rowc, bg="lightgray", bd=3, relief=SUNKEN)
        self.label_valor_hora = Label(self.frame_valor_hora, font=self.root.myFont,
            text=self.root.hora_inicio, bg="lightgray")
        self.frame_valor_hora.pack(side=LEFT, padx=(10, 0), pady=(5, 20))
        if self.root.hora_inicio != None:
            self.label_valor_hora.pack(padx=107-len(str(self.root.hora_inicio))*5)
        else:
            self.label_valor_hora.pack(padx=103)

        # Frame row c
        self.rowd = Frame(self.root_frame.main_container, bg="white")
        self.rowd.grid(column=0, row=3, sticky=W)

        #User
        self.user_frame = Frame(self.rowd, bd=3, bg="yellow", relief=RIDGE)
        self.label_user = Label(self.user_frame, text="USER", bg="yellow",
            font=self.root.myFont)
        self.user_frame.pack(side=LEFT, padx=(50,30), pady=5)
        self.label_user.pack(padx=25)


    def crear_log(self):
        pass
