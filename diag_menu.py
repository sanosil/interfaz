from tkinter import *
import random, math

class Diag_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        width = 370
        height = 430
        self.color = "lightcyan2"
        self.bg_color = "gray64"
        self.frame_termometro = Frame(self.root_frame.main_container,
            bg="gray", relief=SUNKEN, bd=5)
        self.frame_termometro.pack(side=LEFT)
        # ---------------------------- Termometro -----------------------------
        self.termometro = Canvas(self.frame_termometro, bg="white",
            width=width, height=height)
        self.frame_titulo = Frame(self.termometro, relief=RIDGE, bd=3,
            bg=self.root.color)
        self.label_titulo_temp = Label(self.frame_titulo, text="TEMPERATURA", fg="white",
            bg=self.root.color, font=self.root.myFont)
        self.label_titulo_temp.pack(padx=10, pady=10)
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
        self.termometro.create_window(220, 85, window=self.cent_frame,
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
                Label(frm, text=i+1, font=("Verdana", 5),
                    bg=self.bg_color).pack()
                self.termometro.create_window(220, y-(i*2), window=frm,
                    anchor=CENTER)
                self.termometro.create_line(187, y - (i*2), 205, y - (i*2),
                    fill="red")
            else:
                self.termometro.create_line(187, y - (i*2), 200, y - (i*2),
                    fill="blue")
        self.termometro.pack()

        # ----------------------- Velocímetro ------------------------------
        self.angulo_humedad = 90
        self.frame_humedad = Frame(self.root_frame.main_container, bg="gray",
            bd=5, relief=SUNKEN)
        self.frame_humedad.pack(side=LEFT)
        self.canvas_humedad = Canvas(self.frame_humedad, width=width,
            height=height, bg="white")
        self.canvas_humedad.pack()
        self.frame_titulo_humedad = Frame(self.canvas_humedad, relief=RIDGE,
            bd=3, bg=self.root.color)
        self.label_titulo_humedad = Label(self.frame_titulo_humedad,
            bg=self.root.color, text="Humedad Relativa", fg="white",
            font=self.root.myFont)
        self.label_titulo_humedad.pack(padx=10, pady=10)
        self.canvas_humedad.create_window(180, 40,
            window=self.frame_titulo_humedad)
        # Centro x = 185 y = 315
        self.angulo = 180
        # Base indicador
        self.canvas_humedad.create_oval(160, 340, 210, 290, fill="black", outline="black")
        self.canvas_humedad.create_oval(165, 335, 205, 295, fill="gray", outline="gray")
        # Aguja de indicador
        # altura de aguja = 130, radio = 10
        self.x0_aguja = 175
        self.y0_aguja = 315
        self.x1_aguja = 185
        self.y1_aguja = 185
        self.x2_aguja = 195
        self.y2_aguja = 315
        self.canvas_humedad.create_oval(175, 325, 195, 305, fill="red",
            outline="red")
        self.aguja = self.canvas_humedad.create_polygon(self.x0_aguja,
            self.y0_aguja, self.x1_aguja, self.y1_aguja, self.x2_aguja,
            self.y2_aguja, fill="red")
        # Pin blanco que sujeta la aguja
        self.canvas_humedad.create_oval(182.5, 312.5, 187.5, 317.5, fill="white",
            outline="white")
        # radio exerior = 170 radio interior = 150
        self.x0 = 35
        self.y0 = 315
        self.x1 = 45
        self.y1 = 315
        self.angulo = 0
        for i in range(101):
            if (i+1) % 5 == 0:
                self.actualizar_coordenadas(160)
                self.canvas_humedad.create_line(self.x0, self.y0, self.x1,
                    self.y1, width=3, fill="red")
                frm = Frame(self.canvas_humedad, bg="white")
                Label(frm, bg="white", text=i+1, font=("Verdana", 7)).pack()
                if self.angulo < 90:
                    self.canvas_humedad.create_window(self.x0 - 10,
                        self.y0 - 10, window=frm)
                elif i+1 == 55:
                    self.canvas_humedad.create_window(self.x0 ,
                        self.y0 - 12, window=frm)
                else:
                    self.canvas_humedad.create_window(self.x0 + 10,
                        self.y0 - 10, window=frm)
            else:
                if i > 0:
                    self.actualizar_coordenadas(150)
                self.canvas_humedad.create_line(self.x0, self.y0, self.x1,
                    self.y1, fill="blue")


        self.root_frame.after(2000, self.actualizar_termometro)

    def actualizar_coordenadas(self, largo):
        self.angulo = self.angulo + 1.8
        self.x0 = 185 - (largo * math.cos((self.angulo * math.pi)/180))
        self.y0 = 315 - (largo * math.sin((self.angulo * math.pi)/180))
        self.x1 = 185 - (140 * math.cos((self.angulo * math.pi)/180))
        self.y1 = 315 - (140 * math.sin((self.angulo * math.pi)/180))

    def actualizar_termometro(self):
        if self.root_frame.current_menu == "DIAG":
            self.termometro.coords(self.temperatura, 176, 360, 183, 273 -
                (self.root.temp_dht*2))
            self.temp_digital.config(text=str(self.root.temp_dht) + "°C")
            self.root.temp_dht = random.randint(-20, 80)

            self.angulo_humedad = (self.root.humidity_dht * 180) / 100
            self.root.humidity_dht = random.randint(0, 100)



            self.root_frame.after(2000, self.actualizar_termometro)
