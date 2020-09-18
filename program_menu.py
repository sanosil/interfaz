from tkinter import *

class Program_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame

        self.create_widgets()

    def create_widgets(self):
        self.font = ("Verdana", 15, "bold")
        self.ch_select = PhotoImage(
            file=self.root.path+"ch_select.png").subsample(8)
        self.ch_unselect = PhotoImage(
            file=self.root.path+"ch_unselect.png").subsample(8)
        self.radioselect = PhotoImage(file=self.root.path+"radioselect.png")
        self.radiounselect = PhotoImage(file=self.root.path+"radiounselect.png")

        self.main = Frame(self.root_frame, bg="white")
        self.main.grid(sticky=W, column=0, row=1)

        self.frame_programa = Frame(self.main, bg="white")
        self.frame_programa.grid(column=0, row=0, sticky=W, padx=50, pady=5)

        self.frame_titulo_programa = Frame(self.frame_programa, bg="white",
            relief=RIDGE, bd=5)
        self.frame_titulo_programa.grid(column=0, row=0, sticky=W, pady=20)
        self.titulo = Label(self.frame_titulo_programa, bg="white",
            text="Programa", font=self.font)
        self.titulo.pack(padx=30, pady=10)
        self.imagenes = []
        data = self.root.database.execute("SELECT programa, concentration," \
            " volume FROM user_settings " \
            f"WHERE username='{self.root.sesion}';")

        for row in data:
            self.current_program = row[0]
            self.concentracion = row[1]
            self.volume = row[2]

        if self.current_program == "NORMAL":
            self.opcion(self.ch_select, "NORMAL", 1)
            self.opcion(self.ch_unselect, "MANUAL", 2)
        else:
            self.opcion(self.ch_unselect, "NORMAL", 1)
            self.opcion(self.ch_select, "MANUAL", 2)

        self.frame_concentracion = Frame(self.main, bg="white")
        self.frame_concentracion.grid(column=1, row=0, padx=30, pady=5, sticky=N)

        self.frame_titulo_concentracion = Frame(self.frame_concentracion, bg="white",
            relief=RIDGE, bd=5)
        self.frame_titulo_concentracion.grid(column=0, row=0, pady=20)

        self.titulo_concentracion = Label(self.frame_titulo_concentracion, bg="white",
            font=self.font, text="Concentración")
        self.titulo_concentracion.pack(padx=15, pady=10)

        self.frame_opciones = Frame(self.frame_concentracion, bg="white")
        self.frame_opciones.grid(column=0, row=1)

        valores = (6, 8, 10)
        self.con_imgs = []
        self.count = 0
        for i in valores:
            self.opcion_concentracion(i, self.count)
            self.count = self.count + 1

        self.frame_volumen = Frame(self.main, bg="white")
        self.frame_volumen.grid(column=0, row=1, padx=50, pady=5, sticky="nw")
        self.frame_titulo_volumen = Frame(self.frame_volumen, bg="white", bd=5,
            relief=RIDGE)
        self.frame_titulo_volumen.grid(column=0, row=0)
        self.titulo_volumen = Label(self.frame_titulo_volumen, bg="white",
            text="VOLUMEN", font=self.font)
        self.titulo_volumen.pack(padx=15, pady=10)

    def opcion_concentracion(self, valor, i):
        fr = Frame(self.frame_opciones, bg="white")
        fr.pack(side=LEFT, padx=15)
        if valor == self.concentracion:
            self.con_imgs.append(Label(fr, image=self.radioselect, bg="white"))
        else:
            self.con_imgs.append(Label(fr, image=self.radiounselect, bg="white"))
        self.con_imgs[i].pack(side=LEFT)
        self.con_imgs[i].bind("<Button-1>", lambda e, v=valor, c=i:
            self.cambiar_concentracion(e, v, c))
        lbl_text = Label(fr, text=str(valor)+" ml/m3", bg="white", font=self.root.myFont)
        lbl_text.pack(side=LEFT)

    def cambiar_concentracion(self, event, valor, count):
        c = 0
        for img in self.con_imgs:
            if c == count:
                img.config(image=self.radioselect)
            else:
                img.config(image=self.radiounselect)
            c = c + 1

        self.root.database.execute("UPDATE user_settings SET " \
            f"concentration={valor} WHERE username='{self.root.sesion}'")
        self.root.database.commit()

    def opcion(self, image, text, row):
        fr = Frame(self.frame_programa, bg="white")
        fr.grid(column=0, row=row, sticky=W)
        self.imagenes.append(Label(fr, bg="white", image=image))
        self.imagenes[row-1].pack(side=LEFT)
        self.imagenes[row-1].bind("<Button-1>", lambda e, t=text, v=row-1:self.set_program(e, t, v))
        self.imagenes[row-1].picture = image
        lbl = Label(fr, bg="white", text=text, font=self.root.myFont)
        lbl.pack(side=LEFT)


    def set_program(self, event, text, valor):
        if self.current_program != text:
            self.current_program = text
            if valor == 0:
                self.imagenes[valor].config(image=self.ch_select)
                self.imagenes[1].config(image=self.ch_unselect)
            else:
                self.imagenes[valor].config(image=self.ch_select)
                self.imagenes[0].config(image=self.ch_unselect)

            self.root.database.execute(f"UPDATE user_settings SET programa='{text}'"\
                f" WHERE username='{self.root.sesion}';")
            self.root.database.commit()
