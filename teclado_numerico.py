from tkinter import *

class Teclado(Frame):
    def __init__(self, root, titulo, previous):
        self.previous = previous
        self.color = "gray90"
        super().__init__(root, bg=self.color)
        self.titulo = titulo
        self.root = root
        self.root.config(bg=self.color)
        self.nuevo_volumen = ""
        self.grid(column=0, row=0)

        self.crear_teclado()

    def crear_teclado(self):
        self.frm_titulo_teclado = Frame(self, bg="white", relief=RIDGE, bd=5)
        self.frm_titulo_teclado.grid(column=0, row=0, padx=40, pady=15, sticky=W)

        self.titulo_teclado = Label(self.frm_titulo_teclado, text=self.titulo,
            bg="white", font=("Verdana", 25, "bold"))
        self.titulo_teclado.pack(padx=180)

        self.rowa = Frame(self, bg=self.color)
        self.rowa.grid(column=0, row=1, sticky=W, padx=(25, 5))

        self.entry_volumen = Entry(self.rowa, font=("Verdana", 25), width=23,
            relief=SUNKEN, bd=3, state=DISABLED)
        self.entry_volumen.pack(side=LEFT, padx=15, ipady=5, ipadx=5)

        self.esc = Button(self.rowa, text="ESC", command=self.volver, bg="pale green",
            font=("Verdana", 20, "bold"))
        self.esc.pack(side=LEFT, padx=(20, 0), ipadx=20)

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

        self.frm_funciones = Frame(self.frm_teclado, bg=self.color)
        self.frm_funciones.grid(column=1, row=0, sticky="nw")

        self.funcs = (("CLR", self.clear_entry),
            ("DEL", self.erase),
            ("ENTER", self.enter)
            )
        count_row = 0
        for name, func in self.funcs:
            self.frm_funcs(name, func, count_row)
            count_row = count_row + 1


    def frame_numero(self, frm, dig, col):
        btn_dig = Button(frm, bg="gray80", text=dig,
            font=("Verdana", 20, "bold"), command=lambda d=dig: self.ins(d))
        btn_dig.grid(column=col, row=0, ipadx=50, ipady=5, padx=15)

        if dig == "  ":
            btn_dig["state"] = DISABLED

    def frm_funcs(self, name, func, row):
        btn_func = Button(self.frm_funciones, bg="lime green", text=name,
            command=func, font=("Verdana", 20, "bold"))
        if name != "ENTER":
            btn_func.grid(column=0, row=row, ipadx=20, ipady=5, pady=5, padx=15)
        else:
            btn_func.grid(column=0, row=row, ipady=43, pady=5, padx=15)

    def clear_entry(self):
        self.nuevo_volumen = ""
        self.ins("")

    def volver(self):
        self.root.config(bg="white")
        self.grid_forget()
        self.previous.__init__(self.root, "START/STOP")

    def anterior(self):
        self.root.config(bg="white")
        self.grid_forget()
        self.previous.grid(column=0, row=0)

    def ins(self, dig):
        w = 1
        if dig == " .":
            dig = "."
            if dig in self.nuevo_volumen:
                w = 0

        if w == 1:
            self.nuevo_volumen = self.nuevo_volumen + str(dig)
            self.entry_volumen.config(state=NORMAL)
            self.entry_volumen.delete(0, END)
            self.entry_volumen.insert(END, self.nuevo_volumen)

        self.entry_volumen.config(state=DISABLED)

    def erase(self):
        self.nuevo_volumen = self.nuevo_volumen[:-1]
        self.ins("")

    def cambiar_volumen(self, volumen):
        self.root.database.execute("UPDATE user_settings SET " \
            f"volume={volumen} WHERE username='{self.root.sesion}'")
        self.root.database.commit()

    def enter(self):
        if self.nuevo_volumen != "":
            if float(self.nuevo_volumen) < 1000:
                self.cambiar_volumen(float(self.nuevo_volumen))
                self.volver()
            else:
                self.entry_volumen.delete(0, END)
                self.nuevo_volumen = "Volumen demasiado grande"
                self.ins("")
                self.after(2000, self.act_entry)
        else:
            self.nuevo_volumen = "Ingrese volumen"
            self.ins("")
            self.after(2000, self.act_entry)


    def act_entry(self):
        self.nuevo_volumen = ""
        self.ins("")
