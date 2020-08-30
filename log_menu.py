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
        self.rowb.grid(column=0, row=1)

        text = ("LOG ID", "FECHA INICIO", "HORA INICIO",
                "USER", "FECHA FINAL", "HORA FINAL",
                "CONCENTRACION", " VOLUMEN  ", "TIEMPO SANITIZADO",
                "HUMEDAD RELATIVA INICIAL", "HUMEDAD RELATIVA FINAL",
                "TEMPERATURA INICIAL", "TEMPERATURA FINAL")
        count = 0
        for row in range(1, 4):
            for col in range(3):
                self.frame_field(self.rowb, row, col, text[count], 198)
                count= count + 1

        self.rowc = Frame(self.root_frame.main_container, bg="white")
        self.rowc.grid(column=0, row=2)

        for row in range(4, 6):
            for col in range(2):
                self.frame_field(self.rowc, row, col, text[count], 280)
                count = count + 1


    def frame_field(self, parent, row, col, text, offset):
        fr = Frame(parent, bg="yellow", bd=3, relief=RIDGE)
        fr.grid(column=col, row=row, padx=30, pady=10)
        lbl = Label(fr, bg="yellow", text=text, font=self.root.myFont)
        if len(text) % 2 == 0:
            lbl.pack(padx=((offset - (len(text)*11))/2))
        else:
            lbl.pack(padx=((offset+1 - (len(text)*11))/2))

    def frame_value():
        pass

def create_log():
    self.root.fecha_termino = date.today()
    self.root.hora_termino = datetime.now()
