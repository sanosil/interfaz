from tkinter import *
from datetime import datetime, date
import sqlite3

class Log_menu():
    def __init__(self, root, root_frame):
        # Variables root
        self.root = root
        self.root_frame = root_frame
        self.current = 1
        self.create_widgets(self.current)

    def create_widgets(self, log):
        self.rowa = Frame(self.root_frame.main_container, bg="white")
        self.rowa.grid(column=0, row=0)
         # Título y botones
        self.boton_izquierda = Button(self.rowa, bg="lightblue", text="<-",
            font=self.root.myFont, command=self.izquierda)
        self.boton_izquierda.pack(padx=20, side=LEFT)
        self.frame_titulo = Frame(self.rowa, bg="white", bd=3, relief=RIDGE)
        self.label_titulo = Label(self.frame_titulo, text="EVENTOS LOG",
            font=("Verdana", 15, "bold"), bg="white")
        self.frame_titulo.pack(side=LEFT, pady=20)
        self.label_titulo.pack(padx=70)
        self.boton_derecha = Button(self.rowa, bg="lightblue", text="->",
            font=self.root.myFont, command=self.derecha)
        self.boton_derecha.pack(side=LEFT, padx=20, pady=20)

        self.rowb = Frame(self.root_frame.main_container, bg="white")
        self.rowb.grid(column=0, row=1)
        self.valores = []

        self.display_log(log)



    def izquierda(self):
        current = self.root.database.execute("SELECT * FROM current_log;")
        for row in current:
            current_log = row[0]

        if current_log != 1:
            if self.current > 1:
                self.current = self.current - 1
                self.root_frame.main_container.grid_forget()
                self.root_frame.main_container.grid(column=0, row=1, sticky=W)
                self.create_widgets(self.current)
            else:
                self.current = current_log - 1
                self.root_frame.main_container.grid_forget()
                self.root_frame.main_container.grid(column=0, row=1, sticky=W)
                self.create_widgets(self.current)

    def derecha(self):
        current = self.root.database.execute("SELECT * FROM current_log;")
        for row in current:
            current_log = row[0]

        if current_log != 1:
            if self.current < 15 and self.current < current_log - 1:
                self.current = self.current + 1
                self.root_frame.main_container.grid_forget()
                self.root_frame.main_container.grid(column=0, row=1, sticky=W)
                self.create_widgets(self.current)
            else:
                self.current = 1
                self.root_frame.main_container.grid_forget()
                self.root_frame.main_container.grid(column=0, row=1, sticky=W)
                self.create_widgets(self.current)

    def display_log(self, log):
        text = ("LOG ID", "FECHA INICIO", "HORA INICIO",
                "USER", "FECHA FINAL", "HORA FINAL",
                "CONCENTRACION", " VOLUMEN  ", "TIEMPO SANITIZADO",
                "HUMEDAD RELATIVA INICIAL", "HUMEDAD RELATIVA FINAL",
                "TEMPERATURA INICIAL", "TEMPERATURA FINAL")

        self.rowc = Frame(self.root_frame.main_container, bg="white")
        self.rowc.grid(column=0, row=2)
        self.value_lbls = []
        data = None
        try:
            values = self.root.database.execute(f"SELECT * FROM logs WHERE id = {log};")
            for row in values:
                data = row
        except:
            print("No logs available")

        if data != None:
            for i in range(12):
                if i < 4:
                    self.valores.append(data[i])
                elif i == 4:
                    self.valores.append(data[7])
                    self.valores.append(data[8])
                    self.valores.append(data[i])
                elif i < 7:
                    self.valores.append(data[i])
                else:
                    self.valores.append(data[i+2])
        else:
            for i in range(13):
                self.valores.append(0)

        count = 0
        count1 = 0
        for row in range(1, 7):
            for col in range(3):
                if row % 2 != 0:
                    self.frame_field(self.rowb, row, col, text[count], 198)
                    count = count + 1
                else:
                    self.frame_value(self.rowb, row, col, self.valores[count1])
                    count1 = count1 + 1

        for row in range(4, 8):
            for col in range(2):
                if row % 2 == 0:
                    self.frame_field(self.rowc, row, col, text[count], 280)
                    count = count + 1
                else:
                    self.frame_value(self.rowc, row, col, self.valores[count1])
                    count1 = count1 + 1


    def frame_field(self, parent, row, col, text, offset):
        fr = Frame(parent, bg="yellow", bd=3, relief=RIDGE)
        fr.grid(column=col, row=row, padx=30, pady=(0, 5))
        lbl = Label(fr, bg="yellow", text=text, font=self.root.myFont)
        if len(text) % 2 == 0:
            lbl.pack(padx=((offset - (len(text)*11))/2))
        else:
            lbl.pack(padx=((offset+1 - (len(text)*11))/2))

    def frame_value(self, parent, row, col, value):
        fr = Frame(parent, bg="lightgray", relief=SUNKEN, bd=3)
        fr.grid(column=col, row=row, pady=(0, 5))
        lbl = Label(fr, bg="lightgray", font=self.root.myFont, text=value)
        lbl.pack()
        self.value_lbls.append(lbl)

def create_log(root):
    current = root.database.execute("SELECT * FROM current_log;")
    for row in current:
        current_log = row[0]

    root.fecha_termino = date.today()
    root.hora_termino = datetime.now().strftime("%H:%M:%S")
    root.database.execute("INSERT INTO logs(id, fecha_inicio, "\
        "hora_inicio, user, concentracion, volumen, tiempo, fecha_termino, " \
        "hora_termino, hr_inicial, hr_final, temp_inicial, temp_final) " \
        f"VALUES({current_log}, '{str(root.fecha_inicio)}', '{str(root.hora_inicio)}', " \
        f"'{root.sesion}', {root.concentracion}, {root.vol}, {root.time}, " \
        f"'{str(root.fecha_termino)}', '{str(root.hora_termino)}', {root.humidity_dht_inicial}, " \
        f"{root.humidity_dht}, {root.temp_dht_inicial}, {root.temp_dht});")
    root.database.execute(f"UPDATE current_log SET current = {current_log + 1};")
    root.database.commit()
