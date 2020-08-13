from tkinter import *
import random

class Diag_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        width = 370
        height = 420
        self.color = "lightcyan2"
        self.bg_color = "gray25"
        self.frame_termometro = Frame(self.root_frame.main_container,
            bg="gray", relief=SUNKEN, bd=10)
        self.frame_termometro.pack()

        self.termometro = Canvas(self.frame_termometro, bg="white",
            width=width, height=height)
        self.frame_titulo = Frame(self.termometro, relief=RIDGE, bd=3,
            bg=self.root.color)
        Label(self.frame_titulo, text="TEMPERATURA", fg="white",
            bg=self.root.color, font=self.root.myFont).pack(padx=10, pady=10)
        self.termometro.create_window(180, 40, window=self.frame_titulo,
            anchor=CENTER)

        self.contorno = self.termometro.create_rectangle(105, 410, 255, 70,
            fill=self.bg_color)
        self.linea_uno = self.termometro.create_line(205, 405, 235, 405,
            fill="white")
        self.linea_dos = self.termometro.create_line(125, 75, 155, 75,
            fill="white")
        self.cent_frame = Frame(self.termometro, bg=self.bg_color)
        self.temp_digital = Label(self.cent_frame, fg="yellow",
            text=str(self.root.temp_dht) + "°C", font=self.root.myFont,
            bg=self.bg_color)
        self.temp_digital.pack()
        self.termometro.create_window(230, 90, window=self.cent_frame,
            anchor=CENTER)

        self.inicio_term = self.termometro.create_arc(145, 400, 215, 320,
            start=110, extent=320, outline=self.color, fill=self.color)
        self.cuerpo_term = self.termometro.create_rectangle(169, 360, 190, 110,
            fill=self.color, outline=self.color)
        self.term_cabeza = self.termometro.create_arc(169, 121, 190, 99,
            start=0, extent=180, fill=self.color, outline=self.color)
        self.term_interno = self.termometro.create_arc(150, 395, 210, 325,
            fill="red", start=100, extent=340, outline="red")
        self.temperatura = self.termometro.create_rectangle(176, 360,
            183, 273 - (self.root.temp_dht * 2), fill="red", outline="red")
        self.brillo = self.termometro.create_arc(180, 385, 200, 350, extent=170,
            start=230, fill="white", outline="white")
        y = 270

        for i in range(-20, 80):
            if (i + 1) % 5 == 0:
                frm = Frame(self.termometro, bg=self.bg_color)
                Label(frm, text=i+1, fg="white", font=("Verdana", 5), bg=self.bg_color).pack()
                self.termometro.create_window(220, y-(i*2), window=frm, anchor=CENTER)
                self.termometro.create_line(187, y - (i*2), 205, y - (i*2), fill="red")
            else:
                self.termometro.create_line(187, y - (i*2), 200, y - (i*2),fill="blue")
        self.termometro.pack()

        self.root_frame.after(2000, self.actualizar_termometro)

    def actualizar_termometro(self):
        if self.root_frame.current_menu == "DIAG":
            self.termometro.coords(self.temperatura, 176, 360, 183, 273 -
                (self.root.temp_dht*2))
            self.temp_digital.config(text=str(self.root.temp_dht) + "°C")
            self.root.temp_dht = random.randint(-20, 80)
            self.root_frame.after(2000, self.actualizar_termometro)
