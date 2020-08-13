from tkinter import *

class Diag_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        width = 370
        height = 420

        self.frame_termometro = Frame(self.root_frame.main_container,
            bg="gray", relief=SUNKEN, bd=10)
        self.frame_termometro.pack()

        self.termometro = Canvas(self.frame_termometro, bg="white",
            width=width, height=height)
        self.frame_titulo = Frame(self.termometro, relief=RIDGE, bd=3, bg="gray")
        Label(self.frame_titulo, text="TEMPERATURA", fg="white", bg="gray", font=self.root.myFont).pack(padx=10, pady=10)
        self.termometro.create_window(180, 40, window=self.frame_titulo, anchor=CENTER)
        self.inicio_term = self.termometro.create_arc(135, 400, 235, 300,
            start=135, extent=270, outline="blue", fill="blue")
        self.cuerpo_term_frio = self.termometro.create_rectangle(150, 355, 219, 270,
            fill="blue", outline="blue")
        self.cuerpo_term_templado = self.termometro.create_rectangle(150, 270,
            219, 230, fill="green", outline="green")
        self.cuerpo_term_calido = self.termometro.create_rectangle(150, 230,
            219, 190, fill="yellow", outline="yellow")
        self.cuerpo_term_caliente = self.termometro.create_rectangle(150, 190,
            219, 150, fill="orange", outline="orange")
        self.cuerpo_term_hirviendo = self.termometro.create_rectangle(150, 150,
            219, 110, fill="red", outline="red")
        self.cuerpo_term_cabeza = self.termometro.create_arc(150, 150, 219, 81,
            start=0, extent=180, fill="red", outline="red")
        self.termometro.pack()
