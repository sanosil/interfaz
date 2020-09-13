from tkinter import *

class Program_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame

        self.create_widgets()

    def create_widgets(self):
        self.ch_select = PhotoImage(file=self.root.path+"ch_select.png").subsample(8)
        self.ch_unselect = PhotoImage(file=self.root.path+"ch_unselect.png").subsample(8)
        self.main = Frame(self.root_frame, bg="white")
        self.main.grid(sticky=W, column=0, row=1)

        self.frame_programa = Frame(self.main, bg="white")
        self.frame_programa.grid(column=0, row=0, sticky=W, padx=50, pady=5)

        self.frame_titulo_programa = Frame(self.frame_programa, bg="white",
            relief=RIDGE, bd=5)
        self.frame_titulo_programa.grid(column=0, row=0, sticky=W, pady=20)
        self.titulo = Label(self.frame_titulo_programa, bg="white",
            text="Programa", font=("Verdana", 15, "bold"))
        self.titulo.pack(padx=30, pady=10)
        self.imagenes = []
        data = self.root.database.execute("SELECT programa FROM user_settings "\
            f"WHERE username='{self.root.sesion}';")
        for row in data:
            self.current_program = row[0]

        if self.current_program == "NORMAL":
            self.opcion(self.ch_select, "NORMAL", 1, (0, "NORMAL"))
            self.opcion(self.ch_unselect, "MANUAL", 2, (1, "MANUAL"))
        else:
            self.opcion(self.ch_unselect, "NORMAL", 1, (0, "NORMAL"))
            self.opcion(self.ch_select, "MANUAL", 2, (1, "MANUAL"))

    def opcion(self, image, text, row, com):
        fr = Frame(self.frame_programa, bg="white")
        fr.grid(column=0, row=row, sticky=W)
        self.imagenes.append(Label(fr, bg="white", image=image))
        self.imagenes[row-1].pack(side=LEFT)
        self.imagenes[row-1].bind("<Button-1>", lambda e, c=com:self.set_program(e, c))
        self.imagenes[row-1].picture = image
        lbl = Label(fr, bg="white", text=text, font=self.root.myFont)
        lbl.pack(side=LEFT)


    def set_program(self, event, kw):
        if self.current_program != kw[1]:
            self.current_program = kw[1]
            if kw[0] == 0:
                self.imagenes[kw[0]].config(image=self.ch_select)
                self.imagenes[1].config(image=self.ch_unselect)
            else:
                self.imagenes[kw[0]].config(image=self.ch_select)
                self.imagenes[0].config(image=self.ch_unselect)

            self.root.database.execute(f"UPDATE user_settings SET programa='{kw[1]}'"\
                f" WHERE username='{self.root.sesion}';")
            self.root.database.commit()
