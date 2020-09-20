
from tkinter import *

class Teclado(Frame):
    def __init__(self, root, titulo):
        self.color = "chartreuse4"
        super().__init__(root, bg=self.color)
        self.titulo = titulo
        self.root = root
        self.root.config(bg=self.color)
        self.nuevo_volumen = ""
        self.grid(column=0, row=0)

        self.crear_teclado()

    def crear_teclado(self):
        self.frm_titulo_teclado = Frame(self, bg="white", relief=RIDGE, bd=5)
        self.frm_titulo_teclado.grid(column=0, row=0, padx=25, pady=15, sticky=W)

        self.titulo_teclado = Label(self.frm_titulo_teclado, text=self.titulo,
            bg="white", font=("Verdana", 25, "bold"))
        self.titulo_teclado.pack(padx=100)

        self.rowa = Frame(self, bg=self.color)
        self.rowa.grid(column=0, row=1, sticky=W, padx=(25, 5))

        self.entry_volumen = Entry(self.rowa, font=("Verdana", 25), width=30)
        self.entry_volumen.pack(side=LEFT, padx=15)

        self.frm_teclado = Frame(self, bg=self.color)
        self.frm_teclado.grid(column=0, row=2, padx=25, pady=15, sticky=W)

        self.frm_numeros = Frame(self.frm_teclado, bg=self.color)
        self.frm_numeros.grid(column=0, row=0, sticky="nw")

        self.numeros = (
            ("1", "2", "3"),
            ("4", "5", "6"),
            ("7", "8", "9"),
            (" .", "0", "  ")
            )

        count_row = 0
        count_col = 0
        for row in self.numeros:
            frm = Frame(self.frm_numeros, bg=self.color)
            frm.grid(column=0, row=count_row, pady=5)
            count_row = count_row + 1
            for num in row:
                self.frame_numero(frm, num, count_col)
                count_col = count_col + 1
            count_col = 0

    def frame_numero(self, frm, dig, col):
        btn_dig = Button(frm, bg="lightblue1", text=dig,
            font=("Verdana", 20, "bold"), command=lambda d=dig: self.ins(d))
        btn_dig.grid(column=col, row=0, ipadx=50, ipady=5, padx=15)

        if dig == "  ":
            btn_dig["state"] = DISABLED

    def ins(self, dig):
        if dig == " .":
            dig = "."
        self.entry_volumen.insert(END, dig)

    def cambiar_volumen(self, volumen):
        self.root.database.execute("UPDATA user_settings SET " \
            f"volume={volumen} WHERE username='{self.root.sesion}'")
        self.root.database.commit()

    def enter(self):
        pass
